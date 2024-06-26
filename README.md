# Generate Volumes Script

The `generate_volumes.sh` is a bash script used to create a specific directory structure on your local machine. This script creates directories named `data1-1`, `data1-2`, ..., `data4-2`, and inside each directory, it creates subdirectories named `data1` and `data2`.

To run this script, navigate to the directory containing the `generate_volumes.sh` file and use the following command:

```bash
bash generate_volumes.sh
```

# Docker Compose File

The Docker Compose file is a YAML file that defines services, networks, and volumes. It allows you to manage your application's services as a single unit. 

To deploy with Docker Compose, you need to have Docker and Docker Compose installed on your machine. Once installed, navigate to the directory containing your `docker-compose.yml` file and run the following command:

```bash
docker-compose up
```

This command will start and run your entire app. Docker Compose will pull the images for any services that need to be created, and start all the services defined in your `docker-compose.yml` file.

# Locust File

The `locustfile.py` is a Python script that defines the behavior of users (locusts) in your system. It specifies what paths the users should hit and what data they should send.

In the provided `locustfile.py`, there are several tasks defined under the `MinIOUser` class. These tasks simulate the actions of uploading and downloading files to and from a MinIO server. The MinIO server's IP, port, access key, and secret key are defined in the `on_start` method.

# Volumes

In Docker, a volume is a designated directory on the host machine that bypasses the Union File System, to provide several useful features for persistent or shared data:

- Volumes are initialized when a container is created.
- If the container's base image contains data at the specified mount point, that existing data is copied into the new volume upon volume initialization.
- Data volumes can be shared and reused among containers.
- Changes to a data volume are made directly.
- Changes to a data volume will not be included when you update an image.
- Data volumes persist even if the container itself is deleted.

In the context of the `docker-compose.yml` file, volumes are used to persist the data generated by and used by Docker containers. Even when the container stops, the volume data remains and can be reattached to other containers. 

For example, if you have a volume named `data i-j`, you can use it in your services like this:

```yaml
services:
  service_name:
    image: image_name
    volumes:
      - data i-j:/path/in/container
```

This will mount the `data i-j` volume to `/path/in/container` in the `service_name` service's containers. Any data the service writes to `/path/in/container` will be stored in the `data i-j` volume.
