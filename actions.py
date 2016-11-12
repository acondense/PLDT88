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
            "text": 'data['result']['fulfillment']['speech']'
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