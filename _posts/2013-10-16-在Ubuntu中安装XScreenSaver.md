---
layout: post
title:	"在Ubuntu中安装XScreenSaver"
date:	2013-10-14 21:37:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Linux,Ubuntu,安装,XScreenSaver,技巧,教程]
---


这个教程将会给你展示如何在Ubuntu 12.04(也包含其他Ubuntu版本)中加入屏幕保护，它们原本不包含X-windows屏幕保护程序。不过，一些对计算机或linux不熟悉的人，并不了解屏幕保护。到底屏幕保护能做什么呢?


屏幕保护是一个主要用于安全用途的计算机程序（译注：和最初屏幕保护的用途不同了）。当计算机空闲时，这个程序会清空屏幕或者在屏幕上填满移动的图片或图样。屏幕保护也可以用于娱乐或显示系统信息。当你打算离开办公室又不想让任何人看你电脑上的信息时，屏保程序将是绝佳的解决方案。


**屏幕保护怎么让我的电脑变得更安全？**


屏幕保护能配置成在允许用户继续工作之前要求用户输入密码。但是请留意，如果设置为在启动机器后自动登入帐号，那么攻击者可以轻易的重启机器来登入你的帐号。


**怎么安装屏幕保护？**


打开一个新的终端(ctrl+alt+T)，如图一所示。


![](/Asserts/Images/album/201310/14/105837l53dln5xbjp77l34.png) 


图一


在安装一个新的屏幕保护之前我们必须卸载默认屏幕保护，运行 'sudo apt-get remove gnome-screensaver' ，见图二。


![](/Asserts/Images/album/201310/14/105839z8cv2ooi6kkz4o77.png)


图二


用下列命令安装XScreenSaver和一些附加的屏保包。 sudo apt-get install xscreensaver xscreensaver-data-extra xscreensaver-gl-extra


![](/Asserts/Images/album/201310/14/1058425vnjatlttc2c7a45.png)


图三


![](/Asserts/Images/album/201310/14/105845xyuylj2vr345yiim.png)


图四


![](/Asserts/Images/album/201310/14/105847o969gxppxhp99ceo.png)


图五


XScreenSaver 每次启动后会随机选择一个屏幕保护.预了解如何配置XScreenSaver，参见[这里](http://www.jwz.org/xscreensaver/faq.html)。


 


via: <http://www.unixmen.com/installing-xscreensaver-ubuntu/>


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出


译者：[Luoxcat](https://github.com/Luoxcat) 校对：[jasminepeng](https://github.com/jasminepeng)
