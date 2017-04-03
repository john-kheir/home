# Commands

## Core0

Core0 is the first process to start on bare metal. It works as a simple process manager.

When started it first configures the networking, and then starts a local Redis instance to dispatch commands to CoreX cores.

## Command structure

```javascript
{
	"id": "command-id",
	"command": "command-name",
	"arguments": {}, //command arguments depends on the command itself
	"queue": "optional-queue",
	"stats_interval": 0, //optional stats gathering interval (falls to default if not set)
	"max_time": 0, //Max run time of the command, if exceeded command will be killed
	"max_restart": 0, //Max number of retries to start the command if failed before giving up
	"recurring_period": 0, //If provided command is considered recurring
	"log_levels": [int] //Log levels to store locally and not discard.
}
```

The `Core0` Core understands a very specific set of management commands:


- [Core commands](core.md)
- [Info commands](info.md)
- [CoreX commands](corex.md)
- [Bridge commands](bridge.md)
- [Disk commands](disk.md)
- [Btrfs commands](btrfs.md)
