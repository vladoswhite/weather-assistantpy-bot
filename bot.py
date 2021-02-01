import pyowm 
import telebot

owm = pyowm.OWM('3579477a73fa6691daf55b076c6056c0')
bot = telebot.TeleBot("1633512288:AAEAt0oihjhxecO-HONRr4JvHyUJsqsssP8", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')['temp']

	otv = 'В городе ' + message.text  + ' сейчас  '  +  w.detailed_status + "\n"
	otv += "температура сейчас в районе " +  str (temp)  + "\n\n"

	if temp < 5 :
   		otv +=  ("Сейчас холодно,одевайтесь тепло,мой Властелин")
	elif temp > 20 :
   		otv +=  ("на улице тепло ,можете надевать шортики")
	else : 
		otv +=  ("прохладно, не простудитесь")
	
	bot.send_message(message.chat.id, otv)


	

bot.polling(none_stop = True )