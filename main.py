import os
import time
import requests, random
from dhooks import Webhook
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer") # Sets console name.

time.sleep(0.3)

hook = input("[>>] Enter your webhook: ") # Prompts you to enter a webhook

time.sleep(0.1)
print('[>>] What would you like to send to the webhook?')
hookmessage = input('[>>] ') # Prompts you to enter a message e.g 'Hello', '@everyone', 'Nuked by youruser#0000'
print('[>>] You have chose the message:', hookmessage)
warning = input('[>>] Press enter to start')
