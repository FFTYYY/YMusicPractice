import pickle
import os , sys
from YTools.universe import beautiful_str
from YTools.universe.strlen import len_ignore_n
import time
import pdb

class 练习:
	def __init__(self):
		self.种类 = ""
		self.时间 = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
		self.正确次数 = 0
		self.总次数 = 0
		self.备注 = ""
		self.平均误差 = 0

		self.print_buf = []
	def print(self , *x):
		self.print_buf.append(" ".join(x))

	def 输出(self , 额外输出 = [] , 固定位置 = 100):

		固定输出 =[
			"备注    │ {0}".format(self.备注) , 
			"正确次数│ {0}".format(self.正确次数) , 
			"总次数  │ {0}".format(self.总次数) , 
			"正确率  │ {0}".format(self.正确次数 / self.总次数 if self.总次数 != 0 else 0) , 
			"平均误差│ {0}".format(self.平均误差) , 
		]

		for i in range(len(固定输出)):
			b = 固定输出[i]
			if len(self.print_buf) > i:
				a = self.print_buf[i]
			else:
				a = ""
			s = a + " " * (固定位置 - len_ignore_n(a)) + b
			print (s)

		for i in range(len(固定输出) , len(self.print_buf)):
			print (self.print_buf[i])

		self.print_buf = []


	def 正确一次(self , 误差 = 0):
		self.平均误差 = (self.平均误差 * self.总次数 + 误差) / (self.总次数 + 1)
		self.正确次数 += 1
		self.总次数 += 1

	def 错误一次(self , 误差 = 0):
		self.平均误差 = (self.平均误差 * self.总次数 + 误差) / (self.总次数 + 1)
		self.总次数 += 1

	def run(self):
		self.entry()

	def entry(self):
		pass

	def 刷新(self):
		os.system("cls")

	def 获取输入(self , 提示 , 默认 = ""):
		x = input(提示).strip()
		if x == "":
			x = 默认
		return x

	def 获取选项(self , 提示 , 选项列表 , 默认项 = 0):
		print (提示)
		for i in range(len(选项列表)):
			print ("%d) %s" % (i+1 , str(选项列表[i])))

		inp = -1
		while inp <= 0 or inp > len(选项列表):
			x = input(">> ").strip()
			if x == "":
				inp = 默认项
			else:
				inp = int(x)
		return inp

	def 保存(self , file_name = "_save.pkl"):

		if not os.path.exists(file_name):
			练习列表 = []
		else:
			with open(file_name , "rb") as fil:
				练习列表 = pickle.load(fil)

		练习列表.append(self)
		with open(file_name , "wb") as fil:
			pickle.dump(练习列表 , fil)

		return 练习列表

	def 获得练习记录(file_name = "_save.pkl"):
		if not os.path.exists(file_name):
			练习列表 = []
		else:
			with open(file_name , "rb") as fil:
				练习列表 = pickle.load(fil)
		练习列表.reverse()

		info = beautiful_str( ["种类" , "时间" , "正确次数" , "总次数" , "正确率" , "平均误差" , "备注"] , 
			[
				[x.种类 , x.时间 , x.正确次数 , x.总次数 , x.正确次数/x.总次数 , x.平均误差 , x.备注]
				for x in 练习列表
			]
		)

		return info


