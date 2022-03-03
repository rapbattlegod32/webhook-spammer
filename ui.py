import os
import time
import requests
import json
from dhooks import Webhook
import ctypes
from tkinter import *
from tkinter import messagebox
ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer") # Sets console name.

webhookinput = input("[>>] Enter your webhook: ") # Prompts you to enter a webhook

discordwebhook  = webhookinput

print('[>>] What would you like to send to the webhook?')
hookmessage = input('[>>] ') # Prompts you to enter a message e.g 'Hello', '@everyone'
time.sleep(0.2)
print("[>>] How many times do you want it to send?")
amountofmessages = input('[>>] ')

ws = Tk()
ws.title('webhook')

def send():
   start = time.time()
   for i in range(0,int(amountofmessages)):
      data = {"content": hookmessage, "amount": amountofmessages}
      response = requests.post(discordwebhook, json=data)
      print(response.status_code)
      end = time.time()
      print('Completed in: ', end - start,"seconds") # Measures the time that it took.

Button(ws, text="send", command=send).pack(pady=20)


ws.mainloop()

time.sleep(10000)
