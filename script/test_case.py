import allure
import pytest
from api.login import LoginApi
from api.course import CourseApi
from api.contract import ContractApi
import json
import config
import time


# 读取json文件
def read_json_file(file_name):
    # 定义列表，用于存储json数据
    data_list = []
    # 打开json文件
    with open(file_name,"r",encoding="utf-8") as f:
        data = json.load(f)
        # 遍历json数据，将数据添加到列表中
        for item in data:
            # 取出每一个item中的数据，添加到列表中

            username = item.get("username")
            password = item.get("password")
            status = item.get("status")
            msg = item.get("msg")
            code = item.get("code")
            data_list.append((username,password,status,msg,code))

    # 返回列表
    return data_list

print(read_json_file(file_name=config.BASE_PATH + "/data/login.json"))


# 创建测试类
#为测试报告添加项目名称
@allure.epic("项目名称：客达天下接口自动化测试")
class TestCase:
    # 定义全局变量
    uuid = None
    token = None
    fileName = None
    id = None

    # 前置处理方法
    def setup_method(self):
        # 创建登录API对象
        self.login_api = LoginApi()
        # 获取验证码
        res_get_code = self.login_api.get_image_code()
        TestCase.uuid = res_get_code.json().get('uuid')

        # 获取token

        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestCase.uuid
        }
        res_login = self.login_api.login(test_data=login_data)
        # print("登录成功获取token")
        print(res_login.status_code)
        # print(res_login.json())
        TestCase.token = res_login.json().get('token')
        # print(TestCase.token)

        # 创建课程API对象
        self.course_api = CourseApi()
        # 创建合同API对象
        self.contract_api = ContractApi()


    # 后置处理方法
    def teardown_method(self):
        pass


    print(" ")
    print("登录功能操作")
    # 1. 登录功能操作
    # @pytest.mark.parametrize("username,password,status,msg,code",
    #                          read_json_file(file_name = config.BASE_PATH + "/data/login.json"))
    # def test_login_success(self,username,password,status,msg,code):
    #
    #     # 1.2 登录数据
    #     login_data ={
    #         "username": username,
    #         "password": password,
    #         "code": 2,
    #         "uuid": TestCase.uuid
    #     }
    #
    #
    #     res_login = self.login_api.login(test_data=login_data)
    #     # print(res_login.status_code)
    #     # print(res_login.json())
    #     #
    #     # TestCase.token = res_login.json().get('token')
    #     # print(TestCase.token)
    #     # 1.3 断言
    #     assert status == res_login.status_code
    #     assert msg in res_login.text
    #     assert code == res_login.json().get("code")

    print(" ")
    print("新增课程操作")
    # 2.新增课程操作
    # def test_add_course(self):
    #     # 配置模块名称
    #     allure.dynamic.feature("新增课程接口测试")
    #     print("新增课程")
    #     # 2.1 新增课程数据
    #     course_data = {
    #         "name": "测试开发提升课01",
    #         "subject": "6",
    #         "price": 899,
    #         "applicablePerson": "2",
    #         "info":"测试开发提升课01"
    #     }
    #
    #     res_course = self.course_api.add_course(test_data=course_data,
    #                                             token=TestCase.token)
    #
    #
    #     print(res_course.status_code)
    #     print(res_course.json())

    print(" ")
    print("查询课程操作")
    # 3.查询课程操作
    # def test_query_course(self):
    #     allure.dynamic.feature("查询课程接口测试")
    #     print("查询课程")
    #     # 3.1 查询课程数据
    #     question_data = {}
    #
    #     res_query =self.course_api.query_course(test_data=question_data,
    #                                             token=TestCase.token)
    #
    #     print(res_query.status_code)



    print(" ")
    print("上传合同操作")
    # 4.上传合同操作
    def test_upload_contract(self):
        allure.dynamic.feature("上传合同接口测试")
        print('上传合同')

        f = open(config.BASE_PATH + "/data/test.pdf","rb")
        # f = open(config.BASE_PATH + "/data/doro.png", "rb")
        res_upload =self.contract_api.upload_contract(test_data=f,token = TestCase.token)
        print(res_upload.status_code)
        print(res_upload.json())
        TestCase.fileName = res_upload.json().get('fileName')
        print(TestCase.fileName)


    print(" ")
    print("新增合同操作")
    def test_add_contract(self):
        allure.dynamic.feature("新增合同接口测试")
        print('新增合同')
        # 获取当前时间戳
        print(int(time.time()))
        # print(f"HT{int(time.time())}")

        # 新增合同数据
        contract_data = {
            "name": "你跟你爹客气你妈呢",
            "phone": "18635067100",
            "contractNo": f"HT{int(time.time())}",
            "subject": "1",
            "courseId": 17467,
            "channel": "0",
            "activityId": "77",
            "fileName": TestCase.fileName
        }

        res_add = self.contract_api.add_contract(test_data = contract_data, token = TestCase.token)
        print(res_add.status_code)
        # 断言

        assert 200 == res_add.status_code
        assert '操作成功' == res_add.json().get('msg')

    print(" ")
    print("查询合同操作")
    # 6.查询合同操作
    # def test_query_contract(self):
    #     allure.dynamic.feature("查询合同接口测试")
    #     print('查询合同')
    #     # 查询合同数据
    #     query_data = {
    #         'phone': "13811111111"
    #     }
    #     res_query = self.contract_api.query_contract(test_data=query_data, token=TestCase.token)
    #     print(res_query.status_code)
    #     print(res_query.json())
















