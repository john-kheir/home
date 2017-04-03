# Creating Containers

Pre-requirements:

- Make sure you have a working Core0 instance running
- Make sure you can create a Python client instance and you can reach the Core0

In the below example a very basic container is created that only mounts the root filesystem.

We use this flist for testing: `https://hub.gig.tech/gig-official-apps/ubuntu1604.md`.

Here's the Python script using the G8OS client:

```python
import g8core
cl = g8core.Client("{IP OF G8OS}")

flist = 'https://hub.gig.tech/gig-official-apps/ubuntu1604.flist'

container_id = cl.container.create(flist, storage='ardb://hub.gig.tech:16379')
container = cl.container.client(container_id)

print(container.system('ls -l /opt').get())
```

See [Container Management](../interacting/commands/container/container.md) for all available commands for managing containers.
