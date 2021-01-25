import socket
import os

stream = os.popen('ip addr show eth0 | grep \'inet \' | cut -f 6 -d \' \' | cut -f 1 -d \'/\'')
wsl_ip = stream.read()

stream = os.popen('ip route show default | awk \'{print $3 }\'')
windows_ip = stream.read()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((windows_ip, 65432))

client.send(wsl_ip.encode())
client.close()