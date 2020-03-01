import datetime

codes = {
    200: '200 OK',
    400: '400 Bad Request',
    403: '403 Forbidden',
    404: '404 Not Found',
    405: '405 Method Not Allowed',
}

class Response:
    def __init__(self, status):
        self.date = datetime.datetime.now()
        self.status = codes[status]

    def bad_req(self):
        return ('HTTP/1.1 %s\r\nConnection: close\r\nDate: %s\r\nServer: ansushina\r\n' % 
                (self.status, self.date)).encode()
        
    def ok_req(self, cont_type, cont_len, data):
        return ('HTTP/1.1 %s\r\nConnection: close\r\nDate: %s\r\nServer: ansushina\r\nContent-Type: %s\r\nContent-Length: %d\r\n\r\n' %
                (self.status, self.date, cont_type, cont_len)).encode() + data

    def ok_req_head(self, cont_type, cont_len):
        return ('HTTP/1.1 %s\r\nConnection: close\r\nDate: %s\r\nServer: ansushina\r\nContent-Type: %s\r\nContent-Length: %d\r\n\r\n' %
                (self.status, self.date, cont_type, cont_len)).encode()

