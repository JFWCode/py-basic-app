from socket import socket


def client(addr, text):
    sock = socket()
    sock.connect(addr)
    print('Got connection from', addr)
    while True:
        sock.sendall(text.encode('utf-8'))

    print('Client closed connection')
    sock.close()

if __name__ == '__main__':
    client(('', 3333), 'hi')