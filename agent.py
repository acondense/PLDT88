import os.path
import sys
import json

import actions
import logging

# helper
import fbutil

# actions to be executed by the bot
# refer to actions.py
import dispatch

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

# CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
CLIENT_ACCESS_TOKEN = 'd6aa459a69f343b29221684599ebbc62'

def send(recipient_id, message):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = message

    print '\nSending to', recipient_id, ' : ' , message, '\n' 

    try:
        response = request.getresponse()

        data = json.loads(response.read())

        action = data['result']['action']

        print 'Action(agent.py): ', action

        # Call the action
        if action == "":
            speech = data['result']['fulfillment']['speech']
            fbutil.send_message(recipient_id, speech)
        else:
            dispatch.action[action](recipient_id, data)

    except:
        logging.exception('')
        print 'API.AI Call failed on message: ', message