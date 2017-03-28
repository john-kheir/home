# Starting Containers

## Pre-requirements

- Make sure you have a working Core0 based on Docker or VirtualBox
- Make sure you can create a Python client instance and you can reach the Core0

Steps:

- [Creating a data disk](#create-datadisk)
- [Creating a container](#create-container)


<a id="create-datadisk"></a>
## Creating a data disk

The below script will create a partition on the actual device. The data disk is not required, it is just to show a full example of a real life container scenario. So you can also skip this and create a container with no data disks. Alternatively you can create a loop device (against a file) for testing.

```python
# A new disk required a partition table
cl.disk.mktable('/dev/sdb')

# Create a partition that spans 100% of disk space
cl.disk.mkpart('/dev/sdb', '1', '100%')

# inspect the created parition
cl.disk.list()

# Create a btrfs filesystem
cl.btrfs.create("data", "/dev/sdb1")

# make sure mount point exists
cl.system('mkdir /data')

# mount root data disk to /data
cl.disk.mount("/dev/sdb1", "/data")

#create a subvolume
cl.btrfs.subvol_create('/data/vol1')
```

<a id="create-container"></a>
## Creating a container

We will create a very basic container that only mounts the root filesystem.

We use this flist for testing: `https://stor.jumpscale.org/stor2/flist/ubuntu-g8os-flist/ubuntu-g8os.flist`.

Here's the Python script using the G8OS client:

```python
flist = 'https://stor.jumpscale.org/stor2/flist/ubuntu-g8os-flist/ubuntu-g8os.flist'

container_id = cl.container.create(flist, mount=mount)
container = cl.container.client(container_id)

print(container.system('ls -l /opt').get())
```
