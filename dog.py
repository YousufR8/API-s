import requests

response = requests.get("https://api.thedogapi.com/v1/breeds")
requests = response.request


# print(response.status_code)
# print(response.text)
# print(response.headers)
# print(requests.headers)
print(requests.url)
print(requests.path_url)
'/v1/breeds'
requests.method
requests.headers
{'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate',
'Accept': '*/*', 'Connection': 'keep-alive'}
response

response.text
[{"weight":{"imperial":"6 - 13","metric":"3 - 6"},
"height":{"imperial":"9 - 11.5","metric":"23 - 29"},"id":1,
"name":"Affenpinscher"}]
response.status_code

response.headers
{'Cache-Control': 'post-check=0, pre-check=0', 'Content-Encoding': 'gzip',
'Content-Type': 'application/json; charset=utf-8',
'Date': 'Sat, 25 Jul 2020 17:23:53 GMT'}

