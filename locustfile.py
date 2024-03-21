from locust import HttpUser, task, between, events
from minio import Minio
from minio.error import S3Error
import time
import os


count = 0  # Initialize count
TotalTime = 0  # Initialize TotalTime

class MinIOUser(HttpUser):
    wait_time = between(1, 5)  # Random wait time between tasks

    def on_start(self):
        # Set up any required data or perform login
        self.minio_client = Minio(
            "172.19.0.5:9000", # replace with your MinIO server IP and port
            access_key="admin",
            secret_key="password",
            secure=False
        )

        # create test bucket if not already created
        if not self.minio_client.bucket_exists("mybucket"):
            self.minio_client.make_bucket("mybucket")

    @task
    def updateFile(self):

        file_path = "test_file.txt"  # replace with your file path
        try:
            start_time = time.time()
            self.minio_client.fput_object("mybucket", file_path, file_path)
            end_time = time.time()
            total_time = int((end_time - start_time) * 1000)
            events.request.fire(request_type="RpcClient",
                                name="mybucketTest",
                                response_time=total_time,
                                response_length=0,
                                exception=None)

        except S3Error as err:
            print(err)

    @task
    def downloadFile(self):

        file_path = "test_file.txt"  # replace with your file path
        try:
            start_time = time.time()
            self.minio_client.fget_object("mybucket", file_path, file_path)
            end_time = time.time()
            total_time = int((end_time - start_time) * 1000)
            events.request.fire(request_type="RpcClient",
                                name="mybucketTest",
                                response_time=total_time,
                                response_length=0,
                                exception=None)

        except S3Error as err:
            print(err)

    @task
    def updateLargeFile(self):
        file_path = "large_file"  # replace with your large file path
        try:
            start_time = time.time()
            self.minio_client.fput_object("mybucket", file_path, file_path)
            end_time = time.time()
            total_time = int((end_time - start_time) * 1000)
            events.request.fire(request_type="RpcClient",
                                name="mybucketTest",
                                response_time=total_time,
                                response_length=0,
                                exception=None)
        except S3Error as err:
            print(err)

    @task
    def downloadLargeFile(self):
        file_path = "large_file"  # replace with your large file path
        try:
            start_time = time.time()
            self.minio_client.fget_object("mybucket", file_path, file_path)
            end_time = time.time()
            total_time = int((end_time - start_time) * 1000)
            events.request.fire(request_type="RpcClient",
                                name="mybucketTest",
                                response_time=total_time,
                                response_length=0,
                                exception=None)
        except S3Error as err:
            print(err)