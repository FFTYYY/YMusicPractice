from modules.检测录音频率 import 检测录音频率 
from modules.播放随机波 import 播放随机波 
from utils.波处理 import 读取wav文件 , 时域转频域 , 求主导频率
import matplotlib.pyplot as plt
from 练习 import 练习
from 听音识名 import 听音识名
from 看名唱音 import 看名唱音
from 跟唱 import 跟唱
from 自由练习_唱 import 自由练习_唱
from 自由练习_唱_连续 import 自由练习_唱_连续
import os , sys


while True:

	os.system("cls")

	x = input("""选择练习？
0）退出
1）查看日志
2）听音识名
3）看名唱音
4）跟唱
5）自由练习（唱）
6）自由练习（唱+连续）
>> """)
	x = x.strip()
	if x == "":
		x = 1
	else:
		x = int(x)

	if x == 0:
		input("按回车退出")
		break
	elif x == 1:
		练习记录 = 练习.获得练习记录()
		print (练习记录)
		input("按回车返回")
	elif x == 2:
		练 = 听音识名()
		练.run()
	elif x == 3:
		练 = 看名唱音()
		练.run()	
	elif x == 4:
		练 = 跟唱()
		练.run()
	elif x == 5:
		自由练习_唱()	
	elif x == 6:
		自由练习_唱_连续()