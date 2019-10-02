import sys                                                          
import socket                                                   
import os                             

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    path, HOST, PORT = sys.argv[1], sys.argv[2], int(sys.argv[3])
    if not os.path.exists(path):
        print(f"File {path} doesn't exists")
        sys.exit()

    size = os.stat(path).st_size
    print(f'Size of the sending file is {size / 1024:.2f}KB', end='\n\n')

    print(f'Connecting to the {HOST}:{PORT}')
    s.connect((HOST, PORT))
    print(f'Successfully connected to the {HOST}:{PORT}')

    filename = path.split('/')[-1]
    print(f"Send file's name: {filename}", end='\n\n')
    s.sendall(filename.encode())

    flag = s.recv(1024)

    print(f'Start file exchange:')
    f = open(path, 'rb')
    tmp = f.read(1024)
    i = 1
    while tmp != b'':
        s.sendall(tmp)
        print(f'\033[K\033[1G{100* i * 1024 / size - 4:.0f}% has been uploadded', end='')
        i += 1
        tmp = f.read(1024)
    print(f'\nFile {filename} was successfully uploaded!’) 