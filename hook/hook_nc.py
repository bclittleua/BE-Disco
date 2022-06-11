import sys
from discord import Webhook, RequestsWebhookAdapter 

def send (message):
    webhook = Webhook.from_url("COPY-WEBHOOK-URL-HERE", adapter=RequestsWebhookAdapter()) 
    webhook.send(message) 

send( sys.argv[1] )
