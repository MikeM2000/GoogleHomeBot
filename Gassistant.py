# ------------------------------------
# G-Assistant.py
# Telegram bot developed by @mike_2000
# v.1.0 - stable
# ------------------------------------
# libraries here
# --------------
import telepot
import telegram as telegram
import random
import wikipedia

# dictionaries
# ------------
# answers related to "CHE FAI GOOGLE?"
google_is_doing = {1:"Stavo leggendo informazioni interessanti su Wikipedia",
                   2:"Stavo guardando video di gattini su Youtube insieme a ...",
                   3:"Sto finendo una serie su Netflix non disturbarmi!",
                   4:"Stavo progettando un attacco informatico ai server Xiaomi insieme a Lorenzo",
                   5: "Ca**i miei no?",
                   6: "Non è come sembra, posso spiegare!"}

# answer related to "GOOGLE COSA PENSI DI ..."
google_is_thinking = {1:"preferirei non pronunciarmi",
                      2:"risponderà a questa domanda ...",
                      3:"Al momento sono irraggiungibile, riprova tra MAI",
                      4:"Perchè me lo chiedi che tanto sai già che non so che dirti, " \
                      "i dev sono persone etiche, se dici quello che pensi ti vanno tutti contro.\n" \
                      "La gente vuole solo avere ragione senza informarsi, vedi i NO-VAX e i TERRAPIATTISTI." \
                      " Che ne penso? FOTTE SEGA, vivi e lascia vivere",
                      5: "Argomento INTERESSANTISSIMO",
                      6: "Ehm...\n\n*driiiiiin*\n\nScusa mi vogliono al telefono, ne parliamo dopo, addio."}

# bot starts here
# ---------------
def on_chat_message(msg):
    """
    ON_CHAT_MESSAGE reacts to user message

    Parameters
    ----------
    msg (dict) : message sent by the user according to telegram API
    """

    # catch info from chat
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    # set reaction according to the input
    if content_type == 'text':

        # grab information from message
        # -----------------------------
        # user info
        name = msg["from"]["first_name"]
        username = msg["from"]["username"]
        user_id = msg["from"]["id"]
        # text of the message (filtering multiple spaces)
        txt = " ".join(msg['text'].split())
        
        # start command
        # -------------
        if txt == "/start@PythonAndroidbot":
            bot.sendMessage(chat_id, text="<b>Ciao {}</b>, sono ancora in fase di sviluppo, ma prima o poi sarò anche io una AI".format(name), parse_mode=telegram.ParseMode.HTML)
        
        # help command
        # ------------
        if txt == "/help@PythonAndroidbot":
            var_lettura = open("/Users/name/directory/help.txt", "r").read()
            bot.sendMessage(chat_id, text=var_lettura) #here put the file help.txt and write on it wat you want

        # custom reactions
        # ----------------
        if txt.upper() == 'HEY GOOGLE' or txt.upper() == 'OK GOOGLE':
            bot.sendMessage(chat_id, text="Ciao {}, come posso aiutarti?".format(name))
            # log to screen
            print("{} used OK GOOGLE".format(username))

        if txt.upper() == 'GOOGLE LAVORI PER LA CIA?' or txt.upper() == 'GOOGLE LAVORI PER LA CIA':
            bot.sendMessage(chat_id, text="Shut the FUCK UP!")
            # log to screen
            print("{} used CIA".format(username))

        if txt.upper() == 'GOOGLE RACCONTAMI UNA BARZELLETTA' or txt.upper() == 'GOOGLE BARZELLETTA':
            var_lettura = open("/Users/name/directory/esempio.txt", "r").read()
            bot.sendMessage(chat_id, text=var_lettura) #here put the file esempio.txt and write on it what you want
            # log to screen
            print("{} used BARZELLETTA".format(username))

        if txt.upper() == 'COME STAI GOOGLE?' or txt.upper() == 'COME STAI GOOGLE' or txt.upper() == 'GOOGLE COME STAI?' or txt.upper() == 'GOOGLE COME STAI':
            bot.sendMessage(chat_id, text="Io sto bene %s, grazie per avermelo chiesto!"%name)
            # log to screen
            print("{} used COME STAI".format(username))

        if txt.upper() == 'CHE FAI GOOGLE?' or txt.upper() == 'CHE FAI GOOGLE' or txt.upper() == 'COSA STAI FACENDO GOOGLE?' or txt.upper() == 'COSA STAI FACENDO GOOGLE':

            var_numero = random.randint(1,6)
            bot.sendMessage(chat_id, google_is_doing[var_numero])
            # log to screen
            print("{} used CHE FAI".format(username))

        if 'SIRI' in txt.upper():
            bot.sendMessage(chat_id, text="Non nominate quell'ammasso di If statement")
            # log to screen
            print("{} used SIRI".format(username))

        if 'CORTANA' in txt.upper():
            bot.sendMessage(chat_id, text="Cortana la putt...")
            # log to screen
            print("{} used CORTANA".format(username))

        if 'GOOGLE COSA PENSI DI' in txt.upper():
            var_numero = random.randint(1, 6)
            bot.sendMessage(chat_id, google_is_thinking[var_numero])
            # log to screen
            print("{} used COSA PENSI".format(username))

        if txt.upper() == 'CIAO GOOGLE':
            bot.sendMessage(chat_id, text='Ciao a te, {}'.format(name))

        if txt.upper() == 'BUONASERA GOOGLE':
            bot.sendMessage(chat_id, text='Buonasera a te, {}'.format(name))

        if 'BUONANOTTE' in txt.upper():
            bot.sendMessage(chat_id, text='Buonanotte a te, {}.\nSogni d\'oro'.format(name))

        if 'BUONGIORNO' in txt.upper():
            bot.sendMessage(chat_id, text='Buongiorno {}'.format(name))
            
        # New Function [17/01/2019] search a definition
        # ---------------------------------------------
        if 'GOOGLE DEFINISCI' in txt.upper():
            var_messaggio = txt.upper()
            var_messaggio = var_messaggio.replace("GOOGLE DEFINISCI ", "")
            print("{} searced a word".format(username))
            wikipedia.set_lang("it")
            try:
                definition = wikipedia.summary(var_messaggio, sentences=3)
                bot.sendMessage(chat_id, text=definition)
            except:
                bot.sendMessage(chat_id, text="Mi spiace {}, non ho trovato nulla riguardo '{}'".format(name, var_messaggio))


        # Commands in @AOSPItalia network
        # -------------------------------
        if txt == '/nuke':
            bot.sendMessage(chat_id, text='<b>QUESTA NON E\' UN\'ESERCITAZIONE</b>\n\nRecarsi immediatamente al bunker antiatomico, ripeto <b>NON E\' UN\'ESERCITAZIONE</b>', parse_mode=telegram.ParseMode.HTML)

        if txt == '/ban':
            bot.sendMessage(chat_id, text='Chi è lo sfigato stavolta? -_-')


# Token and bot main function that keeps it in loop
# -------------------------------------------------

TOKEN = '<INSERIRE TOKEN QUI>'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

import time
while 1:
    time.sleep(10)
