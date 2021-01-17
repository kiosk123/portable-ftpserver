'''
Created on 2019. 2. 12.

@author: HeoJongTae
'''
from lib.ftpserver import FTPServerDaemon
from config import *

server = FTPServerDaemon()
server.add_user(userid, userpass, homedir, perm=perm)
server.start_server(port=port, blocking=blocking, uselog=uselog, logpath=logpath, loglevel=loglevel)

