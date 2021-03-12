-- Module instantiation
local cjson = require "cjson"
local cjson2 = cjson.new()
local cjson_safe = require "cjson.safe"
local http = require "socket.http"
local socket = require "socket"

-- Start by testing connection to Sidecar and receiving its version
local data = ""

local function collect(chunk)
  if chunk ~= nil then
    data = data .. chunk
  end
  return true
end

print("Testing connection with Substrate-api-sidecar....")

-- We can always change the url path to be set to an env variable
local ok, statusCode, headers, statusText = http.request {
  method = "GET",
  url = "http://127.0.0.1:8080/",
  sink = collect
}

print("ok\t",         ok);
print("statusCode", statusCode)
print("statusText", statusText)
print("headers:", headers)

if headers ~= nil then 
  for i,v in pairs(headers) do
    print("\t",i, v)
  end

  res = cjson.decode(data)
end

if statusCode == 200 then
  print("Running Substrate-api-sidecar version: ", res["version"])
  socket.sleep(0.5) 
  print("Now Running Benchmarks using Wrk")
else 
  print("Connection failure... Make sure Sidecar is running")
  socket.sleep(1)
  print("Exiting script...")
  socket.sleep(1)
  print("Goodbye")
  os.exit() 
end

-- Initialize the pseudo random number generator
-- Resource: http://lua-users.org/wiki/MathLibraryTutorial
math.randomseed(os.time())
math.random(); math.random(); math.random()

-- Shuffle array
-- Returns a randomly shuffled array
function shuffle(paths)
  local j, k
  local n = #paths

  for i = 1, n do
    j, k = math.random(n), math.random(n)
    paths[j], paths[k] = paths[k], paths[j]
  end

  return paths
end

-- Load URL paths from the file
function load_request_objects_from_file(file)
  local data = {}
  local content

  -- Check if the file exists
  -- Resource: http://stackoverflow.com/a/4991602/325852
  local f=io.open(file,"r")
  if f~=nil then
    content = f:read("*all")

    io.close(f)
  else
    -- Return the empty array
    return lines
  end

  -- Translate Lua value to/from JSON
  data = cjson.decode(content)

  return shuffle(data)
end

-- Load URL requests from file
requests = load_request_objects_from_file("./data/block-requests.json")

-- Check if at least one path was found in the file
if #requests <= 0 then
  print("multiplerequests: No requests found.")
  os.exit()
end

print("multiplerequests: Found " .. #requests .. " requests")

-- Initialize the requests array iterator
counter = 1

request = function()
  -- Get the next requests array element
  local request_object = requests[counter]

  -- Increment the counter
  counter = counter + 1

  -- If the counter is longer than the requests array length then reset it
  if counter > #requests then
    counter = 1
  end

  -- Return the request object with the current URL path
  return wrk.format(request_object.method, request_object.path)
end

delay = function()
  -- delay each request by 1 millisecond
  return 1
end

done = function(summary, latency, requests)
  
  -- Print results to the console
  print("Total completed requests: ", summary.requests)
  print("Failed requests: ", summary.errors.status)
  print("Timeouts: ", summary.errors.status)
  print("Average latency: ", (latency.mean/1000).."s")

  -- Save to a local txt file
  local file = io.open("./benchmarks/gcp-instance/sidecar-v" .. res["version"] .. ".txt", "w")
  file:write("Total completed requests: " .. summary.requests .. "\n")
  file:write("Failed requests: " .. summary.errors.status .. "\n")
  file:write("Timeoutes: " .. summary.errors.status .. "\n")
  file:write("Average latency: ", (latency.mean/1000).."s")
  file:close()
end
