import os
import sys
import time
import random
import ResEncryptor as r
from shutil import copyfile

count=10
# randomRange=[1024,16384]
randomRange=[10240,65536]
randomVarRange=[16,128]
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
		rdinput=input('请输入生成的随机数长度，留空将按照默认方式生成：')
		if rdinput=='':
			rstr=''
			for i in range(0,count):
				rstr+=r.randomPassword(random.randint(randomRange[0],randomRange[1]))
				rstr+='\n'
			f=open('random.txt','w')
			f.write(rstr)
			f.close()
			print(rstr)
		else:
			rdCount=int(rdinput)
			f=open('random.txt','wb')
			f.write(r.randomBin(rdCount))
			f.close()
		r.pause('按任意键退出。')
	elif len(sys.argv)==2:
		backupFile(sys.argv[1])
		confuseFile(sys.argv[1])
