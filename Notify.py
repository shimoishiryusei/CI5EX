# -*- coding: utf-8 -*-
import requests

def send_line_notify():
    message = """
    これはテストです．
    """

    line_notify_token = 'dr8JswoCfScuCDn0r2WdS0yV2N1xmKmV1Glnw9esGVo'
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
