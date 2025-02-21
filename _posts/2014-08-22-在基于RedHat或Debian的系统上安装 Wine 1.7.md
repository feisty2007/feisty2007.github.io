---
layout: post
title:	"在基于RedHat或Debian的系统上安装 Wine 1.7"
date:	2014-08-30 21:17:55 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,WINE]
---


Wine,Linux上最流行也是最有力的软件, 可以顺利地在Linux平台上运行Windows程序和游戏。


![安装Wine ](/Asserts/Images/album/201408/30/211803yk7vlgkajllblkug.png)


这篇文章教你怎么在像CentOS, Fedora, Ubuntu, Linux Mint一样基于**Red Hat**和**Debian**的系统上安装最新的**Wine 1.7**。


### 在Linux安装 Wine 1.7


不幸的, 在基于**Red Hat**的系统上没有官方的 Wine 仓库，所以唯一的安装方式是从源码编译。你需要安装一些依赖的包比如gcc, flex, bison, libX11-devel freetype-devel 和 Development Tools，这些包用来从源码编译Wine。我们可以用**yum**命令安装他们。


#### 在 RedHat, Fedora 和 CentOS 上



```
# yum -y groupinstall 'Development Tools'
# yum -y install flex bison libX11-devel freetype-devel

```

接下来，下载最新的开发版本(如**1.7.21**)并用下面的命令解压。



```
$ cd /tmp
$ wget http://citylan.dl.sourceforge.net/project/wine/Source/wine-1.7.21.tar.bz2
$ tar -xvf wine-1.7.21.tar.bz2 -C /tmp/

```

现在，要以普通用户身份编译并搭建Wine的安装程序。(**注意**: 根据机器性能和网络速度的不同，安装过程需要 **15-20** 分钟，安装过程中会要求输入 **root** 密码。)


**32位系统上**



```
$ cd wine-1.7.21/
$ ./tools/wineinstall

```

**64位系统上**



```
$ cd wine-1.7.21/
$ ./configure --enable-win64
$ make
# make install

```

#### 在Ubuntu, Debian 和 Linux Mint 上


在基于**Ubuntu** 的系统上, 你可以用官方的 **PPA**来轻松安装最新的Wine。打开一个新终端用sudo运行如下命令。



```
$ sudo add-apt-repository ppa:ubuntu-wine/ppa 
$ sudo apt-get update
$ sudo apt-get install wine 1.7 winetricks

```

一旦装完了，你可以以如下方式运行基于Windows的软件和游戏。



```
$ wine notepad
$ wine notepad.exe 
$ wine c:\\windows\\notepad.exe

```

**注意**: 请记住，如果是开发版本不要用在生产环境。 建议只用在测试用途


如果你想安装最近的稳定版Wine, 请看下面的文章, 在文章里介绍了在几乎所以Linux系统中安装Wine的方法


* [Install Wine 1.6.2 (Stable) in RHEL, CentOS and Fedora](http://www.tecmint.com/install-wine-in-rhel-centos-and-fedora/)
* [Install Wine 1.6.2 (Stable) in Debian, Ubuntu and Mint](http://www.tecmint.com/install-wine-on-ubuntu-and-linux-mint/)


### 参考链接


* [WineHQ Homepage](http://www.winehq.org/)




---


via: <http://www.tecmint.com/install-wine-in-linux/>


译者：[2q1w2007](https://github.com/2q1w2007) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
