"""

POSTBACK ACTIONS HERE
when button is click

"""

import utils
import json
import datetime
import random
import string
import requests

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
                    "text":"Hi I am the PLDT bot I am created to enhance your customer experience. Are you an existing PLDT customer?",
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
                        },
                        {
                            "type":"postback",
                            "title":"I would like to answer PLDT customer survey.",
                            "payload":"survey"
                        },
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

    """
    fbutil.send_message(recipient_id, "I am created to enhance your customer experience.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "You can ask me anything about PLDT")
    """
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Would you like to link your PLDT Account with me?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"Yes, Link it",
                            "payload":"link"
                        },
                        {
                            "type":"postback",
                            "title":"Not now.",
                            "payload":"not_now"
                        }
                    ]
                }
            }
        }
    })

    utils.post_messenger(data)

# postback if yes is clicked on welcome
def welcome_no(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "I will ask you some question to recommend the best pldt product that will suite you.")

def link(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Please give me your account number")

def not_now(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Oh okay :)")

def survey(recipient_id):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Welcome to PLDT customer survey. Please rate each item from 1-5 where 10 is the highest. Shall we?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"Okay",
                            "payload": "question1"
                        }
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def question1(recipient_id):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"How was your experience with the service of PLDT?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"1",
                            "payload": "question2"
                        },
                        {
                            "type":"postback",
                            "title":"2",
                            "payload": "question2"
                        },
                        {
                            "type":"postback",
                            "title":"3",
                            "payload": "question2"
                        },
                        {
                            "type":"postback",
                            "title":"4",
                            "payload": "question2"
                        },
                        {
                            "type":"postback",
                            "title":"5",
                            "payload": "question2"
                        },
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def question2(recipient_id):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"How will you rate our personnels?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"1",
                            "payload": "question3"
                        },
                        {
                            "type":"postback",
                            "title":"2",
                            "payload": "question3"
                        },
                        {
                            "type":"postback",
                            "title":"3",
                            "payload": "question3"
                        },
                        {
                            "type":"postback",
                            "title":"4",
                            "payload": "question3"
                        },
                        {
                            "type":"postback",
                            "title":"5",
                            "payload": "question3"
                        },
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def question3(recipient_id):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"How likely are you to recommend us to a friend?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"1",
                            "payload": "question4"
                        },
                        {
                            "type":"postback",
                            "title":"2",
                            "payload": "question4"
                        },
                        {
                            "type":"postback",
                            "title":"3",
                            "payload": "question4"
                        },
                        {
                            "type":"postback",
                            "title":"4",
                            "payload": "question4"
                        },
                        {
                            "type":"postback",
                            "title":"5",
                            "payload": "question4"
                        },
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def question4(recipient_id):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"How reliable do you find our service?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"1",
                            "payload": "question5"
                        },
                        {
                            "type":"postback",
                            "title":"2",
                            "payload": "question5"
                        },
                        {
                            "type":"postback",
                            "title":"3",
                            "payload": "question5"
                        },
                        {
                            "type":"postback",
                            "title":"4",
                            "payload": "question5"
                        },
                        {
                            "type":"postback",
                            "title":"5",
                            "payload": "question5"
                        },
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def question5(recipient_id):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"How do you find me helpful?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"1",
                            "payload": "finish"
                        },
                        {
                            "type":"postback",
                            "title":"2",
                            "payload": "finish"
                        },
                        {
                            "type":"postback",
                            "title":"3",
                            "payload": "finish"
                        },
                        {
                            "type":"postback",
                            "title":"4",
                            "payload": "finish"
                        },
                        {
                            "type":"postback",
                            "title":"5",
                            "payload": "finish"
                        },
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def finish(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Thank you for your participation. Your answers are very much appreciated")

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
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Hmmm. It seems that something is wrong but can I ask something more?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"Ok",
                            "payload": "askMore_yes"
                        },
                        {
                            "type":"postback",
                            "title":"No",
                            "payload":"askMore_no"
                        }
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)
    
    """
    now = datetime.datetime.now()
    strDate = str(now.strftime("%Y%m%d"))
    output = "Thank you for reporting this. We are making it to the extent of our best to resolve your problem. Here is your file ticket number: " + strDate + ''.join(random.choice(string.ascii_uppercase) for _ in range(3))


    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "I'm sorry to hear that. We are going record this report and give you file ticket number to track it.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, output)
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Have a nice day!")
    """

def trblsht_no(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "It seems that we don't have any problem with your connection anymore. Thank you for your participation.")

def askMore_yes(recipient_id):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Approximately how many users are currently connected to your modem?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"1-4",
                            "payload": "optiona"
                        },
                        {
                            "type":"postback",
                            "title":"5-10",
                            "payload":"optionb"
                        },
                        {
                            "type":"postback",
                            "title":"11 or more",
                            "payload":"optionc"
                        }
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def askMore_no(recipient_id):
    now = datetime.datetime.now()
    strDate = str(now.strftime("%Y%m%d"))
    output = "Ok then I guess we will just file this as a report. We are making it to the extent of our best to resolve your problem. Here is your file ticket number: " + strDate + ''.join(random.choice(string.ascii_uppercase) for _ in range(3))

    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "I'm sorry to hear that. We are going record this report and give you file ticket number to track it.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, output)
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Have a nice day!")

def optiona(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipeint_id, "I see. Thank you for your response. this conversation is automatically converted to a report. We are making it to the extent of our best to resolve your problem. Here is your file ticket number: " + strDate + ''.join(random.choice(string.ascii_uppercase) for _ in range(3)) + ". You may use it to track our response to this report.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Thank you. Have a nice day!")

def optionb(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipeint_id, "I see. Thank you for your response but we think this is not a technical problem. You are currently subscribed to Fun Plan 699 which may not be reliable enough for approximately 5-10 devices")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "What may I suggest is to for you to upgrade to Speedstar Plan 1899 to enjoy up to 10 MBPS and 50 GB monthly volume allowance.")
    fbutil.send_message(recipient_id, "It also comes with a landline.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "You may do this by following this link","https://shop.pldthome.com/Home/BufferPage?planId=1741&transaction=Upgrade&addOnId=-1", "Upgrade")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Thank you. Have a nice day!")

def optionc(recipient_id):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipeint_id, "I see. Thank you for your response but we think this is not a technical problem. You are currently subscribed to Speedstar Plan 1899 which may not be reliable enough for approximately 11 or more devices")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "What may I suggest is to for you to upgrade to Power Plus Plan 2899 comes with up to 50 MBPS internet speed with no data cap.")
    fbutil.send_message(recipient_id, "It also comes with iflix and FOX Networks Group.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "You may do this by following this link","https://shop.pldthome.com/Home/BufferPage?planId=1637&transaction=Upgrade&addOnId=-1", "Upgrade")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Thank you. Have a nice day!")

