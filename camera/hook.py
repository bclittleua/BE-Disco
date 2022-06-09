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
# 3) Copy the webhook URL and paste it below on line 22 where specified.
# Dependencies: discord tools library, <pip install discord>
# Example usage of this script command line:
#   LINUX: python /path/to/file/hook.py "Message to send to discord channel specified in webhook settings."
#   WINDO: python C:\path\to\file\hook.py "message content"

import sys # need this to parse the argument/message from the CLI to send, line 26
from discord import Webhook, RequestsWebhookAdapter # required to use the webhook function from discord tools lib

def send (message): # the following indented lines define the 'send' function called on line 26
    webhook = Webhook.from_url("COPY-WEBHOOK-URL-HERE", adapter=RequestsWebhookAdapter()) # tells webhook function where to go
    webhook.send(message) # functionally: use webhook to send the first arg after you type ..\hook.py, the "message content"

send( sys.argv[1] ) # everthing before now is just the set up, this one line is the only 'command' this script performs.
