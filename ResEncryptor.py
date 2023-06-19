DRQQTKLZRXrBFhRHXsmgTKkmp='DRQQTKLZRXrBFhRHXsmgTKkmpyI8ZnvwYEa97KO84UGSBSM8cx6B9ri6ROx42S4Yfbt87wH9Dw1LCmasS8OUaPRNk7Y0wb2T1zTvTtHx7K6dhpxKb1M9cR3LFC4iZsB6pGNzz6xQNnqoRBGkCnVBbF4ERu0slxxJMube8iKFM7vjm4FRNDtozhjlo7oW1kiGtlO2uR9Z7EAVlx22f7JiXKoSiPaKOxlXgm56G3vXqNjiT03YRlUcdNekGaH47PT8ThBUCYbrrbAC5wFp9J49RRessvCcYDQojZ8SRswGVjGB5mQ1sM57GVaTiZPofpH35EAPk0jyaGzsqCnaDzYqx7ZRWWZuIbSg4SlsDQ8ka9dDOe6lEeOKFhGs3dfau1BJnsCpFIHf3YIr8Q0SEPduUdVqlHmdbbQcZr5MpP27zaLvAyBxoKPbObhOCXk6sZD7Nvz0CtyFZ5UM3OWCpO8yLCkEODTLU7uebZK4CtgOvDPiZzFzIPNd8pGdUyHOLRkQscUD1ehCdDasydn36NvRc4sa1qo5VUDdLek6vJpuRh6RUzqQFPWDoMyYhWvMEK8GFveuSocx3INej979kAIU0ds2QzLXnViqUm2eisRlps3FaH6CGBGMN5GqPUZVwXp95ipI6hcfAfdpOiiHOpwQRDOyNGScEONsY82qf'

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

Kz6IcjxHWqumRX9gIYwq='Kz6IcjxHWqumRX9gIYwqHRu1G7hBRjmMv4IIciM0YXRr58iJdBkuDY1Tp8HY4UL8mMe0T92Dj0dLXapG5oBgKJAnXikMxVEMoDDFdJROhREOSNNHfGOW3zGrWE7yPQloRaGAUEZh4rrHY0k45f59o7xvvLoSAU48F3rVIRMymv51HkQ22FuP39lJM6J6a7t2B0eQY6zxSfLTFITGa3j1DkPAPraXtOiIhaRR3HTupzK429PSaW1zE58IHtttVRlEeeFRD4f6QP1BAfPeucvBMAI83fpvKlxt3fgCp4YW85ILNihhv9QpM9jfo4ElPQk99oCrKyFTYGJ7YSJzcD9ZlH786pmdmO6G5nikmeU62gdEotpmKT6e9wzyGExPWd9NWx2WJVzmGpV6v1LHf0p3a1JFckTisE9hKcuxZNe0QHRwGbDwQpv3CeXgrJ4vHCsYoSupGgU9CHo1KaStBGJ6ej1rVhZXfilq5gcQQ9g11wS1jGVoapPBdfXdZEzjRNQTM0cqWvE2MBORFLYlG3bxXzHHzgqR9qX062pm4jGObYhgz9dRcEWbncMQZJoBjy2iSwI6PDvMJDoZssfYoDffqpFIUDLCCQZWk8DQWDOURYFjv6RfIZU5df1nvIa0DmzQYsR3lM60bLisF9dTvv6nTf5Yzf0Fzb7dMb1M1Uh1tTbpjCM32N3pH0lXTYUfBlKmf16SoVHSXYaMR9GoVXbnxz2mn0MGRzqym1xii1r4BuzN8qXufwlBVClaIZiWOeIR3HsrikJ7HuS2bkMI8TGP3GEctQpd4wzJSI4mqJZb9U7bsKQ5kqKkfS1Hf7GHlREO5FBDvUDd1Uk3a0YG9mp8o9kH8v0p2Brz5hjup1sOB5LtjpL1FwVOhlPd2zME7BQx59esQ6Oa9d6r3CFslAtwjj1nArnhh46qLIBFe4GKEn5MQ05cPG2OhUC3mxvy4cHH24z70KkSZ6YokjtP3adYR40MCLXF3fhqrY3ZqyvOo'

