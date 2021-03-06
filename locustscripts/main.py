from locust import HttpUser, task, between


class HelloHttpUser(HttpUser):
    wait_time = between(2, 5)
    host = "https://devilonwheels.com"
    print("Browsing homepage")

    @task
    def browse_homepage(self):
        self.client.get("/")
