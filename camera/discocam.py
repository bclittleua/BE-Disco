################################################
####### SUMMER ENGINEERING ACADEMY 2022 ########
########╔╗#┬┌─┐┌─┐┬#┬┌─┐┌┬┐┌─┐┌┬┐┌─┐############
########╠╩╗││#│└─┐└┬┘└─┐#│#├┤#│││└─┐############
########╚═╝┴└─┘└─┘#┴#└─┘#┴#└─┘┴#┴└─┘############
########╔═╗┌┐┌┌─┐┬┌┐┌┌─┐┌─┐┬─┐┬┌┐┌┌─┐###########
########║╣#││││#┬││││├┤#├┤#├┬┘│││││#┬###########
########╚═╝┘└┘└─┘┴┘└┘└─┘└─┘┴└─┴┘└┘└─┘###########
# COLLEGE OF ENGINEERING,UNIVERSITY OF ARIZONA #
################################################
import discord, sys, os, subprocess, time, glob
from discord.ext import commands
###########################################################################
client = commands.Bot(command_prefix="/")
###########################################################################
@client.event
async def on_ready():
    print(f"logged in as {client.user}\n\n")
    chanID = COPY-YOUR-CHAN-ID-HERE
    channel = client.get_channel(chanID)
    time.sleep(3)
    await channel.send("Discord Bot Online.")
###########################################################################
@client.event
async def on_message(message):
    if message.content.startswith("/Motion Detected!"):
        channel = message.channel
        await channel.send("Preparing preview...")
        list_of_pics = glob.glob('/PATH/TO/YOUR/FILES/*.jpg')
        time.sleep(1)
        last_pic = max(list_of_pics, key=os.path.getctime)
        await channel.send(file=discord.File(last_pic))

    if message.content.startswith("/lpic"):
        channel = message.channel
        await channel.send("Preparing image...")
        list_of_pics = glob.glob('/PATH/TO/YOUR/FILES/.jpg')
        time.sleep(3)
        last_pic = max(list_of_pics, key=os.path.getctime)
        await channel.send(file=discord.File(last_pic))

    if message.content.startswith("/Processing") or message.content.startswith("/lvid"):
        channel = message.channel
        list_of_vids = glob.glob('/PATH/TO/YOUR/FILES/*.avi')
        time.sleep(3)
        last_vid = max(list_of_vids, key=os.path.getctime)
        await channel.send(file=discord.File(last_vid))
        await channel.send("Upload complete.")
###########################################################################
token = ""
with open("/PATH/TO/YOUR/FILES/tok.en") as file:
    token= file.read()
client.run(token)
###########################################################################
###########################################################################
