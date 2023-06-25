import ResEncryptor as r
print(r.VERSION)

if __name__=='__main__':
	version=''
	version+=f"# {r.VERSION['appNameCN']}\n"
	for v in r.VERSION['versionUpdate']:
		version+=f"- {v['mainVersion']} {v['dateVersion']}\n"
		for u in v['versionDesc']:
			if u!='':
				version+=f"  - {u}\n"
	
	r.writeFile('VERSION.md',version)
	print('输出完成！')
	r.wait(3)