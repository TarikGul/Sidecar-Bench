# Sidecar Bench

Benchmarking for Substrate-API-Sidecar

### TODO

* Update the `README.md` inside of the `benchmarking/gcp-instance` directory with specs and hardware

* Dockerfile

* Github actions

## GCP Setup (Debian 10)

#### --Git

```
$ sudo apt update
$ sudo apt install git
```

#### --Rust

Restart system after installing Rust

```
$ curl https://sh.rustup.rs -sSf | sh
$ rustup update
```

#### --Linux Pacakges

```
$ sudo apt install build-essential git clang libclang-dev pkg-config libssl-dev
$ sudo apt install wget
$ sudo apt install unzip
```

#### --Polkadot Archive Node

Setup Polkadot and build the source 

```
$ git checkout <latest tagged release>
$ ./scripts/init.sh
$ cargo build --release
```

Start syncing the Archive node in a background process

```
$nohup target/release/polkadot --name "rural-low-8355" --no-prometheus --no-telemetry --database=rocksdb
 --pruning=archive --wasm-execution=Compiled --chain=polkadot &

# Check if process is runnning. Returns a PID
$ pgrep polkadot

# Use PID to kill process
$ kill <PID>
```

#### --Node.js + NPM

This will download node 14.x

```
$ curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

$ npm install --global yarn
```

#### --Substrate-Api-Sidecar

Global
```
$ npm install --global @substrate/api-sidecar
# OR
$ yarn global add @substrate/api-sidecar
```

From source
```
$ git clone https://github.com/paritytech/substrate-api-sidecar.git
$ git checkout <latest tag>
```

#### --Lua && Luarocks (global packages)

```
$ sudo apt install lua 5.1
$ sudo apt install liblua5.1-0-dev
$ wget https://luarocks.org/releases/luarocks-3.3.1.tar.gz
$ tar zxpf luarocks-3.3.1.tar.gz
$ cd luarocks-X.Y.Z
$ ./configure 
$ sudo make bootstrap
```

#### --wrk 

```
git clone https://github.com/wg/wrk.git wrk
cd wrk
make

# move the executable to somewhere in your PATH, ex:
sudo cp wrk /usr/local/bin
```

#### --Sidecar-Bench

```
git clone https://github.com/TarikGul/Sidecar-Bench.git
sh ./lua-scripts/setup.sh
```

## Launch Benchmarks

```
cd Sidecar-bench
sh ./lua-scripts/init.sh
```

## Notes:

Currently there are 3 scripts inside of `./lua-scripts`. We are currently using `lightweight-bench.lua` because of its ability to put less load on the system and have morea ccurate benchmarking. `Json-bench.lua` reads in the paths to send requests too via a json file whereas `lightweight-bench.lua` reads in hardcoded values from a lua vector(array). `heavy-bench.lua` is similar to `json-bench.lua` but it also checks for a connection with Sidecar before running the wrk scripts and then checks for the version of sidecar that is running.

### Aggregate

In order to update the summary file in a benchmarking directory, run `python3 ./scripts/aggregate.py`. If you need to change the path for the benchmarking directory you can change it inside the script in the `main` function. 
