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

1. Copy contents of `hook.py` (or `hook_nc.py`) code to your PC, use notepad or [notepad++](https://notepad-plus-plus.org/downloads/)
2. In debian, make sure you are not root by typing `su admin` (or the username you created while following [instructions](../instructions))
3. Type `cd /home/admin`
4. Paste your WEBHOOK URL where indicated in `hook.py`
5. Save `hook.py` to your desktop in a folder named `seabe`
6. From the Windows Command Prompt, type 
   - `python c:\users\YOUR-USERNAME\Desktop\seabe\hook.py "hello world!"`

If you did everything right, your message should post to the channel you specified in Discord.
