---
layout:   post
title:    "Linux 统计目录下文件数量的方法"
crawlertitle: "Linux 统计目录下文件数量的方法"
description:  "Linux 统计目录下文件数量的方法"
summary:  "Linux 统计目录下文件数量的方法"
date: 2022-3-31 13:49:55
categories:   软件
tags: [软件]
author:   "feisty2007"
---

1、统计当前目录下文件的个数（不包括目录）

	ls -l | grep "^-" | wc -l
2、统计当前目录下文件的个数（包括子目录）

	ls -lR| grep "^-" | wc -l
3、查看某目录下文件夹(目录)的个数（包括子目录）

	ls -lR | grep "^d" | wc -l
4、统计当前文件夹下叫某某的文件的数量

	find . -name filename | wc -l
5、统计当前文件夹下指定类型的文件的数量

例如这里需要找 js 文件的数量：

	find -name "*.js" | wc -l
这里再对使用到的 3 个命令做个介绍。

1、ls -l

长列表输出该目录下文件信息(注意这里的文件是指目录、链接、设备文件等)，每一行对应一个文件或目录，ls -lR 是列出所有文件，包括子目录。

2、grep “^-”

过滤ls的输出信息，只保留一般文件，只保留目录是 grep “^d”。

3、wc -l

统计输出信息的行数，统计结果就是输出信息的行数，一行信息对应一个文件，所以就是文件的个数。
