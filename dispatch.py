"""
DISPATCH FUNCTIONS
"""

import actions
import postbacks
import fbutil

# refer to actions.py, plain text from api.ai
action = {
    'showBestProduct': actions.show_best_product,
    'sendRecentBill': actions.send_recent_bill,
    'tellProduct' : actions.tell_product,
    'checkStatus': actions.check_status,
    'troubleshoot-slowConnection': actions.troubleshoot,
    'input.unknown': actions.unknown
}

# on button click
postback = {
    'welcome': postbacks.welcome,
    'welcome_yes': postbacks.welcome_yes,
    'welcome_no': postbacks.welcome_no,
    'promo_1' : postbacks.promo_1,
    'promo_2' : postbacks.promo_2,
    'promo_3' : postbacks.promo_3
}