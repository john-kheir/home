# Bridge Management Commands

Available Commands:

- [bridge.create](#create)
- [bridge.list](#list)
- [bridge.delete](#delete)


<a id="create"></a>
## bridge.create

Creates a new bridge.

Arguments:
```javascript
{
    "name": "bridge-name", //required
    "hwaddr": "MAC address" //optional
}
```

<a id="list"></a>
## bridge.list

List all available bridges.

Takes no arguments.


<a id="delete"></a>
## bridge.delete

Delete the given bridge name.

Arguments:
```javascript
{
    "name": "bridge-name", //required
}
```
