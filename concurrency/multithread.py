import threading
import time
from concurrent.futures import ThreadPoolExecutor
from socket import socket, AF_INET, SOCK_STREAM

def client(sock, addr):
    print('Got connection from', addr)
    while True:
        msg = sock.recv(1024)
        if not msg:
            break
        print(str(msg))
        sock.sendall(msg)

    print('Client closed connection')
    sock.close()

def server(addr):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    pool = ThreadPoolExecutor(10)
    while True:
        c, addr = sock.accept()
        pool.submit(client, c, addr)

def main():
    server(('', 3333))



if __name__ == '__main__':
    main()