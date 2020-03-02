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
        self.status = codes[status]
        self.data = datetime.datetime.now()
        self.main_part = ('HTTP/1.1 ' + self.status + '\r\n' + 
                          'Connection: close\r\n' + 
                          'Server: ansushina\r\n' + 
                          'Date:' + str(self.data) + '\r\n')

    def get(self, cont_type = '', cont_len = 0, data = None):
        if self.status != codes[200]: 
            return (self.main_part).encode()
        self.main_part = (self.main_part + 
                        'Content-Type:'+ cont_type + '\r\n' + 
                        'Content-Length:'+ str(cont_len) +'\r\n\r\n')
        if data: 
            return (self.main_part).encode() + data
        else: 
            return (self.main_part).encode()

