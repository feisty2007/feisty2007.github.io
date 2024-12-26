---
layout: post
title:	"Linux有问必答：如何查看Linux上程序或进程用到的库"
date:	2014-08-14 11:00:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Linux有问必答,进程,库]
---


**![](/Asserts/Images//attachment/album/201408/14/235224v1parpgwqsspcaio.jpg)**



> 
> **问题**：我想知道当我调用一个特定的可执行文件在运行时载入了哪些共享库。是否有方法可以明确Linux上可执行程序或运行进程的共享库依赖关系？
> 
> 
> 


### 查看可执行程序的共享库依赖关系


要找出某个特定可执行依赖的库，可以使用ldd命令。这个命令调用动态链接器去找到程序的库文件依赖关系。



```
$ ldd /path/to/program

```

![](/Asserts/Images//attachment/album/201408/13/230339h0148vg0y0xtvv44.jpg)


注意！并不推荐为任何不可信的第三方可执行程序运行ldd，因为某些版本的ldd可能会直接调用可执行程序来明确其库文件依赖关系，这样可能不安全。


取而代之的是用一个更安全的方式来显示一个未知应用程序二进制文件的库文件依赖，使用如下命令：



```
$ objdump -p /path/to/program | grep NEEDED 

```

![](/Asserts/Images//attachment/album/201408/13/230128hszsyhz99z7s197b.png)


### 查看运行进程的共享库依赖关系


如果你想要找出被一个运行中的进程载入的共享库，你可以使用pldd命令，它会显示出在运行时被载入一个进程里的所有共享对象。



```
$ sudo pldd <PID>

```

注意你需要root权限去执行pldd命令。


![](/Asserts/Images//attachment/album/201408/13/230255vxylkh62k65073as.jpg)


或者，也可以选择一个叫做pmap的命令行工具。它报告一个进程的内存映射，也能显示出运行进程的库文件依赖。



```
$ sudo pmap <PID>

```

![](/Asserts/Images//attachment/album/201408/13/230346lbtzsw7wltonnbgl.jpg)




---


via: <http://ask.xmodulo.com/check-library-dependency-program-process-linux.html>


译者：[KayGuoWhu](https://github.com/KayGuoWhu) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
