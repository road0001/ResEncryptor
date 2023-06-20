RbHXRuDU39s5I='RbHXRuDU39s5IL4WzJEmC1QqjuH1ErFRHUY8jYuCJIlV0obWFBvRSNcu3ZTkoAGY1PjxO8KF3daE4lUnLHLnzKh6Xs10xdDnNNYZxrKhmGoklSQ9fe9JjjPV01c9117uxVGKHdSacXRnSHG7K4Z5paHObp2ppIQIAuExpZgcXa9SoIj1HOZE0vtTUZvd0E0CjOkcQTezLgrD1Shy6tNwrene5N88Y97Se9NCquKDE6RDtnBUHCdcAJT595yiSzKQStVTjUUcyHlbC7Skkpoc9pWDpW3CmFGKwk3AqpoAcNxkAw2CLRTwLa6yGO1H85mpWjxTOZIAEAYEJmBFT5cOk2vb9kohOUsVoRPNc3OsBCALrzfXZW4Ysz7T2rKu7pK3YVhqRj6PHEfXuarJFloi97n6VwNXuEJcP6FvlBteOeOYhHtgNDhwRjIYrtFasXUeQb80iQ0dsjtbO1y8uFyxofozgbjhxyejhajb1IoPkuqSugwRw34CcDqCbzJLB4mQO24IABvNfMXKSEFEW3anymScxTAQ2iO3PGn9Wx8QOOpjlAyzCZS8lQVvBdrBQcsupT4KlcnUMeT97ig2OZjGtyIkmK25k'

import os
import sys
import glob
import math
import time
import random
from random import shuffle
import base64
from Cryptodome.Util.Padding import pad
from Cryptodome.Cipher import AES
import _7zexe as _7z
import platform
import hashlib
import colorout as out
import json
import send2trash
from shutil import copyfile

bErAcchwMGpML='bErAcchwMGpMLjsQVnH4oU1mPb2nCEbVMhHgebEVChhsAcrbRKOwEcYPa1lhfYDFRfJJxFdvICjfUgnrOHFVs2o9eiGJE0cQESLXOHiIMKxu4ukzh02KRg0rEXmlDQUJVUZ8NkcrmwfFkAaEUbllgdZEHA3Am2uxg1EutKTybvEYv36GzwAd3Rq0BzRKRAmv5lqeIToFV9WeVcxKxzNGeIGTFb6X7SFMawYxpvQY0Zkuqz6iTy4L0M5KQ93D4TR0MqfsBc4nV5oUT82i50C0eUYnl1EXhrBORiPrxhWhaHLBBJdvSAtA5yp8vfc97c4g93s4sVY2KOuWpX9jk3pzpppMghAymv2crOJITe2cVEbH6Rq2CaNxDWFsNP8NnAsqOIDoDiKqjopIRXiRH54lr9rf7gqv2ZLPrvU9WcNOHNX7vpAQRGOCZ3IKT8RmqLEhERNxc8Xrc4jYOBGgHNLrCi3xJ67R6vthV5iI4dgf8kdb3VWZ6K2atrjIP85pnn452lji2Sf4DjrXbXWuAex'

VERSION={
"appName":"ResEncryptor",
"versionUpdate":[
{
	"mainVersion":"1.0.6",
	"dateVersion":"20230620",
	"versionDesc":[
		"更换混淆数据。",
		"将重命名功能改为Python内置库。",
		"调整混淆文件头的数据长度阈值。",
		"加入解密配置重复迭代功能，以对抗暴力破解。",
	""]
},
{
	"mainVersion":"1.0.5",
	"dateVersion":"20230619",
	"versionDesc":[
		"更换混淆数据。",
		"统计文件时，加入文件夹的统计。",
		"加入混淆7Z压缩包文件头功能，规避文件头识别。",
	""]
},
{
	"mainVersion":"1.0.4",
	"dateVersion":"20230613",
	"versionDesc":[
		"更换混淆数据。",
		"略微调整解密流程。",
		"去除配置文件编码base64的操作。",
	""]
},
{
	"mainVersion":"1.0.3",
	"dateVersion":"20230612",
	"versionDesc":[
		"加入密钥随机大小写功能。",
		"加入分卷大小随机增量功能。",
		"在代码中随机位置加入混淆数据。",
	""]
},
{
	"mainVersion":"1.0.2",
	"dateVersion":"20230609",
	"versionDesc":[
		"加入自动清理压缩包功能（移入回收站）。",
		"加入在找不到配置文件时，手动输入配置文件名功能。",
		"将字符串中format引用变量的方法改为f''。",
	""]
},
{
	"mainVersion":"1.0.1",
	"dateVersion":"20230608",
	"versionDesc":[
		"完善功能提示。",
		"完成解密解压功能。",
		"修复文本错误。",
	""]
},
{
	"mainVersion":"1.0",
	"dateVersion":"20230607",
	"versionDesc":[
		"实现基础功能。",
		"完成加密压缩功能。",
	""]
}
]
}

