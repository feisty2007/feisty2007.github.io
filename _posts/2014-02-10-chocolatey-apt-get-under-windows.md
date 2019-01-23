---
layout: post
title: "Windows环境下的apt-get:Chocolatey"
description: ""
category: Blog 
tags: [Windows,Chocolatey]
---

Chocolatey是一个软件包管理工具，类似于Ubuntu下面的`apt-get`,不过是运行在Windows环境下面。

####安装

Chocolatey的安装需要：

1. Powershell

2. Internet链接

下面的操作在Windows 7上面应该是没有问题的。以“管理员方式”打开一个命令行工具，输入下面的命令：

	@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%systemdrive%\chocolatey\bin

经过一段时间的等待，Chocolatey安装完毕。

####使用

举个栗子，你如果想安装7Zip，你可以在命令行输入：

	cinst 7Zip

就会自动安装这个压缩软件。

安装Node.js,输入：

	cinst node.js

另外还可以安装IE10（Windows 7）：

	cinst IE10

安装Visual Studio 2013 Ultimate这个巨无霸也是可以的：

	cinst VisualStudio2013Ultimate

软件列表，可以在[Chocolatey的软件索引](https://chocolatey.org/packages "Chocolatey的软件索引")查到。


