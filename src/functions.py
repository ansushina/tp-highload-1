from urllib.parse import unquote
from response import Response
from request import Request
import os.path

OK = 200
BAD_REQUEST = 400
FORBIDDEN = 403
NOT_FOUND = 404
NOT_ALLOWED = 405

types = {
    'html': 'text/html',
    'css': 'text/css',
    'js': 'application/javascript',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'swf': 'application/x-shockwave-flash',
    'txt': 'text/plain'
}

allowed_methods = [
    'GET',
    'HEAD',
]

def parse_url(url, root):
    newUrl = url
    sep = url.find('?')
    if sep != -1:
        newUrl = newUrl[:sep]
    path = root + newUrl
    path = unquote(path, encoding='utf-8')
    return path

def create_res(req: Request, root):
    if not req.ok:
        res = Response(BAD_REQUEST)
        return res.get()

    if not req.method in allowed_methods:
        res = Response(NOT_ALLOWED)
        return res.get()

    filepath = parse_url(req.url, root)

    if filepath.find('../') != -1:
        res = Response(FORBIDDEN)
        return res.get()
        
    isDir = False
    if os.path.isdir(filepath):
        isDir = True
        filepath = filepath + 'index.html'

    if not os.path.exists(filepath):
        if isDir:
            res = Response(FORBIDDEN)
        else: 
            res = Response(NOT_FOUND)
        return res.get()

    res = Response(OK)
    f = open(filepath, 'rb')
    data = f.read() 
    f.close()
    cont_len = len(data)

    file_type = str(filepath.split('.')[-1])
    if file_type in types.keys():
        cont_type = types[file_type]
    else:
        cont_type ='text/plain'
        
    if req.method == 'HEAD':
        return res.get(cont_type, cont_len)

    return res.get(cont_type, cont_len, data)

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
        if buffer:
            req = Request(buffer)
            answer = create_res(req, root)
            conn.send(answer)
        conn.close()