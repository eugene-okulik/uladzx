from locust import task, HttpUser
import random


class PerfTesting(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object',
            headers={'Content-Type': 'application/json'}
        )

    @task(3)
    def get_the_object(self):
        self.client.get(
            f'/object/{random.choice([1, 10, 1068, 1073])}',
            headers={'Content-Type': 'application/json'}
        )
