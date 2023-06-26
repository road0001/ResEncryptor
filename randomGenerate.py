import os
import sys
import time
import random
import ResEncryptor as r
from shutil import copyfile

count=10
randomRange=[1024,8192]
randomVarRange=[8,16]
splitKeywords='########## CONFUSE ##########\n'

def backupFile(file):
	backupFileName=f'{file}.{int(time.time())}.bak'
	copyfile(file, backupFileName)
	print(f'Backup file: {file} to {backupFileName}.')

def confuseFile(file):
	try:
		f=open(file,'r',encoding='utf-8')
		fileData=f.read()
		f.close()
		fileSplit=fileData.split(splitKeywords)
		for i in range(0,len(fileSplit)):
			if fileSplit[i][0:3]=='___':
				rstr=r.randomPassword(random.randint(randomRange[0], randomRange[1]))
				varName=rstr[0:random.randint(randomVarRange[0], randomVarRange[1])]
				fileSplit[i]=f"___{varName}='{rstr}'\n"
		fileJoin=splitKeywords.join(fileSplit)
		
		f=open(file,'w',encoding='utf-8')
		f.write(fileJoin)
		f.close()
		print(f'Confused file: {file} success.')
		return True
	except Exception as e:
		print(f'Confused file: {file} error.')
		print(e)
		return False

if __name__=='__main__':
	if len(sys.argv)<=1:
		rstr=''
		for i in range(0,count):
			rstr+=r.randomPassword(random.randint(randomRange[0],randomRange[1]))
			rstr+='\n'
		f=open('random.txt','w')
		f.write(rstr)
		f.close()
		print(rstr)
		r.pause()
	elif len(sys.argv)==2:
		backupFile(sys.argv[1])
		confuseFile(sys.argv[1])
