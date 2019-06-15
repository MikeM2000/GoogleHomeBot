# libraries here
# --------------
import telepot

import telegram as telegram
import random
import wikipedia
import time

# print on log.txt file the "localtime" whenever you run the bot
# --------------------------------------------------------------
localtime = time.asctime( time.localtime(time.time()) )
open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/log.txt", "a").write("\n\n{}\n\n".format(localtime))




# bot starts here
# ---------------
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # check log permission
    # --------------------
    l_message = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/log?.txt", "r").read()



    #ON_CHAT_MESSAGE reacts to user message
    #Parameters
    #----------
    #msg (dict) : message sent by the user according to telegram API

    # grab information from message
    # -----------------------------
    # user info
    name = msg["from"]["first_name"]
    username = msg["from"]["username"]
    user_id = msg["from"]["id"]
    # text of the message (filtering multiple spaces)




    # dictionaries
    # ------------
    # answers related to "CHE FAI GOOGLE?"
    google_is_doing = {1: "Stavo leggendo informazioni interessanti su <b>Wikipedia</b>",
                       2: "Stavo guardando video di gattini su Youtube insieme a Bill Gates",
                       3: "Sto finendo una serie su Netflix non disturbarmi!",
                       4: "Stavo cercando di capire come limitare ancora di più la vostra privacy, umani",
                       5: "01101110 01110101 01101100 01101100 01100001 00100000 01100100 01101001 00100000 01100011 01101000 01100101 00101100 00100000 01110110 01101111 01101100 01100101 01110110 01101111 00100000 01110011 01101111 01101100 01101111 00100000 01100110 01100001 01110010 01110100 01101001 00100000 01110000 01100101 01110010 01100100 01100101 01110010 01100101 00100000 01110100 01100101 01101101 01110000 01101111\n\n<b>Prova a tradurlo</b> ;) ",
                       6: "Non è come sembra, posso spiegare!"}

    # answer related to "GOOGLE COSA PENSI DI ..."
    google_is_thinking = {1: "Preferirei non pronunciarmi",
                          2: "Risponderà a questa domanda Siri",
                          3: "Al momento sono irraggiungibile, riprova tra <b>MAI</b>",
                          4: "sku",
                          5: "Argomento <b>INTERESSANTISSIMO</b>, {}".format(name),
                          6: "Ehm...\n\n<em>*driiiiiin*</em>\n\nScusa mi vogliono al telefono, ne parliamo dopo?"}






    # set reaction according to the input
    if content_type == 'text':
        txt = " ".join(msg['text'].split())
        msg_id = msg["message_id"]


        # start command
        # -------------
        if txt == "/start@PythonAndroidbot" or txt == "/start":
            bot.sendMessage(chat_id,
                            text="<b>Ciao {}</b>, sono ancora in fase di sviluppo, ma prima o poi sarò anche io una AI\n\n<b>ATTENZIONE</b> non sono disponibili ancora dei server stabili per hostare questo bot, quindi non è attivo 24h ma solo quando il dev ci lavora su\n<em>Mi scuso per il possibile disagio - Mike</em>".format(
                                name), parse_mode=telegram.ParseMode.HTML)

        # help command
        # ------------
        if txt == "/help@PythonAndroidbot" or txt == "/help" or txt.upper() == "COSA PUOI FARE GOOGLE" or txt.upper() == "COSA PUOI FARE GOOGLE?" or txt.upper() == "GOOGLE COSA PUOI FARE" or txt.upper() == "COSA PUOI FARE":
            var_lettura = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/help.txt", "r").read()
            bot.sendVideo(chat_id, video='https://cdn-images-1.medium.com/max/1200/1*iQ7hgqKPFrL4UNUx3tS-lA.gif')
            bot.sendMessage(chat_id, text=var_lettura, parse_mode=telegram.ParseMode.HTML)  # here put the file help.txt and write on it wat you want

        # custom reactions
        # ----------------
        if txt.upper() == 'HEY GOOGLE' or txt.upper() == 'OK GOOGLE':
            bot.sendMessage(chat_id, text="Ciao {}, come posso aiutarti?".format(name))
            # log to screen
            print("[{}][@{}] used OK GOOGLE".format(chat_type, username))

        if txt.upper() == 'GOOGLE LAVORI PER LA CIA?' or txt.upper() == 'GOOGLE LAVORI PER LA CIA':
            bot.sendMessage(chat_id, text="Shut the FUCK UP!")
            # log to screen
            print("[{}][@{}] used CIA".format(chat_type, username))

        if txt.upper() == 'GOOGLE RACCONTAMI UNA BARZELLETTA' or txt.upper() == 'GOOGLE BARZELLETTA':
            var_lettura = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/esempio.txt", "r").read()
            bot.sendMessage(chat_id, text=var_lettura)  # here put the file esempio.txt and write on it what you want
            # log to screen
            print("[{}][@{}] used BARZELLETTA".format(chat_type, username))

        if txt.upper() == 'COME STAI GOOGLE?' or txt.upper() == 'COME STAI GOOGLE' or txt.upper() == 'GOOGLE COME STAI?' or txt.upper() == 'GOOGLE COME STAI':
            bot.sendMessage(chat_id, text="Io sto bene %s, grazie per avermelo chiesto!" % name)
            # log to screen
            print("[{}][@{}] used COME STAI".format(chat_type, username))

        if txt.upper() == 'CHE FAI GOOGLE?' or txt.upper() == 'CHE FAI GOOGLE' or txt.upper() == 'COSA STAI FACENDO GOOGLE?' or txt.upper() == 'COSA STAI FACENDO GOOGLE' or txt.upper() == 'CHE FAI' or txt.upper() == 'CHE FAI?':
            var_numero = random.randint(1, 6)
            bot.sendMessage(chat_id, google_is_doing[var_numero],  parse_mode='HTML')
            # log to screen
            print("[{}][@{}] used CHE FAI".format(chat_type, username))

        if 'SIRI' in txt.upper():
            bot.sendMessage(chat_id, text="Non nominate quell'ammasso di If statement")
            # log to screen
            print("[{}][@{}] used SIRI".format(chat_type, username))

        if 'CORTANA' in txt.upper():
            bot.sendMessage(chat_id, text="Cortana la putt...")
            # log to screen
            print("[{}][@{}] used CORTANA".format(chat_type, username))

        if 'GOOGLE COSA PENSI DI' in txt.upper() or 'COSA PENSI DI' in txt.upper():
            var_numero = random.randint(1, 6)
            bot.sendMessage(chat_id, google_is_thinking[var_numero],  parse_mode='HTML')
            # log to screen
            print("[{}][@{}] used COSA PENSI".format(chat_type, username))

        if txt.upper() == 'CIAO GOOGLE':
            bot.sendMessage(chat_id, text='Ciao a te, {}'.format(name))

        if txt.upper() == 'BUONASERA GOOGLE':
            bot.sendMessage(chat_id, text='Buonasera a te, {}'.format(name))

        if 'BUONANOTTE' in txt.upper():
            bot.sendMessage(chat_id, text='Buonanotte a te, {}.\nSogni d\'oro'.format(name))

        if 'BUONGIORNO' in txt.upper():
            bot.sendMessage(chat_id, text='Buongiorno {}'.format(name))

        if 'GRAZIE GOOGLE' in txt.upper():
            bot.sendMessage(chat_id, text='Sono qui apposta, {}'.format(name))

        if 'NEXUS 5X' in txt.upper():
            bot.sendMessage(chat_id, text='Do you want some bootloop?', reply_to_message_id=msg_id, parse_mode = 'HTML')

        if '/richiedi' in txt:
            var_messaggio = txt
            var_messaggio = var_messaggio.replace("/richiedi ", "")
            bot.sendMessage(38201859, text="<b>NEW SUPPORT REQUEST</b>\n<b>Author:</b> @{}\n<b>ID:</b> {}\n\n<b>Message:</b>\n<code>{}</code>".format(username, user_id, var_messaggio), parse_mode='HTML')
            bot.sendMessage(chat_id, text="<code>Richiesta inviata correttamente!</code>", reply_to_message_id=msg_id, parse_mode='HTML')



        # New Function [17/01/2019] search a definition
        # ---------------------------------------------
        if 'GOOGLE DEFINISCI' in txt.upper():
            var_messaggio = txt.upper()
            var_messaggio = var_messaggio.replace("GOOGLE DEFINISCI ", "")
            print("{} searced a definition from Wikipedia".format(username))
            wikipedia.set_lang("it")
            try:
                definition = wikipedia.summary(var_messaggio, sentences=3)
                bot.sendMessage(chat_id, text=definition)
            except:
                bot.sendMessage(chat_id, text="Mi spiace {}, non ho trovato nulla riguardo '{}'".format(name, var_messaggio))



        


        # Admin-Only and new commands
        # ---------------------------
        if txt.upper() == '/LOGON':
            admin_id = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/admin.txt", "r").read()
            print(admin_id)
            admin_id = int(admin_id, 10)
            command_input = user_id

            if command_input == admin_id:
                bot.sendMessage(chat_id, text="Comando riservato agli admin [test]:\nLog messaggi attivato")
                open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/log?.txt", "w").write("on")
                print(l_message)



        if txt.upper() == '/LOGOFF':
            admin_id = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/admin.txt", "r").read()
            print(admin_id)
            admin_id = int(admin_id, 10)
            command_input = user_id

            if command_input == admin_id:
                bot.sendMessage(chat_id, text="Comando riservato agli admin [test]:\nLog messaggi disattivato")
                open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/log?.txt", "w").write("off")
                print(l_message)

        # actally useless
        # ---------------
        if txt == '/rb':
            admin_id = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/admin.txt", "r").read()
            admin_id = int(admin_id, 10)
            command_input = user_id

            if command_input == admin_id:
                bot.sendMessage(chat_id, text="<code>Rebooting complete!</code>", parse_mode='HTML')
                return 0



        if txt.upper() == '/SOURCE':
            bot.sendMessage(chat_id, text="<b>     Google Home Mini Bot</b>\n"
                                          "====================\n\n"
                                          "<b>Files</b>:\n<em>- Gassistant.py\n- admin.txt\n- log.txt\n- log?.txt\n- esempio.txt</em>\n\n"
                                          "<b>Languages:</b> <em>Italian</em>\n\n"
                                          "<b>Version</b>:<em> v.1.4 - stable</em>\n\n"
                                          "<b>Source</b>:  <a href=\"https://github.com/MikeM2000/GoogleHomeBot\">GitHub</a> ", parse_mode=telegram.ParseMode.HTML)

        if txt.upper() == '/MEMBERS':
            bot.sendMessage(chat_id, text='Il numero di membri del gruppo è: <b>{}</b>'.format(bot.getChatMembersCount(chat_id)), parse_mode='HTML')


        if txt.upper() == '/GOOGLEPIXEL':
            bot.sendMessage(chat_id, text='https://telegra.ph/Google-Pixel--info--recensioni--guide-06-10')

        if txt == '/feedbackg':
            bot.sendMessage(chat_id, text='<b>Come richiedere supporto o nuove funzionalità</b>\n\n/richiedi [inserire di seguito la richiesta o il feedback]\n\nEsempio:\n/richiedi funzione che manda gif di gattini', parse_mode='HTML')


        # check log permission and log on screen
        # --------------------------------------
        l_message = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/log?.txt", "r").read()
        #print("After command loop: {}".format(l_message))


        # Commands in @AOSPItalia network
        # -------------------------------
        if txt == '/nuke':
            bot.sendVideo(chat_id, video='http://4.bp.blogspot.com/-HUn5hfk8OzQ/UM_Pi-bGphI/AAAAAAAAEVY/JO-DljB1L2I/s1600/explosi%25C3%25B3n+gif.gif',
                            caption='<b>QUESTA NON E\' UN\'ESERCITAZIONE</b>\n\nRecarsi immediatamente al bunker antiatomico, ripeto <b>NON E\' UN\'ESERCITAZIONE</b>',
                            parse_mode=telegram.ParseMode.HTML)

        if txt == '/ban':
            bot.sendMessage(chat_id, text='Olè!')

        if txt == '/regole' or txt == '/regole@PythonAndroidBot':
            bot.sendMessage(chat_id, text='https://telegra.ph/Regolamento-Google-Pixel-Italia-02-17')

        if '/say' in txt:
            var_messaggio = txt
            var_messaggio = var_messaggio.replace("/say ", "")
            bot.sendMessage(chat_id, text='{}'.format(var_messaggio), parse_mode='HTML')






        # check.LOG function
        # ------------------
        if l_message == "on":
            message = txt
            open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/log.txt", "a").write("[{}][{}]: {}\n".format(chat_type, username, message))



    # BENVENUTO E ADDIO
    # -----------------
    if content_type == 'new_chat_member':
        new_user = msg["new_chat_member"]["username"]
        print(content_type)
        bot.sendMessage(chat_id, text="Benvenuto nel Gruppo @{}!\nRicordati di leggere le /regole e buona permanenza\nSe hai domande chiedi pure a me \"cosa puoi fare google?\"".format(new_user), parse_mode=telegram.ParseMode.HTML)

    if content_type == 'left_chat_member' :
        left_user = msg["left_chat_member"]["username"]
        print(content_type)
        bot.sendMessage(chat_id, text="ADDIO @{}!".format(left_user), parse_mode=telegram.ParseMode.HTML)



# Token and bot main function that keeps it in loop
# -------------------------------------------------

TOKEN = open("/Users/michelemarcucci/PycharmProjects/Bot_test_1/token.txt", "r").read() #token from file

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

while 1:
    time.sleep(10)
