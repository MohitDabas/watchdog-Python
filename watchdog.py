import sys
import hashlib
import dump
try:
 fo=sys.argv[1]
except(IndexError):
   print "Wrong usage"
   sys.exit()
try:
 file=open(fo,'r')
except(IOError):
  print "File Doesnot Exit"
  sys.exit()
file_con=file.read()
hash=hashlib.md5(file_con)
print hash.hexdigest()
f_log=open(fo+'log','a')
dump.pickit(fo,hash.hexdigest())

