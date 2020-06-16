import requests
response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
print(response.content)
b'{\n  "authenticated": true, \n  "user": "user"\n}\n'
print(response.json())
{'user': 'user', 'authenticated': True}
