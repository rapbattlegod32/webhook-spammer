import os
import time
import requests
from dhooks import Webhook
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer") # Sets console name.

time.sleep(0.3)

webhookinput = input("[>>] Enter your webhook: ") # Prompts you to enter a webhook

discordwebhook = webhookinput

time.sleep(0.1)
print('[>>] What would you like to send to the webhook?')
hookmessage = input('[>>] ') # Prompts you to enter a message e.g 'Hello', '@everyone', 'Nuked by youruser#0000'
warning = input('[>>] Press enter to start') # When the enter key is pressed it starts the webhook

data = {"content": hookmessage}
response = requests.post(discordwebhook, json=data)
