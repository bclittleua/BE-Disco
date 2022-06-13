# Reading Data from a Log

The ability to read data from logs on the fly is extremely valid for sensitive experiments. This can be further expanded by having a script read log files regularly (via cron) and sending alerts when sensor values are outside of specified limit. 

For now we lack a dynamic sensor log, so we are going to make a file to read on demand. To do so, we first create a BASH script `getwttr.sh` to fetch local [weather data](http://wttr.in) using the cURL tool you installed in the [instructions](../instructions). The Bash script writes the data it fetches to a file, `weather.txt`. The `lview.py` bot, with the `.weather` command, 1) runs the bash script, 2) waits a second, 3) then reads and sends the contents of weather.txt.

## Instructions
1. Open the linux console (Debian for Windows, Console for Mac/Linux)
2. Navigate to the /bin folder, type `cd /home/admin/bin`
3. Make a new folder named 'lview', type `sudo mkdir lview`
4. Navigate to the new folder, `cd lview`
   - You can *always* find out where you are by typing `pwd` to Print your Working Directory
5. Create the bash script, type `sudo nano getwttr.sh`
6. Copy the few lines from getwttr.sh from github to your computer
7. Save the script with `ctrl+x`, `y`, and `enter`
8. Now you must modify the script permissions to read and write a file, as well as execute like a program:
   - type `sudo chmod +rwx getwttr.sh`
9. You can test run the script like so:
   - run with `./getwttr.sh`
   - check output with `cat weather.txt`
10. Create the python script, type `sudo nano lview.py`
11. Copy the contents of lview.py from github to your computer
12. Save the script with `ctrl+x`, `y`, and `enter`
13. For the sake of convenience, let's also modify lview.py to be executable so it doesn't require a password to run
    - Type `sudo chmod +x lview.py`
14. Create a new tok.en file and copy your token from the [instructions](../instructions):
    -Type `sudo nano tok.en` and paste your token. Close/save by repeating steps 7 or 12.
15. Now we start the bot, which will run persistently until the process is killed (or it crashes! lol)
    - Type `python lview.py`
16. AT LAST! In your Discord server you should see your bot come online and post a message.
17. Type `.help` to see your help list
18. Type `.weather` to run our bash script, read the long, and post the result to your channel.

Finally, you have created a bot (not just a one way webhook). Now you are primed to create an interactive bot and there are countless possibilities for what to do next. Your robot army isn't going to build itself, yet!
