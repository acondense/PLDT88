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
def tell_product(recepient_id, data){
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
                            "title":"PLDT HOME FIBR PLAN 2899",
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
}