class Config: 
    def __init__(self, filename = '/etc/httpd.conf'):
        self.cpu_limit = 4
        self.host = '0.0.0.0'
        self.port = 80
        self.document_root = "/var/www/html"
        self.thread_limit = 64

        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            exit('conf is not found')

        for line in f:
            key, value = line.split(' ') 
            if key == 'thread_limit' :
                self.thread_limit = int(value)
            elif key == 'cpu_limit':
                self.cpu_limit = int(value)
            elif key == 'document_root':
                self.document_root = value.rstrip()
            else:
                setattr(self, key, value.rstrip())
        f.close()