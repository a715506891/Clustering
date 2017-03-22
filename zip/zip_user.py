#/usr/bin/python
#coding=utf-8
import os,sys  
import zipfile 
open_path='e:\\data'
save_path='e:\\data' 
os.chdir(open_path)#转到路径
#首先，通过zipfile模块打开指定位置zip文件
#传入文件名列表，及列表文件所在路径，及存储路径
def Decompression(files,file_path,save_path):
	os.getcwd()#当前路径
	os.chdir(file_path)#转到路径
	for file_name in files:
		print(file_name)
		r = zipfile.is_zipfile(file_name)#判断是否解压文件
		if r:
			zpfd = zipfile.ZipFile(file_name, mode='r')#读取压缩文件
			for filename in zpfd.namelist():#获取解压文件中的所有文件名
				print(filename)
				tmpcont = zpfd.read(filename)#读取文件内容,结果为bytes
				content=str(tmpcont,encoding='GBK')#将内容改为str
				os.chdir(save_path)#转到存储路径
				with open(filename,"w") as f:#文件处理，打开写入，使用with，处理异常，权柄关闭
					f.write(content)#写入文件内容

def files_save(open_path):
	for file_path,sub_dirs,files in os.walk(open_path):#获取所有文件名
		print(file_path,sub_dirs,files)
		Decompression(files,file_path,save_path)

files_save(open_path)
'''
可以得到一个三元tupple(dirpath,sub_dirs, filenames)，
其中第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
'''