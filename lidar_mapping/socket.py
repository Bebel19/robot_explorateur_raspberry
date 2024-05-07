import socket
import json

host = '0.0.0.0'  # Listen on all interfaces
port = 12345

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

conn, address = server_socket.accept()
print('Connection from: ' + str(address))

try:
    for scan in lidar.iter_scans():
        scan_data = [item[2] for item in scan]
        data = json.dumps(scan_data)
        conn.send(data.encode())
except KeyboardInterrupt:
    conn.close()

lidar.stop()
lidar.disconnect()

