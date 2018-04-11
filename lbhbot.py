from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Ladybug Bot')

conv = open('parents.txt', 'r').readlines()

bot.set_trainer(ListTrainer)

bot.train(conv)

while True: 
	request = input('You:')
	response = bot.get_respoonse(request)
	
	print('Bot: ', response)