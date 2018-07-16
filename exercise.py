
import glob

#获取指定目录下的所有图片
print (glob.glob(r"/home/qiaoyunhao/*/*.png"))#加上r让字符串不转义

#获取上级目录的所有.py文件
print (glob.glob(r'../*.py')) #相对路径