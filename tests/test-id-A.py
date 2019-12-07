from locust import HttpLocust, TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust

class MyTaskSet(TaskSet):

    @task(1)
    def call_operator_list(self):
        self.client.get("api/v1/operator/41174c3f-e86c-4e5a-a629-32d4d9da6011", {"Authorization":"Bearer "})

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    wait_time = between(5, 15)


# class MyFastLocust(FastHttpLocust):
#     task_set = MyTaskSet
#     wait_time = between(1, 60)