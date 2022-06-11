# Installing Python 3.4+
For Windows, Mac OSX, Linux, and Raspberry Pi


1. Download latest version here: https://www.python.org/downloads/
2. Run the installer
    - Be sure to check box that says 'Add Python 3.x to PATH' for windows
![Example](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
3. After installer completes, verify in command prompt with: `<python --version>`
4. Upgrade the "python installer program" a.k.a "pip": `<python -m pip install --upgrade pip>`
    - When complete, verify in command prompt with: `<pip list>`
5. Installing dependencies for projects in this repo:
    - Discord lib(s): `<pip install discord>`
    - Youtube tools lib: `<pip install youtube_dl>`
6. When complete, verify in command prompt with: `<pip list>`

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
10. click on `Add Bot`, 
11. then `Yes, do it!`
12. Click on `Reset Token`
13. Copy the token ID to notepad (used later for `tok.en`)
14. Toggle 'Public Bot' to OFF
15. Toggle 'Presence Intent' to ON
16. Click on 'OAuth2' on left hand menu
17. Copy Client ID to notepad
18. Add new bot to your private server
    - https://discord.com/api/oauth2/authorize?client_id=0000000000000000&permissions=8&scope=bot 
    - replace all the zeros in this URL with the client_id you copied earlier

### Optional:
- The music bot requires the ffmpeg codec to function.
    - Windows users can find instructions here: https://www.wikihow.com/Install-FFmpeg-on-Windows
    - Linux users can install with a package manager like apt: `<apt-get install ffmpeg>`
    - Mac users can also install with a package manager, but need to install a package manager first. I recommend Homebrew at http://brew.sh: `<brew install ffmpeg>`
