from modules.频率记号对应表 import 获得记号编号 , 获得记号区间 , 去除黑键 , 从记号获得频率 , 获得最接近记号
import random
from modules.检测录音频率 import 检测录音频率 , 获取录音
from modules.播放随机波 import 播放随机波 
from utils.波处理 import 读取wav文件 , 时域转频域 , 求主导频率 , 画频率分布图
import copy
import os
import time
import sys

def 自由练习_唱_连续():
	os.system("cls")

	_stderr = sys.stderr
	sys.stderr = open(os.devnull , "w") #屏蔽stderr
	while True:

		x , f = 获取录音(0.2)

		w = 求主导频率(x , f)		
		m , diff = 获得最接近记号(w)
		print ("%s" % (m))
	sys.stderr = _stderr