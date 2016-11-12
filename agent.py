import os.path
import sys
import json

import actions

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

# CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
CLIENT_ACCESS_TOKEN = 'a7f19d2cb95d4dabb88278146c68fd73'

def send(recipient_id, message):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    # request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = message

    response = request.getresponse()

    data = json.loads(response.read())

    action = data['result']['action']

    # Call the action
    actions.dispatch[action](recipient_id, data)

    print 'ACTION!!!!', action