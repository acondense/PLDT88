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


    fbutil.send_file(recipient_id, "http://www.dmv.org/images/bill-of-sale.pdf")

def check_status(recipient_id, data):
    fbutil.send_bubbles(recipient_id)
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": data['result']['fulfillment']['speech']
        }
    })

    # check the user status here assume that he is conneted
    fbutil.send_message(recipient_id, "All right i checked that your service is active")
    fbutil.send_bubbles(recipient_id)

    # check if users area is still active
    fbutil.send_message(recipient_id, "Hi, we are currently doing an infrastructure upgrade in your area")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Expect the connectioin to be back after 8 hrs")

    # the user account is active and the area is okay suggest trouble shooting

