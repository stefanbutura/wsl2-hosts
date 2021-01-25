# What is this

This is a tool that can be used to automatically update the hosts file on windows with the WSL2 IP.

# How does this work?

The server (server.py) should run on the Windows machine. On WSL startup, you can start client.py inside WSL to send a message to the server containing the WSL IP. When the server receives the message, it updates all the lines in the Windows hosts file that contain '# WSL' by replacing the first word (the IP) (e.g. 172.29.249.42 mysite.local # WSL)

This will not work if there are multiple IPs on the same line.

# Prerequisites

Python on both Windows and the WSL instance.

# How to run this?

1. Make sure that all the lines in the hosts file have one IP per line and end with `# WSL`

172.29.249.42 mysite.local # WSL

2. Copy the server.py file into server.pyw
3. Create a Windows Task Scheduler task that server.pyw with admin privileges
4. On WSL startup, run `python client.py` inside the WSL instance
