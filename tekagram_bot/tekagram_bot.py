import time
import random
import datetime
import telepot

"""
After **inserting token** in the source code, run it:
```
$ python2.7 teka_bot.py
```
Based on [this tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi.

This bot does nothing but accepts some commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/bark` - reply with a bark Au Au
- `/tekafala` - reply with an audio of Teka saying hello
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/tecoco':
        bot.sendMessage(chat_id, 'Au Au')
    elif command == '/late':
        bot.sendMessage(chat_id, 'Au Au')
    elif command == '/bark':
        bot.sendMessage(chat_id, 'Au Au')
    elif command == '/tekafala':
        bot.sendAudio(chat_id, open('hello.mp3', 'rb'), title='Oi')

bot = telepot.Bot('TOKEN_HERE')
bot.message_loop(handle)
print 'Teka is listening ...'

while 1:
    time.sleep(10)
