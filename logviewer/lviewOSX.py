import discord, subprocess, sys, os, time
from discord.ext import commands

###########################################################################
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content
client = commands.Bot(command_prefix=".", intents=intents)
###########################################################################

@client.event
async def on_ready():
    chanID = COPY-YOUR-SERVER-CHANNEL-ID-HERE  # Replace with your actual channel ID
    channel = client.get_channel(chanID)
    await channel.send("Discord Bot Online.") #I see, everything...

###########################################################################
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        channel = message.channel
        await channel.send("Need help? Try:\n" +
                           ".weather for current conditions near main campus\n")

    if message.content.startswith(".weather"):
        # Run the batch file to get weather data
        subprocess.check_output(['cmd', '/c', r'/Users/YOUR-USERNAME-HERE/Desktop/getwttr.bat'])
        time.sleep(2)
        channel = message.channel
        
        # Read the weather data from the text file
        with open(r'/Users/YOUR-USERNAME-HERE/Desktop/weather.txt', 'r') as file:
            await channel.send(file.read())

###########################################################################
# Load the Discord bot token from a file
token = ""
with open(r"/Users/YOUR-USERNAME-HERE/Desktop/tok.en", 'r') as file:
    token = file.read().strip()
client.run(token)
###########################################################################
