from utils.播放波 import 获得波 , 生成wav文件 , 播放wav文件 , 振幅衰减
from utils.文件名 import 随机文件名
import os
import random
import pdb

def 播放波(x , t):
	x = 振幅衰减(x , t , 0.2)
	file_name = 随机文件名()
	生成wav文件(x , t , file_name)
	播放wav文件(file_name)

def 生成随机波(主导频率 , 长度):
	基础振幅 = 12000

	总振幅 = 1
	x , t = 获得波(长度 , 主导频率 , 1)

	k = random.randint(1 , 5)
	for i in range(k):
		振幅 = random.random()* 0.2

		乘或除 = random.randint(0,1) * 2 - 1 #指数
		倍数 = (random.randint(3,9)/2)
		振幅 = 振幅 / 倍数 #离他越远，就越小
		倍数 = 倍数 ** 乘或除
		频率 = 主导频率 * 倍数
		#频率 = random.randint(主导频率 // 3 , 主导频率 * 3)
		_x , _ = 获得波(长度 , 频率 , 振幅)
		
		x = x + _x
		总振幅 = 总振幅 + 振幅
	print (总振幅)

	x = x / 总振幅 #振幅归一
	x = x * 基础振幅 #调整振幅

	return x , t

def 播放随机波(主导频率 , 长度):
	x , t = 生成随机波(主导频率 , 长度)
	播放波(x , t)