w4GP5nFbnfyLNEhRuWbGco='w4GP5nFbnfyLNEhRuWbGco91I4I0EjktkpyiYO5E2kpoz5Z8nJvPTnhbqSEqxsSknY3SO1luEZLRpyTUex9W8WEZC6XZXMUYS4IQyqGbUM6MGMo97BRU3LRYlCWoqTgaTVLw0ZPwYttAnDQsmg4J84Hw9l7QEHE83hwxTInfKaLVOuXsnUBR64XVJG1UkyXaK2Tg6ea6H67dQHD9ltloEONUq9EOlwQQ1EXE22blvPD2NuJI2pix76eVzYSqjisdKS0dH89HLTwtpbo6AhdpCWTMOWEbwhKZDY1CoQI9ZARjGMNx8LMcrFRl6ikDVJrwHsu2Bhuj8Qv5bf9LT2koV2fEwWgvtgF7Hll4aqFnw5fYwjhfb2bHJOnZFY3BaFBF8wupQuTUqvVLCOqpEaQaxwWaIz2rFttQqKCWFxz4VToPZwQpYH7hVYUoZo7D2HA9f6f1OSudIe0aiapwXrM9zOnHW3vTAcxNmbKXG1eJvw8EoeIIpHpBskQot5WBPYZFdGeJsBnbWWLo0SZNpt6hsdZERN3pawwoYb28nDLUJq9vDgXo7KRLzyq3tDeTuwVpBmqt4Zg83tmLvuZn3lg9krB9RPIPqlAa0hZZwFTlLM3d0lc9xyBbvDcxSYGSi8Ejxziln8sxaruGdUo0VssG1q7v72ou6zVeEkVRLxAweGxCayQWQucGO3ToBWyVCuBEGsVjyeqhxKy3tCN8GhH1xSQNwOEe8cpaEujiw8UxFHzY499sx1AsxQhXfvKLu2PvSv9Fb2s0rIy'

'''
Configs
'''
# 输出目录
outputDir=f'{os.getcwd()}\\output'
# 分卷范围（此范围是压缩前的分卷范围，压缩后的情况不可知）。[最少分卷，最多分卷，分卷增量上限]
volumeRange=[20,50,1024]
# 默认盐，和配置文件加解密有关，不可随便更换，否则不兼容其他版本
defaultSalt='KnWn7ZYSa309KyYnruB0JXF9zIRAsQNx'
# 随机文件头长度范围
randomHeadLengthRange=[1024,2048]
# 解密配置数据重复加密迭代次数
# 最大不允许超过25次，每次迭代增加1/3大小
encryptConfigRepeatCount=[20,20]
# 混淆数据长度范围
confuseLength=[4096,8192]

cI2QONfwxiP3LDTPPO3B9WSRg='cI2QONfwxiP3LDTPPO3B9WSRgbmcQEBATwF8IlUwSct1oK2iVWqDzxO9EtMmw0NqbBK4HeenWNMwQ8o6M86MTRnYi4oqp8DKeszZQkWZvJiLZt2sPYKWPUF6po5AmHe3Ka5IMoS7gSmldPBgB2nHgLX2cE3B9qdwfYqzMMtue7BDuUfoXanxsRt0nAwh4QejG24drcz2TsY87Qrqf03uIMysa92YwSke2DV4sMVnTMZKlF06iW0iriWMw0wgbxT1aWsFkAGDjugYNwlfRAx37mx9ObBLB44Q7ta3qQpNDhqvhFhtuEIlFd0CiLtFN8MMKyVs94PVwhStLoMgDPyVERDVDmxiPGfGq7DL5ibgWYLW92ZEviHVjm2emn3hUV0MJRttZmF1qGcS1hcaSZBPlEnb3fDFTeE76BVMZKtsSCPsq5D8D7XirA96p5UwkmDpWWx6FPucWgBKYANOq5wAF4RhvipoTKlqX454S6CHMuaqETNIpE7eqzAu2lv0snysQ1ejGDBY04qzTFtdX5FHTHmJdMf1MUS0VD0YfGPKripJ64jf9LMBuwF1uMMaafl23omWIp9IMJP6GVvAK5lj8AJH3U50qFaf3cq7IKq8yuXKQtoxdF3zI0J5P11iNljWvVnF5oTEU1oodNqscCqS55R5MWSuXfSRsC'

'''
Utils
'''
def cmd(c):
	os.system(c)

def runBat(batStr,output=''):
	writeFile(f'{output}temp.bat',batStr)
	os.system(f'{output}temp.bat')
	os.remove(f'{output}temp.bat')

def pause(c=None):
	if c:
		print(c)
	cmd('pause>nul')

def cwd():
	return os.getcwd()

def exist(dirs):
	return os.path.exists(dirs)

def loadFile(file,tp='r'):
	try:
		f=open(file,tp)
		fs=f.read()
		f.close()
		return fs
	except:
		return None

def writeFile(file,data,tp='w'):
	try:
		f=open(file,tp)
		f.write(data)
		f.close()
		return True
	except:
		return False

def getAllFileList(addr,includeFolders=False):
	allFileList={'files':[],'folders':[]}
	if not exist(addr): #路径不存在的情况
		pass
	elif not os.path.isdir(addr): #路径为文件的情况
		allFileList['files'].append(addr)
	else: #路径为文件夹的情况
		for root, dirs, files in os.walk(addr):
			for name in files:
				allFileList['files'].append(os.path.join(root, name))
			for name in dirs:
				allFileList['folders'].append(os.path.join(root, name))
	if includeFolders==True:
		return allFileList
	else:
		return allFileList['files']

