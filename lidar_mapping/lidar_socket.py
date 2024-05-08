import socket
import json
from rplidar import RPLidar

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 12345

    server_socket.bind((host, port))
    server_socket.listen(5)

    print('Server is listening...')
    client_socket, addr = server_socket.accept()
    print("Connection from: " + str(addr))

    lidar = RPLidar('/dev/ttyUSB0')

    try:
        for scan in lidar.iter_scans():
            data_to_send = json.dumps(scan) + '\n'  # Convert to JSON and add a delimiter
            client_socket.send(data_to_send.encode('ascii'))
    except Exception as e:
        print("An error occurred:", str(e))
    except KeyboardInterrupt:
        print("Program interrupted by user")	
    finally:
        lidar.stop()
        lidar.disconnect()
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()

