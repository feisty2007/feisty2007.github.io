---
layout: post
title:	"Linux 有问必答：如何修复 Raspbian 上的 “Encountered a section with no Package:"
date:	2015-06-14 10:39:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,树莓派,Raspbian]
---



> 
> **问题**: 我在树莓派上安装新版的 Raspbian。但当我使用 sudo apt-get update 命令更新 APT 软件包索引的时候，它抛出下面的错误：
> 
> 
> 



```
E: Encountered a section with no Package: header
E: Problem with MergeList /var/lib/dpkg/status
E: The package lists or status file could not be parsed or opened.

```


> 
> 之后我不能在 Raspbian 上安装任何软件包。我怎样才能解决这个错误？
> 
> 
> 


![](/Asserts/Images/album/201506/13/234143be64iis6d4dzzosr.jpg)


这个错误说 "Problem with MergeList /var/lib/dpkg/status" 表示由于某些原因状态文件损坏了，因此无法解析。这个状态文件包括了已经安装的 deb 软件包的信息，因此需要小心备份。


在这种情况下，由于这是新安装的 Raspbian，你可以安全地删除状态文件，然后用下面的命令重新生成。



```
$ sudo rm /var/lib/dpkg/status
$ sudo touch /var/lib/dpkg/status
$ sudo apt-get update 

```



---


via: <http://ask.xmodulo.com/encountered-section-with-no-package-header-error.html>


作者：[Dan Nanni](http://ask.xmodulo.com/author/nanni) 译者：[ictlyh](https://github.com/ictlyh) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](https://linux.cn/) 荣誉推出
