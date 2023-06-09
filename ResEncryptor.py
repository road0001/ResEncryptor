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

VERSION={
"appName":"ResEncryptor",
"versionUpdate":[
{
	"mainVersion":"1.0",
	"dateVersion":"20230609",
	"versionDesc":[
		"加入自动清理压缩包功能（移入回收站）。",
		"加入在找不到配置文件时，手动输入配置文件名功能。",
		"将字符串中format引用变量的方法改为f''。",
	""]
},
{
	"mainVersion":"1.0",
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
'''
Configs
'''
# 输出目录
outputDir=f'{os.getcwd()}\\output'
# 分卷范围（此范围是压缩前的分卷范围，压缩后的情况不可知）
volumeRange=[20,50]
# 默认盐，和配置文件加解密有关，不可随便更换，否则不兼容其他版本
defaultSalt='KnWn7ZYSa309KyYnruB0JXF9zIRAsQNx'
# 配置文件名
configName=hashlib.md5(f'config{defaultSalt}'.encode(encoding='utf-8')).hexdigest()
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
		'fileList':[]
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
	return encryptKey

def makeOutputDir(addr):
	dirs=f'{outputDir}\\{addr}'
	if not exist(dirs):
		os.makedirs(dirs)
	return dirs

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
		volumeSize=int(targetFileData['fileSize'] / volumeCount)
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

def main():
	os.system('cls')
	if len(sys.argv)<2:
		os.system(f"title 资源解密解压工具 v{VERSION['versionUpdate'][0]['mainVersion']} Build {VERSION['versionUpdate'][0]['dateVersion']}")
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
		os.system(f"title 资源加密压缩工具 v{VERSION['versionUpdate'][0]['mainVersion']} Build {VERSION['versionUpdate'][0]['dateVersion']}")
		out.outlnC('-=<欢迎使用资源加密压缩工具！>=-','purple','black',1)
		out.outlnC('请只拖入一个文件或文件夹！','red','black',1)
		out.outln('按任意键退出。')
		pause()
		return 0
	else:
		os.system(f"title 资源加密压缩工具 v{VERSION['versionUpdate'][0]['mainVersion']} Build {VERSION['versionUpdate'][0]['dateVersion']}")
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

if __name__=='__main__':
	main()