VERSION={
"appName":"ResEncryptor",
"versionUpdate":[
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

CBEQnqeYpMnlS8='CBEQnqeYpMnlS8WDDcFj89QGoUpmfKtRnA33GWWekucQRUmnqN2U4eoyXCwVpIxIlCbhkmuQNqpBzXXPzNLdCqmFvWWRI2meY5uLwgpk6QEvHK28Ws7AJUEu8Oos7kWTywuOhXSnDcyXDKhMEibTYKrfRvNksHocjY2Yfw9U9gYp0HykqVEYfFioXNIRZ7aGqaDi9Qh7Twt5OfGxDH0OHPr9SOPDjv3Y6WBql9jmXz2W2khuTgzXJq82IsGVTbPDtmuyogoQQDrLzsn8ZjCY8C9I5vx2w1Q2zkWcktIa0BxpYFXzHowiOGnpSJpee1PhcFlFM9vl1gbT8nlkHOR1d5AgqRnB7GHs1P20jlFw5OfccbAhGiLi4C0HdNzUfogl8pPbgl2kujffP1uCJhgC6JtdCVmy5eMDYzAgxsAIew1CNlL6KVWRS7MBj7hFH7gj8ff0AxFPukyCjq4wfn7v8AhOhNGXWwcocfpb2znaJrI0sad5rV1kxq2r48k6lpfyUYX6gIS6pI71ruF4Va676n2TomI10CbrZ2vJnViDfgk5tdfNMPhU5ZTT0hr3xESkdbIUXUkQpsgs2vsTC09At1OqNwyryZAUIu2kbAzSYDAhNN7jKuCE62sFNKqg43xeCSMvIWQFNttl3h22nPaeNyuFjUsNL7QlFvc1NVDA4yHRbGQ9aGRelvg1yi7ilgtp8b66Y7ylVydA1XvmwWcyrJaN9wrb5BPqc0c5CujajawxSXJGiCHvWbiwnrvUyhgyzvBa9Pv44pWNbDcvJBBPdun67pKuYT3Dk1s4OmPxKQ3V6Bj3r0vCYkdkkRnWmxiYqAdSOMLZLhfO4NcLJ6z07g4e9on7D7Cggps56DcHX7aU20sWthajvfe3vyS1ySdyyhbgzoIKfMEj0GZ4uk07ceHQxCqQaJPJH3fTvsWJH'

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
randomHeadLengthRange=[128,1024]

lON7I42xI78GZHmKGF='lON7I42xI78GZHmKGFGH2xLHJ7stdKPrOSy8hQobDQYFMOBA2nuGJI9OrJnTWltvfIe61Md6BnHc5sbYzvFHL9MavRxKzsjEfvaDSuveIQBkY9vmPBMOwFYbzOCmhsJr2hzOGQRAp3299Vg6irXzpJpki941w2VDXEXjvVVL3Yj3wvHZMTX4K4L1gcgiqx7OPBZGHCOTy3SzJdhYcdy3EyC4nUHrxfEhWC2LiUlTwPM1MwEEVxdrwnHdXrUrS3KVVFNTF9OZfaAzGqHB3tcWZk3AKfe2SOAMdCw71yPHKWKgahSCNXnDM5lQDtMrPvX9tom5j3UwMIYdZDlEI7qKdC8ZQ5a2aNtEB3XMju3524eakSqCmOQBx59FFprrAl4eUE2tFDr72iQpy5qiAPbgueT2XMqukWF86ssuOHfVYPzrc8ZM6t6ltzPtSTvOW3VYDOF4PGPwdPGNEKHRQrIohyYwUtio2dmz1Hva8fdDGSmD0ss2FJeCQIE13XMuwycGmANShEMzL46xfyD05Avm59hQCJPfvorZRFGh6cPtXZ8mMUphaXfjhFRJtQMRlD4NSN42Sw'

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

O4HGqNt4CIp4c7Ok2bb='O4HGqNt4CIp4c7Ok2bbXAHAJl34WZOhRO5DnckxZUzF6HYhXU9K7clRLkUdLGAyhvMBrJySc59Ou254GdjQHsS9FK8FB8onyfcj2RHtFPtDmUaC4dsdZsQgS8tbDGmRto8ja853Eku8DT4KhC0ytDOmgOQPkgwfZBRtptVQGT7M9sDR6ut8xeaXt8jzZS6zsodgAxc2gMypQaZOB5gDQxUpkzMoNI9mIfJwMa3xZwJ3HlzSWqG6jqYNDiefCkSahs5LA4VTE2KyExkYUdNzB7i3KMPfWC6JzJwvtzaikifxUxjEXdRQNsovIjOh5u2Rt9TGmD7dLDYgmetgguvU2Xs9JKtRgmSc4bRHSit5Q078xS1QKf1k1eAvuV28b3rlFB2iz1WdwhNOjC5B6dMHYfrvfxD0sKkBXjEIj0LqEDUC4mmhlDOobTz5x3kbQ1gGqMMERh5HPl2Fe65dRUQ6gGmmfGBtfjODuOLa8hjedJFH9mwHxnzOn9kxN8whImAiOve9WU37FEMoxWS0tAfEcRarSzOcbVilr9r1wAegZboBPT9uUGMEXSNvxkSwXC6eV9x7rZ7lJZIj4v9q2QwGLvzRlsf42rlqGJYZ63UbNxCX8zZQNAa1rwn0bwkTv5Pg728vN2uM4RROrBRgQVFYButAyy1fEtcpiDlM1wxYaFpernu8XbdiZi'

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

SMW4vkszziN3WCavnS85='SMW4vkszziN3WCavnS85RgCKbeu1eSXdzyXnHp2xIst4rqEvD9x0EC7Qio7zqV8KB9Hk1AZOJpSpe7bowz0kEKGfxQlvM5UHw1nHSjfATWuh1lge1fgyDRZcBfYYg52lMJkW47CaSlCdJI2sRej3iQ8lVYDDAHFW2NgQ3FlQa9Kl95GZ02mLI3gq5WmyS5avqCvIhvZoFq0axSgnfr7bPWlM3SzI7tTW0CUF7iQ1KwTm9JuR9Y3W8SYudTppHDc19W8QFtGNB6gwTg48nyjxBpbtfDqXH4YBLNxJCXRYUdcFEQI3P0WKRnLfS9pLhsL4otSf7vhwGPGPEBHeU3k82F9qRX6qS2FqxriWDOCLxHn4JpFGYZSORUu9o5PMgoCoxqE37nqOLa7EL67RBBka3PWTIT3wW21XsJcVRkCIZJmrXv5mP973obpOXqlKSljP2dUcy6fmPAeroViWsQ8CepIA2zoiw88M1sNsoiYIWnZ3NN5RySSypVa1pTEvmo5TuURxSFLgUC3Nf6w3eozITEbc0cajn64PcvYcZEHYwju5Cqk1iNr0v1QuT1fTnAvwVGfKUevNgM0RLZsLkRnCgWhLNjUimTgdoJS6OBMIVED3bxcao9z2J1SvPiLAjn0Vn3zyi7QS2vTN3NPXXyCH2tamwvkiyKLvngTXhG2hpDTGLEevdV74iuKUNW9PoIOtFPK1E2R1r31su14N9frRRWx81yeVvDL0saKSKUkSo7hRmvnHDZgCnXZFkkUHhd8rNToStDxNj3cQkjEvmyFCYv50jGP8jPQEzh96h6GQSBmGlH7ULqs1rX4w4zj410a9i9rstyTY6CMD9p2UjtL2bBkQ9lc8ZPNYx9xDPN6cedyHa6w21WgJ42O9EIdVmqhA4dJw3VjKPkrBpQHDJNFyp5UmI74KuRur1GdfHYg7teYK1uUno2J88t3tX9YlrfqmS5z2cgOTaD5so'

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

aNcWc0lbrlDfFAaFlzwA='aNcWc0lbrlDfFAaFlzwAIqpfmUfR6sJIP1FK3nHYfXkpzvTqUdo5k9eXAj6lGxCR3wWDF5FFMn1m6XwGFNKEZwuswbY83gP3RGYITLDgsQDvgFvxoaJ0qis1P5hzNRmx1LrXb1yuUrh5fYcomH0BE9KgBeiRSivhQMUHoe4WXaLQiwIcjXDj2aB46CurGBt4wXnYuQwCAUXg4Ni4RF7hlsiaxP6ZDAj7GbMQR0HHowgdUi5RMFpBQoSIeOu8IE6cCv99j1D8U1jxpez23qAHmNIU4crhgJM7UUSL6KmrhxQrgp6zHT0kLp0eZj6151smLDPTphlak14BhDjoLZNYztcThYDUJZ5G74ANl8cFaItwV8zH8cjwu2BdU5ZM5Tar5ENpNAa1c00u8hBtQEJWgBrO2sgqiQLaFczeBTt2jieuNGPyhGaX4GY6XLp1pJm1AtsWkf8TeSDKgdPWi8iPugYFa4p2wm8a70qk64x4B7ZK0Uz7wthSpaxSTkkprVSyvP2CThGaRxwXqsxXrwmpa9z7uIMlSvviiQlbdMdQgWyQewfXj84wSx3wr3WRUahez6KYSKnbDxKkdE17pnKjbxZaSpb0AUE9WjN5qcSyuoHgTJ3usFhzpecOQ5tbRZROGmIbFNTgLR5fohV1JvcS15LNR3lPQQnLaGvDiqyv8CL9nInw2LxN2n22hzIv45CBO2QR2fM0xAnltHTqmAj8sKRRaCllangSOzvIiL3CBy1jmYxLmafF9RSy0dLJUbKC76UVzf81waNPIVSKCXDzcijHWkUqRgynlH0YOqoJmTr1JGwwDfYnM8iYFjEP9AgsuULiKrOs33xYPQz7wrPJ7uVnkBe0lo9Oo63MLe5qIEoW1XONgsjfgaJtLqjnBijgBsWMqfU3mzZjFBPKsltjlh9IwhwQLQWLUNvM0'

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

	# 进行7z文件解混淆
	if 'originHead' in encryptConfig: # 向下兼容没有原始头的配置数据
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

TvmD5ym0xWu4Gqa='TvmD5ym0xWu4GqaBJ2LCBZSr9a4AvKtwAS9ScLO7fLFQtpo8QFqg846o1rQOtmRlAvMrTNYnaoXiG8CRN6l8zADiE79KJfmLuDO289OchjzPeqEfJ6BDPn3vkb6L8n1rLwggBXakXkWYyLayindkx3MMYAErDZNJ54uDQlM1Xs7ter0hOt2v8m6VrB1VeOLr8EszttiyG78TFJCtVFVLjlym3VHz8h9UiPTZorD1wdJJLFkYOmu9WHL7szUgXAVHQKi6CsC8AmJTF5wTVbdqj88VHCXJBEqWbGBOw7dL5wLbcKW9C2owlPSd8lUctQv8d6Z5qdZ0VuxXEyjaQAIjVTNrL018AAf7vIvvjbvtQfmckEfvTiieNuPiM1qTkFwUVMMr7kKwOQM97W8KrBSjcAb8UC1CYE7dfrRKLZDzFmsQetWRrurt6GvsZogkQSlgK2kOtmAY6CaEoeYFYbciE6xDKA3zqDvJ0IwKI54rdCif59cEX7Zr4JVCUOQ5nDFjFBbWqVtpZdhMSgqMIO2PO1JQXeIKjY2c4Ye36SRhQAK97CyXyGpt7xsvuzVIgbFmMCs9hiRqmlechmXgfcabhMXKo626p9l3TvcWycVBCvjTsrwebn4oLJPSoInKa1HSYvBBXLkRREGgivMyUmnTacBqcXJ4uK9UVYZfiwBSp9lSOjkG9IwZA6zOp8mNGqZAf2KDCEDQcFJfeQR0pziGxyAEO0fQ4Wl9DTN4NCMnCL3u9c3YxNiC1dpSsQSkoChVuTtCZHSFs2G407DLRi2i1kYYpQflViYCMn7FYrPUPM9HqtqIQdLJr4GVlYmjVhvexTV1kyJSDnW5FIcnX9p9mN2I9Ype2edpYabjX8397akheuter4bgwSUSF1Okeuy0cJsL67kGWgDMVy2RBXDRSqxBDkvWORjexqbhiPcvQHfLx5bC6PEkuckkbERcDenyACU'

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

eXvx5FYG4x441BQ='8eXvx5FYG4x441BQyVElhxwNZ9q2KcW0pCa7kgcDozrVrKmAeI6JknKUVams8SWJkbNRnPvLe4lIRNh7gBf5zM9BQfyLv78RANPnFxUn573M25a2k48A0DHF9QA9xMkvS6TxuZSyT18H8MpOGZhPe4eugKy73SYUCauGOGjp8SSsnmYZvAwAhsUXk15CJWAiesIcLcJZnqcn7YL5ubv4nHaIpuo6mPBhK0jtsNzz7Volyc1lDcSi6FfT6pJ5MojrJdHvvAVtduffk8KkN6T3r3O67wyIpW0dAUMve3LK9sEApphoRHdrBRFJq04onSN46PKIYvih6Z6yF6GLG31DFLRDK5LGvnTnuINv6NjBKjUkdnspP8Onp7G66g8Ei2cMR75V0zbNnFJL4l6iP5pcbEWMWvlrfUCPjwHHTd5OZDwQGRjOM9dOzF9TTKg4QGEe0Gz6NZc7JeiJNu7C0dq79jCmI24WtHJfO5fU6XOTEHPO8MXNR0ufDQ8EzfmDXEajhc9KXbSO8YAVv0WWdZwDKFceEkC9QqXlSybPA4PLauRw2xCInXsi4M0IERWi02DV2RzbX9j1lcTAfnimIPY1JXJfjQ0J1SMfwrUwQV7tbOQ8In2g9H4NzK7eppDk1PnJ1rE7HuFj6nErqUqJ5pkVJGTs5sJ0dAbcLenLFKFeLQ71NR2LB9FQgO3jmFH224gywjOd3qkB0doN7D4K9X5nx9Fq1AEsT7IMLwz5fFdh8S1VykVWKY2OYKsRFWZjkdgHWfIpmrFu0C4FZBWpIxbcPeMpMLegRUJNwLPujYMoWvCyqUJ8Hw1k6uE9CNRzuG9VeLKilLzBeUg6fXDmESrVOhIvkkhDWh7icAkLyKykrH7X8obfgoooTZX45iDWIbDu4tHjdYmXKzBV4gxOyxDdwlm9hTQLmnGGSNTLTqTDEbJFMF7Ha8dbkEUVw3u94'

if __name__=='__main__':
	main()

NusD21s3SKhG8GPL='NusD21s3SKhG8GPLtFIEYqpkUpL6t8pQ62F8kijHg2ZE0JT2xXuOPia6z6bliivqqDow8c9rOvdIzqLq4f1zxKLvqZc12aUL4erIeBEopf4GSxNvfAXNmpd9jGktaco2MFY8cTJIYMGt9uFIvywtbPC2PtOyFW2vh2ICExGwQwC6b0NbFLun7tgVQKvxrwDoM1IAZjZC9xLOH0z3G4ZR3sKlUgx6FPjpctGFUCSTgmuy2akR3SORqj8nZaxQJSuylLLNa22SEVzviPHNW08dp1ElpRQuQdWpwsnZmUb0DruLY4FuTB229ija0qGsWw7GNvnaXcJPHlkLzX2KxowbFfRCnR99lgF5qnbpLiRTBIalzShPnJFhWQmlvc26jlw2WvBz9HLStZQjG862pODdGxvILq86s0BfcysI03J5h2P3fdfQgxd6i7TzvYAv03OlLMRUeUDwKfYaneRoJ2343GBmox6xYEG5NxvH71TIdZ4r1AFpeNlQ40bo3PFbhwpTMx73pn6WONvff41bLZcwvYcWgc8QKorEVr4QMVERu0y0CphMrT6SgkXAMVlxQrcdJyO6KkH5qHNpVlJdUvXojspqOSK2lgT3O4AzNeTnwHtgZ4yl7LDXTcfUqMlm7pN4LB7NHNdJstgAxsIHn2m6EadoSXVs4hMW2CQJi9YG5r0fLpgQzwrDk9sfRkykq1hXHgaKtPavyqaKyWyLGKf0leZUwOJUCuAhOjA6FpMfoPGJr9NAx7RVxHGwH02tyqqUYF6D5OIhpYVU3fLuEycTQek8bbwj0fakW3yJbOo6lGpFkrsoMk6VvWQfJaTFXVbxrcvZ8UtZrGLd7oo9khW9P67L3Zy1p8QrLFhN9cFxFffwuzKNEYkwYLWO3knX2jsnkte8Y2SCWUQILBjeEMe9Nms'