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
>w(普通编辑)
>
>m(修改编辑)

例:

	w*pim@test.txt>:
	m*pim@test.txt>:

#### **3.异常情况下**
提示符:`!pim:Error:详细信息`

例:

	!pim:Error:This files could not be found!
