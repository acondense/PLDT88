import os
import sys
import json
import logging

import requests
from flask import Flask, request

# API ai
import agent


import utils
import setup

# helper
import fbutil


#
# import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

try:
    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
except:
    logging.exception('')

# for postback
import dispatch 

"""
Set up the bot
"""
try:
    # setup.set_welcome_text()
    # setup.set_get_started_button()
    print "Just commented the setup app.py line28"
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

    return "PLDT Bot Knows!!!!", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                """
                HANDLE MESSAGES HERE
                """
                if messaging_event.get("message"):  # someone sent us a message


                    """ weird checking """
                    if messaging_event['message'].get('is_echo'):
                        print "An echo returning now"
                        return "ok", 200
                    else:
                        print "Not an echo"

                    if messaging_event['message'].get('sticker_id'):
                        print "Thanks for the sticker"
                        sender_id = messaging_event["sender"]["id"]
                        futil.send_message(sender_id, "Thanks for the sticker")
                        return "ok", 200
                    else:
                        print "Not a sticker"
                    """ end of weird checking """

                    try:
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        message_text = messaging_event["message"]["text"]  # the message's text
                        agent.send(sender_id, message_text) # query to api.ai then execute the action
                    
                    except:
                        logging.exception('')


                """
                HANDLE DELIVERY HERE
                """
                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                """
                HANLDE OPTIN HERE
                """
                if messaging_event.get("optin"):  # optin confirmation
                    pass

                """
                HANDLE POSTBACK HERE - postback are button clicks
                """
                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    try:
                        sender_id = messaging_event["sender"]["id"]
                        print "POST BACK RECEIVED"
                        # futil.send_message(sender_id, "MUST GET VALUE OF POST BACK app.py line107")
                        postback = messaging_event["postback"]["payload"]
                        dispatch.postback[postback](sender_id)
                    except:
                        logging.exception('')

    return "ok", 200

def log(message):  # simple wrapper for logging to stdout on heroku
    print str(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)
