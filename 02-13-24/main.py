import socket
import logging

logger = logging.getLogger(__name__)
logging.basicConfig()



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = s.bind(('127.0.0.1', 8080))
s.listen(5)

s.setblocking(False)
s.settimeout(5)

while True:
    try:
        client_socket = s.accept()
    except TimeoutError:
        continue
    
    client, (addr,port) = client_socket
    logger.warning(f"{addr} connected from port {port}")
    
    incoming = client.recv(500)
    #print(incoming)
    client.send(b'HTTP/1.0 200 OK\n')
    client.send(b'Content-Type: text/html\n')
    client.send(b'\n')
    client.send("""
<html lang=en>
<head>
<meta charset=utf-8>
<title>blah</title>
</head>
<body>
<p>I'm the content</p>
</body>
</html>""".encode())
    #client.send("SDG S".encode())
    client.close()
    #break
    #print(client_socket)
 
