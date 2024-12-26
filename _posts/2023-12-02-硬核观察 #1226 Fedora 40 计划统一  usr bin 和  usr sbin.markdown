---
layout: post
title:	"硬核观察 #1226 Fedora 40 计划统一 /usr/bin 和 /usr/sbin"
date:	2023-12-25 21:03:57 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,LSB,目录,Linux,Enlightenment]
---


![](/Asserts/Images//attachment/album/202312/25/210245irtm4rjrggajgt09.jpg)


![](/Asserts/Images//attachment/album/202312/25/210257t9z7k6g9g4z5n77g.png)


### #1 Fedora 40 计划统一 /usr/bin 和 /usr/sbin


Fedora 开发者提议在 Fedora 40 中统一 `/usr/bin` 和 `/usr/sbin`。这有助于简化打包者的工作和终端用户的使用，进一步兼容其它主流 Linux 发行版。有些工具软件在不同的发行版放在不同的位置，比如说，`ip` 命令在 Fedora 放在 `/sbin/` 下，而在 Debian 中放在 `/bin/` 下，其它的例子还有很多。多年前，Fedora 已经将 `/bin` 和 `/sbin` 合并到了 `/usr` 下，因此，这次合并后，这四个目录将是同一个目录。其它 Linux 发行版，比如 Debina、Arch Linux 也在进行类似的合并工作。


*（插图：DA/84fd07e2-84d7-409a-bc1d-a267e65037e4）*



> 
> **[消息来源：Fedora Project](https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin)**
> 
> 
> 



> 
> 老王点评：这是历史遗留问题，当时划分这样琐碎的目录的理由目前看起来已经不再必要。但是这些不应该是在 LSB 中统一改变后，大家都一起改变吗？所以，是 LSB 已经没有人维护了？
> 
> 
> 


![](/Asserts/Images//attachment/album/202312/25/210317l5p55915tq921tq5.png)


### #2 Linus Torvalds 给内核开发者们放了年终假期


新的 Linux 内核上游版本通常在美国时间的周日晚上发布，但根据芬兰的习俗，Linus Torvalds 将在 12 月 24 日忙于庆祝活动，比如去购物，因此他决定提前一天，在上周六就发布了内核 Linux 6.7-rc7。Linus 还在邮件列表中说，由于进展顺利，虽然他可以在下周末按计划发布 6.7 正式版，但他不打算这么做。他计划下周继续发布一个少见的 RC 版本 rc8，但估计大家都放假了，没人会看。然后他会在明年 1 月 7 日再发布 Linux 6.7 正式版，以避免在 1 月 1 日开启 Linux 6.8 的合并窗口。


*（插图：DA/00741f95-1317-40a2-9c09-7380f771bb2d）*



> 
> **[消息来源：Phoronix](https://www.phoronix.com/news/Linux-6.7-rc7)**
> 
> 
> 



> 
> 老王点评：忙碌了一年，是该休息一下了。我是不是也该休息一下呢？我好多年从未因为任何事情和假期停止过了。
> 
> 
> 


![](/Asserts/Images//attachment/album/202312/25/210331i5mictrz5f6zhtm6.png)


### #3 时隔两年，Enlightenment 0.26 发布


Enlightenment 的上一个版本 0.25 发布至今已有两年，但这个新版本主要是一些小错误的修复，以及一些诸如背光设置、任务预览、屏保抑制等方面的微小改进。


*（插图：DA/c271d067-d03f-4a79-906a-ae92f401e0a7）*



> 
> **[消息来源：Phoronix](https://www.phoronix.com/news/Enlightenment-0.26-Released)**
> 
> 
> 



> 
> 老王点评：这是向大家表示软件项目还存活吗？
> 
> 
>
