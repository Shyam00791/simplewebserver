from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
<head>
<title> My Web Server</title>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>
<h1>Laptop Configuration</h1>
<table>
  <tr>
    <th>Configuration</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Processor</td>
    <td>i5</td>
  </tr>
  <tr>
    
    <td>primary memory</td>
    <td>ram 16 gb</td>
  </tr>
  <tr>

    <td>secondary memory</td>
    <td>512 gb</td>
  </tr>
  <tr>
    
    <td>OS</td>
    <td>windows 11</td>
  </tr>
  <tr>
    
    <td>graphic card</td>
    <td>NVIDIA</td>
  </tr>
  
</table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()