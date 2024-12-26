---
layout: post
title:	"在 Linux 下用 mkdir 命令来创建目录和子目录"
date:	2014-03-19 11:31:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Linux,mkdir,目录]
---


了解了用 ls 命令在目录中列出条目后，现在我们要学习在 Linux 系统下创建目录。在 Linux 下，我们可以使用 **mkdir** 命令。Mkdir 是“make directory” 的缩写词。


![](/Asserts/Images//attachment/album/201403/19/113731gzar99fddba09uq3.gif)


### mkdir 是什么呢


Mkdir 是一个用来在 Linux 系统下创建目录的命令。此命令属于内建命令。


### 运行 mkdir 命令


你可以在你的控制台直接键入 **mkdir** 来使用它。



```
$ mkdir

```

默认情况下，不带任何参数运行 mkdir 命令会在当前目录下创建目录。下面是参考示例：


![mkdir command](/Asserts/Images//attachment/album/201403/19/113120i9olvlo35ytq8y51.png)


从上图看出，我们创建了名为 **office** 的目录。当我们运行 mkdir 命令时，我们位于 **/home/pungki** 目录。所以这个新目录 office **创建在/home/pungki**目录下。**如果我们使用绝对路径** - 例如：**/usr/local** - , 则 Linux 会在 **/usr/local**目录下创建一个目录。


当 Linux 发现想要创建的目录已经存在, 那么 Linux 会提示我们 Linux 无法创建它。


![mkdir directory exist](/Asserts/Images//attachment/album/201403/19/113121x32kn1nz58i3zhn8.png)


另外一个创建目录的首要条件是， **在想要创建目录的目标路径下你必须具有访问权限**。当你无法取得权限时 mkdir 会报告这个错误。


![mkdir permission denied](/Asserts/Images//attachment/album/201403/19/113122n0yd9y4zmmfmuvff.png)


### 创建多个目录


我们也可以同时创建多个目录。比如我们要创建的目录有 **ubuntu, redhat 和 slackware**。那么语法会像这样子:



```
$ mkdir ubuntu redhat slackware

```

![create multiple directories](/Asserts/Images//attachment/album/201403/19/113123mti5fi5e550pwth5.png)


### 添加包含子目录的目录 [译注：递归地创建目录]


当你要创建的目录包含子目录时，你需要使用 -p 参数。如果 mkdir 找不到父目录，那么这个参数会首先帮助创建父目录。比如说我们要创建名为 **letter** 的目录，在它的目录下包含有子目录 **important**。那么语法会像这样子：



```
$ mkdir -p letter/important
```

![mkdir sub-directory](/Asserts/Images//attachment/album/201403/19/113125e1k7hc9wgbwqyjuk.png)


### 设置访问权限


使用 **-m** 参数，我们可以给即将生成的新目录设置权限。示例如下：



```
$ mkdir -m=r-- letter
```

上面的命令会创建一个名为 letter 的目录，同时为**目录所有者、用户组和其他用户**针对该目录赋予**只读权限**


![mkdir set privilege](/Asserts/Images//attachment/album/201403/19/113126pwxmqw5xxhiwtaih.png)


### 打印创建目录的过程信息


如果我们要查看信息，我们可以使用 **-v** 参数来实现。示例如下：



```
$ mkdir -v ubuntu redhat slackware
```

![mkdir verbose](/Asserts/Images//attachment/album/201403/19/113127ar5led790p5u7u0m.png)


### 总结


Mkdir 命令也属于一个最基础的命令，对于想要学习 Linux 的朋友这个命令必须掌握。像往常一样，你可以键入**man mkdir**或**mkdir --help**来显示 mkdir 的手册页面和更加深入的探讨。




---


via: <http://linoxide.com/linux-command/linux-mkdir-command/>


译者：[Luoxcat](https://github.com/Luoxcat) 校对：[Mr小眼儿](http://blog.csdn.net/tinyeyeser)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
