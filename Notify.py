# -*- coding: utf-8 -*-
import requests

def main():
    send_line_notify('てすとてすと')
    print("send")

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'dr8JswoCfScuCDn0r2WdS0yV2N1xmKmV1Glnw9esGVo'
    line_notify_api = 'https://notify-api.line.me/api/notify'

    headers = {
        'Authorization': 'Bearer' +  line_notify_token
        }
    data = {
        'message': notification_message
        }

    requests.post(line_notify_api, headers = headers, data = data)
