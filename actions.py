# PLDT related actions in here

import json
import requests

import logging 
import utils

# helper
import fbutil

# show best product
def unknown(recipient_id, data):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": data['result']['fulfillment']['speech']
        }
    })
    utils.post_messenger(data)

# show best product
def show_best_product(recipient_id, data):
    fbutil.send_bubbles(recipient_id)
    
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": data['result']['fulfillment']['speech']
        }
    })

    utils.post_messenger(data)

# send recent bill
def send_recent_bill(recipient_id, data):

    fbutil.send_bubbles(recipient_id)

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": data['result']['fulfillment']['speech']
        }
    })
    utils.post_messenger(data)

# tell product
def tell_product(recipient_id, data):
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
                    "text":"Okay. Which product are you interested about?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"Home Fiber Plan 2899",
                            "payload": "promo_1"
                        },
                        {
                            "type":"postback",
                            "title":"Speedster Plan 1899",
                            "payload":"promo_2"
                        },
                         {
                            "type":"postback",
                            "title":"Fun Plan 699",
                            "payload":"promo_3"
                        }
                    ]
                }
            }
        }
    })

    utils.post_messenger(data)

def check_status(recipient_id, data):
    # check the user status here assume that he is conneted
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "All right i checked that your service is active")
    fbutil.send_bubbles(recipient_id)

    # check if users area is still active
    fbutil.send_message(recipient_id, "Hi, we are currently doing an infrastructure upgrade in your area")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Expect the connection to be back in 8 hrs")

    # the user account is active and the area is okay suggest trouble shooting

def troubleshoot(recipient_id, data):
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "This is a troubleshooting guide for those who are experiencing a slow internet connection. Please follow every step that I will give.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "First, Connect a computer to the modem with an Ethernet cable as shown below.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_image(recipient_id, "http://www.centurylink.com/help/images/uploads/194_wiredconnection.png")
