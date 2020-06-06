import wave
import numpy as np
import pdb
import matplotlib.pyplot as plt

def 读取wav文件(文件名): 
	with wave.open(文件名,"rb") as f:  
		参数 = f.getparams()  
		频道数, 采样长度, 帧率, 帧数 = 参数[:4]  
		数据 = f.readframes(帧数)  

	x = np.fromstring(数据, dtype = np.short)   
	return x , 帧率

def 时域转频域(x , f):
	'''输入一个波形，输出各个频率分量'''
	n = len(x)
	y = np.fft.fft(x , n)
	y = abs(y)

	y = y[:n//2] #只取前一半
	x = (f * np.array(range(n)) / n)[:n//2]

	# 在0附近常常有不正常的波峰，我也不知道为啥
	for i in range(50 * 5):
		y[i] = 0

	return y , x #纵坐标，横坐标

def 求主导频率(x , f):
	'''输入一段复合波形，输出主导分量的频率'''

	y , x = 时域转频域(x,f)

	best_y = np.argmax(y)
	best_x = x[best_y]

	return best_x

