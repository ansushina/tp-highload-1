import os.path

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
        print(lines)
        first = lines[0]
		
        lines = lines[1:]
        chunks = first.split(' ')
        print(chunks)
        if len(chunks) != 3:
            return
        self.method = chunks[0]
        self.url = chunks[1]
        self.version = chunks[2]
        for line in lines: 
            chunks = line.split(':', 1)
            if len(chunks) != 2:
                return
            self.__addHeader(chunks[0], chunks[1])
        ok = True
        print(done)
        
    def __addHeader(self, key, value):
        self.headers[key] = value
    
    def parse_url(self, root): 
        newUrl = self.url
        sep = self.url.find('?') if self.url.find('?') != -1 else self.url.find('#')
        if sep != -1:
            newUrl = newUrl[:sep]
        path = os.path.join(root, newUrl)
        return path




