from 练习 import 练习
from modules.频率记号对应表 import 获得记号编号 , 获得记号区间 , 去除黑键 , 从记号获得频率 , 获得最接近记号
import random
from modules.检测录音频率 import 检测录音频率 
from modules.播放随机波 import 播放随机波 
from utils.波处理 import 读取wav文件 , 时域转频域 , 求主导频率
import copy

class 听音识名(练习):
	def __init__(self):
		super().__init__()
		self.种类 = "听音识名"

	def init(self):

		self.刷新()
		self.难度 = self.获取选项("获取难度（默认：简单）" , [
			"简单：只有白键" , 
			"困难：有白键和黑键" , 
		] , 1)

		self.刷新()
		self.范围左 = self.获取输入("最低音（默认：C4）：" , "C4").upper()
		self.范围右 = self.获取输入("最低音（默认：B5）：" , "B6").upper()

		self.刷新()
		记号列表 = 获得记号区间(self.范围左 , self.范围右)
		if self.难度 == 1:
			记号列表 = 去除黑键(记号列表)
		print ("记号列表：{0}".format(记号列表))
		print ("【听给出的音，选择音名】".format(记号列表))
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
			self.输出()

			m = random.sample(记号列表 , 1)[0]
			f = 从记号获得频率(m)
			
			播放随机波(f , 3)

			伪列表 = copy.copy(记号列表)
			伪列表.remove(m)
			选项 = random.sample(伪列表 , 3) + [m]
			random.shuffle(选项)

			选择 = self.获取选项("听录音，选择唱名" , 选项 , 1)
			选择 = 选项[选择-1]

			self.刷新()
			if 选择 == m:
				self.正确一次()
				self.print("正确！")
				self.print("选择答案：%s" % (选择))
				self.print("正确答案：%s" % (m))
			else:
				self.错误一次()
				self.print("错误！")
				self.print("选择答案：%s" % (选择))
				self.print("正确答案：%s" % (m))
			self.输出()

			print ("")
			x = self.获取选项("接下来（默认进入下一题）：" , [
				"进入下一题" , 
				"退出" , 
			] , 1)
			if x == 2:
				break

		self.leave()



