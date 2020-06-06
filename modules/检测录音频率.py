from utils.文件名 import 随机文件名
from utils.波处理 import 读取wav文件 , 求主导频率
from utils.音频处理 import 录音到文件
import os

def 获取录音(时长 = 3 , 频率 = 9600):
	'''从麦克风获取一段波，输出x和f'''
	file_name = 随机文件名()
	录音到文件(file_name , 时长 , 频率)
	x , f = 读取wav文件(file_name)

	return x , f

def 检测录音频率(时长 = 3):
	x , f = 获取录音(时长)
	w = 求主导频率(x , f)

	return w


if __name__ == "__main__":
	检测录音频率()
