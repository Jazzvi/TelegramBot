#coder :- Jazzvi
import serial
import sys
import time
import random
import datetime
import telepot

arduino = serial.Serial('/dev/ttyUSB0', 9600)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'A':
       bot.sendMessage(chat_id, on(11))
    elif command =='B':
       bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('Bot Token')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)

arduino.close()
