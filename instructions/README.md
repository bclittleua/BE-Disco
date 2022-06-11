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

    
### Optional:
- The music bot requires the ffmpeg codec to function.
    - Windows users can find instructions here: https://www.wikihow.com/Install-FFmpeg-on-Windows
    - Linux users can install with a package manager like apt: `<apt-get install ffmpeg>`
    - Mac users can also install with a package manager, but need to install a package manager first. I recommend Homebrew at http://brew.sh: `<brew install ffmpeg>`


# First Time Discord Setup
1. First create a discord account, strongly suggest 2FA!
2. then setup developer mode, 
3. toggle user settings>advanced>developer mode ON
4. Create a new discord server, or join SEA-BE(prepared for class)
5. create a webhook:
   - server settings> integrations>view webhooks>new webook
7. give it a name and assign to a channel (#general is fine)
8. goto https://discord.com/developers/applications
9. click New Application
10. give it a unique name
11. click Bot on left hand menu
12. click on Add Bot, 
13. then 'Yes, do it!'
14. click on 'Reset Token'
15. copy the token ID to notepad
16. toggle Public Bot to OFF
17. toggle Presence Intent to ON
18. click on OAuth2
19. copy Client ID to notepad
20. add new bot to your private server
    - https://discord.com/api/oauth2/authorize?client_id=000000&permissions=8&scope=bot 
    - replace the zeros with your own client_id from above
