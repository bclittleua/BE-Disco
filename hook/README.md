# Webhooks
## FYI
- API = Application Programming Interface. A way for applications to communicate, typically via the internets.
- WEBHOOK = an API that sends data in one direction via the HTTP protocol, usually referred to as a POST method
- `hook.py` is heavily commented to explain exactly what is going on
- `hook_nc.py` is all code and no comment

## Using your webhook
The first thing we are going to do is learn how to use a Discord webhook. If you followed the [instructions](../instructions) you should already have the Webhook URL copied to notepad. 
<!--
1. Copy `hook.py` (or `hook_nc.py`) code to your PC, use notepad or [notepad++](https://notepad-plus-plus.org/downloads/)
2. Paste your WEBHOOK URL where indicated in `hook.py`
3. Save `hook.py` to your desktop in a folder named `seabe`
4. From the Windows Command Prompt, type 
   - `python c:\users\YOUR-USERNAME\Desktop\seabe\hook.py "hello world!"`
-->

Windows Debian users: Make sure you are not root by typing `su admin` (the username you created while following [instructions](../instructions))
1. Copy contents of `hook.py` (or `hook_nc.py`) code to your PC, use notepad or [notepad++](https://notepad-plus-plus.org/downloads/)
2. Type `cd` to go to your home directory
3. Make a new folder named 'bin', type `mkdir bin`
4. Navigate to that bin by typing `cd bin`
5. Create a new file, type `sudo nano hook.py`
   - This opens the 'nano' editor, just like a notepad
6. Paste the hook.py code into nano
7. Paste your WEBHOOK URL where indicated in `hook.py`
8. Save the file by typing `ctrl+x` to close, and press `y` and `enter` to save.
9. To test, type:
   - `python hook.py "hello world!"`
   - NOTE: you must be in the /bin folder to call the file like this. If you are not in the /bin folder you must specify the path to the file
     - `python /home/admin/bin/hook.py "hello world!"`

If you did everything right, your message should post to the channel you specified in Discord.
