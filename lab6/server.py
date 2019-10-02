import socket
import os
from glob import glob

HOST = ‘0.0.0.0’
PORT = 12345

def get_file(filename):
    def get_last_char(el):
        num = el.split('.')[0][-1]
        return int(num) if str.isdigit(num) else 0

    tmp = filename.split('.')
    name, ext = '.'.join(tmp[:-1]), tmp[-1]
    files = [f.split('/')[2] for f in glob(f'./server_storage/{name}*{ext}')]

    if len(files) != 0:
        tmp = max([get_last_char(i) for i in files]) + 1
        return open(f'./server_storage/{name}_copy{tmp}.{ext}', 'wb')
    else:
        return open(f'./server_storage/{filename}', 'wb')

def start():
    if not os.path.exists('./server_storage') or not os.path.isdir('./server_storage'):
        os.mkdir('server_storage')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Created TCP socket')
        print(f'Start listening on {PORT}', end='\n\n')
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            filename = conn.recv(1024).decode()
            conn.sendall('1'.encode())
            print(f'Recieved filename - {filename}')

            with get_file(filename) as f:
                while True:
data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
                print(f'File {filename} was successfully stored', end='\n\n')

if __name__ == "__main__":
    start()
