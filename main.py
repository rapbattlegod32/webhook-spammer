import os
import time
import requests
from dhooks import Webhook
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer") # Sets console name.

time.sleep(0.3)

webhookinput = input("[>>] Enter your webhook: ") # Prompts you to enter a webhook

discordwebhook  = webhookinput

print('[>>] What would you like to send to the webhook?')
hookmessage = input('[>>] ') # Prompts you to enter a message e.g 'Hello', '@everyone'
time.sleep(0.2)
print("[>>] How many times do you want it to send?")
amountofmessages = input('[>>] ')

start = time.time()
for i in range(0,int(amountofmessages)):
    data = {"content": hookmessage, "amount": amountofmessages}
    response = requests.post(discordwebhook, json=data)
    print(response.status_code)
end = time.time()
print('Completed in: ', end - start,"seconds") # Measures the time that it took.

with open("spammode.json","r") as f:
    webhookdata = json.load(f)

webhookdata[f"Webhook: "] = discordwebhook
webhookdata[f"Message Sent: "] = hookmessage
webhookdata[f"Times Sent: "] = amountofmessages
webhookdata[f"Time Took: "] = end - start ,"seconds"
webhookdata[f"Status Code: "] = response.status_code

with open("spammode.json","w") as f:
     json.dump(webhookdata,f,indent=4)

time.sleep(10000)

hookmessage = input('[>>] ') 
data = {"content": hookmessage}
response = requests.post(discordwebhook, json=data)
print(response.status_code)
