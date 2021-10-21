import telepot, json, time
from telepot.loop import MessageLoop
from ChatBot import R2D2

with open("token.json") as jsonFile:
    jsonF = json.load(jsonFile)

telegram = telepot.Bot(jsonF)
bot = R2D2("R2D2")

def ReceberMensagem(msg):
    frase = bot.listen(phrase=msg["text"])
    resposta = bot.think(frase)
    bot.speak(resposta)
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)
    telegram.sendMessage(chat_id, resposta)

    """if content_type == 'text':
       # telegram.sendMessage(chat_id, msg['text'])
        telegram.sendMessage(chat_id, "ola, tudo bem?")"""

MessageLoop(telegram, ReceberMensagem).run_as_thread()
print ('Executando ...')

# Keep the program running.
while 1:
    time.sleep(10)