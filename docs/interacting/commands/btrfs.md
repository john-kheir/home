# Btrfs Commands

Available Commands:

- [btrfs.create](#create)
- [btrfs.list](#list)
- [btrfs.subvol_create](#subvol_create)
- [btrfs.subvol_list](#subvol_list)
- [btrfs.subvol_delete](#subvol_delete)


<a id="create"></a>
## btrfs.create

Create a btrfs filesystem

Arguments:
```javascript
{
    "label": "FS label/name", // required
    "devices": ["/dev/sdc1", "/dev/sdc2"], // the devices, required
    "data": "data profile",
    "metadata": "metadata profile"
}
```

<a id="list"></a>
## btrfs.list

List all Btrfs filesystems.

Takes no argument. Return array of all filesystems.


<a id="subvol_create"></a>
## btrfs.subvol_create

Creates a new Btrfs subvolume

arguments:
```javascript
{
    "path": "/path/of/subvolume" required
}
```


<a id="subvol_list"></a>
## btrfs.subvol_list

List subvolume under a path

arguments:
```javascript
{
    "path": "/path/of/filesystem" required
}
```


<a id="subvol_delete"></a>
## btrfs.subvol_delete

Delete a Btrfs subvolume

arguments:
```javascript
{
    "path": "/path/of/subvolume" required
}
```
