To generate this message, Docker took the following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
(amd64)
3. The Docker daemon created a new container from that image which runs the
executable that produces the output you are currently reading.
4. The Docker daemon streamed that output to the Docker client, which sent it
to your terminal.


Docker pull image from docker hub 
```
docker pull <image_name>
```

Show list of images
```
docker images
```

Show list containers
```
docker ps

docker ps -a # all container
```

![1](./1.png)

run image
```
docker run
```

run image by name
```
docker run --name <container name>
```

for remove container 
```
docker rm <container name>
```

for remove all of stopped container 
```
docker container prune
```

for run image and delete from stopped container 
```
docker run --rm <image name>
```

for remove image 
```
docker rmi <image name>
```

docker run container with command
```
docker run <container name> <command>
```
```
docker run busybox ls 
```

for interactive 
```
docker run -it <conatiner name>
```

run container in background and print container ID
```
docker run <image name> --detach(-d)
``` 

lifecycle and not stopped
```
docker run -dit <image name>
```

for example 
```
docker run -dit busybox
```
![2](./2.png)

for create container
```
docker create --name <container name> <image>
``` 

for start container
```
docker start <container name>
```

for restart container
```
docker restart <container name>
```

for stop container
```
docker stop <container name>
```

for kill (stop force) container
```
docker kill <container name>
```

execute a command in a running container
```
docker exec <container name> <command>
```

for inteactive terminal
```
docker exec -it <container name> (bash or sh) 
```

## Restart policy

1. no
Do not automatically restart the container. (the default)

2. on-failure[:max-retries]
Restart the container if it exits due to an error, which manifests as a non-zero exi]]]t code. Optionally, limit the number of times the Docker daemon attempts to restart the container using the :max-retries option.

3. always 
Always restart the container if it stops. If it is manually stopped, it is restarted only when Docker daemon restarts or the container itself is manually restarted. (See the second bullet listed in restart policy details)

4. unless-stopped 	
Similar to always, except that when the container is stopped (manually or otherwise), it is not restarted even after Docker daemon restarts.

### always vs unless-stopped 
always -> restart after Docker daemon(sudo systemctl restart docker) 
unless-stopped  -> not restart after Docker daemon(sudo systemctl restart docker)

```
docker run -d --restart <restart poilicy> <image>
```

## Dockerfile
![3](./3.png)
### FROM
```
FROM [--platform=<platform>] <image> [AS <name>]
Or
FROM [--platform=<platform>] <image>[:<tag>] [AS <name>]
Or
FROM [--platform=<platform>] <image>[@<digest>] [AS <name>]
```
The FROM instruction initializes a new build stage and sets the Base Image for subsequent instructions. As such, a valid Dockerfile must start with a FROM instruction. The image can be any valid image – it is especially easy to start by pulling an image from the Public Repositories.

### ENV
```
ENV <key>=<value> ...
```

The ENV instruction sets the environment variable <key> to the value <value>. This value will be in the environment for all subsequent instructions in the build stage and can be replaced inline in many as well. The value will be interpreted for other environment variables, so quote characters will be removed if they are not escaped. Like command line parsing, quotes and backslashes can be used to include spaces within values.
Example:
```
ENV MY_NAME="John Doe"
ENV MY_DOG=Rex\ The\ Dog
ENV MY_CAT=fluffy
```

### RUN
RUN has 2 forms:
```
RUN <command> (shell form, the command is run in a shell, which by default is /bin/sh -c on Linux or cmd /S /C on Windows)
RUN ["executable", "param1", "param2"] (exec form)
```

The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.

Layering RUN instructions and generating commits conforms to the core concepts of Docker where commits are cheap and containers can be created from any point in an image’s history, much like source control.

The exec form makes it possible to avoid shell string munging, and to RUN commands using a base image that does not contain the specified shell executable.

The default shell for the shell form can be changed using the SHELL command.

In the shell form you can use a \ (backslash) to continue a single RUN instruction onto the next line. For example, consider these two lines:
```
RUN /bin/bash -c 'source $HOME/.bashrc && \
echo $HOME'
```

Together they are equivalent to this single line:
```
RUN /bin/bash -c 'source $HOME/.bashrc && echo $HOME'
```

