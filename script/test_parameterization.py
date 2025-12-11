# # 登录接口参数化
# from api.login import LoginApi
# import pytest
#
# # 第一种方式
# test_data = [
#     ("admin", "HM_2023_test", 200, "成功", 200),
#     ("", "HM_2023_test", 200, "错误", 500),
#     ("Fiona", "HM_2023_test", 200, "用户不存在", 500),
#     ("admin", "12345678", 200, "密码错误", 500)
# ]
# class TestLoginApi:
#     uuid =None
#
#     # 前置处理方法
#     def setup_method(self):
#         self.login_api = LoginApi()
#         # 获取验证码
#         res_img_code = self.login_api.get_image_code()
#         TestLoginApi.uuid = res_img_code.json().get('uuid')
#
#     # 后置处理方法
#     def teardown_method(self):
#         pass
#
#     # 登录功能测试
#     # 参数化语法：哪个方法需要使用参数化，就在那个方法上使用装饰器
#     # @pytest.mark.parametrize("参数1,参数2,参数3,参数4,参数5", 参数化列表)
#     @pytest.mark.parametrize("username,password,status,msg,code", test_data)
#     def test_login(self,username,password,status,msg,code):
#         login_data = {
#             "username": username,
#             "password": password,
#             "code": 2,
#             "uuid": TestLoginApi.uuid
#         }
#         res_login = self.login_api.login(test_data=login_data)
#         print(res_login.status_code)
#         print(res_login.json())
#         assert status == res_login.status_code
#         assert msg in res_login.text
#         assert code == res_login.json().get("code")