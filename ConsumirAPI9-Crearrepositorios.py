import requests

if __name__ =='_main_':
        client_id = 'd267134110a0483ccd1b'
        client_secret = 'c79e0948a4b2152999d6acc3686a295b0e992461'
        code ='b0476adbb48dee2933cb'
##https://github.com/login/oauth/authorize?client_id=d267134110a0483ccd1b&scope=repo
        access_token = '41abb5ea3f71476caae788450fbb1489230db098'
        url='https://api.github.com/user/repos'

        payload= {'name' : 'git_api_cf_comunidad'}
        headers = {'Accept' : 'application/json' , 'Authorization' : 'token' + access_token}

        response=requests.post(url,headers=headers,json=payload)

        if response.status_code_code ==200:
             print(response.json())
        else :
             print(response.content)