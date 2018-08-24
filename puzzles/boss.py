# -*- coding: utf-8 -*-
import os
import re

def read_dir(path, fname):
	file = open(fname, 'r')
	return eval(file.read())

def list_files(path):
	return [f for f in os.listdir(path)]

def write_dir(path, fname):
	file = open(fname, 'w')
	file.write(str(list_files(path)))
	file.close()



def diff(path, fname):
	files = set(list_files(path))
	old_files = set(read_dir(path, fname))

	deleted_files = old_files.difference(files)
	new_files = files.difference(old_files)
	return (deleted_files, new_files)

path = "/Users/vn/projects/algo"


def run():
	path = raw_input("Введите путь к каталогу: ").decode('utf-8')
	fname = re.sub('/', '', path)
	if os.path.isfile(fname):
		(deleted_files, new_files) = diff(path, fname)
	
		if len(deleted_files) > 0:
			print("Удалены файлы: ")
			for file in deleted_files:
				print(file)

			print("\n")

		

		if len(new_files) > 0:
			print("Добавлены файлы: ")
			for file in new_files:
				print(file)

	write_dir(path, fname)
	


run()





# print(os.listdir("/Users/vn/Downloads"))
