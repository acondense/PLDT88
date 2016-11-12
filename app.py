import os
import sys
import json
import logging

import requests
from flask import Flask, request

import fbsample # local file will serve as a reference
import agent


import utils

try:
    utils.set_welcome()
except:
    logging.exception('')


app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Alan Knows!!!!", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    if messaging_event['message'].get('is_echo'):
                        print "An echo returning now"
                        return "ok", 200
                    else:
                        print "Not an echo"

                    if messaging_event['message'].get('sticker_id'):
                        print "Thanks for the sticker"
                        sender_id = messaging_event["sender"]["id"]
                        fbsample.send_message(sender_id, "Thanks for the sticker")
                        return "ok", 200
                    else:
                        print "Not a sticker"

                    try:
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        message_text = messaging_event["message"]["text"]  # the message's text

                        agent.send(sender_id, message_text)
                    
                    except:
                        print "Unable to process"
                        log(data)
                        raise
                    else:
                        print "Unable to process"
                        log(data)


                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    try:
                        sender_id = messaging_event["sender"]["id"]
                        print "POST BACK RECEIVED"
                        fbsample.send_message(sender_id, "POST BACK RECEIVED")
                    except:
                        print "Unable to process"
                        log(data)
                        raise
                    else:
                        print "Unable to process"
                        log(data)

    return "ok", 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
