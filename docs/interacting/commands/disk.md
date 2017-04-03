# Disk Commands

Available Commands:

- [disk.list](#list)
- [disk.mktable](#mktable)
- [disk.mkpart](#mkpart)
- [disk.rmpart](#rmpart)
- [disk.mount](#mount)
- [disk.umount](#umount)


<a id="list"></a>
## disk.list
Takes no arguments.
List all block devices (similar to lsblk)


<a id="mktable"></a>
## disk.mktable
Arguments:
```javascript
{
    "disk": "/dev/disk", //device
    "table_type": "gpt", //partition table type
}
```
Creates a new partition table on device. `table_type` can be any value
that is supported by `parted mktable`


<a id="mkpart"></a>
## disk.mkpart
Arguments:
```javascript
{
    "disk": "/dev/disk", //device
    "part_type": "primary", //part_type
    "start": "1", //start sector
    "end": "100%", //end sector
}
```
Creates a partition on given device. `part_type`, `start`, and `end` values must
be supported by the `parted mkpart` command


<a id="rmpart"></a>
## disk.rmpart
Arguments:
```javascript
{
    "disk": "/dev/disk", //device
    "number": 1, //parition number (1 based index)
}
```
Removes a partition on given device with given 1 based index.


<a id="mount"></a>
## disk.mount
Arguments:
```javascript
{
    "options": "auto", //mount options (required) if no options are needed set to "auto"
    "source": "/dev/part", //patition to mount
    "target": "/mnt/data", //location to mount on
}
```

<a id="umount"></a>
## disk.umount
Arguments:
```javascript
{
    "source": "/dev/part", //partition to umount
}
```
