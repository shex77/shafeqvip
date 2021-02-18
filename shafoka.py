import requests

import time

import re

r = requests.session()

print('''

******************************************

*     - [ Report InstaGram ] -           *

*      Tool developer -> : M3GON         *    

*      InstaGram developer -> : _m3gon   *     

*      Channel TeleGram -> : @M3GONPY    *     

******************************************

''')

print('[+] عندك خيارين :')

print('[+] الخيار الاول - ابلاغ اربع بلاغات دفعه وحده اكتب رقم - 1')

print('[+] الخيار الثاني - تختار البلاغ من نفسك اكتب رقم - 2')

alr8m = input('[+] ادخل الرقم ==> : ')

if alr8m == '1':

    print('[!] يفضل انك تستخدم حساب وهمي ..')

    username = input('[+] ادخل اليوزر لتسجيل الدخول ==> : ')

    password = input('[+] ادخل باسورد الحساب ==> : ')

    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {

    'accept': '*/*',

    'accept-encoding': 'gzip, deflate, br',

    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

    'content-length': '274',

    'content-type': 'application/x-www-form-urlencoded',

    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

    'origin': 'https://www.instagram.com',

    'referer': 'https://www.instagram.com/',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

    'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

    'x-ig-app-id': '936619743392459',

    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',

    'x-instagram-ajax': '1cb44f68ffec',

    'x-requested-with': 'XMLHttpRequest'

    }

    data = {

    'username': username,

    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:'+password,

    'queryParams': '{}',

    'optIntoOneTap': 'false'

    }

    req_login = requests.post(url, data=data, headers=headers)

    if '"authenticated":true' in req_login.text:

        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})

        print('[+] تم تسجيل الدخول بنجاح ..')

    else:

        print('[+] اليوزر او الباسورد غلط')

    sessionid1 = req_login.cookies['sessionid']

    print('[+] خش الرابط هاذا ==> : https://codeofaninja.com/tools/find-instagram-user-id/')

    print('[+] واكتب يوزر الشخص وانسخ ايديه والصقه ..')

    idinsta = input('[+] ادخل ايدي الضحيه ==> : ')

    url_report_spam = f'https://www.instagram.com/users/{idinsta}/report/'

    headers_report_spam = {

    'accept': '*/*',

    'accept-encoding': 'gzip, deflate, br',

    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

    'content-length': '37',

    'content-type': 'application/x-www-form-urlencoded',

    'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',

    'origin': 'https://www.instagram.com',

    'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

    'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

    'x-ig-app-id': '936619743392459',

    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

    'x-instagram-ajax': '1cb44f68ffec',

    'x-requested-with': 'XMLHttpRequest',

    }

    data_report_spam = {

    'source_name': '',

    'reason_id': '1',

    'frx_context': ''

    }

    url_report_self = f'https://www.instagram.com/users/{idinsta}/report/'

    headers_report_self = {

        'accept': '*/*',

        'accept-encoding': 'gzip, deflate, br',

        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

        'content-length': '37',

        'content-type': 'application/x-www-form-urlencoded',

        'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',

        'origin': 'https://www.instagram.com',

        'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',

        'sec-fetch-dest': 'empty',

        'sec-fetch-mode': 'cors',

        'sec-fetch-site': 'same-origin',

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

        'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

        'x-ig-app-id': '936619743392459',

        'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

        'x-instagram-ajax': '1cb44f68ffec',

        'x-requested-with': 'XMLHttpRequest',

    }

    data_report_self = {

        'source_name': '',

        'reason_id': '2',

        'frx_context': ''

    }

    url_report_ant7ar = f'https://www.instagram.com/users/{idinsta}/report/'

    headers_report_ant7ar = {

    'accept': '*/*',

    'accept-encoding': 'gzip, deflate, br',

    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

    'content-length': '37',

    'content-type': 'application/x-www-form-urlencoded',

    'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',

    'origin': 'https://www.instagram.com',

    'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

    'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

    'x-ig-app-id': '936619743392459',

    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

    'x-instagram-ajax': '1cb44f68ffec',

    'x-requested-with': 'XMLHttpRequest',

    }

    data_report_ant7ar = {

    'source_name': '',

    'reason_id': '4',

    'frx_context': ''

    }

    url_report_3nf = f'https://www.instagram.com/users/{idinsta}/report/'

    headers_report_3nf = {

    'accept': '*/*',

    'accept-encoding': 'gzip, deflate, br',

    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

    'content-length': '37',

    'content-type': 'application/x-www-form-urlencoded',

    'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid1}; rur=VLL',

    'origin': 'https://www.instagram.com',

    'referer': f'https://www.instagram.com/users/{idinsta}/report/inappropriate',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

    'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

    'x-ig-app-id': '936619743392459',

    'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

    'x-instagram-ajax': '1cb44f68ffec',

    'x-requested-with': 'XMLHttpRequest',

    }

    data_report_3nf = {

    'source_name': '',

    'reason_id': '5',

    'frx_context': ''

    }

    while True:

        req_report_spam = requests.post(url_report_spam, data=data_report_spam, headers=headers_report_spam).text

        if '"description":"Your reports help keep our community free of spam.","status":"ok"' in req_report_spam:

            print(f'[+] تم الابلاغ النوع - سبام = مزعج ')

            time.sleep(3)

        else:

            print('[-] حدث خطاء في الابلاغ نوع الابلاغ - سبام = مزعج')

        req_report_self = requests.post(url_report_self, data=data_report_self, headers=headers_report_self).text

        if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_report_self:

            print('[+] تم الابلاغ النوع - سيلف')

            time.sleep(3)

        else:

            print('[-] حدث خطاء في الابلاغ نوع الابلاغ - سيلف')

        req_report_ant7ar = requests.post(url_report_ant7ar, data=data_report_ant7ar, headers=headers_report_ant7ar).text

        if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_report_ant7ar:

            print('[+] تم الابلاغ النوع - انتحار')

            time.sleep(3)

        else:

            print('[-] حدث خطاء في الابلاغ النوع - انتحار')

        req_report_3nf = requests.post(url_report_3nf, data=data_report_3nf, headers=headers_report_3nf).text

        if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_report_3nf:

            print('[+] تم الابلاغ النوع - عنف')

            time.sleep(3)

        else:

            print('[-] حدث خطاء في الابلاغ نوع الابلاغ - عنف ')

