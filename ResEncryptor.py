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

KdEX89irrza35E='KdEX89irrza35E98idOoxYk3ykjZg8WhDnHpQAT16Wt0NHsd3v8rickInE2FjuecjEROJ7ENMDTbv7z83pWMZQKUc2wqX4xDUvEMVxvpaxA4OMSNYR2hllUgtjeQ2SU3T0lxNe8U9hCRG8HXaaKpeAAPix9S6JZHT9Qlgz41PbsGNmfRshrTWyksrO9cm2KDAXn2hYyVmdyoU7VA5UVz8EwWEBaYmuUejtAZi40RXOZGWVzUS1CqCxZnvDUUrDtwa9tGkUY8hUEvInXagFyFd7AAiZF2YNPXLegFDPxDunMbUdTSRYtDeXS2me16EhaZjiE7CM6Gtvc3YS2xA7ATuqVNDzYHrUh8PIOA0AwYNQgOd2l3NNKNvRzYBOdb1BkjQwVouyn4ttpCV8QRWxkUfunx9dpK3x5HOEh2HKG84Y2zeo8b31LU9IIDO9cwgjyckLxx7o5B7qMFKz9oxXSSWPqOpiChDmSAFS4otF1p8CV7Hufk70MdK6quB3Y1Sw80KybF9T3pRqPx551SFbrCeodiO8GTLggmv0swgeAKF43U6L'

