
# Network Scanner, Logger and Analyzer

<img src="https://socialify.git.ci/PavinDas/ClientServerCommunication/image?description=1&font=KoHo&language=1&name=1&owner=1&pattern=Solid&theme=Dark" alt="Socket" width="640" height="320" />


This project consists of three Python scripts that work together to scan a network, log messages from a client-server communication, and analyze the log files.


## Features

- **TCP Server (server.py):** Listens for incoming connections, logs messages, and echoes them back.

- **TCP Client (client.py):** Sends messages to the server.

- **Network Scanner (main.py):**  Uses ARP requests to identify active hosts in the network.

- **Log Analyzer (main.py):** Parses logs to analyze IP activity and requests.


## Installation

**Prerequisites**

Ensure you have Python 3 installed on your system. You may also need scapy for network scanning:
```bash
pip install scapy     
```
```bash
git clone https://github.com/PavinDas/ClientServerCommunication.git

cd ClientServerCommunication
```
**Run the Server**

Start the server to listen for incoming messages:
```bash
python3 server.py
```
**Run the Client**

Send messages to the server:
```bash
python3 client.py
```
**Run Network Scanner and Log Analyzer**

To scan the network and analyze logs:
```bash
sudo python3 main.py
```

## Usage Details

**Server (server.py)**

- Listens on 127.0.0.1:65432.
- Accepts messages from clients and logs them to network_logs.txt.
- Echoes received messages back to the client.

**Client (client.py)**
- Connects to 127.0.0.1:65432.
- Sends messages to the server and receives responses.

**Network Scanner (main.py)**
- Scans the local network (default: 192.168.1.1/24).
- Identifies active hosts and their MAC addresses.

**Log Analyzer (main.py)**
- Reads network_logs.txt.
- Extracts IPs and request patterns.
- Displays how often each IP and request appears.

**Log Analyzer (main.py)**
- Reads network_logs.txt.
- Extracts IPs and request patterns.
- Displays how often each IP and request appears.
## Example Outputs

**Server Output**
```
Server listening on 127.0.0.1:5050
Connected by ('127.0.0.1', 5050)
Received: Hello, Server!
Received: Another message!
```

**Client Output**
```
Received from server: Hello, Server!
Received from server: Another message!
```
**Network Scanner Outputs**
```
Scanning network for active hosts...
Active hosts:
IP: 192.168.1.10, MAC: AA:BB:CC:DD:EE:FF
IP: 192.168.1.12, MAC: FF:EE:DD:CC:BB:AA
```

**Log Analyzer Outputs**
```
Analyzing network logs...
IP Address Counts:
127.0.0.1: 2 requests

Request Counts:
Request 'Hello, Server!': 1 occurrences
Request 'Another message!': 1 occurrences
```


## Troubleshooting

**Permission Error for Network Scanning**
```bash
sudo python3 main.python3
```
Or grant raw socket privilage:
```bash
sudo setcap cap_net_raw+ep $(which python3)
```
**Port Already in Use**
if server.py fails to bind, another process may be using port 5050. Find and kill it:
```bash
sudo lsof -i :5050
sudo kill <PID>
```


## License

This project is owned by [Pavin Das](https://github.com/PavinDas)


## Authors

Developed by Your [Pavin Das](https://www.github.com/PavinDas). Contributions are welcome!

Feel free to reach out for improvements or issues.
