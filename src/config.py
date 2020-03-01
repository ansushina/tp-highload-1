
DEFAULT_CPU_LIMIT = 4
DEFAULT_HOST = ''
DEFAULT_PORT = 80
DEFAULT_DOCUMENT_ROOT = '/var/www/html'
DEFAULT_THREAD_LIMIT = 64
DEFAULT_FILE_NAME = '/etc/httpd.conf'

class Config: 
    def __init__(self, filename = DEFAULT_FILE_NAME):
        self.cpu_limit = DEFAULT_CPU_LIMIT
        self.host = DEFAULT_HOST
        self.port = DEFAULT_PORT
        self.document_root = DEFAULT_DOCUMENT_ROOT
        self.thread_limit = DEFAULT_THREAD_LIMIT

        try:
            f = open('/etc/httpd.conf', 'r')
        except FileNotFoundError:
            exit('conf is not found')

        for line in f:
            key, value = line.split(' ') 
            if key == 'thread_limit' :
                self.thread_limit = int(value)
            elif key == 'cpu_limit':
                self.cpu_limit = int(value)
            elif key == 'document_root':
                self.document_root = value
            else:
                setattr(self, key, value)
        f.close()



