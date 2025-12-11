# 课程模块
import requests
import config

class CourseApi:
    def __init__(self):
        # 新增课程
        self.add_course_url = config.BASE_URL +"/api/clues/course"
        # 查询课程列表
        self.query_coure_url = config.BASE_URL + "/api/clues/course/list"


    # 新增课程接口
    def add_course(self,test_data,token):
        return requests.post(url=self.add_course_url,
                             json=test_data,
                             headers={"Authorization":token})

    # 查询课程接口
    def query_course(self,test_data,token):
        return requests.get(url=self.query_coure_url,
                            params=test_data,
                            headers={"Authorization":token})


