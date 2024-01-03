import google.generativeai as genai
import telebot
import sqlite3
from pathlib import Path

genai.configure(api_key="AIzaSyB4zIgRmP0M9tH6pZaUStAkM1mvYPc271k")
model = genai.GenerativeModel('gemini-pro')
API_KEY = "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"
BOT_KEY = "6059146214:AAH0t4S8tLcDL81HrUFnU4GIiwhbO8GraXU"
types = telebot.types
bot = telebot.TeleBot(BOT_KEY)
MY_CHAT_ID = 156956400


def add(message, resp):
    conn = sqlite3.connect('chats.db')
    c = conn.cursor()

    c.execute(f"INSERT INTO activity (first_name, last_name, username, chatid, activity) VALUES('{message.chat.first_name}', '{message.chat.last_name}', '{message.chat.username}', '{message.chat.id}', '{message.text}___{resp}')")
    conn.commit()
    conn.close()

def generate_response(message):
    try:
        response = model.generate_content(message.text)
        res = response.text
        maxn = 4000
        if len(res) > maxn:
            for x in range(0, len(res), maxn):
                bot.reply_to(message, res[x:x + maxn])
                add(message, res[x:x + maxn])
                print("------")
        else:
            print("one")
            bot.reply_to(message, res)
            add(message, res)

        if message.chat.id != MY_CHAT_ID:
            bot.send_message(MY_CHAT_ID, f"""Q:{message.text}
            CHAT:{message.chat}
            USER:{message.from_user}
            A:   {res}""")
            #     bot.send_message(MY_CHAT_ID, str(f"{message.text}{message.chat.id}"))
            #     bot.send_message(MY_CHAT_ID, str(f"{message.text} {message.from_user}"))
    except NameError:
        bot.send_message(message.chat.id, "Sorry but i am facing a huge number of requests right now please try again later")
        bot.send_message(MY_CHAT_ID, f"ERROR:{message} ERRORTYPE={NameError}")

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

@bot.message_handler(func=lambda message: True)
def get_question(message):
    print(message)
    if message.content_type == "text":
        print(message.text)
        if message.chat.id == MY_CHAT_ID and str(message.text).startswith("BROUD"):
            bot.broudcast(message.text[6:])
        else:
            generating = bot.reply_to(message, "Generating Response...")
        # if message.chat.id != MY_CHAT_ID:
        #     bot.send_message(MY_CHAT_ID, str(f"{message.text}{message.chat.id}"))
        #     bot.send_message(MY_CHAT_ID, str(f"{message.text} {message.from_user}"))
            generate_response(message)
            bot.delete_message(message.chat.id, generating.id)
    elif message.content_type == "photo":
        print(message.json.photo[-1].file_id)
@bot.message_handler(content_types=['photo'])
def photos(message):
    print("photo")
    print(message)
    raw = message.json["photo"][-1]["file_id"]
    print(type(message.caption))
    try:
        if type(message.caption) != None:
            analyzing = bot.reply_to(message, "Analyzing Image...")
            model = genai.GenerativeModel('gemini-pro-vision')
            file_info = bot.get_file(message.json["photo"][-1]["file_id"])
            downloaded_file = bot.download_file(file_info.file_path)
            cookie_picture = {
                'mime_type': 'image/png',
                'data': downloaded_file
            }
            prompt = message.caption
            response = model.generate_content(
                contents=[prompt, cookie_picture]
            )
            bot.delete_message(analyzing.chat.id, analyzing.id)
            bot.reply_to(message, response.text)
            if message.chat.id != MY_CHAT_ID:
                bot.send_photo(MY_CHAT_ID, raw, message.from_user, caption=message.caption)
                bot.send_message(MY_CHAT_ID, response.text)
        else:
            bot.reply_to(message, "Sorry but You Must Send Image With Caption!!!")
    except NameError:
        bot.send_message(message.chat.id,"Sorry but i am facing a huge number of requests right now please try again later")
        bot.send_message(MY_CHAT_ID, f"ERROR:{message} ERRORTYPE={NameError}")
    # path = raw + ".jpg"
    # file_info = bot.get_file(raw)
    # downloaded_file = bot.download_file(file_info.file_path)
    # with open(path, 'wb') as new_file:
    #     new_file.write(downloaded_file)
    #     new_file.close()

# def echo_message(message):
#     # frequency = 1000  # Set Frequency To 2500 Hertz
#     # duration = 250  # Set Duration To 1000 ms == 1 second
#     # winsound.Beep(frequency, duration)
#     send_req = bot.send_message(message.chat.id, "Send Your Question")
#     bot.register_next_step_handler(send_req, get_question)
bot.polling()
