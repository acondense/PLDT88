# PLDT related actions in here

import json
import requests

import logging 

import utils

# image url is too long, better to assign it on a variable
image_url = 'http://cdn.iflscience.com/images/4a2006cf-753a-5617-8385-8c18ef36590c/large-1464855882-10-harambe-the-gorilla-put-zoo-in-a-lose-lose-situation-by-being-himself.jpg'

# send a chatting bubble indicator
def send_bubbles(recipient_id, data):
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "sender_action":"typing_on"
    })

    utils.post_messenger(data)


# just send a text message
def send_message(recipient_id, data):
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": data['result']['fulfillment']['speech']
        }
    })

    utils.post_messenger(data)

# send a button
def send_button(recipient_id, data):
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":"What do you want to do next?",
                    "buttons":[
                        {
                            "type":"web_url",
                            "url":"https://petersapparel.parseapp.com",
                            "title":"Show Website"
                        },
                        {
                            "type":"postback",
                            "title":"Start Chatting",
                            "payload":"USER_DEFINED_PAYLOAD"
                        }
                    ]
                }
            }
        }
    })

    utils.post_messenger(data)

# send a generic/carousel
# horizantal scroll menu
def send_generic(recipient_id, data):
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type": "generic",
                    "elements":[
                        {
                            "title": "Welcome to Harambe Store",
                            "item_url": "https://www.youtube.com/watch?v=Py_1aCt2c0s",
                            "image_url": image_url,
                            "subtitle":"We need him back!",
                            "buttons":[
                                {
                                    "type":"web_url",
                                    "url": image_url,
                                    "title":"View Full Image in Browser"
                                },
                                {
                                    "type":"web_url",
                                    "url": image_url,
                                    "title":"Web View",
                                    "webview_height_ratio": "tall"
                                },
                                {
                                    "type":"postback",
                                    "title":"Continue Chatting",
                                    "payload":"DEVELOPER_DEFINED_PAYLOAD"
                                }              
                            ]
                        }
                    ]
                }
            }
        }
    })
    utils.post_messenger(data)

#
def send_recent_bill(recipient_id, data):

    send_bubbles(recipient_id, data)

    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": data['result']['fulfillment']['speech']
        }
    })

    utils.post_messenger(data)