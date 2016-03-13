# Configurations for core

The main `core` configuration is auto-loaded from the `/etc/g8os/g8os.toml` file. The main config file has the following sections

- main
- controllers
- extension
- logging

## main section
```toml
[main]
max_jobs = 200
message_ID_file = "/var/run/core.mid"
include = "/etc/g8os/g8os.d"
network = "/etc/g8os/network.toml"
```

- **max_jobs** Max parallel jobs the core can execute at the same time as his own directly children.
- **message_id_file**: tracks log message id (will probably get deprecated in the future)
- **include**: Include all toml files from the specified directory. This directory can have configurations for startup services and extensions
- **network**: Networking configurations file

## controllers section
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

Define one of more controller to connect to.

## extension
example
```toml
[extension.bash]
binary = "bash"
args = ['-c', 'T=`mktemp` && cat > $T && bash $T; EXIT=$?; rm -rf $T; exit $EXIT']
```

Extension are wrapper around the basic `execute` command. It makes calling certain binaries easier for example the above extesnion
will allow the client to send bash script to the core without the need to construct a complex `execute` command.

It basically be translated to a bash command with the provided arguments, which dumps the `stdin` into a file and then execute
that file and return exit code.

Core already ships with lots of extensions including extensions to manage file syncing, and executing jumpscripts.

# logging
example
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

Define logger and log levels to store per logger. Available loggers types are:
- db, stores logs into bolt db files
- ac, patch and send logs to controller
- console, print logs on the console.
