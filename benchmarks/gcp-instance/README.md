This is where descriptions of the benchmarking enviorment will go for the GCP instance will go such as specs and hardware. 

All Benchmarks were queried on a Archive Node with a Block Height less than 
1.1 Million.


wrk script used for these benchmarks
```
wrk -d2m -t4 -c12 --timeout 120s --latency -s ./lua-scripts/lightweight-bench.lua http://127.0.0.1
:8080
```

In order to get an updated summary of the benchmarks run the python script inside of scripts from the main directory. 

ex:
```
python3 ./scripts/aggregate.py
```