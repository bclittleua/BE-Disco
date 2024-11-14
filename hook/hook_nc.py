import sys
from discord_webhook import DiscordWebhook

def send (message):
    webhook = DiscordWebhook(url="COPY-YOUR-WEBHOOK-URL-HERE", content=message)
    response = webhook.execute()

send( sys.argv[1] )
