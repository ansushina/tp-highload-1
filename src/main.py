import socket
from threading import Thread
from config import Config
from response import Response
from request import Request

maxRequestLen = 4096

def handle(sock, root):
    while True:
        conn, info = sock.accept()
        buffer = '' 
        while True:
            data = conn.recv(1024)
            if not data:
                buffer = ''
                break
            buffer += data.decode("utf-8")
            if buffer.find('\r\n\r\n'):
                break
            if len(buffer) >= maxRequestLen:
                buffer = ''
                break
        if buffer:
            req = Request(buffer)
            res = Response(req)
            answer = res.create_res(root)
            conn.send(answer)
        conn.close()



if __name__ == '__main__':
    conf = Config()

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((conf.host, conf.port))
    sock.listen(1)

    for i in range(conf.thread_limit):
        th = Thread(target=handle, args=(sock, conf.document_root))
        th.start()

