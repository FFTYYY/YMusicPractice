import wave
import numpy as np
import pyaudio
import pdb

def 生成wav文件(x , t , 文件名):
	
	采样长度 = 2
	帧率 = int( (1. / (t[1] - t[0])) + 0.5)

	x = x.astype(np.short)

	with wave.open(文件名,"wb") as f:
		f.setnchannels(1)
		f.setsampwidth(采样长度)
		f.setframerate(帧率)

		f.writeframes(x.tostring())
 
def 播放wav文件(文件名):

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

def 生成时间(时间长度 = 3, 帧率 = 9600):
	return np.arange(0 , 时间长度 , 1 / 帧率)

def 获得波(长度 , 频率 , 振幅 = 10000 , 帧率 = 9600):
	'''
	t: 时间
	f: 频率
	A: 振幅
	'''
	t = 生成时间(长度 , 帧率)
	omega = 2 * 3.14159 * 频率
	x = np.sin(omega * t) * 振幅
	return x , t

def 振幅衰减(x , t , At = 0.2):
    '''在t结束时振幅衰减为原来的At倍

    x: 波
    t: 对应时间
    At: 末振幅
    '''
    tmax = t[-1]
    k = (At - 1) / tmax
    return x * (k * t + 1)
