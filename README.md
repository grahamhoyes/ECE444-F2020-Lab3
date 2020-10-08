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