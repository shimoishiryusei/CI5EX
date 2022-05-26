# -*- coding: utf-8 -*-
import requests

def send_line_notify():
    message = """
    これはテストです．
    """

    line_notify_token = '0LnDbDYEJI5znhYIV8tF5QjUkDqYdIQhj6qLY9fCRPW'
    line_notify_api = 'https://notify-api.line.me/api/notify'

    headers = {
        'Authorization': "Bearer" +  line_notify_token
        }

    data = {
        'message': message
        }

    requests.post(
        line_notify_api, 
        headers = headers, 
        data = data,
        )
