# Main Configuration

The main `core` configuration is auto-loaded from the `/etc/g8os/g8os.toml` file.

This configuration file has the following sections:

- [main](#main)
- [sink](#sink)
- [logging](#loging)
- [stats](#stats)
- [globals](#globals)
- [extension](#extension)


<a id="main"></a>
## main

```toml
[main]
max_jobs = 200
include = "/config/root"
network = "/config/g8os/network.toml"
log_level = "debug"
```

- **max_jobs**: Max parallel jobs the core can execute concurrently (as its own direct children), once this limit is reached core0 will not pull for any new jobs from its dedicated Redis queue until it has at least one free job slot to fill
- **include**: Path to the directory with TOML files to include, this directory can have configurations for startup services and extensions, when core0 boots it will try to load all `.toml` files from the given locations, each of these TOML file can define one or more extensions to the core0 commands, and/or start up services
- **log_level** sets the logging level of core0 logs (what prints on console)
- **network**: Path to the network configuration file, discussed in [Network Configuration](network.md)


<a id="sink"></a>
## sink

A sink is a source of commands to run jobs.

Theoretically more than one sink type is supported. Currently only `redis` is supported as a sink type.

Each sink is defined in each own section as `[sink.<name>]` where name can be anything.

```
[sink.main]
# `url` Redis source url as shown below
url = "redis://127.0.0.1:6379"
# `password` optional Redis password.
password = ""
```


<a id="logging"></a>
# logging

In this section you define how core0 processes logs from running jobs.

Available loggers types are:

- **console**: prints logs on stdout (console) of core0
- **redis**: stores logs into bolt db files

For each logger you define log levels, specifying which log levels are logged to this logger

Example:

```
[logging]
  [logging.console]
  type = "console"
  levels = [1, 2, 4, 7, 8, 9]

	[logging.redis]
	type = "redis"
	levels = [1, 2, 4, 7, 8, 9]
	address = "127.0.0.1:6379"
	# batch_size (wrongly named) is how many log messages are kept in the queue
	# if the Redis queue length reached this limit, the queue will start to be trimmed
	# so older log messages will be dropped
	batch_size = 1000
```


<a id="stats"></a>
## stats

```
[stats]
# `interval` is deprecated and should be removed from the config files
interval = 60000 # milliseconds (1 min)

# Redis stats aggregator, use the Redis lua script to aggregate statistics outed by jobs
[stats.redis]
# `enabled`
enabled = true
flush_interval = 10 # seconds
address = "127.0.0.1:6379"
```

<a id="globals"></a>
## globals

```
# global config available for built in modules
[globals]
# `fuse_storage` default g8ufs storage to use when not passed by the container.create command
fuse_storage = ""
```


<a id="extension"></a>
## extension

An extension is simply a new command or functionality to extend what core0 can do. This allows you to add new functionality and commands to core0 without actually changing its code. An extension works as a wrapper around the `core.system` command by wrapping the actual command call.

The below example is a user management extension for adding and removing users, and changing their passwords:

```toml
[extension."user.add"]
binary = "useradd"
args = ["-m", "{username}"]

[extension."user.delete"]
binary = "userdel"
args = ["-f", "-r", "{username}"]

[extension."user.chpasswd"]
binary = "sh"
args = ["-c", "echo '{username}:{password}' | chpasswd"]
```

Adding the above into a TOML file and saving it in one of the paths specified in the `include` section of the main configuration file will add the following commands to core0:

 - **user.add**
   - Args: `{"username": "user name to add"}`
 - **user.delete**
   - Args: `{"username": "user name to remove"}`
 - **user.chpasswd**
   - Args: `{"username": "user", "password": "password to set"}`

This allows you to call the extension from the Python client as follows:

```python
client.raw("user.add", {"username": "testuser"})
client.raw("user.chpasswd", {"username": "testuser", "password": "new-password"})
```

> Core0 takes care of substituting the `{key}` notation in the extension arguments with the ones passed from the client.

Extension also supports the following attributes:

```toml
[extension.test]
binary = "binary"
args = ["args", "list", "to", "binary"]
# cwd of the binary
cwd = "/path"

#env variables will be available during command execution
[extension.test.env]
env1 = "value-1"
env2 = "value-2"
```
