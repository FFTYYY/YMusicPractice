from modules.频率记号对应表 import 获得记号编号 , 获得记号区间 , 去除黑键 , 从记号获得频率 , 获得最接近记号
import random
from modules.检测录音频率 import 检测录音频率 , 获取录音
from modules.播放随机波 import 播放随机波 
from utils.波处理 import 读取wav文件 , 时域转频域 , 求主导频率 , 画频率分布图
import copy
import os
import time

def 自由练习_唱():
	os.system("cls")
	while True:
		x = input("选择操作（默认1）\n"
			"1)开始录音\n" + 
			"2)退出\n" + 
			">> "
		).strip()
		if x == "":
			x = 1
		if int(x) == 2:
			break

		x , f = 获取录音(1)

		#画频率分布图(x , f , lim = 800)

		w = 求主导频率(x , f)
		print ("你唱的频率是：%.2fHz" % w)
		
		m , diff = 获得最接近记号(w)
		print ("最接近的琴键是：%s (%.2fHz)，差距是%.2fHz" % (m , 从记号获得频率(m) , diff))



		print ("------------------------------------------------")