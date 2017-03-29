## Stats

The stats message format is as follows:

```
10::<key string>:<value float>|OP[|tags]
```

- `10::` (const) is the message prefix and must be of this value. it tells `core0/X` that this is a stats message
- `key` (string) is the metric key reported by the process.
- `value` (float) is the metric value at the time of the reporting
- `OP` (string) How to aggregate the reported values
  - `A` Average the values reported at the end of the current aggregator period
  - `D` Differential values (used usually for incremental counters like number of packets over network card)
- `tags` (string optional) user defined tags attached to the metric (currently not used)
