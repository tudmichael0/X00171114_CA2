


from locust  import HttpUser, task, between

class MyUser(HttpUser):
    # Defines the wait time between tasks
    wait_time = between(1, 5)

    @task
    def test_endpoint(self):
        # Replace '/' with the endpoint you want to test
        self.client.get("/")
