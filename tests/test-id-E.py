from locust import HttpLocust, TaskSet, task, between, constant_pacing
from locust.contrib.fasthttp import FastHttpLocust
import os

from dotenv import load_dotenv, find_dotenv
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

class CallPrivilegedOperatorPilot(TaskSet):

    @task(1)
    def call_operator_detail(self):
        authorization_header = "Bearer " + os.environ.get('API_TOKEN')
        self.client.get("/api/v1/operators/41174c3f-e86c-4e5a-a629-32d4d9da6011/privileged", headers={"Authorization":authorization_header})

    @task(2)
    def call_pilot_detail(self):
        authorization_header = "Bearer " + os.environ.get('API_TOKEN')
        self.client.get("/api/v1/pilots/d4b8aa2c-0a52-4adc-806a-f363deb6a1e0/privileged", headers={"Authorization":authorization_header})

class MyLocust(HttpLocust):
    task_set = CallPrivilegedOperatorPilot
    wait_time = between(2,6)


# class MyFastLocust(FastHttpLocust):
#     task_set = MyTaskSet
#     wait_time = between(1, 60)