# Setting up Python and Dependencies

## For Windows Users Only, OPTION 1: Installing Windows Subsystem for Linux
The best method to use all the tools in this repo is to install Windows Subsystem for Linux (WSL), which allows you to run a Linux OS in a window. That sounds complicated, but it is very easy:
1. Turn on Windows Dev mode, click `Start Menu > Settings > Update & Security > For Developers`
   ![](https://www.groovypost.com/wp-content/uploads/2016/05/bash-1.png)
2. Open optionalfeatures menu, open start menu and type `optionalfeatures`, then click on the Best Matched 'Run command'
3. Find WSL, check the box, and click `OK`
   ![](https://www.groovypost.com/wp-content/uploads/2016/05/bash-2.png)
4. Allow Install to complete and Reboot when prompted.
5. Install the Debian Linux distro 
   - Goto the [Windows Store](https://aka.ms/wslstore)
   - Click on Debian
   - Click the `Get` button
   - Allow install to complete (no reboot required here)
6. You should now see `Debian` under your Start Menu. Click to run!
7. Open Debian from your start menu (first use will take a few minutes to setup)
   - choose a username, use `admin`
   - create a password when prompted

## For Windows Users Only, OPTION 2: Install Python for Windows
1. Download the latest Stable Release of the 64-bit Python installer here: [Python for Windows](https://www.python.org/downloads/windows/)
2. Follow the instructions here to complete installation: [Python Installation Windows](https://docs.python.org/3/using/windows.html#windows-full)
   - IMPORTANT! Be sure to check the box to 'Add Python 3.x to PATH'

## Mac OSX Users, how to install Python:
1. Download the latest Stable Release of Python from here (top of left side column): [Python for Mac OSX](https://www.python.org/downloads/macos/)
2. Look at this page for step-by-step instructions: [Python Installation OSX](https://docs.python.org/3/using/mac.html) (no sense copying all that here, lol)

# Installing Python and Dependencies
1. WINDOWS: Open DebianWSL (option 1), Command Prompt or Powershell (option 2)
   MAC/Linux: Open a console to command line 
2. Make yourself a root user by typing `sudo -i`
3. Type `apt-get update` to update package manager
4. Installing Python3.x with `apt` package manager:
   - type `apt-get install python-is-python3` to install latest version
   - type `python --version` to verify python3.x installed correctly, must be 3.4 or greater!
5. Install the Python package manager `pip`:
   - type `apt-get install pip`
   - update pip by typing `pip install --upgrade pip`
6. Installing dependencies for projects in this repo:
    - Discord lib(s): `pip install discord`
    - Discord Webhook: 'pip install discord-webhook'
    - Request tools: `pip install requests`    - 
    - Youtube tools lib: `pip install youtube_dl`
    - Curl, command line web browswer: `apt-get install curl`    
7. When complete, verify dependencies were installed by typing `pip list`

# First Time Discord Setup
1. First create a discord account at https://discord.com/. 
   - Strongly suggest you set up 2FA, but skip this for now to save time.
   - Also in the interest of time, please run in browser if you don't already have the discord app installed on your computer.
2. Setup developer mode: 
   - toggle `User Settings > Advanced > Developer Mode` to ON
3. Join server I prepped for class (link in zoom)
4. Create your own discord server
5. Create a webhook:
   - `Server Settings > Integrations > Add Webook`
   - Give it a fun name and assign a channel (#general is ok)
   - click `Copy Webhook URL` and paste the URL to notepad (used later for hook.py)
6. Goto https://discord.com/developers/applications
7. Click `New Application`
8. Give it a unique name
9. Click `Bot` on left hand menu
10. ~click on `Add Bot`,~    
11. ~then `Yes, do it!`~
12. Click on `Reset Token`, then `Yes, do it!`
13. Copy the token ID to notepad (used later for `tok.en`)
14. Toggle 'Public Bot' to ON
15. Toggle 'Message Content Intent' to ON
16. Leave the other 3 options OFF
17. Click on 'OAuth2' on left hand menu
18. Check the box next to 'bot'
19. Copy Client ID to notepad for record
20. Copy the Generated URL for record, which should look like this:
    - https://discord.com/api/oauth2/authorize?client_id=0000000000000000&permissions=8&scope=bot 
    - replace all the zeros in this URL with the client_id you copied earlier (step 13)


# Optional Stuff:
- The music bot requires the ffmpeg codec to function.
    - Windows/Linux users can install with a package manager like apt: `apt-get install ffmpeg`
    - Mac users can also install with a package manager, but need to install a package manager first. I recommend Homebrew at http://brew.sh: `brew install ffmpeg`
