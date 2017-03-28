## Installing Core0 on a Docker Container

Core0 is the `systemd` replacement for G8OS.

The below steps will guide you through the process to setup Core0 on a Docker container.

Steps:

- [Prepare a base Docker image to host Core0](#base-image)
- [Starting a container with core0](#start-container)
- [Access G8OS from JumpScale](#jumpscale-client)


<a id="base-image"></a>
## Prepare a base Docker image to host Core0

Copy the following content to a new Dockerfile somewhere on your system:

```dockerfile
FROM ubuntu:16.04
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y fuse && \
    apt-get install -y iproute2 && \
    apt-get install -y nftables && \
    apt-get install -y dnsmasq && \
    apt-get install -y libvirt-bin && \
    apt-get install -y redis-server
```

Build the image from your Dockerfile:

```bash
mkdir ~/build
cd ~/build
# write the content above to a Dockerfile in the build director
docker build -t core .
```

When the build is complete you should have the Core0 image ready to be used in the following steps.


<a id="start-container"></a>
## Starting a container with Core0

Make sure this repository is cloned under your correct GOPATH, which should be under $GOPATH/src/github.com/g8os/core0. Then move to that location the do a `make`:

```
cd $GOPATH/src/github.com/g8os/core0
go get github.com/g8os/core0/core0
go get github.com/g8os/core0/coreX
make
```

The do:

```
docker run --privileged -d \
    --name core-jo \
    -v `pwd`/bin/core0:/usr/sbin/core0 \
    -v `pwd`/bin/coreX:/usr/sbin/coreX \
    -v `pwd`/core0/g8os.dev.toml:/root/core.toml \
    -v `pwd`/core0/conf:/root/conf \
    -p 6379:6379 \
    core \
    core0 -c /root/core.toml
```

> Note: You might ask why we do this instead of copying those files directly to the image
> the point is, now it's very easy for development, each time u rebuild the binary or change the config
> u can just do `docker restart core0` without rebuilding the whole image.


> NOTE: if u are intending to use `containers` feature of core0, make sure u either copy the `g8ufs` binary to the container, or bind it (with `-v`) like core0 and coreX binaries


To follow the container logs do
```bash
docker logs -f core0
```

<a id="jumpscale-client"></a>
## Access G8OS from JumpScale

Before using the JumpScale client for G8OS make sure the `./pyclient` is in your `PYTHONPATH`.

This is how to use the JumpScale client for G8OS:

```python
import client

cl = client.Client(host='{ip of Docker container running Core0}')

#validate that core0 is reachable
print(cl.ping())

#then u can do stuff like
print(
    cl.system('ps -eF').get()
)

print(
    cl.system('ip a').get()
)

#client exposes more tools for disk, bridges, and container mgmt
print(
    cl.disk.list()
)
```
