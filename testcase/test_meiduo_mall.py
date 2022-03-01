"""
    testcase1：登录测试：用户名和密码都正确
"""
# 1.导入包
import requests


# 2.定义登录方法
def login():
    # 3.定义测试数据
    url = "http://211.103.136.242:8064/authorizations/"
    data = {
            "username": "python",
            "password": "12345678"
            }
# 4.发送post请求
    result = requests.post(url, json=data)
# 5.输出结果
    print(result.json())
# 6.获取json里的token
    token = result.json()['token']
    return token


"""
    testcase2：获取个人信息测试：登录后获取个人信息成功
"""


def info():
    url = "http://211.103.136.242:8064/user/"
    token = login()
    headers = {
        'Authorization': 'JWT ' + token
    }
    result = requests.get(url, headers=headers)
    print(result.json())


if __name__ == "__main__":
    login()
    info()
