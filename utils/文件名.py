import random
import os
from .自动清理 import append_tmp_file

def 随机文件名(pref = "tmp_waves/_tmp" , suf = ".wav" , 自动清理 = True):

	file_name = pref + "_" + str(random.randint(23333,2333333)) + suf

	if not os.path.exists(os.path.dirname(file_name)):
		os.makedirs(os.path.dirname(file_name) , exist_ok = True)

	if 自动清理:
		append_tmp_file(file_name)

	return file_name

