# -*- coding: utf-8 -*-
import requests

def main():
    send_line_notify('てすとてすと')

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'M4nCabhd0kNDtFexkBH0GpdzuujN3nSIetz0y5ZEzES'
    line_notify_api = 'https://notify-api.line.me/api/notify'

    headers = {
        'Authorization': 'Bearer' +  line_notify_token
        }
    data = {
        'message': notification_message
        }

    requests.post(line_notify_api, headers = headers, data = data)