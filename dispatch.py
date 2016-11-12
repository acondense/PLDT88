"""
DISPATCH FUNCTIONS
"""

import actions
import postbacks

# refer to actions.py
action = {
    'send_bubbles' : actions.send_bubbles,
    'send_message' : actions.send_message,
    'send_button' : actions.send_button,
    'send_generic' : actions.send_generic,
    'getRecentBill': actions.send_message,
    'input.unknown' : actions.send_message,
    'sendRecentBill': actions.send_recent_bill
}

postback = {
    'WELCOME': postbacks.welcome
}