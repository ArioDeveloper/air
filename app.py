from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import dbCon

app = Client(
    "bot",
    api_id=1300697,
    api_hash="d78bcfa88c1b9abd71c58d1b9cdf52d8"
)

db = dbCon

enText = {
"start":"""Hi!

With @ETHtokenExplorer_bot you can track transactions with your wallets and check the current balance of your wallets.

To start working with bot, click the "Add Wallet" button and send the address of your wallet.""",
'key1':'Get balance',
'key2':'Add wallet',
'key3':"Settings",
'key4':'Feedback',
'key5':'Donate',
"key6":"Airdrops & bounties",
"key7":"refral",
"refText":"you can send your link for frinds to get refreal \nyour link:\n",
"botId":"TestingArioBot",
"sendFeedback":"send your Feedback:",
"sentFeedback":"your message sent for admins"}

admins = [524344586]

def start (id):
	    app.send_message(id,enText['start'],
        reply_markup=ReplyKeyboardMarkup(
            [
                [enText['key1']],  # First row
                [enText['key2'], enText['key3']],
                [enText["key6"],enText["key4"],enText["key7"]],
                [enText['key5']]
            ],
            resize_keyboard=True  # Make the keyboard smaller
        )
    )

def newRef (ref , id):
	global enText
	db.setRef(id , db.getRef(id)+1)
	app.send_message(id , f"you have new refral by {ref} , your refrals :{db.getRef(id)}")
	
def sendRefral(id):
    app.send_message(id,f"your refrals : {db.getRef(id)}\n" +enText["refText"]+f"t.me/{enText['botId']}?start={id}")

def sendFeedback(message):
    db.setStep(message.chat.id , 0)
    refraled = db.getRefraled(message.chat.id)
    for i in admins:
        app.send_message(i , f"new Feedback from {message.chat.id} \nrefraled by{refraled}\nmessage : {message.text} ")
    app.send_message(message.chat.id ,enText["sentFeedback"] )


@app.on_message()
def main(client,message):
    if message.chat.type == "private":
        if "/start" in message.text:
            try:
              
              db.addUser(message.chat.id , message.chat.first_name,0,"en")
              if len(message.text.split(" "))==2:
              	newRef(message.chat.id,message.text.split(" ")[1])            
            except Exception as error:
                print(error)
          
            start(message.chat.id)
        elif message.text == enText["key7"]:
            sendRefral(message.chat.id)

        elif message.text == enText["key4"]:
            app.send_message(message.chat.id,enText["sendFeedback"])
            db.setStep(message.chat.id,2)
        
        elif db.getStep(message.chat.id) == 2:
            sendFeedback(message)
            
            
app.run()