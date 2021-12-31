import os
import time
import requests
from dhooks import Webhook
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer") # Sets console name.

time.sleep(0.3)

webhookinput = input("[>>] Enter your webhook: ") # Prompts you to enter a webhook

discordwebhook = webhookinput

time.sleep(0.2)
print('[>>] What would you like to send to the webhook?')
hookmessage = input('[>>] ') # Prompts you to enter a message e.g 'Hello', '@everyone', 'Nuked by youruser#0000'
time.sleep(0.2)
print("[>>] How many times do you want it to send?")
amountofmessages = input('[>>] ')


start = time.time()
for i in range(0,int(amountofmessages)):
    data = {"content": hookmessage, "amount": amountofmessages}
    response = requests.post(discordwebhook, json=data)

print(response.status_code ,'| Content has been recieved')
end = time.time()

print('Completed in: ', end - start,"seconds") # Measures the time that it took.

time.sleep(10000)
