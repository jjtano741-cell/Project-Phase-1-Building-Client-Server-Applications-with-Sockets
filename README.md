# Project-Phase-1-Building-Client-Server-Applications-with-Sockets
A dual-protocol echo server and client implementation using UDP and TCP on localhost. 

#How It Works

This project includes Python scripts for both UDP and TCP echo servers and clients, designed to run on localhost (`127.0.0.1`). You can observe the network traffic using Wireshark.

### 1. Start the Server
Run one of the server scripts:
```bash
python udp_server.py
# or
python tcp_server.py

#Run the Client
Run the matching client script:
python udp_client.py
# or
python tcp_client.py

#Enter a question when prompted:
Are you Bruce Wayne?

#Server Response:
The server replies:
- If the question matches: Yes, I am Batman.
- Otherwise: No, I'm just a server.

