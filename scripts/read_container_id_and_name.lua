function get_container_id(tag, timestamp, record)
  path = record["filepath"]
  container = {}
  for s in string.gmatch(path, "([^/]*)/") do
    table.insert(container, s)
  end
  record["container_id"] = container[6]
  return 2, timestamp, record
end

function get_container_name(tag, timestamp, record)
  id = record["container_id"]
  file = "./var/lib/docker/containers/" .. id .. "/config.v2.json"
  if not file_exists(file) then return {} end
  local lines = ""
  for line in io.lines(file) do
    lines = lines .. line
  end

  pattern="\"LogPath\":\"[^\"]*\",\"Name\":\"[/]?([^\"]+)\""
  record["container_name"] = string.match(lines, pattern)
  return 2, timestamp, record
end

function file_exists(file)
  local f = io.open(file, "rb")
  if f then f:close() end
  return f ~= nil
end

