# Logging

In Core0 terminology, logging means capturing the output of the running processes and store or forward it to loggers.

A logger can decide to print the output of the command to the console, and/or push it to Redis.

The logger decides what messages to be logged based on the logger configurations, which can be overriden by the `command` `log_levels` attribute (if set) to force all loggers to capture and process these specific levels.

The default configuration template of Core0 will log all messages of levels `[1, 2, 4, 7, 8, 9]` both to the console and Redis.

CoreX logging is not configurable, it simply forwards all logs to Core0 logging. Which means Core0 logging configuration applies for both Core0 and CoreX domains.


## Logging Messages

When running any process on Core0 or CoreX the output of the processes are captured and processed as log messages. By default messages that are output on `stdout` stream are considered of level `1`, messages that are output on `stderr` stream are defaulted to level `2` messages.

The running process can leverage on the ability of Core0 to process and handle different log messages level by prefixing the output with the desired level as:

```
8::Some message text goes here
```

Or for multi-line output bulk:

```
20:::
{
    "description": "A structured json output from the process",
    "data": {
        "key1": 100,
    }
}
:::
```

Using specific levels, you can pipe your messages through a different path based on your nodes.

Also all `result` levels will make your return data captured and set in the `data` attribute of your job result object.


## Log Levels

- 1: stdout
- 2: stderr
- 3: message for endusers / public message
- 4: message for operator / internal message
- 5: log msg (unstructured = level5, cat=unknown)
- 6: log msg structured
- 7: warning message
- 8: ops error
- 9: critical error
- 10: statsd message(s)
- 20: result message, json
- 21: result message, yaml
- 22: result message, toml
- 23: result message, hrd
- 30: job, json (full result of a job)
