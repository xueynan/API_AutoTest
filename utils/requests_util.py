"""
    封装get请求
"""
import requests


def requests_get(url, headers=None, data=None):
    result = requests.get(url, headers=headers, data=data)
    code = result.status_code
    try:
        body = result.json()
    except Exception as e:
        body = result.text
        print(f"{e}不是json")
    contents = dict()
    contents["code"] = code
    contents["body"] = body
    return contents


"""
    封装post请求
"""


def requests_post(url, headers=None, data=None):
    result = requests.post(url, headers=headers, data=data)
    code = result.status_code
    try:
        body = result.json()
    except Exception as e:
        body = result.text
        print(f"{e}不是json")
    contents = dict()
    contents["code"] = code
    contents["body"] = body
    return contents
