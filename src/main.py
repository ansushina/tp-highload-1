import socket
from threading import Thread
from config import Config
from functions import handle
import os

if __name__ == '__main__':
    conf = Config()

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((conf.host, conf.port))
    sock.listen(1)

    threads = []

    for i in range(conf.thread_limit):
        th = Thread(target=handle, args=(sock, conf.document_root))
        threads.append(th)

    for i in range(conf.cpu_limit): 
        n = os.fork()
        if n == 0: 
            for j in range(i, conf.thread_limit, conf.cpu_limit): 
                threads[j].start()
            print("child")
            exit(0)
        if n > 0:
            print(n)
        if n < 0:
            print("error")
            exit(1) 

    for i in range(conf.cpu_limit):
        er = os.wait()
        print(er)