def getAllFileSize(fileList):
	fileSize=0
	for file in fileList:
		fileSize+=os.path.getsize(file)
	return fileSize

def formatFileSize(b):
	units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
	size = b
	unitIndex = 0
	while size >= 1024 and unitIndex < len(units) - 1:
		size /= 1024
		unitIndex+=1
	
	# 保留两位小数，四舍五入
	size = round(size * 100) / 100
	return f'{size} {units[unitIndex]}'

def randomPassword(length=10):
	pasArr = [
		'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
		'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
		'0','1','2','3','4','5','6','7','8','9',
		# '\'','~','!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',']','\\',';',''',',','.','/','{','}','|',':','"','<','>','?',
		# '~','!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',']',';',''',',','.','/','{','}','|',':','"','<','>','?',
	]
	password = ''
	pasArrLen = len(pasArr)
	for i in range(0,length):
		password += random.choice(pasArr)
	return password

def genSalt():
	return randomPassword(32)

def randomBin(length=10):
	return os.urandom(length)

def genCapsList(length):
	capsList=[]
	for i in range(length):
		isCaps=random.randint(0,1)
		if isCaps==1:
			capsList.append(i)
	return capsList

ZtgwI1uLBvV0zyw='ZtgwI1uLBvV0zywmwYhAs0Hs2tiLoetUSSbZHraaL3hIuNY4YW99XRiPk0gx2m2MQJhDWFfo0T2ScTJZLsmH8q0DV2xl5bZj0f5UhEL6dioxyxTLVDZ0VIyGBO60P089bKB5vB7OTHF5mHcUDTzA3OM97RP2ywDJdnfGO4Icnthftyl1zlDBIzZry8CT0lxGz0ndfQbaB6GSDBsVZRMkk0zTxU6o1S84SOgO4ksVIvvdhMWUMitwqgFEEJNAlxQhND1HgoJyrDZzASDtHDd998jHncVuDcsQB6CkZZs6pTWRaUeY66Y5hWC9ytWZJXwTGVdsaxP2zEsJYiY3BKeIAodD0i3TlCWTAWt4qz3WITFZgygHH5jWONfxv4onApCiy5ge7KXOi6HDdViNikrsYSJUa4ureNtwIeUbGfhEK3ad0ekxglcoZuWUd1qGDbGl20KyIHMgOeVvCXyTAK9BcvUYNlPZHH3y2PSHJbl99TseesIbOeXM32M9vzmDKhCVv4xtFJRwzdTcopTiNMMzqiDkY3CVdz8qUBZDCfX82FSK8vsgmQbddvAxf6i08s62Ztu0MUSjEj2V15tj8YAPjLggu8Fr9ZsMq5XKWuPeiiWYqogVGjXmQATXXNQgW4zHN3JoyyKRkgYoVhzLMSVJM2HKfDI7G64jQSmO8SufpDYx8oE5sL6ZC2Iam'

'''
AES加密
'''
# 将明文用AES加密
def AES_Encrypt(password, data):
	key=hashlib.md5((password+defaultSalt).encode(encoding='utf-8')).hexdigest()
	iv=hashlib.md5((key).encode(encoding='utf-8')).hexdigest()[0:16]
	obj = AES.new((key).encode(), AES.MODE_CBC, (iv).encode())
	# return base64.b64encode(obj.encrypt(pad(data.encode(),16)))
	return obj.encrypt(pad(data.encode(),16))

def AES_Decrypt(password, data):
	key=hashlib.md5((password+defaultSalt).encode(encoding='utf-8')).hexdigest()
	iv=hashlib.md5((key).encode(encoding='utf-8')).hexdigest()[0:16]
	obj = AES.new((key).encode(), AES.MODE_CBC, (iv).encode())
	# return obj.decrypt(base64.b64decode(data))
	return obj.decrypt(data)

fARnc9DTA7tfUh='fARnc9DTA7tfUhvjeCH98p6QpHBlsdS9qnKwFOL2lcjRypU9DBvhFmH0FZRnXb0nFzPjw8yIh8qF14l3qHTYVvlNOPQMqoipEtQyOLbmYlgJTaMVX3ZjBAlB0v2BpuA77g1A5d3BSP7Alq1MQXamKTKy9NYXdYOxWyD2NhUQPCxfaFEf4OKVgtr4k5LEd2zDTAWVHX5ZTZkH7Cn7bITFb5tvmcSQFsexjULN4RiC7LHAw1SQ0jFtPybYexjn2GgzbJQ7k1koZyZbFbOpGNpiURVr7UlEz45cILp0mtWj4S502oSR66TG7X1pc4AQvwvnZ8jWaQOu5mhLQZPJQrfz9V69p1EIqRtiuDUz5l0cRObTxFQb2TSlp3ul753xZZZ1vBcAJA8Ra6rXYdzv0VFBeCkMoD6eWJOOIGKUcwKRW83foIP4wm2mfV0tJlpmKKTMLOSdg4jqVUVnyONnit19K5ET3NhKgRof4J2CklfN5Rcs9TMeIvPLM4djItHL0AaJowOkfdngmJyDrbmKxmHqPGsHYKVZnnnQ5wZQJHROcBoZ2XrI8nEEkGgvemXAb1OCoGSSPW8OU1Msx16EqdJDJweZi6IkUCSYZ5C32WCc3XDdMeIfCBVy6lFEu3PFz0lZJ6r2IpZqh4fAZOctWxG3Q1xpk'

