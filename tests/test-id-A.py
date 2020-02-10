from locust import HttpLocust, TaskSet, task, between, constant_pacing
from locust.contrib.fasthttp import FastHttpLocust
import os

from dotenv import load_dotenv, find_dotenv
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

class CallOperatorAircraftList(TaskSet):

    @task(1)
    def call_operator_list(self):
        authorization_header = "Bearer " + os.environ.get('API_TOKEN')
        self.client.get("/api/v1/operators", headers={"Authorization":authorization_header})

    @task(2)
    def call_aircraft_list(self):
        authorization_header = "Bearer " + os.environ.get('API_TOKEN')
        self.client.get("/api/v1/aircrafts", headers={"Authorization":authorization_header})

class MyLocust(HttpLocust):
    task_set = CallOperatorAircraftList
    wait_time = between(1,2)


# class MyFastLocust(FastHttpLocust):
#     task_set = MyTaskSet
#     wait_time = between(1, 60)