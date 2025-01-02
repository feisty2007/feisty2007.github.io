---
layout: post
title:	"Linux 有问必答：如何在debian及其衍生发行版中改变默认的 Java 版本"
date:	2015-11-16 08:05:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,java]
---



> 
> **提问**：当我尝试在Linux中运行一个Java程序时，我遇到了一个错误。看上去像程序编译所使用的Java版本与我本地的不同。我该如何在Linux上切换默认的Java版本？
> 
> 
> 


当Java程序编译时，编译环境会设置一个“target”变量来设置程序可以运行的最低Java版本。如果你Linux系统上运行的程序不能满足最低的JRE版本要求，那么你会在运行的时候遇到下面的错误。



```
Exception in thread "main" java.lang.UnsupportedClassVersionError: com/xmodulo/hmon/gui/NetConf : Unsupported major.minor version 51.0

```

比如，程序在Java JRE 1.7下编译，但是系统只有Java JRE 1.6。


![](/Asserts/Images/album/201511/16/001124yixixswnwri0kryr.jpg)


要解决这个问题，你需要改变默认的Java版本到Java JRE 1.7或者更高（假设JRE已经安装了）。


首先，试用下面的update-alternatives命令**检查你系统上可用的Java版本**：



```
$ sudo update-alternatives --display java

```

![](/Asserts/Images/album/201511/16/001134bkktx3x859cscu5f.jpg)


本例中，总共安装了4个不同的Java版本：OpenJDK JRE 1.6、Oracle Java JRE 1.6、OpenJDK JRE 1.7 和 Oracle Java JRE 1.7。现在默认的Java版本是OpenJDK JRE 1.6。


如果没有安装需要的Java JRE，你可以参考[这些指导](http://ask.xmodulo.com/install-java-runtime-linux.html)来完成安装。


现在有可用的候选版本，你可以用下面的命令在可用的Java JRE之间**切换默认的Java版本**：



```
$ sudo update-alternatives --config java

```

看到提示的时候，选择你想试用的Java版本。本例中，我们选择Oracle Java JRE 1.7。


![](/Asserts/Images/album/201511/16/001134edxwy2dd9l9ya2tw.jpg)


现在用下面的命令验证默认的Java版本。



```
$ java -version

```

![](/Asserts/Images/album/201511/16/001135i0aq1cwjxt5wj9qj.jpg)


最后，如果你定义了JAVA\_HOME环境变量，根据你设置的Java版本更新变量。




---


via: <http://ask.xmodulo.com/change-default-java-version-linux.html>


作者：[Dan Nanni](http://ask.xmodulo.com/author/nanni) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
