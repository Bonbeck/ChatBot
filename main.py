import telepot, json, time
from telepot.loop import MessageLoop

with open("token.json") as jsonFile:
    jsonF = json.load(jsonFile)

telegram = telepot.Bot(jsonF)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        telegram.sendMessage(chat_id, msg['text'])

MessageLoop(telegram, handle).run_as_thread()
print ('Executando ...')

# Keep the program running.
while 1:
    time.sleep(10)