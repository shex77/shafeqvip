#ZoF

import os

try:

    import requests

except ImportError:

    os.system("pip install requests")

import requests

from time import sleep

import re

ig_did = ''

csrftoken = ''

sessionid = ''

post_id = ''

done = 0

wait = 0

error = 0

r1 = requests.session()

def welcome():

    print("""

    
█▀ █░█ ▄▀█ █▀▀ █▀█
▄█ █▀█ █▀█ █▀░ █▄█
             
         
             

                                                                                            

    """)

    print("Programmed By #SHAFO/@sha_fo_ka")

welcome()

def close_bot():

    input("Enter To Close..")

    exit(0)

def login():

    global ig_did, csrftoken, sessionid

    username = input("[?] Username : ")

    password = input("[?] Password : ")

    login_url = 'https://www.instagram.com/accounts/login/ajax/'

    login_headers = {

        'accept': '*/*',

        'accept-encoding': 'gzip, deflate, br',

        'accept-language': 'en-US,en;q=0.9',

        'content-length': '275',

        'content-type': 'application/x-www-form-urlencoded',

        'cookie': 'ig_did=303991DA-0420-41AC-A26D-D9F27C8DF624; mid=X0padwAEAAEPS5xI4RZu1YV6z7zS; rur=ASH; csrftoken=xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6; urlgen="{\"185.88.26.35\": 201031}:1kC1CG:D41DVXmf-j-T5nYho3c7g7K3MQU"',

        'origin': 'https://www.instagram.com',

        'referer': 'https://www.instagram.com/',

        'sec-fetch-dest': 'empty',

        'sec-fetch-mode': 'cors',

        'sec-fetch-site': 'same-origin',

        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',

        'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',

        'x-ig-app-id': '936619743392459',

        'x-ig-www-claim': 'hmac.AR3tv9HzzLkZIUlGMRu3lzHfEeePw9CgWg8cuXGO22LfU8x0',

        'x-instagram-ajax': '0c15f4d7d44a',

        'x-requested-with': 'XMLHttpRequest'

    }

    login_data = {

        'username': f'{username}',

        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',

        'queryParams': '{}',

        'optIntoOneTap': 'false'

    }

    login_to_acc = r1.post(login_url, data=login_data, headers=login_headers)

    if login_to_acc.content == b'{"user": false, "authenticated": false, "status": "ok"}':

        print("[!] Check Your Username And Try Again")

        close_bot()

    if login_to_acc.content == b'{"user": true, "authenticated": false, "status": "ok"}':

        print("[!] Check Yo Password And Try Again")

        close_bot()

    if ('{"message": "checkpoint_required"') in login_to_acc.text:

        print("[!] Checkpoint")

        close_bot()

    if 'userId' in login_to_acc.text:

        print("[+] Login Done")

    else:

        print("[!] Check Your Acc And Try Again")

        close_bot()

    ig_did = login_to_acc.cookies['ds_user_id']

    csrftoken = login_to_acc.cookies['csrftoken']

    sessionid = login_to_acc.cookies['sessionid']

login()

def get_post_id():

    global post_id

    post_url = input("[?] Post Url = ")

    post_id_url = post_url+'?__a=1'

    try_to_get_post_id = r1.get(post_id_url).text

    hmmmm = re.findall('"GraphImage","id":"(.*?)"', try_to_get_post_id)

    post_id = " ".join(hmmmm)

get_post_id()

def add():

    global error,done,wait

    comment_url = f'https://www.instagram.com/web/comments/{post_id}/add/'

    head = {

        'accept': '*/*',

        'accept-encoding':'gzip, deflate, br',

        'accept-language': 'en-US,en;q=0.9',

        'content-length': '47',

        'content-type': 'application/x-www-form-urlencoded',

        'origin': 'https://www.instagram.com',

        'referer': 'https://www.instagram.com/p/CFM5P9BnlyY/',

        'sec-fetch-dest': 'empty',

        'sec-fetch-mode': 'cors',

        'sec-fetch-site': 'same-origin',

        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',

        'x-csrftoken': csrftoken,

        'x-ig-app-id': '936619743392459',

        'x-ig-www-claim': 'hmac.AR1c2rpKOfs9PQJlx-EoLF4rQ-K0DMnVj3wLf3_HpJyvGxyY',

        'x-instagram-ajax': 'a1de4804d095',

        'x-requested-with': 'XMLHttpRequest'

    }

    comment = input("[?] Comment : ")

    sl = int(input("[?] Sleep :"))

    data = {

        'comment_text': comment,

        'replied_to_comment_id':''

    }

    os.system("cls")

    welcome()

    while True:

        post_comment = r1.post(comment_url,headers=head,data=data)

        if post_comment.status_code == 200:

            done +=1

        elif post_comment.status_code == 429:

            wait +=1

        else:

            error +=1

        print(f"\rDone = {done}   Spam = {wait}   Error = {error}",end="")

        sleep(sl)

add()
