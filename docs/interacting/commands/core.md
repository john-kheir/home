# Core Commands

Available Commands:

- [core.ping](#ping)
- [core.system](#system)
- [core.kill](#kill)
- [core.killall](#killall)
- [core.state](#state)
- [core.reboot](#reboot)


<a id="ping"></a>
## core.ping
Doesn't take any arguments. Returns a "pong". Main use case is to check wether the core is responding.


<a id="system"></a>
## core.system
Arguments:
```javascript
{
	"name": "executable",
	"dir": "pwd",
	"args": ["command", "arguments"]
	"env": {"ENV1": "VALUE1", "ENV2": "VALUE2"},
	"stdin": "data to pass to executable over stdin"
}
```

Executes a given command.


<a id="kill"></a>
## core.kill
Arguments:
```javascript
{
    "id": "process-id-to-kill"
}
```
Kills a certain process giving the process ID. The process/command ID is the ID of the command used to start this process
in the first place.


<a id="killall"></a>
## core.killall
Takes no arguments
Kills ALL processes on the system. (only the ones that where started by core0 itself) and still running by the time of calling this command


<a id="state"></a>
## core.state
Takes no arguments.
Returns aggregated state of all processes plus the consumption of core0 itself (cpu, memory, etc...)


<a id="reboot"></a>
## core.reboot
Takes no arguments.
Immediately reboot the machine.
