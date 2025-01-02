---
layout: post
title:	"Linux/Unix 桌面趣事：让桌面下雪"
date:	2015-12-25 14:48:00 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,xsnow]
---


在这个节日里感到孤独么？试一下 Xsnow 吧。它是一个可以在 Unix/Linux 桌面下下雪的应用。圣诞老人和他的驯鹿会在屏幕中奔跑，伴随着雪片让你感受到节日的感觉。


我第一次安装它还是在 13、4 年前。它最初是在 1984 年 Macintosh 系统中创造的。你可以用下面的方法来安装：


### 安装 xsnow


Debian/Ubuntu/Mint 用户用下面的命令：



```
$ sudo apt-get install xsnow

```

Freebsd 用户输入下面的命令：



```
# cd /usr/ports/x11/xsnow/
# make install clean

```

或者尝试添加包：



```
# pkg_add -r xsnow

```

#### 其他发行版的方法


1. Fedora/RHEL/CentOS 在 [rpmfusion](http://rpmfusion.org/Configuration) 仓库中找找。
2. Gentoo 用户试下 Gentoo portage，也就是[emerge -p xsnow](http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2&chap=1)
3. Opensuse 用户使用 yast 搜索 xsnow


### 我该如何使用 xsnow？


打开终端（程序 > 附件 > 终端），输入下面的额命令启动 xsnow：



```
$ xsnow

```

示例输出:


![](/Asserts/Images/album/201512/25/144759v3z84b28bmdhkhmk.jpg)


*图01: 在 Linux 和 Unix 桌面中显示雪花*


你可以设置背景为蓝色，并让它下白雪，输入：



```
$ xsnow -bg blue -sc snow

```

设置最大的雪片数量，并让它尽可能快地掉下，输入：



```
$ xsnow -snowflakes 10000 -delay 0

```

不要显示圣诞树和圣诞老人满屏幕地跑，输入：



```
$ xsnow -notrees -nosanta

```

关于 xsnow 更多的信息和选项，在命令行下输入 man xsnow 查看手册：



```
$ man xsnow

```

建议阅读


* 官网[下载 Xsnow](http://rpmfusion.org/Configuration)
* 注意 [MS-Windows](http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2&chap=1) 和 [Mac OS X](http://dropmix.xs4all.nl/rick/Xsnow/) 版本有一次性的共享软件费用。




---


via: <http://www.cyberciti.biz/tips/linux-unix-xsnow.html>


作者：Vivek Gite 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
