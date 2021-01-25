import socket

hosts_path = 'C:\Windows\System32\drivers\etc\hosts'

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('', 65432))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break

        # The data is the WSL IP
        ip = data.decode().rstrip()

        with open(hosts_path) as file_in:
            lines = []
            for line in file_in:
                line = line.rstrip()
                # If the line contains '# WSL', replace the first word (the old IP)
                # with the received IP
                if line.__contains__('# WSL'):
                    replacement = ip
                    s = line.split()
                    s[0] = replacement
                    line = ' '.join(s)
                lines.append(line)
        hosts_content = '\n'.join(lines)

        f = open(hosts_path, "w")
        f.write(hosts_content)
        f.close()
    conn.close()
