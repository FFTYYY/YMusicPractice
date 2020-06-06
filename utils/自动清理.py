import atexit
import os

tmp_files = []
def append_tmp_file(file_name):
	tmp_files.append(file_name)


def on_quit():
	for x in tmp_files:
		os.remove(x)

atexit.register(on_quit)