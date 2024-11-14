import discord, subprocess, sys, os, time
from discord.ext import commands

###########################################################################
client = commands.Bot(command_prefix=".")
###########################################################################

@client.event
async def on_ready():
    chanID = COPY-YOUR-CHANNEL-ID-HERE  # Right-click desired channel with dev mode enabled and `Copy ID`
    channel = client.get_channel(chanID)
    await channel.send("Discord Bot Online.")  # NOTE: Sends to a specified channel, chanID

###########################################################################
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        channel = message.channel
        await channel.send("Need help? Try:\n" +
                           ".weather for current conditions near main campus\n")

    if message.content.startswith(".weather"):
        # Replace this with a Windows-compatible way to get weather data
        result = subprocess.check_output(['powershell', '-Command', r'C:\path\to\getwttr.ps1']) #this path needs to be updated!
        time.sleep(2)
        channel = message.channel
        with open(r'C:\path\to\weather.txt', 'r') as file:  #this path needs to be updated
            await channel.send(file.read())

###########################################################################
token = ""
with open(r"C:\path\to\tok.en", 'r') as file:   #this path needs to be updated
    token = file.read().strip()
client.run(token)
###########################################################################
