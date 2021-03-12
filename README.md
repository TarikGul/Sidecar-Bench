# Sidecar Bench

Benchmarking for Substrate-API-Sidecar

### TODO

* Need to add my step by step instructions on launching the GCP instance and setting up the enviornment to run the scripts. Currently I have it configured for a GCP instance in my own personal account. Next is to setup one via the Parity GCP developer hub. Then setup a CI workflow with a docker container via github actions to run the benchmarks.

* Additional routes to the data field and add a weight to blocks queries

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

$npm install --global yarn
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
```

## Launch Benchmarks

```
cd Sidecar-bench
sh init.sh
```

Version's of sidecar to benchmark and archive

    v3.0.5
    v3.0.4
    v3.0.3
    v3.0.2
    v3.0.1
    v3.0.0
    v2.1.2
    v2.1.1
    v2.1.0
    v2.0.0
    v1.1.0
    v1.0.0
    v1.0.0-rc4
    v1.0.0-rc3
    v1.0.0-rc2
    v1.0.0-rc1
    v0.18.1
    v0.18.0
    v0.17.0
    v0.16.0
    v0.15.0
    v0.14.0
    v0.13.0
    v0.12.0
    v0.11.3
    v0.11.2
    v0.11.1
    v0.11.0
    ...
