"""
DISPATCH FUNCTIONS
"""

import actions
import postbacks

# refer to actions.py
action = {
    'showBestProduct': actions.show_best_product,
    'sendRecentBill': actions.send_recent_bill
}

postback = {
    'welcome': postbacks.welcome,
    'welcome_yes': postbacks.welcome_yes,
    'welcome_no': postbacks.welcome_no
}