'''
App
'''
targetFileData={}
def applyFileData(file):
	targetFileData['path']=file
	targetFileData['name']=file.split('\\')[-1]
	pathList=getAllFileList(targetFileData['path'],True)
	fileList=pathList['files']
	fileSize=getAllFileSize(fileList)
	folderList=pathList['folders']

	targetFileData['fileList']=fileList
	targetFileData['fileCount']=len(fileList)
	targetFileData['folderCount']=len(folderList)
	targetFileData['fileSize']=fileSize

	out.outlnC('加载文件：【{path}】\n共{fileCount}个文件，{folderCount}个文件夹，总大小：{fSize}'.format(**targetFileData,fSize=formatFileSize(fileSize)),'green','black',1)
'''
生成配置数据
参数：混淆头，混淆尾
'''
def genEncryptConfig(chead, ctail, desc):
	# ctype=1：混淆头尾合并；ctype=2：混淆头尾拆分
	ctype=random.randint(1,2)
	config={
		'salt':genSalt(),
		'description':desc,
		'timestamp':int(time.time()),
		'fileList':[],
		'capsList':genCapsList(128),
	}
	if ctype==1:
		config['confuse']=chead+ctail
	elif ctype==2:
		config['confuseHead']=chead
		config['confuseTail']=ctail
	# 随机配置序列
	ckeys=list(config.keys())
	random.shuffle(ckeys)
	cconfig={}
	for k in ckeys:
		cconfig[k]=config[k]
	return cconfig

'''
加密配置数据
参数：配置，混淆头，混淆尾
'''
def encryptEncryptConfig(password,config,chead,ctail):
	# return base64.b64encode('{}\b{}\b{}'.format(chead,json.dumps(config,ensure_ascii=False),ctail).encode(encoding='utf-8')).decode('UTF-8')
	# return AES_Encrypt(password,f'{chead}\b{json.dumps(config,ensure_ascii=False)}\b{ctail}').decode('UTF-8')
	# return AES_Encrypt(password,f'{chead}\b{json.dumps(config,ensure_ascii=False)}\b{ctail}')
	
	# 使用多次加密迭代，增加解密时间成本，抗暴力破解
	encryptCount=random.randint(encryptConfigRepeatCount[0], encryptConfigRepeatCount[1])
	encConfigStr=f'{chead}\b{json.dumps(config,ensure_ascii=False)}\b{ctail}'
	for i in range(0,encryptCount-1):
		encConfigStr=base64.b64encode(AES_Encrypt(password,encConfigStr)).decode('UTF-8')
	encConfigStr=AES_Encrypt(password,encConfigStr)

	return encConfigStr
'''
解密配置数据
参数：已加密的配置数据
'''
def decryptEncryptConfig(password,data):
	# decData=AES_Decrypt(password,data)
	# # config=base64.b64decode(data).decode(encoding='utf-8').split('\b')[1]
	# config=decData.decode(encoding='utf-8').split('\b')[1]
	# return json.loads(config)
	
	# 使用多次加密迭代，增加解密时间成本，抗暴力破解
	decData=AES_Decrypt(password,data)
	for i in range(0, encryptConfigRepeatCount[1]):
		decData=AES_Decrypt(password,base64.b64decode(decData))
		try:
			decSplit=decData.decode(encoding='utf-8').split('\b')
			if len(decSplit)==3:
				config=decSplit[1]
				try:
					return json.loads(config)
				except:
					pass
		except:
			pass
	return False
'''
根据配置计算压缩包密钥
参数：密码，配置数据
'''
def calcEncryptKey(password, config):
	# 生成盐和盐的MD5
	salt=config['salt']
	saltMd5=hashlib.md5((salt).encode(encoding='utf-8')).hexdigest()
	# 生成密码的MD5
	passwordMd5=hashlib.md5((password+salt).encode(encoding='utf-8')).hexdigest()
	# 生成时间戳和时间戳的MD5
	timestamp=config['timestamp']
	timestampMd5=hashlib.md5((f'{timestamp}').encode(encoding='utf-8')).hexdigest()
	# 生成【密码的MD5|盐|时间戳】拼合的MD5
	comitMd5=hashlib.md5((f'{passwordMd5}|{salt}|{timestamp}').encode(encoding='utf-8')).hexdigest()
	# 生成密钥：【密码的MD5盐的MD5时间戳的MD5拼合的MD5】，每个MD5长度32位，总密钥长度128位
	encryptKey=f'{passwordMd5}{saltMd5}{timestampMd5}{comitMd5}'
	# 根据capsList更改大小写
	encryptKeyList=list(encryptKey)
	for caps in config['capsList']:
		encryptKeyList[caps]=encryptKey[caps].upper()
	encryptKey=''.join(encryptKeyList)

	return encryptKey

