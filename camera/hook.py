#▄▄▄▄·#▪########.▄▄#·##▄·#▄▌.▄▄#·#▄▄▄▄▄▄▄▄#.•#▌#▄#·.#.▄▄#·#
#▐█#▀█▪██#▪#####▐█#▀.#▐█▪██▌▐█#▀.#•██##▀▄.▀··██#▐███▪▐█#▀.#
#▐█▀▀█▄▐█·#▄█▀▄#▄▀▀▀█▄▐█▌▐█▪▄▀▀▀█▄#▐█.▪▐▀▀▪▄▐█#▌▐▌▐█·▄▀▀▀█▄
#██▄▪▐█▐█▌▐█▌.▐▌▐█▄▪▐█#▐█▀·.▐█▄▪▐█#▐█▌·▐█▄▄▌██#██▌▐█▌▐█▄▪▐█
#·▀▀▀▀#▀▀▀#▀█▄▀▪#▀▀▀▀###▀#•##▀▀▀▀##▀▀▀##▀▀▀#▀▀##█▪▀▀▀#▀▀▀▀#
####▄▄▄#.#▐#▄##▄▄#•#▪###▐#▄#▄▄▄#.▄▄▄#.▄▄▄##▪###▐#▄##▄▄#•##
####▀▄.▀·•█▌▐█▐█#▀#▪██#•█▌▐█▀▄.▀·▀▄.▀·▀▄#█·██#•█▌▐█▐█#▀#▪#
####▐▀▀▪▄▐█▐▐▌▄█#▀█▄▐█·▐█▐▐▌▐▀▀▪▄▐▀▀▪▄▐▀▀▄#▐█·▐█▐▐▌▄█#▀█▄#
####▐█▄▄▌██▐█▌▐█▄▪▐█▐█▌██▐█▌▐█▄▄▌▐█▄▄▌▐█•█▌▐█▌██▐█▌▐█▄▪▐█#
#####▀▀▀#▀▀#█▪·▀▀▀▀#▀▀▀▀▀#█▪#▀▀▀##▀▀▀#.▀##▀▀▀▀▀▀#█▪·▀▀▀▀##
# Sends a message to a Discord Server/Channel via webhook. To create a webhook:
# 1) Go to your Discord Server Settings > Integrations > Webhooks and click 'Create Webhook' or 'New Webhook'
# 2) Give webhook a name and specify a channel if different than #general
# 3) Copy the webhook URL and past it below on line 12 where specified.
#
# Example usage of this script command line:
#   python /path/to/file/hook.py "Message you want to send to discord channel specified in webhook settings."

import sys
from discord import Webhook, RequestsWebhookAdapter

def send (message):
    webhook = Webhook.from_url("COPY-WEBHOOK-URL-HERE", adapter=RequestsWebhookAdapter())
    webhook.send(message)

send( sys.argv[1] )
