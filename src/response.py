from request import Request
import os.path
import datetime

OK = 200
BAD_REQUEST = 400
FORBIDDEN = 403
NOT_FOUND = 404
NOT_ALLOWED = 405

codes = {
    200: '200 OK',
    400: '400 Bad Request',
    403: '403 Forbidden',
    404: '404 Not Found',
    405: '405 Method Not Allowed',
}

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

class Response: 
    date = datetime.datetime.now()
    server = 'server/1.0'
    connection = 'close'
    status = 404
    content_length = 0
    contetnt_type = ''
    index = False

    def __init__(self, buffer):
        self.req = Request(buffer)

    def __bad_req(self):
        st = codes[self.status]
        r = ('HTTP/1.1 %s\r\nConnection: %s\r\nDate: %s\r\nServer: %s\r\n' % (st, self.connection, self.date, self.server)).encode()
        return r

    def __ok_req(self, data):
        st = codes[self.status]
        return ('HTTP/1.1 %s\r\nConnection: %s\r\nDate: %s\r\nServer: %s\r\nContent-Type: %s\r\nContent-Length: %d\r\n\r\n' %
                (st,  self.connection, self.date, self.server, self.content_type, self.content_length)).encode() + data

    def __ok_req_head(self):
        st = codes[self.status]
        return ('HTTP/1.1 %s\r\nConnection: %s\r\nDate: %s\r\nServer: %s\r\nContent-Type: %s\r\nContent-Length: %d\r\n\r\n' %
                (st,  self.connection, self.date, self.server, self.content_type, self.content_length)).encode()

    def create_res(self, root):
        self.req.parse_req()
        if not self.req.ok:
            print(self.req.ok)
            self.status = BAD_REQUEST
            return self.__bad_req()
        if not self.req.Method in allowed_methods:
            self.status = NOT_ALLOWED
            return self.__bad_req()

        filepath = self.req.parse_url(root)

        if filepath.find('../') != -1:
            self.status = FORBIDDEN
            return self.__bad_req
        
        isDir = False
        if os.path.isdir(filepath):
            isDir = True
            filepath = os.path.join(filepath, 'index.html')

        if not os.path.exists(filepath):
            if isDir:
                self.status = FORBIDDEN
            else: 
                self.status = NOT_FOUND
            return self.__bad_req


        self.status = OK
        f = open(file, 'rb')
        data = f.read() 
        f.close()
        self.content_length = len(data)

        file_type = str(file.split('.')[-1])
        if file_type  in types.keys():
            self.content_type = types[self.file_type]
        else:
            self.content_type ='text/plain'
        
        if self.req.method == 'HEAD':
            return self.__ok_req_head()

        return self.__ok_req(data)

         
    