def makeOutputDir(addr):
	dirs=f'{outputDir}\\{addr}'
	if not exist(dirs):
		os.makedirs(dirs)
	return dirs

iITvQXJA3i985K='iITvQXJA3i985KfKzKgWvehHUekZnw0XxRTFsCdPIPvW6HRUFtXkKssoPExGztnwXGK4xVpRqVn2lfKbUycndC0aUNZ7TSh8OnkTlZNCoNUCms4aNaAnGBYj6oPhY35pARUZnQYN5pdR0J7RY0EwsVw04rznHTShdmX7QLoXmtXf7ysRRthx0nBkS9LSon94q4JLUSYVqhhmVg37QRfaHNCHLath6uhlfEEUZyZODCXCi0zLMLQCkNmUMtHPQCUSPSIXzYkfFVZNWkLZPiHJUTLuaEMm8xGJcno5PfuJD10eG1aLgmoo6gLN6YJKWUvVtDneCEYnsrs1l1ysDnElXkyrPboNNmNYLWoIL2iAGucOieNRQV6RSi8BPMgJKLfmnirFeRfgOrmD5v2r1IHOaqZJXNhXbYRK4DfcIp96cs5Nr5xq1C17APMs6tRhRcLTJEfxj5mbzxyJDGO9WwukN9QOPUWzmWPZc4KOpkFuMPHUbd9aTYEyy6lInsJEed7yOXNaXD9c8xIVoSj0r9kRC7wJ6EFdzl6q5JbbOsy20TeMQQukQoCDOgEBORuMasVkoU9CDnT53VWEswKfpmFosmyocKmqJ9bMAOSGZPQRFhW8ElwqBkRJjEaq1KWzpJuFCKPb8gYjvrkHJlTG0Ei1FQVwR6qGAOha8lXphtWpn9dMEAbo1qeQSW8qcmbWMsQ269zvPDm7JvYfjjFfTHvepj0kfL9fu4t0Pe9JYibbxd1vcINeji8oro2YnujrHw61vWTojMEJaj8WzUhz2HRVMh6jI8bo6kWiKkMlJFBhhLGHAcht2OpcS3cnUld4YdBQH1e7wIjN6QQO5ZTR5XX9ZaYhMdKMCkAX1JTOGNcsQtMaUXysSr77W2WdHOYDG7oSHalIyKnVwUT3xGNXeQt2XbwDi'

