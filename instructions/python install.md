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

    
## Not Required:
- The music bot requires the ffmpeg codec to function.
    - Windows users can find instructions here: https://www.wikihow.com/Install-FFmpeg-on-Windows
    - Linux users can install with a package manager like apt: `<apt-get install ffmpeg>`
    - Mac users can also install with a package manager, but need to install a package manager first. I recommend Homebrew at http://brew.sh: `<brew install ffmpeg>`
