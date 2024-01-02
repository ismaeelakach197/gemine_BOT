import google.generativeai as genai
import telebot

genai.configure(api_key="AIzaSyB4zIgRmP0M9tH6pZaUStAkM1mvYPc271k")
model = genai.GenerativeModel('gemini-pro')
API_KEY = "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"
BOT_KEY = "6059146214:AAH0t4S8tLcDL81HrUFnU4GIiwhbO8GraXU"
types = telebot.types
bot = telebot.TeleBot(BOT_KEY)
MY_CHAT_ID = 156956400


def generate_response(prompt):
    response = model.generate_content(prompt)
    res = response.text
    return res

@bot.message_handler(commands=['start'])
def start(message):
    print("started")
    bot.send_message(message.chat.id, "Welcome, Im Artificial intelligence bot ready for your questions \n try /ask to start chating")

@bot.message_handler(commands=['ask'])
def ask(message):
    # frequency = 1000  # Set Frequency To 2500 Hertz
    # duration = 250  # Set Duration To 1000 ms == 1 second
    # winsound.Beep(frequency, duration)
    print("ask")
    send_req = bot.send_message(message.chat.id, "Send Your Question")
    bot.register_next_step_handler(send_req, get_question)

def get_question(message):
    print(message.text)
    print(message.chat)
    if message.chat.id != MY_CHAT_ID:
        if message.chat.photo == None:
            bot.send_message(MY_CHAT_ID, str(f"{message.text}{message.chat}"))
        else:
            print("photo")
    bot.reply_to(message, generate_response(message.text))

bot.polling()
