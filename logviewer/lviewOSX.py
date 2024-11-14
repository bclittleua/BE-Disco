import discord, subprocess, sys, os, time
from discord.ext import commands

###########################################################################
client = commands.Bot(command_prefix=".")
###########################################################################

@client.event
async def on_ready():
    chanID = COPY-YOUR-CHANNEL-ID-HERE  # Replace with your actual channel ID
    channel = client.get_channel(chanID)
    await channel.send("Discord Bot Online.")  # Sends to the specified channel

###########################################################################
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        channel = message.channel
        await channel.send("Need help? Try:\n" +
                           ".weather for current conditions near main campus\n")

    if message.content.startswith(".weather"):
        try:
            # Run the shell script to fetch weather data (update the path as needed)
            result = subprocess.check_output(['/Users/yourusername/bin/lview/getwttr.sh'])  #this path needs to be updated!
            time.sleep(2)
            
            # Read the weather data from the text file
            channel = message.channel
            with open('/Users/yourusername/bin/lview/weather.txt', 'r') as file: #this path needs to be updated!
                await channel.send(file.read())
        except Exception as e:
            await message.channel.send(f"Error fetching weather data: {str(e)}")

###########################################################################
# Load the Discord bot token from a file
token = ""
try:
    with open("/Users/yourusername/bin/lview/tok.en", 'r') as file: #this path needs to be updated!
        token = file.read().strip()
except FileNotFoundError:
    print("Error: Token file not found. Please check the path.")
    sys.exit(1)

# Run the bot
client.run(token)
###########################################################################
