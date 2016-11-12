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
    fbutil.send_file(recipient_id, "https://www.pdf-archive.com/2016/11/12/bill1116/bill1116.pdf")

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

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": data['result']['fulfillment']['speech']
        }
    })
    utils.post_messenger(data)

    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "This is a troubleshooting guide for those who are experiencing a slow internet connection. Please follow every step that I will give.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "First, connect your computer to your modem with an Ethernet cable as shown below.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_image(recipient_id, "http://www.centurylink.com/help/images/uploads/194_wiredconnection.png")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Next is try to disconnect and power down all devices that access the Internet like other computers, gaming systems, Netflix or other movie streaming devices, DVRs, other routers, switches, VoIP phones, mobile phones and wireless printers.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_bubbles(recipient_id)
    fbutil.send_link(recipient_id, "Run a speedtest with...",  "http://speedtest.net", "Speedtest")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Write down the date, time, and your results each time you run a test.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Compare your results against the table below. Are your speeds lower than or at/above the Target Download Speed?")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "If your speedtest was at at or above the Target Download Speed, then you're receiving your subscribed speed. For example, if you've purchased a CenturyLink Internet package with 1.5 Mbps speed, your Target Download Speed shouldn't be lower than 1.2 Mbps.")
    fbutil.send_bubbles(recipient_id)
    fbutil.send_message(recipient_id, "Bad wiring can also cause slow connections so you better check it.")

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"Is your internet connection still slow?",
                    "buttons":[
                        {
                            "type":"postback",
                            "title":"Yes",
                            "payload": "trblsht_yes"
                        },
                        {
                            "type":"postback",
                            "title":"No",
                            "payload":"trblsht_no"
                        }
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

def tagUser(recipient_id, data):
    fbutil.send_bubbles(recipient_id)
    print data['result']['parameters']['account-number']
    print recipient_id




    
    

    
    
    

    

    
