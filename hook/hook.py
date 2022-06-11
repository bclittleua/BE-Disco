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
# Dependencies: discord tools library, <pip install discord>
# Example usage of this script command line:
#   LINUX: python /path/to/file/hook.py "Message to send to discord channel specified in webhook settings."
#   WINDO: python C:\path\to\file\hook.py "message content"

# need this ↓ to parse the argument/message from the CLI to send, line 26
import sys
# required ↓ to use the webhook function from discord tools lib
from discord import Webhook, RequestsWebhookAdapter 

# the following indented lines define the 'send' function called on line 26
def send (message):
    # tells ↓ webhook function where to go
    webhook = Webhook.from_url("COPY-WEBHOOK-URL-HERE", adapter=RequestsWebhookAdapter()) 
    # functionally ↓: use webhook to send the first arg after you type ..\hook.py, the "message content"
    webhook.send(message) 

# everthing before now is just the set up, the next line is the only 'command' this script performs
send( sys.argv[1] )
