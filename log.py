
def log_file(message,hash,fil_name):
 import logging
 import time

 log_file=fil_name+'log'
 logging.basicConfig(filename=log_file,level=logging.INFO,)
 logging.info(message+' of '+fil_name+' on '+time.ctime()+' '+hash)

if __name__=='main':
     log_file(message,hash)
    

