import requests
import json

# Azure ADアプリケーションのクライアントID、テナントID、クライアントシークレットを設定
client_id = 'aaa'
tenant_id = 'bbb'
client_secret = 'ccc'

# Azure ADにアクセスするためのトークンを取得
url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'https://graph.microsoft.com/.default'
}
response = requests.post(url, headers=headers, data=data)
token = response.json()['access_token']

# Microsoft Graph APIを使用してアプリケーションを登録する
url = 'https://graph.microsoft.com/v1.0/applications'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
data = {
    'displayName': 'MyApplication',
    'signInAudience': 'AzureADandPersonalMicrosoftAccount',
    'requiredResourceAccess': [
        {
            'resourceAppId': '00000003-0000-0000-c000-000000000000', #この値はどう決まる？
            'resourceAccess': [
                {
                    'id': 'e1fe6dd8-ba31-4d61-89e7-88639da4683d', #この値はどう決まる？
                    'type': 'Scope'
                }
            ]
        }
    ],
    'web': {
        'redirectUris': [
            'https://localhost:8080' #パラメータ化が必要
        ]
    }
}
response = requests.post(url, headers=headers, json=data)
if response.ok:
    app_id = response.json()['id']
    print(f'Application registered with ID {app_id}')
else:
    print(f'Error registering application: {response.text}')