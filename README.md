# Dockerfiles
Collection of `Dockerfile`s for isolating closed-source software, creating custom
coding environments, etc.

### qcad
Build with:
`docker buildx build -t qcad .`

Add a qcad alias to your `.bashrc`:
```
alias qcad="xhost +local:docker \
    && docker run \
        --rm \
        --detach \
        --user qcad \
        --env DISPLAY \
        --device /dev/dri \
        --volume /tmp/.X11-unix:/tmp/.X11-unix \
        --volume /dev/shm:/dev/shm \
        --volume /home/<userdirecotry>/.qcad:/home/qcad \
        --volume /home/<userdirecotry>/Documents/qcad:/home/qcad/Documents \
        qcad"
```
Where `<userdirectory>` is your home directory.

Execute with: `qcad`
