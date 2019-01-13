# libraries here
# --------------
import telepot
import telegram as telegram
import random

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
            bot.sendMessage(chat_id, text="<b>Ciao %s</b>, sono ancora in fase di sviluppo, ma prima o poi sarò anche io una AI"%name, parse_mode=telegram.ParseMode.HTML)
        
        # help command
        # ------------
        if txt == "/help@PythonAndroidbot":
            var_lettura = open("/Users/name/directory/help.txt", "r").read()
            bot.sendMessage(chat_id, text=var_lettura) #here put the file help.txt and write on it wat you want

        # custom reactions
        # ----------------
        if txt.upper() == 'HEY GOOGLE' or txt.upper() == 'OK GOOGLE':
            bot.sendMessage(chat_id, text="Ciao %s, come posso aiutarti?"%name)
            print("[%s] used OK GOOGLE"%username)

        if txt.upper() == 'GOOGLE LAVORI PER LA CIA?' or txt.upper() == 'GOOGLE LAVORI PER LA CIA':
            bot.sendMessage(chat_id, text="Shut the FUCK UP!")
            print("[%s] used CIA" %username)

        if txt.upper() == 'GOOGLE RACCONTAMI UNA BARZELLETTA' or txt.upper() == 'GOOGLE BARZELLETTA':
            var_lettura = open("/Users/name/directory/esempio.txt", "r").read()
            bot.sendMessage(chat_id, text=var_lettura) #here put the file esempio.txt and write on it what you want
            print("[%s] used BARZELLETTA" %username)

        if txt.upper() == 'COME STAI GOOGLE?' or txt.upper() == 'COME STAI GOOGLE' or txt.upper() == 'GOOGLE COME STAI?' or txt.upper() == 'GOOGLE COME STAI':
            bot.sendMessage(chat_id, text="Io sto bene %s, grazie per avermelo chiesto!"%name)
            print("[%s] used COME STAI" %username)

        if txt.upper() == 'CHE FAI GOOGLE?' or txt.upper() == 'CHE FAI GOOGLE' or txt.upper() == 'COSA STAI FACENDO GOOGLE?' or txt.upper() == 'COSA STAI FACENDO GOOGLE':

            var_numero = random.randint(1,4)
            if var_numero == 1:
                bot.sendMessage(chat_id, text="Stavo leggendo informazioni interessanti su Wikipedia")


            if var_numero == 2:
                bot.sendMessage(chat_id, text="Stavo guardando video di gattini su Youtube insieme a ...")


            if var_numero == 3:
                bot.sendMessage(chat_id, text="Sto finendo una serie su Netflix non disturbarmi!")


            if var_numero == 4:
                bot.sendMessage(chat_id, text="Stavo progettando un attacco informatico ai server Xiaomi insieme a Lorenzo")

            print("[%s] used CHE FAI" %username)

        if 'SIRI' in txt.upper():
            bot.sendMessage(chat_id, text="Non nominate quell'ammasso di If statement")
            print("[%s] used SIRI" %username)

        if 'CORTANA' in txt.upper():
            bot.sendMessage(chat_id, text="Cortana la putt...")
            print("[%s] used CORTANA" %username)

        if 'GOOGLE COSA PENSI DI' in txt.upper():
            var_numero = random.randint(1, 4)
            if var_numero == 1:
                bot.sendMessage(chat_id, text="preferirei non pronunciarmi")

            if var_numero == 2:
                bot.sendMessage(chat_id, text="risponderà a questa domanda ...")

            if var_numero == 3:
                bot.sendMessage(chat_id, text="Al momento sono irraggiungibile, riprova tra MAI")

            if var_numero == 4:
                bot.sendMessage(chat_id,
                                text="Perchè me lo chiedi che tanto sai già che non so che dirti, i dev sono persone etiche, se dici quello che pensi ti vanno tutti contro.\n"
                                     "La gente vuole solo avere ragione senza informarsi, vedi i NO-VAX e i TERRAPIATTISTI. Che ne penso? FOTTE SEGA, vivi e lascia vivere")
                print("[%s] used COSA PENSI" %username)

        if txt.upper() == 'CIAO GOOGLE':
            bot.sendMessage(chat_id, text='Ciao a te, %s'%name)

        if txt.upper() == 'BUONASERA GOOGLE':
            bot.sendMessage(chat_id, text='Buonasera a te, %s'%name)

        if 'BUONANOTTE' in txt.upper():
            bot.sendMessage(chat_id, text='Buonanotte a te, %s.\nSogni d\'oro'%name)

        if 'BUONGIORNO' in txt.upper():
            bot.sendMessage(chat_id, text='Buongiorno %s'%name)

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
