Allows you to play music through a Discord voice channel. Check out the [documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html#ext-commands-cogs) for details on what cogs are and how to use them. 

*You only have to copy these files as you see them into a folder, change 1 line of code, and chmod 2 files!*

# How to use
1. Copy mbot.py, music_cog.py, & npformater.sh to same folder
2. Copy your bot token to tok.en in same folder
3. Edit mbot.py and paste your own channel ID on line `10`, `channel = Bot.get_channel(copy-channel-ID-here)`
4. Modify privs for npformatter.sh and initiate.sh, 
   - `sudo chmod +rwx npformatter.sh` and `sudo chmod +rwx initiate.sh`
6. Run/schedule ./initiate.sh to start bot

# Dependencies for Linux users (I use a RPi or Debian for WindowsWSL):
  - for WSL, it's best to install apt and pip packages as root with `sudo -i`, toggle back with `su username`
1. the discord lib requires python 3.4 or better
2. install ffmpeg with apt: ```apt-get install ffmpeg```
3. install ffmpeg support for python with: ```pip install ffmpeg```
4. install discord for python with: ```pip install discord```
5. install voice_client support for python with: ```python -m pip install -U discord.py[voice]```
6. install PyNaCl: ```pip install pynacl```

# Windows users:
Run this in WSL and Debian. I have [instructions](../instructions) here get you started, it is super easy.

# Set up your bot at https://discord.com/developers/applications/  
- Make sure your bot is private, toggle Public to OFF
- No intents required, disable them in bot settings
- The only scope required for OAuth2 is 'bot'
- Give your bot admin permission to make things easy, permissions=8
- Add the bot to Discord server with https://discord.com/api/oauth2/authorize?client_id=0000000000000&permissions=8&scope=bot
  - You must replace the `0000000000000` with your own client_id!