def beginEncryptFiles(file):
	applyFileData(file)
	if targetFileData['path']:
		if targetFileData['fileCount']<1:
			out.outlnC('文件数量为0，无法继续进行操作！','yellow','black',1)
			return 0
		password=''
		while True:
			if password!='':
				break
			else:
				password=input('请输入密码：')
		desc=input('请输入留言，如果不需要，请留空：\n')
		print()
		out.outlnC('开始进行加密压缩！','black','green',1)

		# 生成混淆头尾和配置数据
		out.outC('正在生成混淆数据……','cyan','black',1)
		confuseHead=base64.b64encode(randomBin(random.randint(confuseLength[0],confuseLength[1]))).decode('UTF-8')
		confuseTail=base64.b64encode(randomBin(random.randint(confuseLength[0],confuseLength[1]))).decode('UTF-8')
		encryptConfig=genEncryptConfig(confuseHead, confuseTail, desc)
		out.outlnC('[完成]','green','black',1)

		#生成加密KEY
		out.outC('正在生成加密密钥……','cyan','black',1)
		encryptKey=calcEncryptKey(password,encryptConfig)
		out.outlnC('[完成]','green','black',1)

		# 创建输出目录，并写入必备文件
		out.outC('创建输出目录并写入必备文件……','cyan','black',1)
		projOutputDir=makeOutputDir(targetFileData['name'])
		projCfgname='cfname'
		_7z.output7zExe(f'{projOutputDir}\\7z.exe')
		volumeCount=random.randint(volumeRange[0],volumeRange[1])
		volumeSize=int(targetFileData['fileSize'] / volumeCount)+random.randint(0,volumeRange[2])
		out.outlnC('[完成]','green','black',1)

		# 调用7Z进行加密压缩
		out.outlnC('开始进行压缩，这可能需要一定时间……','cyan','black',1)
		cmdParms={
			'projOutputDir':projOutputDir,
			'encryptKey':encryptKey,
			'volumeSize':volumeSize,
			'fileName':targetFileData['name'],
			'filePath':targetFileData['path'],
			'fileSize':targetFileData['fileSize'],
		}
		cmdStr='@echo off\n"{projOutputDir}\\7z.exe" a -p{encryptKey} -mhe=on -v{volumeSize}b "{projOutputDir}\\{fileName}.7z" "{filePath}"'.format(**cmdParms)
		runBat(cmdStr,'output\\')
		out.outlnC('压缩完成！','green','black',1)

		# 进行7z文件混淆
		out.outC('正在混淆文件头……','cyan','black',1)
		firstFileName=f"{projOutputDir}\\{targetFileData['name']}.7z.001"
		firstFileNameTmp=f'{firstFileName}.tmp'
		randomHeadLength=random.randint(randomHeadLengthRange[0],randomHeadLengthRange[1])
		randomHead=randomBin(randomHeadLength)
		with open(firstFileName,'rb') as originFile, open(f'{firstFileNameTmp}','wb') as targetFile:
			originData=originFile.read()
			encryptConfig['originHead']=base64.b64encode(originData[0:randomHeadLength]).decode('UTF-8')
			targetFile.write(originData)
			targetFile.seek(0x00)
			targetFile.write(randomHead)
			targetFile.flush()
		os.remove(firstFileName)
		os.rename(f'{firstFileNameTmp}',firstFileName)
		out.outlnC('[完成]','green','black',1)

		# 删除不需要的文件
		out.outC('正在清理不必要的文件……','cyan','black',1)
		os.remove(f'{projOutputDir}\\7z.exe')
		out.outlnC('[完成]','green','black',1)

		# 对文件进行乱序重命名
		out.outC('正在重命名文件……','cyan','black',1)
		for fp in getAllFileList(projOutputDir):
			fileName=fp.split('\\')[-1]
			fakeName=genSalt()
			encryptConfig['fileList'].append({
				'fileName':fileName,
				'fakeName':fakeName,
			})
			os.rename(f'{projOutputDir}\\{fileName}',f'{projOutputDir}\\{fakeName}')
		# renStr=f'@echo off\ncd {projOutputDir}\n'
		# for fp in getAllFileList(projOutputDir):
		# 	fileName=fp.split('\\')[-1]
		# 	fakeName=genSalt()
		# 	renStr+=f'ren "{fileName}" "{fakeName}"\n'
		# 	encryptConfig['fileList'].append({
		# 		'fileName':fileName,
		# 		'fakeName':fakeName,
		# 	})
		# runBat(renStr,'output\\')
		out.outlnC('[完成]','green','black',1)

		# 生成混淆后的配置数据
		out.outC('正在生成混淆配置数据……','cyan','black',1)
		configName=genSalt()
		decryptConfigString=encryptEncryptConfig(password, encryptConfig, confuseHead, confuseTail)
		writeFile(f'{projOutputDir}\\{configName}',decryptConfigString,'wb')
		writeFile(f'{projOutputDir}\\{projCfgname}',configName) # 用python将文件名写入到临时文件中，以待后续合并使用。不能使用bat的echo，会输出空行
		out.outlnC('[完成]','green','black',1)

		# 复制执行文件到输出目录
		out.outC('正在生成解压程序……','cyan','black',1)
		originFile=sys.argv[0]
		originFileName=originFile.split('\\')[-1]
		if(originFileName.split('.')[-1]!='exe'):
			out.outlnC('[请不要直接运行源码，否则无法解包！]','yellow','black',1)
		else:
			targetFile=projOutputDir+'\\'+originFileName
			copyfile(originFile, targetFile)
			# 混淆exe并重命名
			cpyStr =f'@echo off\ncd "{projOutputDir}"\n'
			cpyStr+=f'copy /b {originFileName}+{configName}+{projCfgname} {genSalt()}.exe>nul\n'
			cpyStr+=f'del {projCfgname}>nul\n'
			cpyStr+=f'del {originFileName}>nul\n'
			runBat(cpyStr,'output\\')
			out.outlnC('[完成]','green','black',1)

		out.outC('加密压缩已完成，您可以分享您的文件了！','black','green',1)
		out.outlnC('','white','black',0)

		return 0

