#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys

file_Status = "No Files"
file_Data = {} #创建文件数据库
print"***************************************"
print"* Pim.                                *"
print"* 2019                                *"
print"* https://www.github.com/Pygriaaf/Pim *"
print"* Debug0.1                            *"
print"***************************************\n"
while True:
    if not file_Data: #判断文件数据库里是否存在文件
        file_Status = "No Files"
    command = raw_input("$pim@%s>:"%(file_Status,))
    command_List = command.split() #解析命令
    if not command_List: #当不输入命令时直接跳过
        continue
    if command_List[0] == "new":
        try:
            a = open(command_List[1],'r')
            a.close()
        except:
            pass
        else:
            print"!pim:Error:File already exists!"
            continue
        file_Name = command_List[1].split("\\")[-1]
        if file_Name in file_Data:
            print"!pim:Error:This file already exists!"
            continue
        try:
            mkfile = open(command_List[1],'w')
            mkfile.close()
        except:
            print"!pim:Error:Failed to create file! Please try again."
        fileInfo_List = []
        fileInfo_List.append([""]) #这里加一行是为了方便编辑
        fileInfo_List.append(command[1])
        fileInfo_List.append("1")
        file_Data[file_Name] = fileInfo_List
        file_Status = file_Name

    elif command_List[0] == "open":
        file_Name = command_List[1].split("\\")[-1] 
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
        file_line = fileopen.read()
        fileLine_List = file_line.split("\n") 
        '''
        将文件存入数据库
        '''
        fileInfo_List.append(fileLine_List)
        fileInfo_List.append(command_List[1])
        fileInfo_List.append("1") #这里是文件保存状态("1"为已保存,"2"为未保存)
        file_Data[file_Name] = fileInfo_List
        fileopen.close()

    elif command_List[0] == "save":
        if file_Status == "No Files": #判断文件状态
            print"!pim:Error:No file!"
            continue
        if command_List == "-n":
            if file_Status == "No Work_Files":
                print"!pim:Error:No working file!:"
                continue
            try:
                filesave_Open = open(file_Data[file_Status][1],'w')
            except:
                print"!pim:Error:An error occurred while processing the file!"
                continue
            fileinfo = ""
            for file_line in file_Data[file_Status][0]: #将文件数据库里的文本按一定格式变为字符串
                file_line += "\n"
                fileinfo += file_line
            filesave_Open.write(fileinfo) #写入文件
            filesave_Open.close()
            file_Data[file_Status][2] = "1"
            filesave_Open.close()
        #print file_Data[command_List[1]][1]
        try:
            filesave_Open = open(file_Data[file_Status][1],'w')
        except:
            print"!pim:Error:An error occurred while processing the file!"
            continue
        fileinfo = ""
        for file_line in file_Data[file_Status][0]: #将文件数据库里的文本按一定格式变为字符串
            file_line += "\n"
            fileinfo += file_line
        filesave_Open.write(fileinfo) #写入文件
        filesave_Open.close()
        file_Data[file_Status][2] = "1"
        filesave_Open.close()

    elif command_List[0] == "close":
        if command_List[1] not in file_Data:
            print"!pim:Error:This file could not be found!"
            continue
        if file_Data[command_List[1]][2] == "0":
            print"!pim:Error:The file was not saved! Please save!"
            continue
        del file_Data[command_List[1]]
        file_Status = "No Work_Files"

    elif command_List[0] == "see":
        if file_Status == "No Files": #判断文件状态
            print"!pim:Error:No file!"
            continue
        if command_List[1] == "-n":
            if file_Status == "No Work_Files":
                print"!pim:Error:No working file!:"
                continue
            i = 1
            for line_for in file_Data[file_Status][0]:
                j = " "*(len(str(len(file_Data[file_Status][0])))-len(str(i))) #循环打印出文件内容
                print"%s[%s]|%s"%(j,i,line_for)
                i += 1
            continue
        if command_List[1] == "-l":
            if file_Status == "No Work_Files":
                print"!pim:Error:No working file!:"
            try:
                if type(eval(command_List[2])) != int:
                    print"!pim:Error:The parameter has an error!"
                    continue
            except:
                print"!pim:Error:The parameters are incorrect! Please check the parameters."
                continue
            print "[%s]|%s"%(str(command_List[2]),str(file_Data[file_Status][0][int(command_List[2])-1])) #打印出某一行内容
            continue
        if command_List[1] not in file_Data:
            print"!pim:Error:This file could not be found!"
            continue
        else:
            i = 1
            for line_for in file_Data[file_Status][0]:
                j = " "*(len(str(len(file_Data[command_List[1]][0])))-len(str(i))) #与"-n"类似#<--报错
                print"%s[%s]|%s"%(j,i,line_for)
                i += 1

    elif command_List[0] == "chfi":
        if file_Status == "No Files":
            print"!pim:Error:No file!"
            continue
        if command_List[1] not in file_Data:
            print"!pim:Error:This file could not be found!"
            continue
        file_Status = command_List[1]

    elif command_List[0] == "write":
        if file_Status == "No Files":
            print"!pim:Error:No file!"
            continue
        if file_Status == "No Work_Files":
            print"!pim:Error:No working file!:"
            continue
        if command_List[1] == "-m":
            try:
                if type(eval(command_List[2])) != int: #判断参数是否正确
                    print"!pim:Error:The parameter has an error!"
                    continue
            except:
                print"!pim:Error:This file could not be found!"
            write_M_input = raw_input("m*pim@%s>:"%(file_Status,)) #输入文本
            file_Data[file_Status][0][int(command_List[2])-1] = write_M_input
            file_Data[file_Status][2] = "0" #修改文件保存状态
            continue
        if command_List[1] == "-nl":
            try:
                if type(eval(command_List[2])) != int:
                    print"!pim:Error:The parameter has an error!"
                    continue
            except:
                print"!pim:Error:This file could not be found!"
            file_Data[file_Status][0].insert(int(command_List[2]),"") #添加空行
            file_Data[file_Status][2] = "0"
            continue
        if command_List[1] == "-dl":
            try:
                if type(eval(command_List[2])) != int:
                    print"!pim:Error:The parameter has an error!"
                    continue
            except:
                print"!pim:Error:This file could not be found!"
            file_Data[file_Status][0].pop(int(command_List[2])-1) #删除某一行
            file_Data[file_Status][2] = "0"
            continue
        try:
            if type(eval(command_List[1])) != int:
                print"!pim:Error:The parameter has an error!"
                continue
        except:
            print"!pim:Error:This file could not be found!"
        if file_Data[file_Status][0][int(command_List[1])-1] != "":
            print"!pim:Error:There is text in the line and cannot be written!"
            continue
        write_input = raw_input("w*pim@%s>:"%(file_Status,))
        file_Data[file_Status][0][int(command_List[1])-1] = write_input
        file_Data[file_Status][2] = "0"
        continue

    elif command_List[0] == "exit":
            exit()

    elif command_List[0] == "again": #重新启动,方便开发用
        os.system("python C:\\Users\\user\\Pim\\pim.py")
        exit()

    else:
        print"!pim:Error:This command could not be found!"
        continue
