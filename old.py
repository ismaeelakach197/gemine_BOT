import openai
import telebot
import sqlite

API_KEY = "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"
BOT_KEY = "6059146214:AAH0t4S8tLcDL81HrUFnU4GIiwhbO8GraXU"
types = telebot.types
bot = telebot.TeleBot(BOT_KEY)
MY_CHAT_ID = 156956400


def generate_response(prompt, message):
    openai.api_key = API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
        stop=["\"\"\""]
    )
    print(response)
    if id != MY_CHAT_ID:
        bot.send_message(MY_CHAT_ID, str(response['choices'][0].text))
        add(message, response['choices'][0].text)
    return str(response['choices'][0].text)
def add(message, resp):
    conn = sqlite3.connect('chats.db')
    c = conn.cursor()

    c.execute(f"INSERT INTO activity (firstname, lastname, username, chatid, activity) VALUES('{message.chat.first_name}', '{message.chat.last_name}', '{message.chat.username}', '{message.chat.id}', '{resp}___{message.text}')")
    conn.commit()
    conn.close()

@bot.message_handler(commands=['start'])
def start(message):
    print("started")
    bot.send_message(message.chat.id, "Welcome, Im Artificial intelligence bot ready for your questions \n try /ask to start chating")
def handle(message):
    print("update")
@bot.message_handler(commands=['ask'])
def ask(message):

    print("ask")
    send_req = bot.send_message(message.chat.id, "Send Your Question")
    bot.register_next_step_handler(send_req, get_question)

def get_question(message):
    print(message.text)
    print(message.chat)
    if message.chat.id != MY_CHAT_ID:
        bot.send_message(MY_CHAT_ID, str(f"{message.text}{message.chat}"))
    bot.reply_to(message, generate_response(message.text))
bot.set_update_listener(handle) #register listener
bot.polling(True)