if alr8m == '2':

    print('انواع البلاغات المتوفره حاليا :')

    print('[+] النوع الاول - سبام اكتب رقم - 1')

    print('[+] النوع الثاني - سيلف اكتب رقم - 2')

    print('[+] النوع الثالث - انتحار اكتب رقم - 3')

    print('[+] النوع الرابع - عنف اكتب رقم - 4')

    alr8m2 = input('[+] اكتب الرقم ==> : ')

    if alr8m2 == '1':

        print('[!] يفضل انك تستخدم حساب وهمي ..')

        username_login = input('[+] ادخل اليوزر لتسجيل الدخول ==> : ')

        password_login = input('[+] ادخل باسورد الحساب ==> : ')

        url_login = 'https://www.instagram.com/accounts/login/ajax/'

        headers_login = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '274',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'origin': 'https://www.instagram.com',

            'referer': 'https://www.instagram.com/',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest'

        }

        data_login = {

            'username': username_login,

            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login,

            'queryParams': '{}',

            'optIntoOneTap': 'false'

        }

        req_login2 = requests.post(url_login, data=data_login, headers=headers_login)

        if '"authenticated":true' in req_login2.text:

            r.headers.update({'X-CSRFToken': req_login2.cookies['csrftoken']})

            print('[+] تم تسجيل الدخول بنجاح ..')

        else:

            print('[+] اليوزر او الباسورد غلط')

        sessionid2 = req_login2.cookies['sessionid']

        print('[+] خش الرابط هاذا ==> : https://codeofaninja.com/tools/find-instagram-user-id/')

        print('[+] واكتب يوزر الشخص وانسخ ايديه والصقه ..')

        idinsta2 = input('[+] ادخل ايدي الضحيه ==> : ')

        url_report_spam2 = f'https://www.instagram.com/users/{idinsta2}/report/'

        headers_report_spam2 = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '37',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid2}; rur=VLL',

            'origin': 'https://www.instagram.com',

            'referer': f'https://www.instagram.com/users/{idinsta2}/report/inappropriate',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest',

        }

        data_report_spam2 = {

            'source_name': '',

            'reason_id': '1',

            'frx_context': ''

        }

        while True:

            req_spam2 = requests.post(url_report_spam2, data=data_report_spam2, headers=headers_report_spam2).text

            if '"description":"Your reports help keep our community free of spam.","status":"ok"' in req_spam2:

                print(f'[+] تم الابلاغ النوع - سبام = مزعج ')

                time.sleep(3)

            else:

                print('[-] حدث خطاء في الابلاغ نوع الابلاغ - سبام = مزعج')

    if alr8m2 == '2':

        print('[!] يفضل انك تستخدم حساب وهمي ..')

        username_login3 = input('[+] ادخل اليوزر لتسجيل الدخول ==> : ')

        password_login3 = input('[+] ادخل باسورد الحساب ==> : ')

        url_login3 = 'https://www.instagram.com/accounts/login/ajax/'

        headers_login3 = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '274',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'origin': 'https://www.instagram.com',

            'referer': 'https://www.instagram.com/',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest'

        }

        data_login3 = {

            'username': username_login3,

            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login3,

            'queryParams': '{}',

            'optIntoOneTap': 'false'

        }

        req_login3 = requests.post(url_login3, data=data_login3, headers=headers_login3)

        if '"authenticated":true' in req_login3.text:

            r.headers.update({'X-CSRFToken': req_login3.cookies['csrftoken']})

            print('[+] تم تسجيل الدخول بنجاح ..')

        else:

            print('[+] اليوزر او الباسورد غلط')

        sessionid3 = req_login3.cookies['sessionid']

        print('[+] خش الرابط هاذا ==> : https://codeofaninja.com/tools/find-instagram-user-id/')

        print('[+] واكتب يوزر الشخص وانسخ ايديه والصقه ..')

        idinsta3 = input('[+] ادخل ايدي الضحيه ==> : ')

        url_report_self2 = f'https://www.instagram.com/users/{idinsta3}/report/'

        headers_report_self2 = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '37',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid3}; rur=VLL',

            'origin': 'https://www.instagram.com',

            'referer': f'https://www.instagram.com/users/{idinsta3}/report/inappropriate',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest',

        }

        data_report_self2 = {

            'source_name': '',

            'reason_id': '2',

            'frx_context': ''

        }

        while True:

            req_self = requests.post(url_report_self2, data=data_report_self2, headers=headers_report_self2).text

            if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_self:

                print('[+] تم الابلاغ النوع - سيلف')

                time.sleep(3)

            else:

                print('[-] حدث خطاء في الابلاغ نوع الابلاغ - سيلف')

    if alr8m2 == '3':

        print('[!] يفضل انك تستخدم حساب وهمي ..')

        username_login4 = input('[+] ادخل اليوزر لتسجيل الدخول ==> : ')

        password_login4 = input('[+] ادخل باسورد الحساب ==> : ')

        url_login4 = 'https://www.instagram.com/accounts/login/ajax/'

        headers_login4 = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '274',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'origin': 'https://www.instagram.com',

            'referer': 'https://www.instagram.com/',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest'

        }

        data_login4 = {

            'username': username_login4,

            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login4,

            'queryParams': '{}',

            'optIntoOneTap': 'false'

        }

        req_login4 = requests.post(url_login4, data=data_login4, headers=headers_login4)

        if '"authenticated":true' in req_login4.text:

            r.headers.update({'X-CSRFToken': req_login4.cookies['csrftoken']})

            print('[+] تم تسجيل الدخول بنجاح ..')

        else:

            print('[+] اليوزر او الباسورد غلط')

        sessionid4 = req_login4.cookies['sessionid']

        print('[+] خش الرابط هاذا ==> : https://codeofaninja.com/tools/find-instagram-user-id/')

        print('[+] واكتب يوزر الشخص وانسخ ايديه والصقه ..')

        idinsta4 = input('[+] ادخل ايدي الضحيه ==> : ')

        url_report_ant7ar2 = f'https://www.instagram.com/users/{idinsta4}/report/'

        headers_report_ant7ar2 = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '37',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid4}; rur=VLL',

            'origin': 'https://www.instagram.com',

            'referer': f'https://www.instagram.com/users/{idinsta4}/report/inappropriate',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest',

        }

        data_report_ant7ar2 = {

            'source_name': '',

            'reason_id': '4',

            'frx_context': ''

        }

        while True:

            req_ant7ar = requests.post(url_report_ant7ar2, data=data_report_ant7ar2, headers=headers_report_ant7ar2).text

            if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_ant7ar:

                print('[+] تم الابلاغ النوع - انتحار')

                time.sleep(3)

            else:

                print('[-] حدث خطاء في الابلاغ النوع - انتحار')

    if alr8m2 == '4':

        print('[!] يفضل انك تستخدم حساب وهمي ..')

        username_login5 = input('[+] ادخل اليوزر لتسجيل الدخول ==> : ')

        password_login5 = input('[+] ادخل باسورد الحساب ==> : ')

        url_login5 = 'https://www.instagram.com/accounts/login/ajax/'

        headers_login5 = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '274',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; rur=VLL; csrftoken=Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'origin': 'https://www.instagram.com',

            'referer': 'https://www.instagram.com/',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Iwq1hnXNJ3Y8IH1fRYDND6r72Zezq28I',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9J8a',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest'

        }

        data_login5 = {

            'username': username_login5,

            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613212725:' + password_login5,

            'queryParams': '{}',

            'optIntoOneTap': 'false'

        }

        req_login5 = requests.post(url_login5, data=data_login5, headers=headers_login5)

        if '"authenticated":true' in req_login5.text:

            r.headers.update({'X-CSRFToken': req_login5.cookies['csrftoken']})

            print('[+] تم تسجيل الدخول بنجاح ..')

        else:

            print('[+] اليوزر او الباسورد غلط')

        sessionid5 = req_login5.cookies['sessionid']

        print('[+] خش الرابط هاذا ==> : https://codeofaninja.com/tools/find-instagram-user-id/')

        print('[+] واكتب يوزر الشخص وانسخ ايديه والصقه ..')

        idinsta5 = input('[+] ادخل ايدي الضحيه ==> : ')

        url_report_3nf2 = f'https://www.instagram.com/users/{idinsta5}/report/'

        headers_report_3nf2 = {

            'accept': '*/*',

            'accept-encoding': 'gzip, deflate, br',

            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

            'content-length': '37',

            'content-type': 'application/x-www-form-urlencoded',

            'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz; ds_user_id=45334757205; sessionid={sessionid5}; rur=VLL',

            'origin': 'https://www.instagram.com',

            'referer': f'https://www.instagram.com/users/{idinsta5}/report/inappropriate',

            'sec-fetch-dest': 'empty',

            'sec-fetch-mode': 'cors',

            'sec-fetch-site': 'same-origin',

            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',

            'x-csrftoken': 'Dhb6bMBo4RssngCWH9sEK51yg5eIT6xz',

            'x-ig-app-id': '936619743392459',

            'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9D2b',

            'x-instagram-ajax': '1cb44f68ffec',

            'x-requested-with': 'XMLHttpRequest',

        }

        data_report_3nf2 = {

        'source_name': '',

        'reason_id': '5',

        'frx_context': ''

        }

        while True:

            req_3nf = requests.post(url_report_3nf2, data=data_report_3nf2, headers=headers_report_3nf2).text

            if '"description":"We take your reports seriously. We look into every issue, and take action when people violate our Community Guidelines","status":"ok"' in req_3nf:

                print('[+] تم الابلاغ النوع - عنف')

                time.sleep(3)

            else:

                print('[-] حدث خطاء في الابلاغ نوع الابلاغ - عنف ')