To use a different shell, other than ‘/bin/sh’, use the exec form passing in the desired shell. For example:
```
RUN ["/bin/bash", "-c", "echo hello"]
```

### CMD
The CMD instruction has three forms:
```
CMD ["executable","param1","param2"] (exec form, this is the preferred form)
CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
CMD command param1 param2 (shell form)
```

**There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect.**

The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well.

If CMD is used to provide default arguments for the ENTRYPOINT instruction, both the CMD and ENTRYPOINT instructions should be specified with the JSON array format.

for build of Dockerfile
```
docker build -t <name image>:<tag name> <path Dockerfile>
```
for example
```
docker build -t web:latest .
```

## Port Forwarding
```
docker run -p <system-port>:<container-port> <image name>
``` 

Example
```
docker run -p 1012:6379 redis
``` 

### Save And Load
save image to tar file
```
docker save -o <file.tar> <image name>
```

load image from tar file
```
docker load -i <file.tar>
```

### Commit
Create a new image from a container's changes
```
docker container commit <container name> <new image name>
```
```
docker container commit -a <author> -m <message> <container name> <new image name>
```

### Volumes
Volumes are the preferred mechanism for persisting data generated by and used by Docker containers. While bind mounts are dependent on the directory structure and OS of the host machine, volumes are completely managed by Docker

```
docker run -v <system-path>:<container-path> <image-name>
```

Example
```
docker run -d \
    --name devtest \
    --mount source=myvol2,target=/app,readonly \
    nginx:latest 
```
```
docker run -d \
    --name devtest \
    -v myvol2:/app:ro \
    nginx:latest
```
```
docker run -itd --name app2 --volumes-from app1 alpine
```
## Networking
Create a network
Usage
```
docker network create [OPTIONS] NETWORK
```

Refer to the options section for an overview of available OPTIONS for this command.
Description

Creates a new network. The DRIVER accepts bridge or overlay which are the built-in network drivers. If you have installed a third party or your own custom network driver you can specify that DRIVER here also. If you don’t specify the --driver option, the command automatically creates a bridge network for you. When you install Docker Engine it creates a bridge network automatically. This network corresponds to the docker0 bridge that Engine has traditionally relied on. When you launch a new container with docker run it automatically connects to this bridge network. You cannot remove this default bridge network, but you can create new ones using the network create command.

```
docker network create -d bridge my-bridge-network
```

## Docker Compose
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

Compose works in all environments: production, staging, development, testing, as well as CI workflows. It also has commands for managing the whole lifecycle of your application:

* Start, stop, and rebuild services
* View the status of running services
* Stream the log output of running services
* Run a one-off command on a service

Example
```
services:
    rabbitmq:
        container_name: rabbitmq
        image: rabbitmq:latest
        networks:
          - main
        ports:
            - "5672:5672"
        restart: on-failure

    postgres:
        container_name: postgres
        image: postgres:latest
        environment:
            - POSTGRES_DB=postgres
            - POSTGRES_USER=postgres
            - POSTGRES_PASSWORD=postgres
        networks:
            - main
        ports:
            - "5432:5432"
        restart: on-failure
        volumes:
            - postgres_data:/var/lib/postgresql/data

    celery_worker:
        container_name: celery_worker
        command: "celery -A A worker -l INFO"
        depends_on:
            - app
            - rabbitmq
            - postgres
        image: app-image
        environment:
            - C_FORCE_ROOT="true"
        networks:
            - main
        restart: on-failure

    app:
        build: .
        command: sh -c "python manage.py migrate && gunicorn A.wsgi -b 0.0.0.0:8000"
        container_name: app
        volumes:
            - .:/code/
        depends_on:
            - postgres
            - rabbitmq
        expose:
            - "8000"
        networks:
            - main
        restart: on-failure

    nginx:
        container_name: nginx
        command: nginx -g 'daemon off;'
        depends_on:
            - app
        image: nginx:latest
        networks:
            - main
        ports:
            - "80:80"
        restart: on-failure
        volumes:
            - ./nginx.conf:/etc/nginx/nginx.conf


networks:
    main:

volumes:
    postgres_data:
```

## Danging Image
