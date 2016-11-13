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
    'troubleshootSlowConnection': actions.troubleshoot,
    'input.unknown': actions.unknown,
    'troubleshoot' : actions.troubleshoot,
    'tagUser' : actions.tagUser,
    'smalltalk.greetings' : actions.default,
    'smalltalk.appraisal' : actions.default
}

# on button click
postback = {
    'welcome': postbacks.welcome,
    'welcome_yes': postbacks.welcome_yes,
    'welcome_no': postbacks.welcome_no,
    'promo_1' : postbacks.promo_1,
    'promo_2' : postbacks.promo_2,
    'promo_3' : postbacks.promo_3,
    'trblsht_yes' : postbacks.trblsht_yes,
    'trblsht_no' : postbacks.trblsht_no,
    'askMore_no' : postbacks.askMore_no,
    'askMore_yes' : postbacks.askMore_yes,
    'optiona' : postbacks.optiona,
    'optionb' : postbacks.optionb,
    'optionc' : postbacks.optionc,
    'link' : postbacks.link,
    'not_now': postbacks.not_now
}