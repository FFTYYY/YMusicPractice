from 练习 import 练习
from modules.频率记号对应表 import 获得记号编号 , 获得记号区间 , 去除黑键 , 从记号获得频率 , 获得最接近记号
import random
from modules.检测录音频率 import 检测录音频率 
from modules.播放随机波 import 播放随机波 
from utils.波处理 import 读取wav文件 , 时域转频域 , 求主导频率
import copy

class 看名唱音(练习):
	def __init__(self):
		super().__init__()
		self.种类 = "看名唱音"

	def init(self):

		self.刷新()
		self.难度 = self.获取选项("获取难度（默认：简单）" , [
			"简单：只有白键" , 
			"困难：有白键和黑键" , 
		] , 1)

		self.刷新()
		self.范围左 = self.获取输入("最低音（默认：C3）：" , "C3").upper()
		self.范围右 = self.获取输入("最低音（默认：B4）：" , "B4").upper()

		self.刷新()
		记号列表 = 获得记号区间(self.范围左 , self.范围右)
		if self.难度 == 1:
			记号列表 = 去除黑键(记号列表)
		print ("记号列表：{0}".format(记号列表))
		print ("【看给出的音名，把它唱出来！】".format(记号列表))
		input ("初始化完成。按回车开始！")


		self.备注 = "难度：%d ，范围：%s~%s" % (self.难度 , self.范围左 , self.范围右)

	def leave(self):
		self.刷新()
		选择 = self.获取选项("保存记录？" , ["是","否"] , 1)
		self.备注 += "『" + self.获取输入("输入备注 >> ") + "』"
		if 选择 == 1:
			self.保存()

	def entry(self):
		self.init()

		记号列表 = 获得记号区间(self.范围左 , self.范围右)
		if self.难度 == 1:
			记号列表 = 去除黑键(记号列表)

		while True:
			self.刷新()

			m = random.sample(记号列表 , 1)[0]
			f = 从记号获得频率(m)
			
			self.print("唱出这个音：%s" % m)
			self.print("录音开始...")
			self.输出()
			w = 检测录音频率(3)
			print("录音结束")

			获得记号 , _ = 获得最接近记号(w) 
			误差 = abs(w - f)

			self.刷新()
			if 获得记号 == m:
				self.正确一次(误差)
				self.print("正确！")
				self.print("你唱的音最接近于：%s" % (获得记号))
				self.print("正确的音是      ：%s" % (m))
				self.print("你唱的误差      ：%s" % (误差))
			else:
				self.错误一次(误差)
				self.print("错误！")
				self.print("你唱的音最接近于：%s" % (获得记号))
				self.print("正确的音是      ：%s" % (m))
				self.print("你唱的误差      ：%s" % (误差))

			self.输出()
			print ("")
			x = self.获取选项("接下来（默认进入下一题）：" , [
				"进入下一题" , 
				"退出" , 
			] , 1)
			if x == 2:
				break


		self.leave()



