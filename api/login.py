# 登录模块
import requests
import config
# 创建一个接口类
class LoginApi:
    def __init__(self):
        # 获取验证码接口地址
        self.img_url = config.BASE_URL + "/api/captchaImage"
        # 登录接口地址
        self.login_url = config.BASE_URL + "/api/login"

    # 封装获取验证码接口
    def get_image_code(self):
        return requests.get(self.img_url)

    # 封装登录接口
    def login(self,test_data):
        # 在post中传入json数据，requests会自动添加Content-Type: application/json的请求头
        return requests.post(self.login_url,json=test_data)
