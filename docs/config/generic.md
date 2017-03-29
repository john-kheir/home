# Main Configuration

The main `core` configuration is auto-loaded from the `/etc/g8os/g8os.toml` file.

This configuration file has the following sections:

- [main](#main)
- [controllers](#controllers)
- [extension](#extension)
- [logging](#loging)

<a id="main"></a>
## main

```toml
[main]
max_jobs = 200
message_ID_file = "/var/run/core.mid"
include = "/etc/g8os/g8os.d"
network = "/etc/g8os/network.toml"
```

- **max_jobs**: Max parallel jobs the core can execute at the same time as its own direct children
- **message_ID_file**: Tracks log message id (will probably get deprecated in the future)
- **include**: Path to the directory with TOML files to include, this directory can have configurations for startup services and extensions
- **network**: Path to the network configuration file, discussed in [Network Configuration](network.md)


<a id="controller"></a>
## controllers

In this section you define one or more controllers to connect to:

```toml
[controllers]
    [controllers.main]
    url = "http://localhost:8966"
        [controllers.main.security]
        #UNCOMMENT THE FOLLOWING LINES TO USE SSL
        client_certificate = "/path/to/client-test.crt"
        client_certificate_key = "/path/to/client-test.key"
        # defines an extra CA to trust (used in case of server self-signed certs)
        # should be empty string otherwise.
        certificate_authority = "/path/to/server.crt"
```


<a id="extension"></a>
## extension

Extensions are wrappers around the basic `execute` command. It makes calling certain binaries easier.

For example the following extension will allow the client to execute a `bash` script without having to construct a complex `execute` command:

```toml
[extension.bash]
binary = "bash"
args = ['-c', 'T=`mktemp` && cat > $T && bash $T; EXIT=$?; rm -rf $T; exit $EXIT']
```

It basically translates to a bash command with the provided arguments, which dumps the `stdin` into a file and then executes that file and returns the exit code.

Core already ships with lots of extensions including extensions to manage file syncing, and executing JumpScripts.


<a id="logging"></a>
# logging

In this section you define the logger and the log levels to store per logger.

Available loggers types are:

- **db**: stores logs into bolt db files
- **ac**: patches and sends logs to controller
- **console**: prints logs on the console

Example:

```
[logging]
    [logging.db]
    type = "DB"
    address = "/var/log/g8os/"
    levels = [2, 4, 7, 8, 9, 11]  # (all error messages + debug) empty for all

    [logging.ac]
    type = "AC"
    flush_int = 300 # seconds (5min)
    batch_size = 1000 # max batch size, force flush if reached this count.
    controllers = [] # empty for all controllers, or controllers keys
    levels = [2, 4, 7, 8, 9, 11]  # (all error messages + debug) empty for all

    [logging.console]
    type = "console"
    levels = [2, 4, 7, 8, 9]
```
