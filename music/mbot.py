import discord, sys
from discord.ext import commands
from music_cog import music_cog
###########################################################################
Bot = commands.Bot(command_prefix='/')
Bot.add_cog(music_cog(Bot))
###########################################################################
@Bot.event
async def on_ready():
    channel = Bot.get_channel(copy-channel-ID-here) # CHANGE THIS!
    await channel.send("Beep beep! New Bot Online")
###########################################################################
@Bot.command()
async def h(ctx):
    await ctx.send("Music Bot Commands (/h for this menu): \n "+
                   "/add songname-goes-here  to add a song to queue \n "+
                   "/pause and /resume       to toggle pause and \n "+
                   "/skip   to play next song \n "+
                   "/q or /np      to see the queue or now_playing\n\n "+
                   "/clear  stops playback and clears queue \n"+
                   "/dc     to kick bot out of voice channel \n\n"+
                   "/limits I'm not perfect and can't do some things \n\n"+
                   "queue stuck? try /skip")
###########################################################################
@Bot.command(name="limits", help="List of bot's limitations")
async def limits(ctx):
    await ctx.send("This bot cannot:\n"+
                   "- play playlists\n"+
                   "- handle quality above 192kbps (can play but sounds crappy)\n"+
                   "- be in more than one voice channel at a time\n"+
                   "  - must be /dc from previous channel\n"+
                   "- queue can't resolve some unicode chars, i.e. endash \\u2013")
###########################################################################
@Bot.command(name="rstbot", help="Resets the bot, can take up to a minute to reconnect.", hidden=True)
async def rstduffy(ctx):
    await ctx.send("Fine. I'll brb.")
    sys.exit()
###########################################################################
@Bot.command(hidden=True)
async def echo(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)
###########################################################################
token = ""
with open("tok.en") as file:
    token= file.read()
Bot.run(token)
###########################################################################
