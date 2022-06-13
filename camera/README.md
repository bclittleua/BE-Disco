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

