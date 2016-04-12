#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lisa.py
#  
#  Copyright 2015 Arkadiy <arkadiy@arkadiy-SVE1511T1RW>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import shutil
import time
import sys

def sort_by_ext(files, directory):
	
	for i in files:
		ext = os.path.splitext(i)
		if ext[1] != '':
			dst_dir = os.path.join(directory, ext[1][1:])
			if os.path.exists(dst_dir) == False: 
				os.mkdir(dst_dir)
		
			shutil.move(os.path.join(directory, i), os.path.join(dst_dir, i))
			print ('{} ==> {}'.format(os.path.join(directory, i), os.path.join(dst_dir, i)))
	return 0
			
def sort_by_date(files, directory):
	for i in files:
		abs_path = os.path.join(directory, i)
		if os.path.isdir(abs_path) == False:
			acc_time = time.gmtime(os.path.getmtime(abs_path))
			file_time_year = time.strftime('%Y', acc_time)
			file_time_month = time.strftime('%B', acc_time)
			
			dst_dir_year = os.path.join(directory, file_time_year)
			dst_dir_month = os.path.join(dst_dir_year, file_time_month)
			if os.path.exists(dst_dir_year) == False: 
				os.mkdir(dst_dir_year)
			if os.path.exists(dst_dir_month) == False: 
				os.mkdir(dst_dir_month)
			
			shutil.move(os.path.join(directory, i), os.path.join(dst_dir_month, i))
			print ('{} ==> {}'.format(abs_path,os.path.join(dst_dir_month, i)))
			
	return 0
	
def input_dir():
	args = sys.argv[1:]
	if not args:
		print('usage: [--sort dir]')
		sys.exit(1)

	if args[0] == '--sort':
		if os.path.exists(os.path.join(os.getcwd(), args[1])) == False and os.path.exists(args[1]) == False:
			print ('Sorry. This directory is not found!')
			exit(1) 
		directory = os.path.join(os.getcwd(), args[1])
		#del args[0:2]
	return directory	

def out_file_dir(files):
	user_input = input('Output list files in directory? y/n \n')
	if user_input == 'y':
		print ('List files in derectory')
		for i in files:
			print (i)
	return 0

def main():
	directory = input_dir()
	files = os.listdir(directory)
	
	out_file_dir(files)

	while True:
		input_mode = input('How sorted files? \n 1 - By date \n 2 - By extension \n 0 - Exit\n')
		if input_mode == '1':
			sort_by_date(files, directory)
			exit(0)
		if input_mode == '2':
			sort_by_ext(files, directory)
			exit(0)
		if input_mode == '0':
			exit(0)
	
	return 0

if __name__ == '__main__':
	main()