def beginDecryptFiles():
	execFile=sys.argv[0]
	execFileName=execFile.split('\\')[-1]
	# 读取exe文件，并获取末尾32位字符串作为解密配置文件名
	f=open(execFileName,'rb')
	fileData=f.read()
	f.close()
	configName=fileData[-32:].decode('utf-8')
	alreadyTiped=False
	while True:
		if not exist(configName):
			out.outlnC('找不到解密配置文件！','black','red',1)
			if not alreadyTiped:
				out.outlnC('如果需要进行加密压缩，请将文件或文件夹拖放到程序图标上！','cyan','black',1)
				alreadyTiped=True
			configName=input('如果您知道配置文件名，请在此处输入：')
		else:
			break
	
	password=''
	encryptConfig={}
	while True:
		password=''
		encryptConfig={}
		while True:
			if password!='':
				break
			else:
				password=input('请输入密码：')
		
		out.outlnC('开始进行解压！','black','green',1)
		# 解密配置数据
		out.outC('正在解密配置数据……','cyan','black',1)
		try:
			encryptConfig=decryptEncryptConfig(password, loadFile(configName,'rb'))
			if encryptConfig!=False:
				out.outlnC('[完成]','green','black',1)
				break
			else:
				out.outlnC('[解密失败！密码错误？]','red','black',1)
		except:
			out.outlnC('[解密失败！密码错误？]','red','black',1)
	
	# 输出描述和欢迎信息
	if encryptConfig['description']!='':
		out.outln('')
		out.outln(encryptConfig['description'])
		out.outln('')

	# 对文件进行乱序重命名
	out.outC('正在重命名文件……','cyan','black',1)
	zFileName=''
	for fl in encryptConfig['fileList']:
		fileName=fl['fileName']
		fakeName=fl['fakeName']
		if fileName.split('.')[-1]=='001':
			zFileName=fileName
		os.rename(fakeName,fileName)
	# renStr='@echo off\n'
	# for fl in encryptConfig['fileList']:
	# 	fileName=fl['fileName']
	# 	fakeName=fl['fakeName']
	# 	renStr+=f'ren "{fakeName}" "{fileName}"\n'
	# 	if fileName.split('.')[-1]=='001':
	# 		zFileName=fileName
	# runBat(renStr)
	out.outlnC('[完成]','green','black',1)

	# 进行7z文件解混淆
	out.outC('正在解混淆文件头……','cyan','black',1)
	firstFileName=zFileName
	firstFileNameTmp=f'{firstFileName}.tmp'
	originHead=base64.b64decode(encryptConfig['originHead'])
	with open(firstFileName,'rb') as targetFile, open(f'{firstFileNameTmp}','wb') as originFile:
		targetData=targetFile.read()
		originFile.write(targetData)
		originFile.seek(0x00)
		originFile.write(originHead)
		originFile.flush()
	os.remove(firstFileName)
	os.rename(f'{firstFileNameTmp}',firstFileName)
	out.outlnC('[完成]','green','black',1)
		

	# 生成解密KEY
	out.outC('正在生成解密密钥……','cyan','black',1)
	encryptKey=calcEncryptKey(password,encryptConfig)
	out.outlnC('[完成]','green','black',1)

	# 创建输出目录，并写入必备文件
	out.outC('创建输出目录并写入必备文件……','cyan','black',1)
	_7z.output7zExe('7z.exe')
	out.outlnC('[完成]','green','black',1)

	# 调用7Z进行加密压缩
	out.outlnC('开始进行解压，这可能需要一定时间……','cyan','black',1)
	cmdStr=f'@echo off\n"7z.exe" x -p{encryptKey} "{zFileName}"'
	runBat(cmdStr)
	out.outlnC('解压完成！','green','black',1)

	# 删除不需要的文件
	out.outC('正在清理不必要的文件……','cyan','black',1)
	os.remove('7z.exe')
	out.outlnC('[完成]','green','black',1)

	out.outC('解压成功，请尽情使用吧！','black','green',1)
	out.outlnC('','white','black',0)
	print()
	out.outC('按任意键清理压缩包，如果不需要，请关闭窗口！','cyan','black',1)
	pause()
	# 删除压缩包和解压配置（移入回收站）
	if exist(configName):
		try:
			send2trash.send2trash(configName)
		except:
			pass
	for fl in encryptConfig['fileList']:
		fileName=fl['fileName']
		try:
			if exist(fileName):
				send2trash.send2trash(fileName)
		except:
			pass
	out.outC('[完成]','green','black',1)
	out.outlnC('','white','black',0)

XJN9j9cHRrlM3='XJN9j9cHRrlM3tVGkukbleFrVg6lHC0k1mDZHFHZRfu1eu1thI0hw9zOkMrKyeo9Jyc41c2CfxXYVzSAvToaTtnUVfZ80nPOkrE17N1y5k4XJI6sT13P0UxCpGymlvogqWeKCedfLjTpi5spS2PGmviQ78nmWFu5tjKqbYhfAsghoMUSy7cvsLuwy6RLEPahi4p5f1ZnAWBfj8YfuEFaBRIcnq0I6Cu8258HAEQuwYBIQCGHlXAio84o6mIHOravxyjRvfNNKK6eEDx0n5hJFn536Wws2INfkppf3wFi0lBSctALF5WkR36eexfLki7PGY8W9uIN4X9wLrWPLvhI7nAltlJi9U4GEY9KvVMxwHQ0Hdb65BsnIZyGf06OG3R9denJymOAAlLZAD3NQKg0ccVkhkUaSZ8WqP78XHRkoMRhfBLfqnSNcfzkSjTNQSS2936rcZsXBFRntYBROur2ymE4kUQXJ46zirvLc4IJJXcw8KSDwvcdHGmuDh9caBllWTCHdvTZdf4nrfjHtTSsIK1q6Hsh4GCAvG40zM1Ue8sok4I2LqNtaOoR988R14ZWgygafsaF2Nef72wOKJBbNmaHNzxd3fl9e31QRMl2s22hmWrLZh7ILKtCkwgv4c6xQpfnpUbUBLTQkrsS8vxAdEIFd335PjbW43nz1pExvR65eEefQvof0cbGSegN7AbFoWgtYQjs2xN0XHl6Y3KeviIyPoI8jpwFQnsc66ztW5UNbmvmWmJHXzFnld7KhZJnlcbVJIAwES6rbqIAnrglvxCNwjp1N0WTGxllZ'

