# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def send_line_notify(mode): #mode1: wake up mode2: sleep
    #LINE notifyの設定を行う
    url = "https://notify-api.line.me/api/notify"
    access_token = '0LnDbDYEJI5znhYIV8tF5QjUkDqYdIQhj6qLY9fCRPW'
    headers = {'Authorization': 'Bearer ' + access_token}

    #天気サイトから欲しい情報を取得する
    url2 = "https://tenki.jp/forecast/9/46/8610/43216/"   #欲しい情報があるURLを指定
    res = requests.get(url2)                              #上記URL情報を取得する
    soup = BeautifulSoup(res.content, 'html.parser')      #取得した情報をhtmlで解析する

    # 以下各種情報を取得
    ddd = soup.find(class_="left-style").text                 

    telop = soup.find("p", class_="weather-telop").text

    highlists = soup.find("dd",class_="high-temp temp").text

    lowlists = soup.find("dd",class_="low-temp temp").text

    ttt = soup.find(class_="rain-probability")

    row=[]
    for t in ttt:
        row.append(t)

    # message変数に通知したい文を代入する　改行したい場合は "\n" とダブルクォテーションで囲う
    if mode == 1:
        message="\n" + ddd + "\n" + telop + "\n" + "最高　" + highlists + "\n" + "最低　" + lowlists + "\n"+ "---------" + "\n" +row[1].text +"\n" + "~6  : " + row[3].text + "\n" + "~12 : " + row[5].text +"\n" + "~18 : " + row[7].text +"\n" + "~24 : " + row[9].text + "\n" + "おはようございます！" + "\n" + "今日も元気に頑張りましょう！"
    elif mode == 2:
        message = "Good night"
    
    payload = {'message': message}
    requests.post(url, headers=headers, params=payload,)
