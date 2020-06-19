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

	#在100以内有噪音
	for i in range(1000):
		if x[i] > 100:break
		y[i] = 0

	return y , x #纵坐标，横坐标

def 平滑(y , k = 10):
	for i in range(k):
		for i in range(1 , len(y)-1):
			y[i] = (y[i-1] + y[i] + y[i+1]) / 3
	return y


def 寻找波峰(y):
	ret = []
	for i in range(1 , len(y)-1):
		if (y[i] > y[i-1]) and (y[i] > y[i+1]):
			if len(ret) > 0 and abs(i - ret[-1]) < 10: #不要太近
				continue
			ret.append(i)
	return ret 



def 求主导频率(x , f):
	'''输入一段复合波形，输出主导分量的频率'''

	x = 平滑(x , 10)
	y , x = 时域转频域(x,f)
	y = 平滑(y , 10)

	波峰 = 寻找波峰(y)
	最高峰 = np.max(y[波峰])

	pos = 波峰[0]
	for p in 波峰:
		if y[p] > 最高峰/4: #至少是最高峰的1/4
			pos = p
			break

	best_x = x[pos]

	return best_x

def 画频率分布图(x , f , noise = (None,None) , lim = -1):

	nx , nf = noise

	x = 平滑(x , 10)
	y , x = 时域转频域(x,f)

	if nx is not None:
		nx = 平滑(nx , 10)
		ny , nx = 时域转频域(nx,nf)
		y -= ny

	y = 平滑(y)

	if lim > 0:
		t = 1 / (x[1] - x[0])
		x = x[:int(lim * t)]
		y = y[:int(lim * t)]
	plt.plot(x , y)
	plt.show()