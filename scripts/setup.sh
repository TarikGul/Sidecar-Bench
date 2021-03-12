#!/bin/sh

# Install the global lurocks packages
echo "Downloading luarocks dependencies"

echo "lua-cjson"
luarocks install lua-cjson

echo "luasocket"
luarocks install luasocket
