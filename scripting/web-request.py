import requests

r = requests.get('https://xkcd.com/353/')

# print(r.text)

# print(dir(r))

p = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(p.content)

# with open('pic.png', 'wb') as pic:
#     pic.write(p.content)
    
    
payload = {'page': 2, 'count': 25}
hbin_get = requests.get('https://httpbin.org/get', params=payload)

# print(hbin_get.text)

payload2 = {'username': 'Subhranil', 'password': 'pass'}
hbin_post = requests.get('https://httpbin.org/post', data=payload2)

print(hbin_post.text)


hbin_auth = requests.get('https://httpbin.org/basic-auth/subhranil/pass', auth=('subhranil', 'pass'), timeout=3)

print(hbin_auth)