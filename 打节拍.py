# TODO

import wave
import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import pdb
import threading
import time

def 获得波(t , f , A = 10000):
	'''
	t: 时间
	f: 频率
	A: 振幅
	'''
	omega = 2 * 3.14159 * f
	x = np.sin(omega * t) * A
	return x

def 振幅衰减(x , t , At = 0.2):
	'''在t结束时振幅衰减为原来的At倍

	x: 波
	t: 对应时间
	At: 末振幅
	'''
	tmax = t[-1]
	k = (At - 1) / tmax
	return x * (k * t + 1)

def 离散频谱图(t , f_and_A, prime_A = 10000):
	'''通过一个离散的频谱图来生成波
	f_and_A中给出相对振幅，最后生成的振幅会被归一化为prime_A


	t: 时间
	f_and_A: 二元组列表，每个二元组是（频率，相对振幅）
	prime_A: 基础振幅
	'''
	x = None
	sum_A = 0
	for f , A in f_and_A:
		波 = 获得波(t , f , prime_A * A)
		x = 波 if x is None else x + 波
		sum_A += A
	x /= sum_A
	return x

def 生成wav文件(x , t, 文件名 = "_gane_wav.wav", 采样长度 = 2, 帧率 = 9600):

	x = x.astype(np.short)

	with wave.open(文件名,"wb") as f:
		f.setnchannels(1)
		f.setsampwidth(采样长度)
		f.setframerate(帧率)

		f.writeframes(x.tostring())

def 生成时间(时间长度 = 3, 帧率 = 9600):
	return np.arange(0 , 时间长度 , 1 / 帧率)


def 读取wav文件(文件名 = "_gene_wave.wav"): 
	with wave.open(文件名,"rb") as f:  
		参数 = f.getparams()  
		频道数, 采样长度, 帧率, 帧数 = 参数[:4]  
		数据 = f.readframes(帧数)  

	x = np.fromstring(数据, dtype = np.short)   
	t = np.arange(0, 帧数) * (1.0 / 帧率)  
	return x , t

def 绘制wav图像(绘制帧数 = 100, 文件名 = "_gane_wav.wav"):
	x, t = 读取wav文件(文件名)
	plt.plot(t[:绘制帧数], x[:绘制帧数])
	plt.grid(True)
	plt.show()

def 播放wav文件(文件名 = "_gene_wave.wav"):

	chunk = 1024

	with wave.open(文件名,"rb") as f:
		p = pyaudio.PyAudio()
		stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
						channels = f.getnchannels(),
						rate = f.getframerate(),
						output = True)
		data = f.readframes(chunk)

		while data != b'':
			stream.write(data)
			data = f.readframes(chunk)
		stream.stop_stream()
		stream.close()
		p.terminate()

#----------datas----------

音叉_拉 = [
	(440  , 6),
	(435  , 2.5),
	(445  , 2.5),
	(430  , 1),
	(450  , 1),
	(420  , 0.5),
	(460  , 0.5),
]

#-------------------------

速度 = 75
每拍时间 = 60 / 速度
播放时间 = 0.1
绘图间隙 = 每拍时间 / 16

文件名 = "_.wav"
t = 生成时间(播放时间)
x = 离散频谱图(
	t,
	f_and_A = 音叉_拉,
)
x = 振幅衰减(x, t, 0.0)
生成wav文件(x, t , 文件名 = 文件名)


class 绘图(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.close = False
	def run(self):
		while not self.close:
			time.sleep(绘图间隙)
		print (self.close)

class 播放(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.close = False
	def run(self):
		while not self.close:
			s_time = time.time()
			播放wav文件(文件名 = 文件名)
			e_time = time.time()
			time.sleep(每拍时间 - (e_time-s_time))
		print ("播放者退出")
			
播放者 = 播放()
绘图者 = 绘图()
绘图者.start()
播放者.start()


time.sleep (5)
播放者.close = True
绘图者.close = True

绘图者.join()
播放者.join()