def main():
	os.system('cls')
	version=f"v{VERSION['versionUpdate'][0]['mainVersion']} Build {VERSION['versionUpdate'][0]['dateVersion']}"
	if len(sys.argv)<2:
		os.system(f"title 资源解密解压工具 {version}")
		out.outlnC('-=<欢迎使用资源解密解压工具！>=-','purple','black',1)
		try:
			beginDecryptFiles()
			out.outln('按任意键退出。')
		except Exception as e:
			out.outlnC('程序执行错误！','black','red',1)
			out.outlnC(e,'red','black',1)
			out.outln('按任意键退出。')
		pause()
		return 0
	elif len(sys.argv)>2:
		os.system(f"title 资源加密压缩工具 {version}")
		out.outlnC('-=<欢迎使用资源加密压缩工具！>=-','purple','black',1)
		out.outlnC('请只拖入一个文件或文件夹！','red','black',1)
		out.outln('按任意键退出。')
		pause()
		return 0
	else:
		os.system(f"title 资源加密压缩工具 {version}")
		out.outlnC('-=<欢迎使用资源加密压缩工具！>=-','purple','black',1)
		out.outlnC('请在开始加密前，清空output文件夹，以免造成文件污染！','yellow','black',1)
		try:
			beginEncryptFiles(sys.argv[1])
			out.outln('按任意键退出。')
		except Exception as e:
			out.outlnC('程序执行错误！','black','red',1)
			out.outlnC(e,'red','black',1)
			out.outln('按任意键退出。')
		pause()
		return 0

PmajalGmEOq5fM3='PmajalGmEOq5fM3mzT61Icd0BA1jT4vYVROOooyUzskSY5xTZesWvcSOF7CGWZO4uWPD7lbIbTbxh1Vb9iTD51aTQjlVc5u4GEvoq7BkRNroClENXjlYPlWhZeEc9ZejdIdz4oH875qup8Nf6cYdTFdsqRRaJt5WWqhS5gZLE9i2AeRtW9EKh6CRqEigK8PYtQgRiywcv3nURpuWsHsJEItpcdJ3OVjHlis4TOPPAQ7OJZKOTayupnIYXQU2rwT6ixefzs8PTtzvVq7FZtKoHKfOSwCSk7BgaEERWOdS3K2gTOykGnVvY5wc3MGrx7e83EBXVL7mvx9pslnbFS6Atn0SZxYyRNmJwXyEN1uz4PEC9hTC4R7xEeJiytHRCihVnc2ldNFD87lx84QITfkslJvbiuLQ1c4Kb3gQ5BvvinFAB9WlHL1mBFX1YfFBpBqqi6d7KNiZSneZ9zc3iG2atuPbpuduFbbU3bhuLNPsPHsjLNrR44NCNYzs9gUPyCq7CEPEZoUjURPGvDgEoVHJnmwlhpUKBVMVLKosi8IfAG2My0ZS37kzP8W2FwDdwl4vJjxpLpcdKP0cSFabowRw4IiJGj3bMj3vMNOSZqvILsrDi253zbbUkIiqQCCgeIDlqrBzjRNBITFN7yfa42ggFujQCRjGTKRRqFqFRdSgeUTFb3JZexp01nAch7aTbM0SmusV63sbOPKnU9Q4gWlLBQP6TCWMM5p6E1iUgksn4sJkLa86IZiPAZGAI4APVDczWpphRTnVpGG97bVF0EOKGvnDGWAE1tP46MrOWDaWV9877FnZ9ER2ljmZC7rVbBTEydSv6y90QTNuxIK5a0Pn7kvri3rhPQtVNyFOtwYxlz244HWmide0FZV79iKqh4HXKNnAp8nX1ecnB6tsJhCRgNVuLJ5Ykew1Xp1GdqytaZEKLoBc3MMBuhqWp35LLmkSwtazcByQl8TWylTFjYNnc5ucK94scmtd4V9h6Uml'

if __name__=='__main__':
	main()

E5zUE8OXhxboIMKcu='E5zUE8OXhxboIMKcu7Zqk7GipgUPsfwQdz44PsObD7w1eTElDy0hHsmW6R21qQv4HdQQ64mn3RGXWqngwfVUp4TUVHaY8MlMWjZsfQM6DTsxpq4JdoDCbwz7WJx2cet9TnbhACGDhAq72Rx5gCJNHJREfICHfc7B2C6QiVELf5tvO3XVo4lDxKtpkPBqPAQewvYf0fuEqxly61p3lcRX9kOIYldx232YDVA4a4GS1TI30S5xH5vt2yuVz7xz4EKzGdCfxEL7vD9XaVQrMKcnhMyuk6GOREpJeZ7Dm4qnQOk0eitNH4cUViXtb57HHzpaB9mCRBMwgk5eonoQcTMoTFv9i6lUiKqHEsgk4cuYVI8giHthgMgQjVAB3TwQz9ppjcwTkoaVs7StIRhnrXarillXChfzLgxeQx50pg7yQQjrFn20MgmE67eGumCQ3OPgpsjWKZcBZoFiXbyVTElmtCDsWvtQPA5GaQNSndxwNPo9QyLgeVwhhWUhZri6ZtXtWrmwGhINoAbL3cmeBNlBQRjpHq2cJ7afEvBNLlT17BEnAUofpE1ebPf5cVebrdSAlQKNiseQJW8b5TKS6x1myUNKVAaK12BnqwQ77uk'