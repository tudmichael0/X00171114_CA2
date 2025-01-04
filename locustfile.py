

from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 5)  #  Defines the wait time between tasks

    @task
    def test_endpoint(self):
        self.client.get("/")  #  Replace '/' with the endpoint you want to test
