import allure
import yaml

from api.login import LoginApi
import pytest
import json
import config

# 第二种方式： 数据在json文件中，读取json文件，然后用json.loads()方法转换成字典，再传入login()方法中。
# 读取json文件
def read_json_file(file_name):
    # 定义列表，用于存储json文件中的数据
    data_list = []
    # 打开json文件
    with open(file_name, 'r', encoding='utf-8') as f:
        # 读取json文件中的数据
        # data = json.load(f)
        # 读取yaml文件中的数据
        data = yaml.safe_load(f)
        # 遍历json文件中的数据，将数据添加到列表中
        for item in data:
            # 取出每一个item中的数据，添加到列表中
            username = item.get('username')
            password = item.get('password')
            status = item.get("status")
            msg = item.get("msg")
            code = item.get("code")
            data_list.append((username,password,status,msg,code))
    return data_list

# print(read_json_file(file_name=config.BASE_PATH + "/data/login.json"))
print(read_json_file(file_name=config.BASE_PATH + "/data/login.yaml"))

# 创建测试类
class TestLoginApi:
    # 定义全局变量
    uuid = None
    token = None

    # 前置处理方法
    def setup_method(self):
        self.login_api = LoginApi()
        # 获取验证码
        res_get_code = self.login_api.get_image_code()
        TestLoginApi.uuid = res_get_code.json().get('uuid')


    # 后置处理方法
    def teardown_method(self):
        pass

    # 1. 登录功能测试
    # 参数化语法：哪个方法需要使用参数化，就在那个方法上使用装饰器
    # @pytest.mark.parametrize("参数1,参数2,参数3,参数4,参数5", 参数化列表)
    @pytest.mark.parametrize("username,password,status,msg,code",
                             read_json_file(file_name=config.BASE_PATH + "/data/login.yaml"))
    def test_login(self,username,password,status,msg,code):
        allure.dynamic.feature("登录功能接口测试")
        # 登录数据
        login_data = {
            "username": username,
            "password": password,
            "code":2,
            "uuid": TestLoginApi.uuid
        }
        res_login = self.login_api.login(test_data=login_data)
        assert status == res_login.status_code
        assert msg in res_login.text
        assert code == res_login.json().get('code')








