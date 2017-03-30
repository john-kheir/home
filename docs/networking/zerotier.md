# ZeroTier

More info about Zerotier: https://zerotier.com/manual.shtml

## How to connect to a zerotier network

For this example we assume you have a g8os node running and you can connect to it.

The following code make your g8os node to join the a public network provided by zerotier.
```python
import g8core

cl = g8core.Client(host='ip of the g8os')
cl.zerotier.join('8056c2e21c000001')
```

To check all the joined network:
```python
import g8core

cl = g8core.Client(host='ip of the g8os')
cl.zerotier.list()
```

and to leave a joined network
```python
import g8core

cl = g8core.Client(host='ip of the g8os')
cl.zerotier.leave('8056c2e21c000001')
```

## How to create a container and make the container join a zerotier network

You can also specify a zerotier network id when you create a container. This will make the container connect to the zerotier network just after creation. This is a nice way to allow people to reach you container without using natting.

Just pass the network id you want to join to the container create command of the client in the zerotier argument:
```python
import g8core

cl = g8core.Client(host='ip of the g8os')
cl.container.create("flist url", zerotier="8056c2e21c000001")
```
