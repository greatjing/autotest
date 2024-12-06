import requests
import json

class DingTalkNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, message):
        headers = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "测试报告通知",
                "text": message
            }
        }
        response = requests.post(
            self.webhook_url,
            headers=headers,
            data=json.dumps(data)
        )
        return response
