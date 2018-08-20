import zipfile
 
flag = 0
 
def zipbp(zip_file,passwd):
	try:
		zip_file.extractall(pwd = passwd)
		print("[*] success! password is %s"%passwd)
		global flag
		flag = 1
	except:
		print('Sorry, %s failed'%passwd)
 
def main():
	zip_file = zipfile.ZipFile('2bs.zip')

   # for i in zip_file.infolist():
   #     print i.file_size, i.header_offset 

	for i in range(000000,999000):
		passwd = str(i).encode(encoding = 'utf-8')
		zipbp(zip_file,passwd)
		if flag == 1:
			break
 
if __name__ == '__main__':
	main()
