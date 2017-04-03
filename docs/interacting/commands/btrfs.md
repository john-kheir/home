# Btrfs Commands

Available Commands:

- [btrfs.create](#create)
- [btrfs.list](#list)
- [btrfs.subvol_create](#subvol_create)
- [btrfs.subvol_list](#subvol_list)
- [btrfs.subvol_delete](#subvol_delete)


<a id="create"></a>
## btrfs.create

Create a Btrfs filesystem with the given label, devices, and profiles.

Arguments:
```javascript
{
    "label": "{label}",
    "devices": ["/dev/sdc1", "/dev/sdc2"],
    "data": "{data-profile}",
    "metadata": "{metadata-profile}"
}
```

Values:
- **label**: Name/label.
- **devices**: Array of devices, e.g. `["/dev/sdc1", "/dev/sdc2"]`
- **data-profile**: `raid0`, `raid1`, `raid5`, `raid6`, `raid10`, `dup` or `single`
- **metadata-profile**: Same as data-profile


<a id="list"></a>
## btrfs.list

List all Btrfs filesystems. It takes no arguments. Return array of all filesystems.


<a id="subvol_create"></a>
## btrfs.subvol_create

Creates a new Btrfs subvolume in the specified path.

arguments:
```javascript
{
    "path": "{path}"
}
```

Values:
- **path**: Path where to create the subvolume, e.g. `/path/of/subvolume`

<a id="subvol_list"></a>
## btrfs.subvol_list

Lists all subvolume under a path.

arguments:
```javascript
{
    "path": "{path}"
}
```

Values:
- **path**: Path to list.


<a id="subvol_delete"></a>
## btrfs.subvol_delete

Deletes a Btrfs subvolume in the specified path.

arguments:
```javascript
{
    "path": "{path}"
}
```

Values:
- **path**: Path where to deleted the subvolumes.
