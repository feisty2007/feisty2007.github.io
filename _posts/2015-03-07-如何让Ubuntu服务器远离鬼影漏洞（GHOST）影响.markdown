---
layout: post
title:	"如何让Ubuntu服务器远离鬼影漏洞（GHOST）影响"
date:	2015-03-27 08:05:00 +0800 
categories:	系统运维 linuxcn 
tags:	[linuxcn,GHOST,安全漏洞]
---


2015年1月27日，GNU C库（glibc）的一个漏洞也称鬼影漏洞（GHOST）被公诸于众。总的来说，这个漏洞允许远程攻击者利用glibc中的GetHOST函数的缓冲区溢出漏洞来获得系统的完全控制。点击[这里](http://chargen.matasano.com/chargen/2015/1/27/vulnerability-overview-ghost-cve-2015-0235.html)获得更多细节。


鬼影漏洞可在版本在glibc-2.18之前的Linux系统上被利用。也就是说没有打过补丁的版本2.2到2.17都是有风险的。


![](/Asserts/Images//attachment/album/201503/26/150802cavgbdgbdbm9eq8b.jpg)


### 检查系统漏洞


你可以使用下面的命令来检查glib的版本



```
ldd --version

```

### 输出


ldd (Ubuntu GLIBC 2.19-10ubuntu2) **2.19** Copyright (C) 2014 Free Software Foundation, Inc. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Written by Roland McGrath and Ulrich Drepper.


glib的版本应该高于2.17，我们的输出是2.19。如果你看到glib的版本在2.2到2.17之间。你应该运行下面的命令。



```
sudo apt-get update

sudo apt-get dist-upgrade

```

安装完之后，你应该用下面的命令重启系统。



```
sudo reboot

```

重启完成之后，你可以用同样的命令来检查glib的版本。




---


via: <http://www.ubuntugeek.com/how-to-protect-ubuntu-server-against-the-ghost-vulnerability.html>


作者：[ruchi](http://www.ubuntugeek.com/author/ubuntufix) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
