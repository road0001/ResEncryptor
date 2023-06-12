tdv35bZhqvC5aV='tdv35bZhqvC5aV0aTju0fDATTZB4UFSOEl0ZMqCYuVDvKZDiczEGSKM9JH4ATTbPWnBizLT0R5e9pPDexk5t0IIu0EsRleRW5ILHtVqqUw2m9DoHvwk6ENeixZpeLh7xiBrAsYcTCzHJyWBP1aeuYqxXZppFc3iA6ifJDyOXFr1an82bmriSXEbzEGGnANMDgDfOAQTM1DyIR0W7gyENEQvhr4UBmQ4Ls7usId4Krh0ZJDqAo32VQJCySGtDFmvnsQrYF78RFAixxOFzhd1o7OkRZEFJFNxdRGgV07CRPOesFzVIup26Bj0E6FBrFgQRWIFJ8lEjBuAgt5mcznfwXeWMOQOMfZo7OeFOgDqGlO8WTDVjo0sictcHPDpwOVWtaVSN1Yd39DsdvzfZXsP4bf23Uc1iM0cfN4xscVGWWwd82IsOBsr9oYKAmEk68DtfXJLI5miBIUOR9dTPNpvlMXFQHBzlqU6nRBzfhHwWbD0sMuPLeMTLAf2TbeHwUXZXTfcHQ38NZBtQsxwwQkMjevlB1UPPftxp8afwof3BYPMUFHLsQJjEY4lrYu8VfdTFJm8hOWB3smXQRecIoFmtnjNDa9H0UiGFCFwBtWBkeMMzeLyuxwmiilvtOHU6h1bBNrQPWc7r9dTYzfOgXf4n0xOWdzkDWVED3I51Dsjn709UUt39fbh5vEtSHVWLPrqzEbN7mmM6A7yviqSVqEzOb6iMbUvvRLzzHmNHNATEFcgylRaoQQDMQDP1HBlS7f8jePFpmeXNvMcZpCFbvqYslVOSQBXJFsi4YaLENoi0bY8oQFiaDtp5mgNp4NqHS8WFJCmjefcz4K5X1nnzwYA0IvCZhGYWzLVAryWbgGBrWJB6KgmLQB2hr48ENc5yTHFjc2'

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

CSlEXH418d='CSlEXH418d5bAsRVMU2Ambq0Hj0hGKeXx4l5tNk1pxGnIoXb8Bc2vqfNLZ6A3VSvKQqmAmtihKCdPEM6i4kKUd20CRQ83gMnW4bpLfYMSjegEN6EGmk63Yx5b6fBAGptWCKCiFSzJFId35LEFYJnxEn2U9JQWIHRnzjbUeYHl6ROn71gsoIwnfSCB0H65feFNBo6o7gBMkrAfxDRON89ziOap3e4lf8nPpatyQmLzSWL2J5sePc4q7ywLvqwLgkDjEFqllUhCIPWK8cLwOXlCWye5cCw1yVlZPuqHczmcV3r75LJgPLILaJcSLNSfEC59ZC0XcT7wfNpzlqtAHItyzp0qSoHyK24YooxgNNbANmYWjvWetlCrBiqgv4gakHp6vAik9jhnIOaoT6EIpYR17mlrTnxpfVL2ZfKgmIy9DMscyipwA9m6h5QMOPqkR1KZzTj9k7ITdG4k5S1rUlu7QkgIecDpR59p2IuLK2JsPFBENKjNOk1bKQyEeOuM1gv1Dq3cJzVdqdbXOQAXgZBqVbxFBy5UDfA7o1oVPvq8eoY1zEOdExhNe2jKyaqkEcmMSFPaWlGNiJD1XjSB60lzDgZLcn62ixEQTq1k7igAXq79dFadoQ1dIoyqBG3hRh76UR2CzD3LP5EUZGebIiQOMrJO4Ie2CP0rQ1blnaK14sjONltDMnJAbMpriJYbmGJPUiJtFkNlOpXjszJvlsYQbgNJECBtX2izT9cyQ5s7mFnHRPzWI1aUy8huHNih5yHcj9wsYVvF6fpmeeP2rRDOI59KpnhyiYlmIe2d3qgR2dWpAqCCLM0aAPe7UofIXd8PcC7UFyMw3Py7CgC75eEXoedCe8GKz6lMPmxH1Qr91lW2n3zxgcBrwrD2TGqcjTRZ4whyRnpPzd00bHvsp23nKrpfX4oLica5IYzsdMwtyCcHjkdG6A6fv6dfgvbyZ0v7LpWIwjCp2CVa5AKQxcWISypjoXWkfEclR7VJPg'

