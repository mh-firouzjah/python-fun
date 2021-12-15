import logging
import socket
import threading

logging.basicConfig(format='%(asctime)s-%(levelname)s: %(message)s',
                    level=logging.INFO, datefmt='%A %d-%b-%y %H:%M:%S')

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(
    socket.gethostname()
)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn: socket, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f'{addr} {msg}')
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'{addr} disconnected')
            conn.send("MSG received".encode(FORMAT))


def start():
    server.listen()
    print(f'[LISTENNING] Server is listenning on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')


print('[STARTING] server is starting...')
start()
