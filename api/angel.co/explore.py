import unirest

response = unirest.get("https://community-angellist.p.mashape.com/startups?filter=raising",
  headers={
    "X-Mashape-Key": "u27xLtWps9mshthalITEZIxHphg2p1qyWQRjsnI5lxX2NqC0ta",
    "Accept": "text/plain"
  }
)

print response.code # The HTTP status code
print response.headers # The HTTP headers
print response.body # The parsed response
print response.raw_body # The unparsed response


























