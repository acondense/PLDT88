"""

POSTBACK ACTIONS HERE
when button is click

"""

import utils

# action to take upon the bot click on get started
def welcome():
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": "Hi i am the pldt bot. Created to serve you."
        }
    })

    utils.post_messenger(data) 