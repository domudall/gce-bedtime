import requests
import os

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


class Notify(object):
    def __init__(self):
        self.active = False
        if SLACK_WEBHOOK_URL != None and SLACK_WEBHOOK_URL != "":
            self.active = True

    def send(self, instances, action):
        if self.active:
            fields = []
            for inst in instances:
                field = {"title": inst["name"]}
                fields.append(field)

            message = "The following instances have been %s:" % action
            payload = {"fallback": message, "text": message, "fields": fields}
            requests.post(SLACK_WEBHOOK_URL, json=payload)
