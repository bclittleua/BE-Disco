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
10. 
