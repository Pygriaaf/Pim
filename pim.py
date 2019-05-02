#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

file_Status = "No files"
file_Data = {} #创建文件数据库

while True:
    command = raw_input("$pim@%s>:"%(file_Status,))
    command_List = command.split() #解析命令
    if command_List[0] == "new":
        pass
    if command_List[0] == "open":
        file_Name = None
        file_Name = command_List[-1].split("\\")[-1]
        if file_Name in file_Data: #判断是否存在文件
            print"!pim:Error:This file already exists!" #抛出错误
            continue
        try:
            fileopen = open(command_List[1],'r') #打开文件
        except:
            print"!pim:Error:Can't open!" #抛出错误
            continue
        file_Status = file_Name
        fileLine_List = []
        fileInfo_List = []
        #读取文件
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
        fileInfo_List.append(command_List[1])
        fileInfo_List.append("1")
        file_Data[file_Name] = fileInfo_List
    if command_List[0] == "write":
        if command_List[1] == "-m":
            pass
        else:
            pass
    if command_List[0] == "see":
        if command_List[1] == "-n":
            i = 1
            #n = len(str(file_Data[file_Status][0]))-len(str(i))-3
            #print n
            k = " "*(len(str(len(file_Data[file_Status][0])))-len(str(i)))
            for line_for in file_Data[file_Status][0]:
                j = " "*(len(str(len(file_Data[file_Status][0])))-len(str(i)))
                print"[%s]%s|%s"%(i,j,line_for)
                i += 1
        if command_List[1] == "-l":
            if command_List[2].isdigit():
                print"!pim:Error:The parameter has an error!"
            print "[%s]|%s"%(command_List[2],file_Data[file_Status][0][command_List[2]])
    if command_List[0] == "chfi":
        if command_List[1] not in file_Data:
            print"!pim:Error:This file could not be found!"
            continue
        file_Status = command_List[1]
    if command_List[0] == "exit":
        sys.exit()
    if command_List[0] == "again": #重新启动,方便开发用
        os.system("python C:\\Users\\user\\Pim\\pim.py")
        sys.exit()
