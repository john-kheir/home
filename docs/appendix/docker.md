## Running Core0 on a Docker Container

Core0 is the `systemd` replacement for G8OS.

The below steps will guide you through the process to running Core0 on a Docker container running Ubuntu.

Steps:

- [Starting a container with core0](#start-container)
- [Access G8OS from JumpScale](#jumpscale-client)

<a id="start-container"></a>
## Starting a container with Core0
```
docker run --privileged -d --name core -p 6379:6379 g8os/g8os:1.0
```

To follow the container logs do
```bash
docker logs -f core
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
