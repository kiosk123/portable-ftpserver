'''
Created on 2019. 2. 12.

@author: HeoJongTae
'''
import logging
from logging.handlers import RotatingFileHandler

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


class FTPServerDaemon:
    def __init__(self):
        self.authorizer = DummyAuthorizer()
        self.handler = FTPHandler
        self.handler.timeout=None
        
    def add_user(self, userid, password, homedir, perm="elradfmw"):
        self.authorizer.add_user(userid, password, homedir, perm=perm)
    
    def add_anonymous(self, homedir, perm="elradfmw"):
        self.authorizer.add_anonymous(homedir, perm=perm)
    
    def start_server(self, ip="0.0.0.0", port=33333, timeout=None,  blocking=True, handle_exit=True, uselog=True, logpath='/var/log/ftpserver.log', loglevel=logging.INFO):
        self.handler.authorizer = self.authorizer
        if uselog:
            logging.basicConfig(filename=logpath, format='%(asctime)s.%(msecs)03d %(levelname)s %(message)s', level=loglevel, datefmt='%Y-%m-%d,%H:%M:%S')
        self.server = FTPServer((ip, port), self.handler)
        self.server.serve_forever(timeout, blocking, handle_exit)