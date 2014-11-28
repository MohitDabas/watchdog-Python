def pickit(file_name,hash):
 import pickle
 try: 
  fil_pic=open(file_name+'dump.pickle','r')
 except(IOError,EOFError):
      data={'file_name':'secret.txt','hash':hash}
      fil_pic=open(file_name+'dump.pickle','w')
      pickle.dump(data,fil_pic)
      import log
      log.log_file('Starting Hash',hash,file_name)
      fil_pic.close()
      fil_pic=open(file_name+'dump.pickle','r')

 data=pickle.load(fil_pic)
  
 if(data['hash']==hash):
     print 'Hash Not Changed'
 

 else:
    data={'file_name':'secret.txt','hash':hash}

    print 'Hash Has Been Changed'
    fil_pic=open(file_name+'dump.pickle','w')
    pickle.dump(data,fil_pic)
    import log
    log.log_file("Hash Has Been changed",hash,file_name)

 fil_pic.close()



if __name__=='main':
    pickit(file_name,hash)
