import os
import requests
import json

def post_messenger(data):
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    # send the post request along with the data to facebook messenger
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        print str(r.status_code)
        print str(r.text)


def set_welcome():
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "setting_type":"call_to_actions",
                "thread_state":"new_thread",
                "call_to_actions":[
                    {
                        "payload":"USER_DEFINED_PAYLOAD"
                    }
                ]
    })

    r = requests.post("https://graph.facebook.com/v2.6/me/thread_settings", params=params, headers=headers, data=data)
    if r.status_code != 200:
        print str(r.status_code)
        print str(r.text)