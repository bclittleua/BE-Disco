import discord, subprocess, sys, os, time

@client.event
async def on_ready():
    chanID = Your-channel_ID-here-no-quotes # w/ dev mode enabled, rt-click desired channel and `Copy ID`
    channel = client.get_channel(chanID)
    await channel.send("Discord Bot Online.") # NOTE: this sends to a specified channel, chanID
###########################################################################
@client.event
async def on_message(message):
    if message.content.startswith(".help"):
        channel = message.channel
        await channel.send("Need help? Try:\n" +
            ".weather for current conditions near main campus\n" +
    if message.content.startswith(".weather"):
        result = subprocess.check_output(['/path/to/your/files/getwttr.sh']);
        time.sleep(2)
        channel = message.channel
        await channel.send(open('/path/to/your/files/weather.txt').read())
###########################################################################
token = ""
with open("/path/to/your/files/tok.en") as file:
    token= file.read()
client.run(token)
###########################################################################
