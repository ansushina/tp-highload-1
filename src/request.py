class Request:
    method = ''
    url = ''
    version = ''
    headers = {}
    ok = False
    def __init__(self, req):
        self.req = req

        self.__parse_req()
    
    def __parse_req(self):
        lines = self.req.split('\r\n')
        first = lines[0]
        lines = lines[1:-2]
        chunks = first.split(' ')
        if len(chunks) != 3:
            return
        self.method = chunks[0]
        self.url = chunks[1]
        self.version = chunks[2]
        for line in lines: 
            chunks = line.split(':', 1)
            if len(chunks) != 2:
                return
            self.headers[chunks[0].rstrip()] = chunks[1].rstrip()
        self.ok = True
       