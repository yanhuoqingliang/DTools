import requests

# 发送GET请求到目标网站
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
response = requests.get('http://192.168.12.165:8980/', headers=headers)

# 获取响应中的cookies
cookies = response.cookies

# 输出所有cookies
for cookie in cookies:
    print('Name:', cookie.name)
    print('Value:', cookie.value)
    print('Domain:', cookie.domain)
    print('Path:', cookie.path)
    print('Expires:', cookie.expires)
    print('Secure:', cookie.secure)
    # print('HttpOnly:', cookie.httponly)
    print('---------------------------------')
