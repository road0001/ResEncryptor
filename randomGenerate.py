import os
import random
import ResEncryptor as r

count=10
if __name__=='__main__':
	rstr=''
	for i in range(0,count):
		rstr+=r.randomPassword(random.randint(512,1024))
		rstr+='\n'
	f=open('random.txt','w')
	f.write(rstr)
	f.close()
	print(rstr)
	r.pause()