VERSION={
"appName":"ResEncryptor",
"versionUpdate":[
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

Sqak0c2dfkBEiC='Sqak0c2dfkBEiCtYPnTFG7IGZIASmsDlBbfeylgJt90tpvHifREx4NubZE3ui9gos6J3CkE0GuRPmSsPoSIqV0fOa5r8SPpxcV6mciR7vgMigQT7zeXCkcMYpGmDLqs0ITmBmceIdi2U9iHJATOFvgZJG09lU95iG7JB2IbaTfP63yCtRO2C4ImtEvlOC6I9XiZi3OJqS5DN6ckklYp7J06BXqRY6mnxkK024UepdVRGKHUpGqFVlrMt0soTBEClcnhRrOQguitLGCejgH9rNSV3GXxUopxwtqaaHKXSnbTGJLsfxe5b68nZMhNkcqGZzNmx75UddYfwdQntnXl7jnp6I5rWa4Wrbslm9zoeqPMSnOExumWnwKTnGDgm74WlKNjoGsG8T4sI84AlWVkMpJFRyWUHgOjbsfhsYZt8ulQHpGunIfIgWCGCoLBfNwB76M9HnX2krX5yqQQEunnY5aVmM2sUY6M0mFQSRwAqpTOZYgbXOQ7HBp65ItoW9iWDVDsDi3EY58P6AUXN5UeRSgWhd6dKpC5Imh8LU4neOwFQVJVzIV97VdoWh8aEf74yyX1ZF2wCOhoBBnW6UC1mjDYnW9rkobdNgf1DeygoUuIzbVcKnsx7wOi9Gx1oO1fov5rXraQZOxLftS3DIHgAap2ru8Q2Fq7TqXGJsUsyeVNzNo8ROCjEEwkeZmoS2otS6HhyLR8Rjn0WsHbkRjMKekztcOVodJz9dsKkgS8SJyb8V9QBycK2mXvf8MJrZ8J1AM3UrRjVIk63unxVXInitu'

'''
Configs
'''
# 输出目录
outputDir=f'{os.getcwd()}\\output'
# 分卷范围（此范围是压缩前的分卷范围，压缩后的情况不可知）。[最少分卷，最多分卷，分卷增量上限]
volumeRange=[20,50,1024]
# 默认盐，和配置文件加解密有关，不可随便更换，否则不兼容其他版本
defaultSalt='KnWn7ZYSa309KyYnruB0JXF9zIRAsQNx'
# 配置文件名
configName=hashlib.md5(f'config{defaultSalt}'.encode(encoding='utf-8')).hexdigest()

rhl6lOU0bNihIBTk='rhl6lOU0bNihIBTk0o6MRuqqy10pGixgupLBgvrAPkMDte258y7vahymALVzIg41VbgwAYO39R2ZRlgq2jtLsiN4JfQzOMZU2XpgKF5p3aJWS2lyyCRuPnvUNUWUMtfXdK8PMWZwTM9Wqgshk6JhhjhEQF0OnNcmEzdrX9UhvYYCcFMs0HAPPXBIU2fhlhZx5T3yqb3E7GFVn547gRQPJvDaCnDuf3tkIijvMj4tqbCYjmECzUHRaaCFpzKrHizthYKtOriaW4RfhHVsnqMrke8E0Sgjb9CD3wqr39pRoBNuQhy7LxEsy2EMfhYAdff8wQ6pcDThwtbluZ77jJnQ59MHWm0tFf1s2xzhayAAu0VXcdmRI5vGs987BePTZokLu9C1Gy9uNUGxnhJdo5kfDgEaMJdgC8LqCqTplqwnNXouZ6qMlLPU56x7xl4MVY0LWJemATzaB2UZELklGeJcYbuhgEtvvZ8XhQwDrLTe3hsBPZACXnkjU3TXpoJY0liYMLVEzLVnBn0gyeT2Y1YAqesXYab6rXbdqEsRVxsE9L4OKVEvb4pHry0jMXj1pzW1emfHyZBOhvtw4h2fI13FiwFM0wKVugb2CYUbYLZ2Qev8KzHxEmoyAcNHihzVlbJij4CpWoxKoJsyjRZzJdrGtHCYPCcf2yX17xPWEkPBPuDUhq8SmRRTBJRhTtFwV53slDST4exl9ERPovXToDIDUho0fnhlmc5qAvoMxes02fDpt0FZrvl6Ued94kdBsEBDbXFI5NHmgPTjJHx0eYIUisy0kCVQCi8bEoIijwJEim0sM0YJ1n9nJc7WCHNt'

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

def loadFile(file):
	try:
		f=open(file,'r')
		fs=f.read()
		f.close()
		return fs
	except:
		return None

def writeFile(file,data):
	try:
		f=open(file,'w')
		f.write(data)
		f.close()
		return True
	except:
		return False

def getAllFileList(addr):
	allFileList=[]
	if not exist(addr): #路径不存在的情况
		pass
	elif not os.path.isdir(addr): #路径为文件的情况
		allFileList.append(addr)
	else: #路径为文件夹的情况
		for root, dirs, files in os.walk(addr):
			for name in files:
				allFileList.append(os.path.join(root, name))
			# for name in dirs:
			# 	allFileList.append(os.path.join(root, name))
	return allFileList

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

a7MmGsAAN5QqJ='a7MmGsAAN5QqJYRX9BseBvVfAgFvjMSRFeGILf1Z7XAUae2F5XbPOqYeNn65gzQ4YgWp6xwyVhi0YoKPVtbegS8qRSYylm5n5dZlf8hVM44yCNZfRnxN5yZb14rTYl5vuWNZU5PipWFEXmQ1uPEKc7DbCguzcFbeutf1ybPc9YneeeuQ3VEZQz66VjlPrAfTadHLeN8eQ7q9MZpJ0f2UPeeZxNqYqafiqs5ixfQ6BG6YlW6Nj4AGtSuq4bfqnK931LEgnC9KQmCjDviZHb2GCxj4hqCWBrKStMFwTd8Y9rk0qbtUx8aG1XkKubs48vlDxlcBCNHjIREyGrXkIulH6IFGKv6G9ZMD1WYWryUsRgzkma74OV7M2LRtvW3jdFCB1U1P85N6j90ZCvVjp4NyUHeQn1cxGwUf5mrJBUVbKiAtHIbiKjuDHVwPjh9Jhh9ap5BW2bXeRBjYtYI8yUTYQPb0TZSuM2LO615WOezAWxRGJAkncebwscTyL1gWR0sJuFa0MXSyWTEbNfemCVMgoQHiDdOGZjinHKU9sehPWePtEx583GGku22bJYGumtXeJBrASb6zzBLNWLmjJGe5PASLS69ilqlY40ZIBoiO9VzT384fweZgBApgJjqj1mIjZ6jQzhjdObjrzdF8yU0ATjGIxKLMxrfH7mXNYU7f1EEGsascZ84W9piPVls40f6sDo9RSPuFgp7h4CieqPTpNPOWjd3O5mlrtKpMvUnHtJNrplOsEM9x4MrYlek8qpCeK7kGaOad7Gr6CqLkNyLmoLovuKcsz7AKZA8d9lzbSCUxEQLK8BXRgnTjBq9Svg2oH8TTRGTUpYAUZjWv2vFeeTysp4sMAULudgq1UmSdvNScObTkXAbPTY8pt4LmntagoiToTEy5QcsOQ8GlfGig8OD3DeSZQZGQRwfsGR2OY0cqsa3AvCVm'

'''
AES加密
'''
# 将明文用AES加密
def AES_Encrypt(password, data):
	key=hashlib.md5((password+defaultSalt).encode(encoding='utf-8')).hexdigest()
	iv=hashlib.md5((key).encode(encoding='utf-8')).hexdigest()[0:16]
	obj = AES.new((key).encode(), AES.MODE_CBC, (iv).encode())
	return base64.b64encode(obj.encrypt(pad(data.encode(),16)))

def AES_Decrypt(password, data):
	key=hashlib.md5((password+defaultSalt).encode(encoding='utf-8')).hexdigest()
	iv=hashlib.md5((key).encode(encoding='utf-8')).hexdigest()[0:16]
	obj = AES.new((key).encode(), AES.MODE_CBC, (iv).encode())
	return obj.decrypt(base64.b64decode(data))

FFaI6GkLlmXCVtt3='FFaI6GkLlmXCVtt3x8aJD9qo178ctSitdnurgdUtty9aioPgh4YK2atNW0NJf24MQr4lHYT92zUJRbBG5At06vi06GPAkl6KJtk8AfUag1IJvk2f99JDOPWx1jOAxJ0qWcunrC2WlmdadH15vnt4QTnpNe9wD7MEa1WQwpFjPY2eiGvd9ZvhjV5vDmsg07gYQiXcpWTVrPGeklRqWBCfGDJbFVOaZZKtoNIZjJeHUNhz6CBQ73OACk2vnmyc9S6rY6t8iBShZqwKat0VfmL4vsfOk03RNhJxrHv0dictpJ2XiyhDgYtRXJX6OIvP64p1gQfJYL3whB36NbiiYHLsJCiWBXPnsxFsAM3pKnf1FssgPkmdVWdvM2jYuTdwa63j2TXxgVwHPUZiTiW7kKeVaqsx9ygpZEyS8kNKM4BCHefrpNEZ2IrDIdMCx44cWIWUwInWVGP01dDtGUDuAyyW9SvOj1fHNzGjoiV7aVRSnxLNvn5AuPex5GIjNffSGydAaXLJswTYpnzoBeARWSyL7jzntjDhhHQJFs2lm2IM3gmgdYo9pPtAZDOFpb6tjpr7dBw8YoQLf4yEImUSyFPjPL9ZrnVy3mpEixXaySlmpYIP5C34ucZYdikwdcCwiQsQZQec8cjjmpsy9dh09ILls5XLu8GdtLgeArLTC1H5hg7IvTAH3TNHuC65v41rswpts6dGzWBvOO3YUxbAZWqfzc9uEablFobhoEI'

'''
App
'''
targetFileData={}
def applyFileData(file):
	targetFileData['path']=file
	targetFileData['name']=file.split('\\')[-1]
	fileList=getAllFileList(targetFileData['path'])
	fileSize=getAllFileSize(fileList)

	targetFileData['fileList']=fileList
	targetFileData['fileCount']=len(fileList)
	targetFileData['fileSize']=fileSize

	out.outlnC('加载文件：【{path}】\n共{fileCount}个文件，总大小：{fSize}'.format(**targetFileData,fSize=formatFileSize(fileSize)),'green','black',1)
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
	return AES_Encrypt(password,f'{chead}\b{json.dumps(config,ensure_ascii=False)}\b{ctail}').decode('UTF-8')
'''
解密配置数据
参数：已加密的配置数据
'''
def decryptEncryptConfig(password,data):
	decData=AES_Decrypt(password,data)
	# config=base64.b64decode(data).decode(encoding='utf-8').split('\b')[1]
	config=decData.decode(encoding='utf-8').split('\b')[1]
	return json.loads(config)
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

Z2zgKLXZNkbMEdl='Z2zgKLXZNkbMEdlVjyOsqzkm08wfoK0C8cdlkVpRwW5ZDYjal7gAymIb6JUD31Lawr5cnuCCYVZmSgQD6WDFGuL1haNtHoGK9ajI74etvSVmBpYwWMUlAXREV3E1iyrC0BwAsm5J2GJUH59Pv4wXrP1oYIcB1czjxCqroLDX6w6dZQW3X2ueZUXXnxSVKyaQEUOOoEhp1TZwKdja7sMpwSVqLPOiq7tvYg24aRwDAPgFewPX9exZxCovxl58glafpgtu9vES6DtZADUW2Rh1Uzq9Owcxv8OvyUadYdvgBFHNTMGc7ATEPhSRHlLlVFvvimSWP5v4iz9bObtBWex608Zq9PbBxIllmjKNRjsF8x2Ie72o5ZpUBQxOXRS4cZIbHit7rflZOmHJCc0fg4WVkvmrv785g8h5fHU3qPdVTr46jCt8RAvubvbLG5sdMUehY8NapiZXBdyYRB8SANVTKizVtIdpGrgQAkxIJMxPLHqPoRUbFK72BxPv3nq7XNgY5qX27edWDKPbSeWRYLDnipUTs5G3cHm88cuY0YicjFZWQ4349HbPQ5aLNgdoclALb6ld8FDa5oly8KJIBfHOnyh7M8HLUkziQSc5nHo3rC9dTZ9uqTApSD8QIZLivRYzfel7hlNpVxDWmtpbLUYN2kxrq1WZ4UZA5CF5NytrBtnT4Qr6SrIlujdpg5kuqxFVsiMF475WfcQFU5UUCAeVitVTcsWWnRrZQr'

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
		confuseHead=base64.b64encode(randomBin(random.randint(512,1024))).decode('UTF-8')
		confuseTail=base64.b64encode(randomBin(random.randint(512,1024))).decode('UTF-8')
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

		# 删除不需要的文件
		out.outC('正在清理不必要的文件……','cyan','black',1)
		os.remove(f'{projOutputDir}\\7z.exe')
		out.outlnC('[完成]','green','black',1)

		# 对文件进行乱序重命名
		out.outC('正在重命名文件……','cyan','black',1)
		renStr=f'@echo off\ncd {projOutputDir}\n'
		for fp in getAllFileList(projOutputDir):
			fileName=fp.split('\\')[-1]
			fakeName=genSalt()
			renStr+=f'ren "{fileName}" "{fakeName}"\n'
			encryptConfig['fileList'].append({
				'fileName':fileName,
				'fakeName':fakeName,
			})
		runBat(renStr,'output\\')
		out.outlnC('[完成]','green','black',1)

		# 生成混淆后的配置数据
		out.outC('正在生成混淆配置数据……','cyan','black',1)
		configName=genSalt()
		decryptConfigString=encryptEncryptConfig(password, encryptConfig, confuseHead, confuseTail)
		writeFile(f'{projOutputDir}\\{configName}',decryptConfigString)
		writeFile(f'{projOutputDir}\\{projCfgname}',configName) #用python将文件名写入到临时文件中，以待后续合并使用。不能使用bat的echo，会输出空行
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
			if not alreadyTiped:
				out.outlnC('找不到解密配置文件！','black','red',1)
				out.outlnC('如果需要加密压缩，请将文件或文件夹拖放到程序图标上！','cyan','black',1)
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
			encryptConfig=decryptEncryptConfig(password, loadFile(configName))
			out.outlnC('[完成]','green','black',1)
			break
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
	renStr='@echo off\n'
	for fl in encryptConfig['fileList']:
		fileName=fl['fileName']
		fakeName=fl['fakeName']
		renStr+=f'ren "{fakeName}" "{fileName}"\n'
		if fileName.split('.')[-1]=='001':
			zFileName=fileName
	runBat(renStr)
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

ma94JTXlUIiR5='ma94JTXlUIiR5Md0zzt0V1oy8x1CfWVkrWfQXPFKJXfgQglkPPMKvED3aZYeTKAYKhsEhU91BJA3jpQ3y7Wr1XMFDpq02uM9PqRKhz3fMv99RUAUTCR1cHUFkSU9xWMnhISLV9UpWdY36mqLjBmoqq7yNRrqqZeSSKQgW2FZCO64Tygjln9o5q7lUfJEU10OZ82GyRb8h8jDPOt4V200Pdz5uHskGg4Gcf5ARIDGkOspWnPW7ApzJHeBzcU3y1TcMeuF9Fy0Cv1w1pHzh96i5FUVthODXWTAlfItOko5hvJTfl67KKJNHTdMZvweGDnTuDDxKRpgxrneltODZdx7WnP9HnHXY9KUZTnfit2gZJ5YatPX0Jx9nALp7cD0Bz0eJygjJRNYV4wHLb5dZCNwuBqx9VScb5LBsr6BolEnypyUcHGduqTi2v2l6esbSr1oo4pfKL4FvUb9o0UdWVSqJgsAlrAA87lrhIuCmLfHubxWcpsuo7tfQWrya3BFmJfjxUXqYTHHD7Rh6MKKQkSPkm5yKCMkgw3AM2it8fByurjL2pYT76TrSEqjKHXooL8sn0tyeKbKqfSTLz9OgDxbmsUW3DDVm180snQokPQXd1S74GZOZbFr74q3WHgP92MWU1yp8qxcllNgAx7vQ68ErdELqQfUiARb5ScVBt2rovUggdRrIJGlMSWK1MjhIymSpfXPPLcZoWnOntS383m4PhRNqIAs9W8tI2ZelwAvXKSMhs3RGsjExLEjedCypwaTkv5o1AuqLv0JbKstVMEizfX8gR6D5USWs8d65ISeLVZwWUZ7GY9peGqdyl7cl1hIW4YEDJQWwIFkqUTkiLeXHafkhiB2NuvrbXrjSiuBVfHlYOmiqbktsEZPRo87uwSICYXcPbWJPVgCbwAzNJohAVqmKSu9csRi3bDWZkNbOsOMpSY8cJVhzGqY7HQFsUlskV5mqHsEMQRgGGfVu'

def main():
	os.system('cls')
	version=f"v{VERSION['versionUpdate'][0]['mainVersion']} Build {VERSION['versionUpdate'][0]['dateVersion']}"
	if len(sys.argv)<2:
		os.system(f"title 资源解密解压工具 {version}")
		out.outlnC('-=<欢迎使用资源解密解压工具！>=-','purple','black',1)
		try:
			beginDecryptFiles()
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
		except Exception as e:
			out.outlnC('程序执行错误！','black','red',1)
			out.outlnC(e,'red','black',1)
			out.outln('按任意键退出。')
		pause()
		return 0

dD9SDtpcle4KbELr='dD9SDtpcle4KbELrmSKhMkz7aHMBswroHGTl1wdj0pf1A1TgB1iwFXHVYcSzncIAemKU8bkfEqNrP9v1TF9Ja5Rr3yFk1q4c1bjUA34SpD7dn64yq3f6JTlhRA0k89YXv2ROojyiDLPDG2rTJH9xtkuWGRKlYcoRwKwvpNz81wWCstUvnTTTwNCUESq900KkykWDh7bkL497NCAHHcyIbjVfe4sv9dxGLKMpx0lIw6eajEmiyIKqoQZXLUXmyF3PcdUFH7Rv7oPOKfdC7frO3nxQTuAQXW4ZtGgZrIsMDz7BrZTWmE3Kip1wWoKa9K47vzvTyYnod34XIVqupuDiXAy3PzwgnYPFwYiBE2TZ9Dfy9HOKE3waL1hGana6UuznLKn81yiwFox2CWg24AivQ7r8QQVM5I3aNeYjFVMVSudsa7t76IATLof3GYKdXeBvT3xqa8KBRF023s8TM9YSKgPAKIIKlaMwbKkZ2PU5JfRr3FXAhtjesNeaVJ3ux57cVUY2DR4JeSKHFzSZ1QO16jFXZ0JBwr9Q8CM3Bhl7tYxcq2RETnY5sbvR76jKAsbhlForPbFi2SRaCPs51WjRZAdGa1RpHNeDcnehx4rQ7edFt8rDfl6XMKquzsC65txH2itPbAv7khpwtPozpSsk8AXLCuLUWU9uv7mrxmNVuwuaNCDPqXdhiuwijWM6dIdXCvIkqpJlCtBMkJLjvX'

if __name__=='__main__':
	main()

GDPusI2VHeshuOeI3='GDPusI2VHeshuOeI3nM5hxUT8OIzI6Xm188YKyItXpuCJKilJUg9eI1fviEcwJ295ys6Mt3GUagkAvWxjejp12dbNF4dJW2EeDilkNYu5L6IWaN51UWmPmznsHkVXXm6EdCDvJDpw5xn3fSayiAr1hsvLQ7kuibaziK4i2AnaTSHhq4VHIGKek7cojc0gRBFC1w8038upJ91pNPBndtqBLEinS4VAvUhEkQaKVA3zfm0xJc3LmPoQosnOi9uJzt1gnCTJpEmhaf2oRSv2r0WqPM3oozeaKWWsMfRP15C3SbneYzgQtLKNZ6oy1wNvoIfBovJ0wAODT5fpRlnvzhCd5lbe1cFpTxQ7OfUAWVup7NKyTuD04KoghoB8pL6pOS74Fedc2xilk7CfPGSYGy9lywJl5osrqyGCZtDOXTKOQK8GUQXYtrpOkg4K4T9zhvRyIOhaIBhUWY3AhqAR2YOhHnoFQeTa8wRqKMJrb5zhgZdZxjqe7qAIgNKSxCE5F8F4vxoS1oxN8rYM31BjajVeuhavtFezkr2UyZBH9IsfJxhncV8XTdY2igcWG4Xu4bJHr9TRijduMFAJBLLjbyMRiwy6WRhB93jlc6GcxipEJK46IyG5aF9H6swgiDcl8Wf83U6yBb0EtYtpyNj7BD6JKmMdU6VAihg5MN3uFNscveTQgHia9Yk2tgwCQmgxGGeHcQ'