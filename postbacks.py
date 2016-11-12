"""

POSTBACK ACTIONS HERE
when button is click

"""

import utils
import json

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
def promo_1(recipient_id)
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "The new Power Plus Plan 2899 comes with up to 50 MBPS internet speed with no data cap.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "It also comes with iflix and FOX Networks Group.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Apply now by following this link https://shop.pldthome.com/Home/AreaCoverage?planId=1636")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Or upgrade your current subscription instead by following this link https://shop.pldthome.com/Home/BufferPage?planId=1637&transaction=Upgrade&addOnId=-1")
    
