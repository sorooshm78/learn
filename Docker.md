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

