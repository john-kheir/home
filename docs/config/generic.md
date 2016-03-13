# Configurations for core

The main `core` configuration is auto-loaded from the `/etc/g8os/g8os.toml` file. The main config file has the following sections

- main
- controllers
- channel
- extension
- logging
- hubble 

##Networking
The core applies the network configuration as follows
- It applies the configuration as configured in the `/etc/g8os/network.toml` file
- It tries to reach at least one of the configured `controllers`
- If it can't reach any, it tries `dhcp` on all interfaces one at a time and try to reach any of the controllers again
- If it still can't reach, it will fall back to random static IP (in range `10.254.254.0/24`) and tries to reach a controller on `10.254.254.254`

The network configuration file is structured as follows
```toml
[network]
auto = true

[interface.<ifname>]
protocol = "<protocol>"

[<protocol>.<ifname>]
#protocol specific configuration
#for that interface
```

The `[network]` section currently only have the `auto` flag, which tells core to auto configure all found interfaces using the dhcp method if there is no specific `interface` section for that interface.
if `auto` is set to false, the `core` will just ignore any interface that is not specificly configured in the network.toml file.

### Network protocols
Currently only the following configurations protocols are supported
#### dhcp
The `dhcp` method doesn't require any further configurations, specifying `protocl = "dhcp"` is enough.
#### static
The `static` method requires a `[static.<if>]` section
Example:
```toml
[interface.eth0]
protocol = "static"

[static.eth0]
ip = "10.20.30.40/24"
gateway = "10.20.30.1"
```


