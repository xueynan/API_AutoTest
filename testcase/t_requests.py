# 1、导入包
import requests
# 2、发送get请求
result = requests.get("https://www.baidu.com")
# 3、打印结果
print(result.status_code)
print(result.headers)
# print(result.json())
print(result.url)
print(result.cookies)
print(result.text)
