## Motion reporting to Discord
BEST USED WITH A RASPBERRY PI

- This python3.4+ script operates in conjunction with Motion for linux/mac (https://motion-project.github.io/). 

- Example motion config included, `motion.conf`.

- Motion is very useful but I don't know of a windows varitant. However, windows users can try WSL, which is a linux kernal that runs on top of windows, no stupid dual booting required! For details on WSL check the [instruction](../instructions) page.

  - Motion runs fine in WSL/Debian for me, but it runs without a camera, lol. There's some unofficial support for USB devices in WSL [here](https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/). Also, [here](https://github.com/microsoft/WSL/issues/4103).


- Install motion with a package manager like apt: `apt-get install motion`
  - Per motion.conf, hook.py is triggered by on_event_start and on_movie_end (lines 106, 109, and 112 in motion.conf)
  - discomotion.py listens for the hooks and responds by uploading an image or video respectively
  - clean_motion.sh is run periodically by cron, once an hour recommended. deletes files older than specified time.
  - tok.en contains only the bot token created at discord.com/developers/applications





## Getting USB devices to work on WSL/Debian (WORK IN PROGRESS)
1. Using Powershell with admin privs:
   ```
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```
   - [download+install wsl2 update](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
   `wsl --set-default-version 2`
    - *if this fails, find c:\users\USERNAME\appdata\local\packages\thedebianproject...\localstate
      - rt-click, properties, advanced, uncheck `compress contents to save space`
   ```
   wsl --update
   wsl --shutdown
   ```
   - [download+install usbipd for windows](https://github.com/dorssel/usbipd-win/releases/download/v2.3.0/usbipd-win_2.3.0.msi)

2. In Debian console:
   ```
   sudo -i
   apt-get install usbipd
   apt-get install v4l-utils
   usbipd &
   su admin
   ```
   - second to last line runs usbipd in background before switching users

3. Back in Powershell:
   ```
   usbipd wsl list
   usbipd wsl attach --busid 6-2
   ```
   - replace with busid of the webcam you want to use

4. In Debian console:

   `lsusb` to verify your webcam is detected
   



ResourceLinks:
[microsoft.com dev blog](https://devblogs.microsoft.com/commandline/connecting-usb-devices-to-wsl/)
[updating wsl1 to wsl2](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)
