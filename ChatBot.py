import json
import sys
import os
import subprocess as sp

class R2D2():
    #construtor da classe
    def __init__(self, name):
        try:
            memory = open(name + '.json', 'r')
        except FileNotFoundError:
            memory = open(name + '.json', 'w')
            memory.write('[["R2D2"], {"oi": "Olá! Qual seu nome?", "tchau": "Tchau! Tchau!"}]')
            memory.close()
            memory = open(name + '.json', 'r')
        
        self.name = name
        self.known, self.phrases = json.load(memory)
        memory.close()
        self.historic = [None]

    def listen(self, phrase=None):
        if phrase == None:
            phrase = input('Digite aqui: ')
        #phrase = phrase
        phrase = phrase.lower()
        return phrase
        
    def think(self, phrase):
        if phrase in self.phrases:
            return self.phrases[phrase]
        if phrase == 'Aprende':
            return 'O que você quer que eu aprenda?'
        if phrase == 'Jogar CTF':
            return "https://tryhackme.com/"
        if phrase == 'Jogar':
            return "https://brunolemos.github.io/trust/?fbclid=IwAR02exqRjzyqq3niDcqNpYKxNBj-HV6yU6VxpDdyHFN6m4GmC4WYOYpOuSw"
           
        # historic
        lastPhrase = self.historic[-1]
        if lastPhrase == None:
            lastPhrase = 'Olá! Qual seu nome?'
        if lastPhrase == 'Olá! Qual seu nome?':
            name = self.getName(phrase)
            response = self.answerName(name)
            return response
        elif lastPhrase == 'O que você quer que eu aprenda?':
            self.key = phrase
            return 'Digite o que eu devo responder:'
        elif lastPhrase == 'Digite o que eu devo responder:':
            response = phrase
            self.phrases[self.key] = response
            self.saveMemory()
            return 'Aprendido!'
        else:
            try:
                response = str(eval(phrase))
                return response
            except:
                #pass
                return 'Não entendi...'

    def getName(self, name):
        if 'Meu nome é ' in name:
            name = name[11:]
        name = name.title()
        return name
        
    def answerName(self, name):
        if name in self.known:
            if name != 'R2D2':
                phrase = 'Eaew, '
            else:
                phrase = 'https://www.youtube.com/watch?v=2-BKjnAgNgY&t=27s'
        else:
            phrase = 'Muito prazer '
            self.known.append(name)
            self.saveMemory()
        return phrase + name + '!'

    def saveMemory(self):
        memory = open(self.name + '.json', 'w')
        json.dump([self.known, self.phrases], memory)
        memory.close()

    def speak(self, phrase):
        if 'Abre link ' in phrase:
            platform = sys.platform
            command = phrase.replace('Abre link ', '')
            if 'win' in platform:
                os.startfile(command)
            if 'linux' in platform:
                try:
                    sp.Popen(command)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', command])
        else:
            print(phrase)
        self.historic.append(phrase)