# Container Management

Available commands:
- [container.create](#create)
- [container.list](#list)
- [container.terminate](#terminate)
- [container.client](#client)


<a id="create"></a>
## container.create

Creates a new container with the given root plist, mount points and ZeroTier ID, and connects it to the given bridges.

Arguments:

```javascript
{
  'root': {root_url},
  'mount': {mount},
  'network': {
      'zerotier': {zerotier},
      'bridge': {bridge},
  },
  'port': {port},
  'hostname': {hostname},
}
```

Values:

- **root_url**: the root filesystem plist

- **mount**: a dict with `{host_source: container_target}` mount points, where `host_source` directory must exists, `host_source` can be a URL to a plist to mount

- **zerotier**: An optional ZeroTier network ID to join

- **bridge**: list of tuples as `('bridge_name': 'network_setup')` where `network_setup` can be one of the following:
  - `''` or `'none'`: no IP is gonna be set on the link
  - `'dhcp'`: Run `udhcpc` on the container link, of course this will only work if the `bridge` is created with `dnsmasq` networking
  - `'CIDR'`: Assign static IP to the link

  Example: `bridge=[('br0', '127.0.0.100/24'), ('br1', 'dhcp')]`

- **port**: A dict of `host_port: container_port` pairs

  Example: `port={8080: 80, 7000:7000}`

- **hostname**: Specific hostname you want to give to the container, if None it will automatically be set to core-x, x being the ID of the container


<a id="list"></a>
### container.list

<a id="terminate"></a>
### container.terminate

<a id="client"></a>
### container.client
