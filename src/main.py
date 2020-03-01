import socket
from threading import Thread
from config import Config
from functions import handle

if __name__ == '__main__':
    conf = Config()

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((conf.host, conf.port))
    sock.listen(1)

    for i in range(conf.thread_limit):
        th = Thread(target=handle, args=(sock, conf.document_root))
        th.start()

