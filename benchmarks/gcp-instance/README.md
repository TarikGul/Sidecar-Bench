## Specs

```
Machine type:
n2-standard-4 (4 vCPUs, 16 GB memory)

CPU Platform:
Intel Cascade Lake

Hard-Disk:
500GB
```

## Notes

All Benchmarks were queried on a Polkadot Archive Node with a Block Height less than 
1.1 Million.

### wrk

wrk script used for these benchmarks
```
wrk -d2m -t4 -c12 --timeout 120s --latency -s ./lua-scripts/lightweight-bench.lua http://127.0.0.1
:8080
```

### Aggregate

In order to get an updated summary of the benchmarks run the python script inside of `../../scripts`. 

ex:
```
python3 ./scripts/aggregate.py
```