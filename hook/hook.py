################################################
####### SUMMER ENGINEERING ACADEMY 2022 ########
########╔╗#┬┌─┐┌─┐┬#┬┌─┐┌┬┐┌─┐┌┬┐┌─┐############
########╠╩╗││#│└─┐└┬┘└─┐#│#├┤#│││└─┐############
########╚═╝┴└─┘└─┘#┴#└─┘#┴#└─┘┴#┴└─┘############
########╔═╗┌┐┌┌─┐┬┌┐┌┌─┐┌─┐┬─┐┬┌┐┌┌─┐###########
########║╣#││││#┬││││├┤#├┤#├┬┘│││││#┬###########
########╚═╝┘└┘└─┘┴┘└┘└─┘└─┘┴└─┴┘└┘└─┘###########
# COLLEGE OF ENGINEERING,UNIVERSITY OF ARIZONA #
################################################
# Sends a message to a Discord Server/Channel via webhook. To create a webhook:
# 1) Go to your Discord Server Settings > Integrations > Webhooks and click 'Create Webhook' or 'New Webhook'
# 2) Give webhook a name and specify a channel if different than #general
# 3) Copy the webhook URL and paste it below on line 25 where specified.
# Dependencies: discord tools library, <pip install discord-webhook>
# Example usage of this script command line:
#   MAC or LINUX: python /path/to/file/hook.py "Message to send to discord channel specified in webhook settings."
#   WINDOWS: python C:\path\to\file\hook.py "message content"
#
# Discord-Webhook reference: https://pypi.org/project/discord-webhook/
#
# need this ↓ to parse the argument/message from the CLI to send, line 35
import sys
# required ↓ to use the webhook function from discord tools lib
from discord_webhook import DiscordWebhook

# the following indented lines define the 'send' function called on line 35
def send (message):
    # tells ↓ webhook function where to go
    webhook = DiscordWebhook(url="COPY-WEBHOOK-URL-HERE", content=message) 
    # functionally ↓: use webhook to send the first arg after you type ..\hook.py, the "message content"
    response = webhook.execute()
    
# everthing before now is just the set up, the next line is the only 'command' this script performs
send( sys.argv[1] )
