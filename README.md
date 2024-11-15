# EX01 Developing a Simple Webserver
## Date:
14.11.2024
## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```

## OUTPUT:
![alt text](<Screenshot 2024-11-14 153449.png>)
![alt text](<Screenshot 2024-11-14 153559.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
