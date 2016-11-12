"""

POSTBACK ACTIONS HERE
when button is click

"""

import utils
import json
import datetime
import random

#helper
import fbutil

# action to take upon the bot click on get started
def welcome(recipient_id):
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Hi i am the PLDT bot I am created to enhance your customer experience. Are you an existing PLDT customer?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"Yes, I am",
                            "payload": "welcome_yes"
                        },
                        {
                            "type":"postback",
                            "title":"No, but I would like to be",
                            "payload":"welcome_no"
                        }
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

# postback if yes is clicked on welcome
def welcome_yes(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Glad to know that you are a pldt customer")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "I am created to enhance your customer experience.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "You can ask me anything about PLDT")

# postback if yes is clicked on welcome
def welcome_no(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "I will ask you some question to recommend the best pldt product that will suite you.")

#postback for promo_1
def promo_1(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "The new Power Plus Plan 2899 comes with up to 50 MBPS internet speed with no data cap.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "It also comes with iflix and FOX Networks Group.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "Apply now by following this link","https://shop.pldthome.com/Home/AreaCoverage?planId=1636", "Apply")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "Or upgrade your current subscription instead by following this link","https://shop.pldthome.com/Home/BufferPage?planId=1637&transaction=Upgrade&addOnId=-1", "Upgrade")

def promo_2(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "The new Speedster Plan 1899 comes with up to 10 MBPS and 50 GB monthly volume allowance.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "It also comes with a landline.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "Apply now by following this link", "https://shop.pldthome.com/Home/AreaCoverage?planId=1740", "Apply")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "Or upgrade your current subscription instead by following this link","https://shop.pldthome.com/Home/BufferPage?planId=1741&transaction=Upgrade&addOnId=-1", "Upgrade")
 
def promo_3(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "The new Fun Plan 699 comes with up to 3 MBPS at 30 GB monthly volume allowance.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Installation is free an no cash out.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "Apply now by following this link","https://shop.pldthome.com/Home/UlteraCoverageChecking?planId=1950", "Apply")

def trblsht_yes(recipient_id):
    now = datetime.datetime.now()
    strDate = now.strftime("%Y%m%d")
    ranStr = strDate.join(random.choice(string.ascii_uppercase) for _ in range(6))


    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "I'm sorry to hear that. We are going record this report and give you file ticket number to track it.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Thank you for reporting this. We are making it to the extent of our best to resolve your problem. Here is your file ticket number: ")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Have a nice day!")

def trblsht_no(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "It seems that we don't have any problem with your connection anymore. Thank you for your participation.")