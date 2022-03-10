from base64 import b64encode

import requests


def get_token():
    header_code = b64encode("4s34iacov".encode()).decode()
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {header_code}'
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': '4s345u2ohl',
        'code': '2bab7ded-1c32-47a4-9d92-a2dc26f4ac0e',
        'redirect_uri': r'https://03ac-61-1-208-167.ngrok.io/user/register/callback'
    }
    res = requests.get('https://coito.com/oauth2/token', data=data, headers=headers)

    print(res)
    print(res.status_code)
    print(res.text)


# get_token()


def meth2():

    client_id = ""
    client_secret = ""

    callback_uri = "https://03ac-61-1-208-167.ngrok.io/user/register/callback"

    cognito_app_url = "http"
    code = "3e21d44a-cc40-4f7c-954f-5b7556e5f4ac"

    token_url = f"{cognito_app_url}/oauth2/token"
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

    params = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "code": code,
        "redirect_uri": callback_uri
    }

    response = requests.post(token_url, auth=auth, data=params)

    print(response.json())


meth2()
