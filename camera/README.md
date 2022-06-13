This python3.4+ script operates in conjunction with Motion for linux/mac (https://motion-project.github.io/). 

Example motion config included.

Motion is very useful but I don't know of a windows varitant. However, windows users can try WSL2, which is a linux kernal that runs on top of windows, no stupid dual booting required! For details on WSL2 check the [instruction](../instructions) page.

Install motion with a package manager like apt: `apt-get install motion`

1. Per motion.conf, hook.py is triggered by on_event_start and on_movie_end (lines 106, 109, and 112 in motion.conf)
2. discomotion.py listens for the hooks and responds by uploading an image or video respectively
3. clean_motion.sh is run periodically by cron, once an hour recommended. deletes files older than specified time.
4. tok.en contains only the bot token created at discord.com/developers/applications
