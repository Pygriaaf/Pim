#!/usr/bin/python
#codig=utf-8

import os
import sys

file_Status = "No files"
line_Status = "No lines"
file_Date = {} #创建文件数据库

while True:
    while True:
        command = raw_input("$pim[%s][%s]>:"%(file_Status,line_Status))
        command_List = command.split() #解析命令
        if command_List[0] == "new":
            pass
        if command_List[0] == "open":
            try:
                fileopen = open(command_List[1],'r') #打开文件
            except:
                print"!pim:FileError:Can't open!" #抛出错误
                break
            fileLine_List = []
            file_line = fileopen.readline()
            fileLine_List.append(file_line)
            try:
                while True:
                    file_line = fileopen.next()
                    fileLine_List.append(file_line)
            except:
                pass
            '''
            将文件存入数据库
            '''
            print fileLine_List
        if command_List[0] == "exit":
            sys.exit()
