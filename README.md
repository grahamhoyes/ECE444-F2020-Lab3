This repo is adapted from https://github.com/miguelgrinberg/flasky

# Running in Docker
The Dockerfile for running locally is [Dockerfile](Dockerfile). This configuration copies the app folder into the container at build time, which is not ideal for development as it requires rebuilding the container with every change. For optimal development experience, this should be replaced with a volume mount to take advantage of Flask's hot reloading.

A docker-compose configuration is in [docker-compose.yml](docker-compose.yml). If you have `docker-compose` on your system, this simplifies the Docker commands below.

## Building
To build the image with standalone Docker, from the project root run:

```bash
$ docker build -t ece444-flask-lab4:latest .
```

This will create build the container, and tag the image `ece444-flask-lab4:latest`.

If using `docker-compose`, run:

```bash
$ docker-compose build
```

This will likewise build and tag the docker container.

You can inspect the image with `docker image ls ece444-flask-lab4`:

![image](https://user-images.githubusercontent.com/26036279/95507310-3a631280-097f-11eb-8e79-90b95b33629b.png)

## Running
To run the project using standalone Docker:

```bash
$ docker run -it --rm -p 5000:5000 ece444-flask-lab4:latest
```

![image](https://user-images.githubusercontent.com/26036279/95508613-48b22e00-0981-11eb-8433-5ab46e143a5b.png)

Explanation:
- `-it` attaches an interactive terminal, to monitor the output of the container. Alternatively, run `docker logs <container id>` if running in detached mode.
- `--rm` will delete the container once it is stopped.
- `-p 5000:5000` binds container port 5000 to host port 5000, so the service is accessible.

If using `docker-compose`, run:

```bash
$ docker-compose up
```

![image](https://user-images.githubusercontent.com/26036279/95508533-2cae8c80-0981-11eb-8228-5a5d81f25a51.png)

This will attach the container and print logs to the console. To run detached, pass the `-d` flag.

`docker-compose up` does not automatically delete containers when they are killed. To remove the container, or to stop and remove it if running detached, run `docker-compose down`.

Docker compose defaults container names to `<project name>_<service>_<id>`. Project name defaults to the name of the folder containing docker-compose.yml, which in my case is `lab3`. To change the project name, set the `COMPOSE_PROJECT_NAME` environment variable before running `docker-compose up`.

The app should now be live, and accessible in your browser at [localhost:5000](http://localhost:5000/).

![image](https://user-images.githubusercontent.com/26036279/95508911-b52d2d00-0981-11eb-8421-aa591c5d92ec.png)

# Docker vs Virtual Machines
While Docker containers may appear to be miniature VMs, they are not. The key distinction is that virtual machines contain their own operating system kernel. User mode programs in virtual machines trap into the host OS kernel, and are then passed down to the guest OS kernel for processing system calls. Processes in Docker containers, on the other hand, interact directly with the OS kernel of the host running docker. Docker containers also share resources with the host directly, whereas VMs see virtualized hardware (with services such as Docker Swarm or Kubernetes, it is possible to constrain the resources given to a docker container).

Any easy way to verify this is to run a process in a docker container (such as the web service above), and check your computer's process monitor (`htop` on linux, for example). The processes in the docker container will be visible alongside the rest of the native processes on your system, whereas processes running inside a VM are not visible to the host and vice-versa.

The benefit of using Docker containers is they provide a consistent user space when running across machines, so processes don't need to worry about all dependencies being installed on every host machine. They are also much quicker to run than traditional VMs. The downside is that programs must be compatible with the host Kernel. As a result, if you run a linux-based container on Windows, under the hood Docker will be running a lightweight VM of some kind to provide a linux environment on Windows.