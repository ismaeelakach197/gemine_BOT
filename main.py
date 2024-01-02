import google.generativeai as genai
import telebot

genai.configure(api_key="AIzaSyB4zIgRmP0M9tH6pZaUStAkM1mvYPc271k")
model = genai.GenerativeModel('gemini-pro')
API_KEY = "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"
BOT_KEY = "6059146214:AAH0t4S8tLcDL81HrUFnU4GIiwhbO8GraXU"
types = telebot.types
bot = telebot.TeleBot(BOT_KEY)
MY_CHAT_ID = 156956400




def generate_response(message):
    response = model.generate_content(message.text)
    # res = response.text
    res = "Namquisnulla. Integermalesuada. Ininenimaarcuimperdietmalesuada. Sedvellectus. Donecodiourna, tempusmolestie, porttitorut, iaculisquis, sem. Phasellusrhoncus. Aeneanidmetusidvelitullamcorperpulvinar. Vestibulumfermentumtortoridmi. Pellentesqueipsum. Nullanonarculacinianequefaucibusfringilla. Nullanonlectussednislmolestiemalesuada. Proinintellussitametnibhdignissimsagittis. Vivamusluctusegestasleo. Maecenassollicitudin. Nullamrhoncusaliquammetus. Etiamegestaswisiaerat. Loremipsumdolorsitamet, consectetueradipiscingelit. Nullamfeugiat, turpisatpulvinarvulputate, eratliberotristiquetellus, necbibendumodiorisussitametante. Aliquameratvolutpat. Nuncauctor. Maurispretiumquameturna. Fuscenibh. Duisrisus. Curabitursagittishendreritante. Aliquameratvolutpat. Vestibulumeratnulla, ullamcorpernec, rutrumnon, nonummyac, erat. Duiscondimentumaugueidmagnasemperrutrum. Nullamjustoenim, consectetuernec, ullamcorperac, vestibulumin, elit. Proinpedemetus, vulputatenec, fermentumfringilla, vehiculavitae, justo. Fusceconsectetuerrisusanunc. Aliquamornarewisieumetus. Integerpellentesquequamvelvelit. Duispulvinar. Loremipsumdolorsitamet, consectetueradipiscingelit. Morbigravidaliberonecvelit. Morbiscelerisqueluctusvelit. Etiamduisem, fermentumvitae, sagittisid, malesuadain, quam. Proinmattislaciniajusto. Vestibulumfacilisisauctorurna. Aliquaminloremsitametleoaccumsanlacinia. Integerrutrum, orcivestibulumullamcorperultricies, lacusquamultriciesodio, vitaeplaceratpedesemsitametenim. Phasellusetloremidfelisnonummyplacerat. Fusceduileo, imperdietin, aliquamsitamet, feugiateu, orci. Aeneanvelmassaquismaurisvehiculalacinia. Quisquetinciduntscelerisquelibero. Maecenaslibero. Etiamdictumtinciduntdiam. Donecipsummassa, ullamcorperin, auctoret, scelerisquesed, est. Suspendissenisl. Sedconvallismagnaeusem. Craspedelibero, dapibusnec, pretiumsitamet, temporquis, urna. Etiamposuerequamacquam. Maecenasaliquetaccumsanleo. Nullamdapibusfermentumipsum. Etiamquisquam. Integerlacinia. Nullaest. Nullaturpismagna, cursussitamet, suscipita, interdumid, felis. Integervulputatesemanibhrutrumconsequat. Maecenaslorem. Pellentesquepretiumlectusidturpis. Etiamsapienelit, consequateget, tristiquenon, venenatisquis, ante. Fuscewisi. Phasellusfaucibusmolestienisl. Fusceegeturna. Curabiturvitaediamnonenimvestibuluminterdum. Nullaquisdiam. Uttempuspurusatlorem. Insemjusto, commodout, suscipitat, pharetravitae, orci. Duissapiennunc, commodoet, interdumsuscipit, sollicitudinet, dolor. Pellentesquehabitantmorbitristiquesenectusetnetusetmalesuadafamesacturpisegestas. Aliquamiddolor. Classaptenttacitisociosquadlitoratorquentperconubianostra, perinceptoshymenaeos. Maurisdictumfacilisisaugue. Fuscetellus. Pellentesquearcu. Maecenasfermentum, seminpharetrapellentesque, velitturpisvolutpatante, inpharetrametusodioalectus. Sedelitdui, pellentesquea, faucibusvel, interdumnec, diam. Maurisdolorfelis, sagittisat, luctussed, aliquamnon, tellus. Etiamligulapede, sagittisquis, interdumultricies, scelerisqueeu, urna. Nullamatarcuaestsollicitudineuismod. Praesentdapibus. Duisbibendum, lectusutviverrarhoncus, dolornuncfaucibuslibero, egetfacilisisenimipsumidlacus. Namsedtellusidmagnaelementumtincidunt. Morbiametus. Phasellusenimerat, vestibulumvel, aliquama, posuereeu, velit. Nullamsapiensem, ornareac, nonummynon, lobortisa, enim. Nunctinciduntantevitaemassa. Duisanteorci, molestievitae, vehiculavenenatis, tinciduntac, pede. Nullaaccumsan, elitsitametvariussemper, nullamaurismollisquam, temporsuscipitdiamnullavelleo. Etiamcommododuiegetwisi. Doneciaculisgravidanulla. Donecquisnibhatfelisconguecommodo. Etiambibendumelitegeterat. Praesentinmauriseutortorporttitoraccumsan. Maurissuscipit, ligulasitametpharetrasemper, nibhantecursuspurus, velsagittisvelitmaurisvelmetus. Aeneanfermentumrisusidtortor. Integerimperdietlectusquisjusto. Integertempor. Vivamusacurnavelleopretiumfaucibus. Mauriselementummaurisvitaetortor. Indapibusauguenonsapien. Aliquamante. Curabiturbibendumjustononorci. Morbileomi, nonummyeget, tristiquenon, rhoncusnon, leo. Nullamfaucibusmiquisvelit. Integerinsapien. Fuscetellusodio, dapibusid, fermentumquis, suscipitid, erat. Fuscealiquamvestibulumipsum. Aliquameratvolutpat. Pellentesquesapien. Craselementum. Nullapulvinareleifendsem. Cumsociisnatoquepenatibusetmagnisdisparturientmontes, nasceturridiculusmus. Quisqueporta. Vivamusporttitorturpisacleo. Maecenasipsumvelit, consectetuereu, lobortisut, dictumat, dui. Inrutrum. Sedacdolorsitametpurusmalesuadacongue. Inlaoreet, magnaidviverratincidunt, semodiobibendumjusto, velimperdietsapienwisisedlibero. Suspendissesagittisultricesaugue. Maurismetus. Nuncdapibustortorvelmidapibussollicitudin. Etiamposuerelacusquisdolor. Praesentidjustoinnequeelementumultrices. Classaptenttacitisociosquadlitoratorquentperconubianostra, perinceptoshymenaeos. Inconvallis. Fuscesuscipitliberoegetelit. Praesentvitaearcutempornequelaciniapretium. Morbiimperdiet, maurisacauctordictum, nislligulaegestasnulla, etsollicitudinsempurusinlacus. Aeneanplacerat. Invulputateurnaeuarcu. Aliquameratvolutpat. Suspendissepotenti. Morbimattisfelisatnunc. Duisviverradiamnonjusto. Innisl. Nullamsitametmagnainmagnagravidavehicula. Mauristinciduntsemsedarcu. Nuncposuere. Nullamlectusjusto, vulputateeget, mollissed, temporsed, magna. Cumsociisnatoquepenatibusetmagnisdisparturientmontes, nasceturridiculusmus. Etiamneque. Curabiturligulasapien, pulvinara, vestibulumquis, facilisisvel, sapien. Nullamegetnisl. Donecvitaearcu. Namquisnulla. Integermalesuada. Ininenimaarcuimperdietmalesuada. Sedvellectus. Donecodiourna, tempusmolestie, porttitorut, iaculisquis, sem. Phasellusrhoncus. Aeneanidmetusidvelitullamcorperpulvinar. Vestibulumfermentumtortoridmi. Pellentesqueipsum. Nullanonarculacinianequefaucibusfringilla. Nullanonlectussednislmolestiemalesuada. Proinintellussitametnibhdignissimsagittis. Vivamusluctusegestasleo. Maecenassollicitudin. Nullamrhoncusaliquammetus. Etiamegestaswisiaerat. Loremipsumdolorsitamet, consectetueradipiscingelit. Nullamfeugiat, turpisatpulvinarvulputate, eratliberotristiquetellus, necbibendumodiorisussitametante. Aliquameratvolutpat. Nuncauctor. Maurispretiumquameturna. Fuscenibh. Duisrisus. Curabitursagittishendreritante. Aliquameratvolutpat. Vestibulumeratnulla, ullamcorpernec, rutrumnon, nonummyac, erat. Duiscondimentumaugueidmagnasemperrutrum. Nullamjustoenim, consectetuernec, ullamcorperac, vestibulumin, elit. Proinpedemetus, vulputatenec, fermentumfringilla, vehiculavitae, justo. Fusceconsectetuerrisusanunc. Aliquamornarewisieumetus. Integerpellentesquequamvelvelit. Duispulvinar. Loremipsumdolorsitamet, consectetueradipiscingelit. Morbigravidaliberonecvelit. Morbiscelerisqueluctusvelit. Etiamduisem, fermentumvitae, sagittisid, malesuadain, quam. Proinmattislaciniajusto. Vestibulumfacilisisauctorurna. Aliquaminloremsitametleoaccumsanlacinia. Integerrutrum, orcivestibulumullamcorperultricies, lacusquamultriciesodio, vitaeplaceratpedesemsitametenim. Phasellusetloremidfelisnonummyplacerat. Fusceduileo, imperdietin, aliquamsitamet, feugiateu, orci. Aeneanvelmassaquismaurisvehiculalacinia. Quisquetinciduntscelerisquelibero. Maecenaslibero. Etiamdictumtinciduntdiam. Donecipsummassa, ullamcorperin, auctoret, scelerisquesed, est. Suspendissenisl. Sedconvallismagnaeusem. Craspedelibero, dapibusnec, pretiumsitamet, temporquis, urna. Etiamposuerequamacquam. Maecenasaliquetaccumsanleo. Nullamdapibusfermentumipsum. Etiamquisquam. Integerlacinia. Nullaest. Nullaturpismagna, cursussitamet, suscipita, interdumid, felis. Integervulputatesemanibhrutrumconsequat. Maecenaslorem. Pellentesquepretiumlectusidturpis. Etiamsapienelit, consequateget, tristiquenon, venenatisquis, ante. Fuscewisi. Phasellusfaucibusmolestienisl. Fusceegeturna. Curabiturvitaediamnonenimvestibuluminterdum. Nullaquisdiam. Uttempuspurusatlorem. Insemjusto, commodout, suscipitat, pharetravitae, orci. Duissapiennunc, commodoet, interdumsuscipit, sollicitudinet, dolor. Pellentesquehabitantmorbitristiquesenectusetnetusetmalesuadafamesacturpisegestas. Aliquamiddolor. Classaptenttacitisociosquadlitoratorquentperconubianostra, perinceptoshymenaeos. Maurisdictumfacilisisaugue. Fuscetellus. Pellentesquearcu. Maecenasfermentum, seminpharetrapellentesque, velitturpisvolutpatante, inpharetrametusodioalectus. Sedelitdui, pellentesquea, faucibusvel, interdumnec, diam. Maurisdolorfelis, sagittisat, luctussed, aliquamnon, tellus. Etiamligulapede, sagittisquis, interdumultricies, scelerisqueeu, urna. Nullamatarcuaestsollicitudineuismod. Praesentdapibus. Duisbibendum, lectusutviverrarhoncus, dolornuncfaucibuslibero, egetfacilisisenimipsumidlacus. Namsedtellusidmagnaelementumtincidunt. Morbiametus. Phasellusenimerat, vestibulumvel, aliquama, posuereeu, velit. Nullamsapiensem, ornareac, nonummynon, lobortisa, enim. Nunctinciduntantevitaemassa. Duisanteorci, molestievitae, vehiculavenenatis, tinciduntac, pede. Nullaaccumsan, elitsitametvariussemper, nullamaurismollisquam, temporsuscipitdiamnullavelleo. Etiamcommododuiegetwisi. Doneciaculisgravidanulla. Donecquisnibhatfelisconguecommodo. Etiambibendumelitegeterat. Praesentinmauriseutortorporttitoraccumsan. Maurissuscipit, ligulasitametpharetrasemper, nibhantecursuspurus, velsagittisvelitmaurisvelmetus. Aeneanfermentumrisusidtortor. Integerimperdietlectusquisjusto. Integertempor. Vivamusacurnavelleopretiumfaucibus. Mauriselementummaurisvitaetortor. Indapibusauguenonsapien. Aliquamante. Curabiturbibendumjustononorci. Morbileomi, nonummyeget, tristiquenon, rhoncusnon, leo. Nullamfaucibusmiquisvelit. Integerinsapien. Fuscetellusodio, dapibusid, fermentumquis, suscipitid, erat. Fuscealiquamvestibulumipsum. Aliquameratvolutpat. Pellentesquesapien. Craselementum. Nullapulvinareleifendsem. Cumsociisnatoquepenatibusetmagnisdisparturientmontes, nasceturridiculusmus. Quisqueporta. Vivamusporttitorturpisacleo. Maecenasipsumvelit, consectetuereu, lobortisut, dictumat, dui. Inrutrum. Sedacdolorsitametpurusmalesuadacongue. Inlaoreet, magnaidviverratincidunt, semodiobibendumjusto, velimperdietsapienwisisedlibero. Suspendissesagittisultricesaugue. Maurismetus. Nuncdapibustortorvelmidapibussollicitudin. Etiamposuerelacusquisdolor. Praesentidjustoinnequeelementumultrices. Classaptenttacitisociosquadlitoratorquentperconubianostra, perinceptoshymenaeos. Inconvallis. Fuscesuscipitliberoegetelit. Praesentvitaearcutempornequelaciniapretium. Morbiimperdiet, maurisacauctordictum, nislligulaegestasnulla, etsollicitudinsempurusinlacus. Aeneanplacerat. Invulputateurnaeuarcu. Aliquameratvolutpat. Suspendissepotenti. Morbimattisfelisatnunc. Duisviverradiamnonjusto. Innisl. Nullamsitametmagnainmagnagravidavehicula. Mauristinciduntsemsedarcu. Nuncposuere. Nullamlectusjusto, vulputateeget, mollissed, temporsed, magna. Cums"
    maxn = 4000
    if len(res) > maxn:
        parts = len(res) / maxn
        for i in range(1, int(parts)):
            print(i, parts)
            if i == 1:
                #print(res[0:maxn * i])
                bot.reply_to(message, res[0:maxn * i])

            else:
                #print(res[(i - 1) * maxn:maxn * i])
                bot.reply_to(message, res[(i - 1) * maxn:maxn * i])
    else:
        print("one")
        bot.reply_to(message, res)

    if message.chat.id != MY_CHAT_ID:
        bot.send_message(MY_CHAT_ID, f"""Q:{message.text}
        CHAT:{message.chat}
        USER:{message.from_user}
        A:   {res}""")
        #     bot.send_message(MY_CHAT_ID, str(f"{message.text}{message.chat.id}"))
        #     bot.send_message(MY_CHAT_ID, str(f"{message.text} {message.from_user}"))

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
        # if message.chat.id != MY_CHAT_ID:
        #     bot.send_message(MY_CHAT_ID, str(f"{message.text}{message.chat.id}"))
        #     bot.send_message(MY_CHAT_ID, str(f"{message.text} {message.from_user}"))
        generate_response(message)
    elif message.content_type == "photo":
        print(message.json.photo[-1].file_id)
@bot.message_handler(content_types=['photo'])
def photos(message):
    print("photo")
    raw = message.json["photo"][-1]["file_id"]
    if message.chat.id != MY_CHAT_ID:
        bot.send_photo(MY_CHAT_ID, raw, message.from_user)
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
