'''
Created on 2019. 2. 13.

@author: HeoJongTae
'''
from datetime import datetime

#loglevel
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

#configuration
userid='user'
userpass='123123'
homedir='/home/user'
blocking=True
perm='elradfmw'
port=33333
uselog=True
logpath='log/{:%Y-%m-%d}_ftpserver.log'.format(datetime.now())
loglevel=INFO
