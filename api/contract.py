# 合同模块
import requests
import config

# 封装class类
class ContractApi:

    def __init__(self):
        # 合同上传地址
        self.upload_url = config.BASE_URL + "/api/common/upload"

        # 新增合同地址
        self.addContract_url = config.BASE_URL + "/api/contract"

        # 查询合同列表地址
        self.queryContract_url = config.BASE_URL + "/api/contract/list"

        # 删除合同地址
        self.deleteContract_url = config.BASE_URL + "/api/contract/remove"



    # 上传合同
    def upload_contract(self, test_data, token):
        return requests.post(self.upload_url,
                             files={"file": test_data},
                             headers={"Authorization":token})

    # 新增合同
    def add_contract(self, test_data, token):
        return requests.post(self.addContract_url,json=test_data,headers={"Authorization":token})

    # 查询合同列表
    def query_contract(self, test_data, token):
        return requests.get(self.queryContract_url,
                            params=test_data,
                            headers={"Authorization":token})

    # 删除合同
    def delet_contract(self, test_data, token):
        return requests.post(self.deleteContract_url,
                             data=test_data,
                             headers={"Authorization":token})