#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
os.system("")
file_Status = "No Files"
file_Data = {} #创建文件数据库
print"***************************************"
print"* Pim.                                *"
print"* 2019                                *"
print"* https://www.github.com/Pygriaaf/Pim *"
print"* Debug0.1.2                          *"
print"***************************************\n"

while True:
    if not file_Data: #判断文件数据库里是否存在文件
        file_Status = "No Files"
    if file_Status in ["No Files","No Work_Files"]:
        command = raw_input("\033[1;32m$\033[0;35mpim\033[0;36m@\033[1;31m%s\033[0;37m>:\033[0m"%(file_Status,))
    else:
        command = raw_input("\033[1;32m$\033[0;35mpim\033[0;36m@\033[1;33m%s\033[0;37m>:\033[0m"%(file_Status,))
    command_List = command.split() #解析命令
    if not command_List: #当不输入命令时直接跳过
        continue
    if command_List[0] == "new":
        if len(command_List) == 1:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo parameters or options!\033[0m"
            continue
        try: #判断文件是否存在
            a = open(command_List[1],'r')
            a.close()
        except:
            pass
        else:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mFile already exists!\033[0m"
            continue
        file_Name = command_List[1].split("\\")[-1]
        if file_Name in file_Data:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThis file already exists im Pim!\033[0m"
            continue
        try:
            mkfile = open(command_List[1],'w')
        except:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mFailed to create file! Please try again.\033[0m"
            continue
        mkfile.write("\n")
        mkfile.close()
        fileInfo_List = []
        fileInfo_List.append([""]) #这里加一行是为了方便编辑
        fileInfo_List.append(command[1])
        fileInfo_List.append("1")
        file_Data[file_Name] = fileInfo_List
        file_Status = file_Name

    elif command_List[0] == "open":
        if len(command_List) == 1:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo parameters or options!\033[0m"
            continue
        file_Name = command_List[1].split("\\")[-1] 
        if file_Name in file_Data: #判断是否存在文件
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThis file already exists!\033[0m" #抛出错误
            continue
        try:
            fileopen = open(command_List[1],'r') #打开文件
        except:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mCan't open!\033[0m" #抛出错误
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
        if len(command_List) == 1:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo parameters or options!\033[0m"
            continue
        if file_Status == "No Files": #判断文件状态
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo file!\033[0m"
            continue
        if command_List[1] == "-n":
            if len(command_List) == 3:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            if file_Status == "No Work_Files":
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo working file!\033[0m"
                continue
            try:
                filesave_Open = open(file_Data[file_Status][1],'w')
            except:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mAn error occurred while processing the file!\033[0m"
                continue
            fileinfo = ""
            for file_line in file_Data[file_Status][0]: #将文件数据库里的文本按一定格式变为字符串
                file_line += "\n"
                fileinfo += file_line
            filesave_Open.write(fileinfo) #写入文件
            filesave_Open.close()
            file_Data[file_Status][2] = "1"
            filesave_Open.close()
        elif command_List[1] == "-a":
            for fileName_Key in file_Data:
                if file_Data[fileName_Key][2] == "0":
                    try:
                        filesave_Open = open(file_Data[fileName_Key][1],'w')
                    except:
                        print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mAn error occurred while processing the file!\033[0m"
                        continue
                    fileinfo = ""
                    for file_line in file_Data[fileName_Key][0]: #将文件数据库里的文本按一定格式变为字符串
                        file_line += "\n"
                        fileinfo += file_line
                    filesave_Open.write(fileinfo) #写入文件
                    filesave_Open.close()
                    file_Data[fileName_Key][2] = "1"
                    filesave_Open.close()
        else:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo such option!\033[0m"
            continue
        try:
            filesave_Open = open(file_Data[file_Status][1],'w')
        except:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mAn error occurred while processing the file!\033[0m"
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
        if len(command_List) == 1:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo parameters or options!\033[0m"
            continue
        if command_List[1] not in file_Data:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThis file could not be found!\033[0m"
            continue
        if file_Data[command_List[1]][2] == "0":
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThe file was not saved! Please save!\033[0m"
            continue
        if command_List[1] == "-a":
            for fileName_Key in file_Data:
                if file_Data[fileName_Key][2] == 0:
                    print"\033[1;31m?\033[0;35mpin:\033[1;34mclose:\033[1;37;44mSome files are not saved, do you need to save them?(Y/N)\033[0m"
                    YN = raw_input(">")
                    while True:
                        if YN.lower() == "y":
                            for fileName_Key in file_Data:
                                if file_Data[fileName_Key][2] == "0":
                                    try:
                                        filesave_Open = open(file_Data[fileName_Key][1],'w')
                                    except:
                                        print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mClosing failure!\033[0m"
                                        a = 1 #用于判断是否保存成功
                                        break
                                    fileinfo = ""
                                    for file_line in file_Data[fileName_Key][0]: #将文件数据库里的文本按一定格式变为字符串
                                        file_line += "\n"
                                        fileinfo += file_line
                                    filesave_Open.write(fileinfo) #写入文件
                                    filesave_Open.close()
                                    file_Data[fileName_Key][2] = "1"
                                    filesave_Open.close()
                        if a != 1:
                            file_Data.clear()
                        break
                        if YN.lower() == "n":
                            file_Data.clear()
                            break
                        if a == 1:
                            break
                        YN = raw_input(">")
            continue
        del file_Data[command_List[1]]
        if file_Data[command_List[1]] == file_Status:
            file_Status = "No Work_Files"

    elif command_List[0] == "see":
        if len(command_List) == 1:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo parameters or options!\033[0m"
            continue
        if file_Status == "No Files": #判断文件状态
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo file!\033[0m"
            continue
        if command_List[1] == "-n":
            if len(command_List) != 2:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            if file_Status == "No Work_Files":
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo working file!\033[0m"
                continue
            i = 1
            for line_for in file_Data[file_Status][0]:
                j = " "*(len(str(len(file_Data[file_Status][0])))-len(str(i))) #循环打印出文件内容
                print"%s[%s]|%s"%(j,i,line_for)
                i += 1
            continue
        elif command_List[1] == "-l":
            if len(command_List) != 3:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            if file_Status == "No Work_Files":
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo working file!\033[0m"
                continue
            if type(eval(command_List[2])) != int and int(command_List[2]) < 0:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThe parameter has an error!\033[0m"
                continue
            print "[%s]|%s"%(str(command_List[2]),str(file_Data[file_Status][0][int(command_List[2])-1])) #打印出某一行内容
            continue
        if command_List[1] not in file_Data:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThis file could not be found!\033[0m"
            continue
        else:
            i = 1
            for line_for in file_Data[file_Status][0]:
                j = " "*(len(str(len(file_Data[command_List[1]][0])))-len(str(i))) #与"-n"类似
                print"%s[%s]|%s"%(j,i,line_for)
                i += 1

    elif command_List[0] == "chfi":
        if len(command_List) == 1:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo parameters or options!\033[0m"
            continue
        if file_Status == "No Files":
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo file!\033[0m"
            continue
        if command_List[1] not in file_Data:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThis file could not be found!\033[0m"
            continue
        file_Status = command_List[1]

    elif command_List[0] == "write":
        if len(command_List) == 1:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo parameters or options!\033[0m"
            continue
        if file_Status == "No Files":
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo file!\033[0m"
            continue
        if file_Status == "No Work_Files":
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo working file!\033[0m"
            continue
        if command_List[1] == "-m":
            if len(command_List) == 2:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            if type(eval(command_List[2])) != int and int(command[2]) < 0: #判断参数是否正确
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThe parameter has an error!\033[0m"
                continue
            write_M_input = raw_input("\033[1;33mm\033[0m*\033[0;35mpim\033[0;36m@\033[1;33m%s\033[0;37m>:\033[0m"%(file_Status,)) #输入文本
            file_Data[file_Status][0][int(command_List[2])-1] = write_M_input
            file_Data[file_Status][2] = "0" #修改文件保存状态
            continue
        elif command_List[1] == "-nul":
            if len(command_List) > 3:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            if type(eval(command_List[2])) != int and int(command_List[2]) < 0:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThe parameter has an error!\033[0m"
                continue
            file_Data[file_Status][0].insert(int(command_List[2])-1,"") #添加空行
            file_Data[file_Status][2] = "0"
            continue
        elif command_List[1] == "-ndl":
            if len(command_List) > 3:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            if type(eval(command_List[2])) != int(command_List < 0):
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThe parameter has an error!\033[0m"
                continue
            file_Data[file_Status][0].insert(int(command_List[2]),"") #添加空行
            file_Data[file_Status][2] = "0"
            continue
        elif command_List[1] == "-dsl":
            if len(command_List) != 3:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            if type(eval(command_List[2])) != int and command_List[2] < 0:
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThe parameter has an error!\033[0m"
                continue
            file_Data[file_Status][0].pop(int(command_List[2])) #删除某一行
            file_Data[file_Status][2] = "0"
            continue
        elif command_List[1] == "-dml":
            if len(command_List) != 4 and int(command_List[2]) > int(command_List[3]) and int(command_List[2]) < 0 and int(command_List[3]) < 0:
                print len(command_List)
                print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
                continue
            del file_Data[file_Status][0][int(command_List[2])-1:int(command_List[3])] #删除多行
            continue
        else:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mNo such option!\033[0m"
            continue
        if len(command_List) != 2:
            print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mHave extra parameters!\033[0m"
            continue
        write_input = raw_input("\033[1;32w\033[0m*\033[0;35mpim\033[0;36m@\033[1;33m%s\033[0;37m>:\033[0m"%(file_Status,))
        file_Data[file_Status][0][int(command_List[1])-1] = write_input
        file_Data[file_Status][2] = "0"
        continue

    elif command_List[0] == "exit":
            exit()

    elif command_List[0] == "again": #重新启动,方便开发用
        os.system("python C:\\Users\\user\\Pim\\pim.py")
        exit()

    else:
        print"\033[1;31m!\033[0;35mpim:\033[1;31mError:\033[1;37;41mThis command could not be found!\033[0m"
        continue
