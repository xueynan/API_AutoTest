"""
    美多商城接口测试
"""
# 1.导入包
import requests
from utils import requests_util
from utils.requests_util import Request

"""
    testcase1：登录成功
"""


# 2.定义登录方法
def login():
    # 3.定义测试数据
    url = "http://211.103.136.242:8064/authorizations/"

    data = {
            "username": "python",
            "password": "12345678"
            }
    method = "post"
# 4.发送post请求
#     result = requests.post(url, json=data)
#     result = requests_util.requests_post(url, data=data)
    result = Request().requests_api(url=url, method=method, data=data)
# 5.输出结果
#     print(result.json())    # 结果会有两条print后的，以为info()调用的时候会调用login()里的print
# 6.获取json里的token
#     token = result.json()['token']
    token = result["body"]["token"]
    return token


"""
    testcase2：登录后获取个人信息成功
"""


def info():
    url = "http://211.103.136.242:8064/user/"
    token = login()
    headers = {
        'Authorization': 'JWT ' + token
    }
    method = "get"
    result = Request().requests_api(url=url, method=method, headers=headers)
    # result = requests_util.requests_get(url, headers=headers)
    # result = requests.get(url, headers=headers)
    # print(result.json())
    print(result)


"""
    testcase3：获取商品信息成功
"""


def product_list():
    method = 'get'
    url = "http://211.103.136.242:8064/categories/115/skus/"
    data = {
            "page": "1",
            "page_size": "1000",
            "ordering": "create_time"
            }
    # result = requests.get(url, json=data)
    # print(result.json())
    # result = requests_util.requests_get(url,data=data)
    result = Request().requests_api(url=url, method=method, data=data)
    print(result)


"""
    testcase4：添加购物车成功
"""


def shop():
    url = "http://211.103.136.242:8064/cart/"
    data = {
            "sku_id": "3",
            "count": "3",
            "selected": "true"
            }
    token = login()
    headers = {
        'Authorization': 'JWT ' + token
    }
    method = "post"
    # result = requests.post(url, json=data, headers=headers)
    # print(result.json())
    # result = requests_util.requests_post(url, data=data, headers=headers)
    result = Request().requests_api(url=url, method=method, data=data, headers=headers)
    print(result)


"""
    testcase5：保存订单成功
"""


def order():
    url = "http://211.103.136.242:8064/orders/"
    data = {
            "address": "1",
            "pay_method": "1"
            }
    token = login()
    headers = {
        'Authorization': 'JWT ' + token
    }
    method = "post"
    # result = requests.post(url, json=data, headers=headers)
    # print(result.json())
    # result = requests_util.requests_post(url, data=data, headers=headers)
    result = Request().requests_api(url=url, method=method, data=data, headers=headers)
    print(result)


if __name__ == "__main__":
    login()
    info()
    product_list()
    shop()
    order()
