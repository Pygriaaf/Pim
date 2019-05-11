# **Pim**
> ***我不是刻意模仿Vim，而是致敬。***
***
## **前言**
### **1.我为什么要编写这个程序?**
*	提升自己的编程技术
*	作为临时的编辑器
*	希望大佬们和我交流学习
### **2.这个程序有什么特点?**
*	纯交互，纯命令，即没有快捷键
*	操作简单
***
## **使用教程**
### **一、安装**
#### **1.如何安装**
下载之后便可直接使用。
#### **2.注意事项**
由于程序是由Python2编写，所以需要安装 [Python2](https://www.python.org/downloads/release/python-2713/) 。
### **二、命令提示符**
#### **1.正常情况下**
提示符:`$pim@文件状态>:`
> 文件状态:
> 
> `No Files` 无文件
> 
> `No Work_Files` 无工作文件
>
>注：当有文件时显示文件名，即工作文件。

例:

	$pim@No Files>:
	$pim@No Work_Files>:
	$pim@test.txt>:
#### **2.write命令下**
提示符:`命令状态*pim@~>:`
>命令状态:
>
>`w`(普通编辑)
>
>`m`(修改编辑)

例:

	w*pim@test.txt>:
	m*pim@test.txt>:

#### **3.异常情况下**
提示符:`!pim:Error:详细信息`

例:

	!pim:Error:This files could not be found!
### **三、命令**
#### **1.新建文件** ##
命令:`new [要创建的文件的路径]`

例:

	$pim@No Files>:new C:\test.txt
	$pim@test.txt>:
#### **2.打开文件** ####
命令:`open [要打开文件的路径]`

例:

	$pim@No Files>:open C:\test.txt
	$pim@test.txt>:
#### **3.保存文件** ####
命令:`save [-n] [文件名]`
>`-n`:保存当前文件
>
>注：`save`后面只能使用一个参数。

例:

	$pim@test.txt>:save -n
	$pim@test.txt>:save test.py
#### **4.关闭文件** ####
命令:`close [文件名]·
>注:
>
>* 当关闭了工作文件时，文件状态会变为`No Work_Files`
>
>* 当所有文件全部关闭时，文件状态为`No Files`
>
>* 想要关闭文件，必须使文件保存。

例:

	$pim@test.txt>:close test.py
	$pim@test.txt>:close -n
	$pim@No Work_Files>:close test.md
	$pim@No Files>:
#### **5.切换工作文件** ##
命令:`chfi [文件名]`

例:

	$pim@test.txt>:chfi test.py
	$pim@test.py>:
>注:
>
>当文件状态为"No Work_Files"时就要用`chfi`命令
>
>如:
>
>     $pim@No Work_Files>:chif test.py
>     $pim@test.py>:

#### **6.编辑文本**
命令:`write <-m> <-nul> <-ndl> <-dsl> <-dml 第一个行号 第二个行号> [行号]`
>`-m`:修改编辑
>
>`-nul`:创建上一行
>
>`-ndl`:创建下一行
>
>`-dsl`:新建单行
>
>`-dml`:新建多行
>
>注:无格外参数时为普通编辑，普通编辑只能在空行里使用

例:

	$pim@test.txt>:write 1
	w*pim@test.txt>:Hello World!
	$pim@test.txt>:write -m 1
	m*pim@test.txt>:Hello Pim!
#### **7.查看文件** ####
命令:`see <-n> <-l 行号> [文件名]`
>`-n`:查看当前文件内容
>
>`-l`:查看某一行

例:

	$pim@test.txt>:see -n
	[1]|Hello World!
	[2]|Hello Pim!
	$pim@test.txt>:see -l 2
	[2]|Hello Pim!
	$pim@test.txt>:see test.py
	[1]|#!/usr/bin/python
	[2]|#coding=utf-8
	[3]|
	[4]|print"Hello World!"
	$pim@test.txt>:
***