import discord, subprocess, sys, os, time
from discord.ext import commands
###########################################################################
client = commands.Bot(command_prefix=".")
###########################################################################
@client.event
async def on_ready():
    chanID = COPY-YOUR-CHANNEL-ID-HERE # w/ dev mode enabled, rt-click desired channel and `Copy ID`
    channel = client.get_channel(chanID)
    await channel.send("Discord Bot Online.") # NOTE: this sends to a specified channel, chanID
###########################################################################
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        channel = message.channel
        await channel.send("Need help? Try:\n" +
            ".weather for current conditions near main campus\n")

    if message.content.startswith(".weather"):
        result = subprocess.check_output(['/home/admin/bin/lview/./getwttr.sh']);
        time.sleep(2)
        channel = message.channel
        await channel.send(open('/home/admin/bin/lview/weather.txt').read())
###########################################################################
token = ""
with open("/home/admin/bin/tok.en") as file:
    token= file.read()
client.run(token)
###########################################################################