VERSION={
"appName":"ResEncryptor",
"versionUpdate":[
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

ruxRJILwM0dHT7Zfe='ruxRJILwM0dHT7ZfeNrWhdXcOw2mD6a2ZAhu85rWWVCm5MVUEXVqqq7JAZyEcFwR9LONKS01aN6R7snpYpsGH5ZWu4yQEAyrcmOBTIT37peJ1JoBUjt3B5vHiVAAth5ny9v7tBOrlJNpDsHEZKCjM41PbETroPEmzrzCoyMKNY2bnvCTFBE6PC5zfx7XokDYwdDFQDZqaSMLhdz7e8Fn7gCH18ReaUBpML8y7bDAHQ9OJRfBwpfGr5CMKSu2pWogVNQMsp00MGgNekvRtZsVUa22GTTBJL3bQS6RiJAsCgdjC7C9TB86nU3APpThcizr5HoeRkpgv9xLNKQ9l83L1wYfbi6jo9eyXBadw2wB2gQMl8fSpSYkMWjVUuKmLcJHunEKYyO8h2aKjPadsNSKPFMHVVHI6bmsymwTYH6bKjHypQhM9eGxtwSdCgtGmoBDAGE0RG1oVAs8b0oJAYmO5ih84xC9F7czn9mXpl4yw6EzNP5fBZp2etR3xupv3AwX68yfBuDdGlDWjAKYgxYVPkQq5H0gH8Y9NybgR1dBiSX1Itog1HeWW2avC4f9EhXaK2BZrSD0N4J2nqf6yqg4V1WrAsqkmTibbeOnZvsMEY5QbXb4faMvRlDyH3urZ85c0AuK6Enl2WoQPCzcEo85BIuaXnKhusSnhaxB5nqlTZYFthZyiImkuIN7MkSgPTBPAihey9z16cCb1JbRYXO3N9SDDCEtiLyC8y3Q6HYFyh2ugLiwbps0s3XjRxtztdSv9Mvxfo8avN54Qn0BcPuCpj0tCf0LXbLn93zY4htlDtBWf1RY6Y8bB04Gk8RH9WP4ahIMzqvI7sZpl9IrzOmuvHMDAcdfagwII2OQTux'

'''
Configs
'''
# 输出目录
outputDir=f'{os.getcwd()}\\output'
# 分卷范围（此范围是压缩前的分卷范围，压缩后的情况不可知）。[最少分卷，最多分卷，分卷增量上限]
volumeRange=[20,50,1024]
# 默认盐，和配置文件加解密有关，不可随便更换，否则不兼容其他版本
defaultSalt='KnWn7ZYSa309KyYnruB0JXF9zIRAsQNx'

AshnnKQrBm='AshnnKQrBmi9PS0uX4uh8MdBHH1USyh8jW0MBdGoavza58ynLbq5tlucx2I7JwfoAz6haKgHRtLoDP4130XRkRF10GwdeA2GJeOC9NVOtKSyRu23NbNAS3bYWNW7n6f5zlfkEi28Z3JiV4FpYCAjPWRsQ8KwByJgbl3EkqyD8WUXc4fKh68G5reDDfHYhuKpX7GhD882xx9eZk9dGzAaqFgL46ipIfsz82yXXXFdBOSU04sDAfzZwtxPi1C2zCri9gAWYuu6C2OxY3pLPnJm6lJuaZqtjRqg1wVBgSZhFHGbXwcYC21QruxX5uscPZSwyh3xvczvaIczrh6wfMeCfLmt0Gs63RHvg6JiHRdsvqAW9SHQz3AySj9NGfxOgLYBtUuXOhrp2lP3h6rWxbsd2PfVxtdg7YplEiBk69El0Cbs3FVJDACKr69tJcyt9uCM0W0ZozHTiC5wttUt2zX83unKa5qOVWDVW12Lb1Ah7xSW53sSnTr7BW2QA3sPhcXM6pRE4WEnf5n8Lz301CwuKG3ocf9W7c9js3b8p2Z2n5eIyUG6ujbeEzPViflg5owFL82DrdG6kcHSLSalJhaAxMMBWzo9JiX7vT4wWaXqhJ4DFcuorw27yBNntjZchT3JDvXFddJ7WnG5glZHj2l4NsZCsc5G100qugfq7cHHd56MBEWUzAzt19O3UZQsktoBw4knimUdl374LZaosp3Vl9XmwOZhvVuG8mTkNw2imMIOoDNAVdwB1TV3zjOeUtyXiVsxP5AH3tT5Dngv7c45wWNUzVUIE4nC4aBMBB6En5HjnAaQ5ftE5eXwYTY9xrPbbag4HhONfGy4BiGl5Jo2DyhXtf9Zvyw9JVhkHLmMEWQ4TgYIinQIDfblS7'

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

ntpBpUsVqknVRtb='ntpBpUsVqknVRtbDpmQU6u1jb806sxqhVcHTiJP73v7CA0UfjTPNDYXbgmI6yfkBFkxLbPtNCrhTizwJVgaK0tmh2KvyOUlPbdT9eC9zd2IZmHmDHY3vbBhZSWlLtTkSb7n2ZY4qqTVop53OaG9j5DOhmTDbEWU7cvqv4lLO8GNds4iLL0fqtDxR7ZcIqXxURwJbJTYVIqEguy0IgsFuLJIENslsGE2cYMQEqYsKZ8g6TBIhkTPLYgAGLaVyPWKHb8e8uMCerERWlSUxceUhDUm4U62TBIAUGns230La1hObzMMtTEmJZ3QxaLl9ZqTdzpaeyw4LrjrmB2VqR0Txf3kx5uSvaxuDF1WYpb6tYzUCW344M4zQsF3n3p5jgw2Qxf8bnwi7awUayTMUmIjbho1EeZUIdddBrgQAxKuHYTO46uIZq4uKPXAjI8jeGzQbw3idUHzuHxcBCN4yusQl4As0BE9EtOahi2RrMzn4vJudo0XDewJZJ7MWqnBsrANwMPOw7Cqz0zBXXeRWw6QpkdjjpNjMTlYefwBbILun2440cBhdZnolPSUyek6mWqy5MMBWInNRIY8X3sImEfnkbT66fY5Kh4ZQdLwJ95qhvJ28cVyuBR5ZFOPGov4PO4iFlUqxlmbWcBHiFuz3xNOfV7oauPLFF1Drg11EpWAgvRgXZAcjLaW5p8vEmze5v8BXU7BNF1D8H2wFiXWxwLtZROCbbEPjCKYe48FlDyXzjuWwDg83WNRdurq3pqhVuTNKERTENalPMIUM2MhUlZPy29Xmo2c2cHGlhIQSgDh6H1t05zJ6wxyjbuzxhaIPEydfBc3eGYZMndb1Qqe0edp5dnR87gLRYyxPE2lXy0OVVgHTwGH9QulqR3KmAZE8lcfAuFje5O56vQylH9zfnQh5qjIZRh5TrwINcZz4JcFvOxnu4zr4sKGCRO9rJdeAisR0CwiVnm8VF0b35DWFpB'

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

StwbiZaly4tDUOgtRIf0K='StwbiZaly4tDUOgtRIf0KfKLm5QNhggBvcelSoBhMVummd6sNb2y31BUHjzie4f3pmtfKXNVF6rGDNp6AhPDmpZSG1IZbDS7xrvyWN6YlblLBl8RLMrutCZjsNBxke3HNOtgZ2rG4IzjdvLCzaTSK1b1aO0EXuGaW37ohVwGiwpz0OItrPEW7UdFvUVybMyKDxVBpLblhvy1zShTBx5HiTblzQqlXS8GOTHSNOQ3G2wL3BM7JAHt8NeMoUGM8NRvI9PWx8OiHpNER2o30ejV4w0eJkgV9rYo41v12GjJ08h2YSaJAaS022Em9346WIG8mecgBVRdjb20iVJfWf5IsIp74CRGOZxLT6W7onnFgVUuvfaPBwi0VLI2ojojioi787O9821n3GYETEppXorBTPdldYqPVfGuCNrge4UkFB4IQwvnYg8sWlQRUsGxhw40CaFu2fmUgvwjYxyTujPHyWLOv0LXK7UeDwFpFjczo34xule0FN5qhwCH6jiOhsKXwwlOFB4cBGuObgC4nL1PkN8MDQYe3xy8ml1KAdnYbln1uzGE6PqNVA1Rkbe9UO5WIxOImV4hVehDV211p0XUJFlJ4qRi4thE1q89MEhmYvayCzgEIMcxsrcLFqG31yZX0pd968xE1us'

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
	# return AES_Encrypt(password,f'{chead}\b{json.dumps(config,ensure_ascii=False)}\b{ctail}').decode('UTF-8')
	return AES_Encrypt(password,f'{chead}\b{json.dumps(config,ensure_ascii=False)}\b{ctail}')
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

GHyKm342KdqSpHhF7='GHyKm342KdqSpHhF7ApbUGjtfNS8JTsjLsZ2uqXmQvUPlQXRj8wbEwJuR1IPMWd9Yc2zHhvYvsuJJWu8nChvWdMC0hEB811PBXJhkvqPs6YrT6PCpYANXoWpcJm5laG7aief53LMMF2zWfzQBncc0lh6aMjXp50K5zr5uvkphXs8i13q92YSFYUDWOK8lXosibjWSWbgDQh5AphgBChVYS2Spy268vl6Y8NQ2ykSuzrIKqW4jendRUAcjRCaA9Z6SofInEcqsVeASyAGjyZv48rNjGa1dV7FGdGFGSOvGv2WwjQs8JfknyK7S7jQWmGPnEKrzT1q07GK1tF4dQYZ1iW8xhninn6ix1kIyH9wpyFZ1hWF5eLQM6xxwgS8KTdFsp7zeTit9d8pnTb66BNb4Zbf66CDt9ATBIBrvE1Telxc6cTGGK1ET9evZ3ZVz4wEeflCvalA5nrBtCVTKlR6523Jdzo9n0akZ0S3A3JWgRy0jTeoVPUvktHoDdF06qt4J3mduN8XJpHzGHBPgYp8VsNH8c0YWeIkBtFASSScuY4jMAykO0x3uNhLw34AZBQ4aFJ5yR8JupBSaH2BmubLbw470Gay0T0yfWaUlVhH5QUSwrVMzyLzgAPD7lbavrLpibiEReRPzH0ut8ggC7JrAE3rBdIfYeKP8T'

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
		writeFile(f'{projOutputDir}\\{configName}',decryptConfigString,'wb')
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

SlJZjLC6TcXsZ='SlJZjLC6TcXsZeb3LBWYpH8dNrlrSt1NMAGQpDsXTlQY0Pyt2E6LXy6KFYzxLLURNX0dze7pEX2INP23Qy59rVgNGyBG6BjKesvMEIv4DBaf7BOulBPsq4cpKxh2VBi2bHFS8Rv2SkYwcjDLrE1XcxJQmGZQvsZEXPeD6rBpjlEtgHn60vdQxe8xSe3KiZIJb96mvSAyPUbnTI0XOy8YXKRPje1PY6nNzq8bGwnKwdZIkFaTdhiw1cpZ83XGOdhrJVQ7eplp8Z61rqvQqeQRWLPmsQ0qwLEiKAKfeOFji8Hr9WL1odWkfBmlTGe7fx2s8c2fChZzO8FAdwhIzfHHXONXVUHlT7zScB9dsdiNzSA0bjQcMsgd6g4rfjcQgzWgAEFbDTrbMMA6uiEjGXBhD1W4PgGJxc4je1G8XQckuSW0niYJ7pyCO9UxIJhrujutGo5Ve35O9eF68OAgZ7bFl2p2mhvhdsrA0TXApdk7oU3zkNtJGDDRavl6dCHOgBGaRqUQ5otWLB3M0bxJmQqDU9fuEil2JTXpeXv2FTLa2sVdHoqosM0yfuv3Dvh0pj19BQoq9MLQ4vYIZinXkFeZPbTxBPoAJr976gBbEM6UpiodtCt1OkyyXmofiu6sa3Mcg5LFPrGDi6HTgzxl6NmjhU82Rwc0TdIOxyvOGUMqkFBb6KYsmJTtuYBtMw6uPFgYd7wfJ2bzwsLDml6jGGEinv3MyahaGRKXFny72BVqJYxhfFtFuJMV4NoBIz5rVMV7Bh0KTMiXFEmFbnBSALcjnOVQI4NMdSCXoXf2bd0VPKrugt8fM0JudTfLboqoliC0X9dtGDewlcrFCXiG6k7lGxQa693qcy5dmJgJoyhVekDWRPw885Lej4Pilbz'

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

bsWErzxWvaxL='bsWErzxWvaxLl1fzsHBGSo0qqztQl9nELVw6Q80Cd5FbG8YbPjR3XrkP7n6Qs9MONJpw3VWrt8XK3jw0FGJuCA5aFsQbD5XsnI5vOzkTG8PFX3cl2Cn735ALhsyTUHXTQHj1sFtGUOlDfRga6bKETKVCwaSsaVoAykw8EGhTW5aQUnU5mMGPvrzx2aVe3rfdzCpfTKry9b2el5AA6ef5KAm9ENqdiTlMhgjolfxEqYwhcH5vANXHCUpArOeCPn3C9UAKVcHzBS0ZfXESBQAxJGrMZud7FVvFcgKUW3YBb7mEAUkAy5aZtbaA82bwybYXtnFDt0EQ8ua4EoO8p5A9NAXwlGspkbSJHtNth2KJG0WcAt24IXHuu96Hlh5xJGcRfy8e7pZ3GPKxg7KTL1VXkCQyMAQ3fHWlaGU9z0JPgKMt2NNJguVjAcwEuZ2oMKEEOjOyaxh7fykZFomBmvkLlWbhQ3foXOAUKlCGVOAFbgUrnFQxr8u2Mw0FsOJiQuxszW58rXDNUTyECRShgcVv5sS8LVVQ8opcKKunpSSvdwdfHzdC1yJhg2Ru3J4T5DxsrO2hdaeGJ4hGgFBlTo6WceNCNvSlOr9PsTXGS47WE8rAnmwdmYGOiT1YP11ouMzkxi8n9UxoaHe8rRFib5TFOKT8Pae8XsqY1J5wQiaoLlvlGoUebddCfiL1LY1wliSob1d5tJJfNjiP1fOHLKCQxtyTAYoscpBGrJ9D5bMz4b2gAVCAWAyMvLysHOUk2JlqxO8sIGIeCSaJ1qDNds4dCtwhC8HV3EC64KuQCJhIaAcWfBdWNG4Q7MX7gvW4zk8h2nEWIeSHPJg1r03hTX'

if __name__=='__main__':
	main()

qrgi0HcXVZO='qrgi0HcXVZOlGML0m3BeLyYFGdDezh2IPq8uMVTMBUiFr4yJ4UHtQQ1cFOiHpMtHfFGWIOa1hCeINRuWRF2GuNID9Hwh4B0MG3AxB34uDagdDqwmx5Ns1F2eoazwJzaG4eDD5YJCfHk2a5NvgjswYpWXsG2pSiW76bY6hWrnePdYrKWYZD0VOOFBI01jwgXjzkZZk2jZOEyOagqZ63y62dOuImdI1KHokuBANnfPyZ1sQWngIslubk10GsbHdlbckExEGZiBLlk9KckGo5PmEL46xCiwGe0jJkinBqksYektVV89hsMeEV0NSxUp6hGiHRjYnfcaiOCOxeKPxmTM37PsYMA5t4GYVVd68XyTdliMKPh3kU66krEek04P6vfyNSIRMEANoNwi1QOjkt89uo2QdVyOXVuVi7HBmrfrmHqTva3fR6gb6hHq0eE6o0U98w6jciASObWPtHAUSaCjsejN3V13jNOWtNv7qrGE8nJvcZ2obqIGLhd7Oc1pQ8yKXYfC6edPjh4H3oYhh3Kgi2zLI4VkG98a8FXPZOiEhxcpxgv6T2VhHZeMvgtBvj2BuuSq6kR5Uk5xSL8LU4xxDVwlaq8AbAGD2OALzxU9QMZdkFyA39AVooQU8ABfxPYBY91MpR9CSv9v6T8EuYTiR7XmwiXFHp2KtzBu8E7YNZMVeeO0HoyGS9op9r5w2lJXCc0jyz8vBrn2jF7JRYKTaPh8ihnacydgE0ogGjtezPLxp9DO1886Z8AkjUedFtPFVVJj9G7cYJ8sCauxAKhSdA5uTfznF7Opquq3q6nB457apsiMCexqJPnDQ5Am'