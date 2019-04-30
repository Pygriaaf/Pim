#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

file_Status = "No files"
file_Date = {} #创建文件数据库

while True:
    command = raw_input("$pim[%s]:"%(file_Status,))
    command_List = command.split() #解析命令
    if command_List[0] == "new":
        pass
    if command_List[0] == "open":
        file_Name = None
        file_Name = command_List[-1].split("\\")[-1]
        if file_Name not in file_Date:
            print"!pim:SystemError:This file already exists!"
            continue
        else:
            file_Status = file_Name
        try:
            fileopen = open(command_List[1],'r') #打开文件
        except:
            print"!pim:FileError:Can't open!" #抛出错误
            continue
        fileLine_List = []
        fileInfo_List = []
        file_line = fileopen.readline()
        file_line = file_line[:-1]
        fileLine_List.append(file_line)
        try:
            while True:
                file_line = fileopen.next()
                file_line = file_line[:-2]
                fileLine_List.append(file_line)
        except:
            pass
        '''
        将文件存入数据库
        '''
        fileInfo_List.append(fileLine_List)
        fileInfo_List.append(command[1])
        fileInfo_List.append(int("1"))
        print fileInfo_List
    if command_List[0] == "exit":
        sys.exit()
