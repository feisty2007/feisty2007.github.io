---
layout: post
title:	"微软发布“Ubuntu on Windows” 项目，Linux 程序可原生运行于 Windows 10 中"
date:	2016-03-31 07:05:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,微软,Canonical,Ubuntu on Windows]
---


昨晚，北京时间2016/3/30 23点30分，微软 //Build 2016 开发者大会在美国旧金山莫斯康展览中心拉开帷幕。


在本次大会上宣布，微软与 Ubuntu 的母公司 Canonical 合作开发了一个超级隐秘的项目，将 Ubuntu 的<ruby> 用户空间 <rp>  （ </rp> <rt>  user space </rt> <rp>  ） </rp></ruby>带到了 Windows 10 之中。 据大会现场消息披露，你现在可以**在 Windows 10 中直接运行 Linux 下的 bash 以及其它的数万个二进制程序了**。


![](/Asserts/Images//attachment/album/201603/31/070407k9a577aqzrt0rrt4.jpg)


正在旧金山参加本次大会的 Canonical 的 Ubuntu 产品与战略负责人 Dustin Kirkland 也在其[博客](http://blog.dustinkirkland.com/2016/03/ubuntu-on-windows.html)上宣布了这个消息。


“这对于我来说也许有点奇怪，我已经快有16年没有使用 Windows 了。但在几个月前有了变化，我参与到了微软和 Canonical 合作的一个超级隐秘（也十分令人震惊）的项目中，这一切会在这次 Build 大会上由 Kevin Gallo 揭晓...”，[他说](http://blog.dustinkirkland.com/2016/03/ubuntu-on-windows.html)，“现在可以在 Windows 10 cmd.exe 窗口内原生地运行 Ubuntu 用户空间和 bash ！”


“好吧，这是一个运行在虚拟机的 Ubuntu 吗？” 不！**这根本不是一个虚拟机**，不用在虚拟机中启动 Linux 内核，它就是 Ubuntu 的用户空间。


“哦，那是运行在容器里面啰？” 不不！**这也不是一个容器**，这是在 Windows 里面直接运行原生的 Ubuntu 二进制程序。


“嗯，就像 cygwin 那样？”不不不！cygwin 所包括的开源程序是以源代码重新编译后才能原生运行在 Windows 上。而这里，我们说的是一个比特都不差、校验值**完全一样的 Ubuntu 的 ELF 二进制程序可以直接运行在 Windows 下**！


... ...


“那么，这就像是模拟器一样么？”越来越接近真相了，来自微软的一些技术人员正在研究一种技术，**将 Linux 的系统调用实时地转换为 Windows 的系统调用**。你可以把它当成 Wine 的一种反向技术。微软将其称之为“<ruby> Windows 下的 Linux 子系统 <rp>  （ </rp> <rt>  Windows Subsystem for Linux </rt> <rp>  ） </rp></ruby>”，当然现在还没有开源。


![](/Asserts/Images//attachment/album/201603/31/070418uk5dg151dg1k7udc.jpg)


如果你使用 Windows 10 来开发跨平台应用，那么“Ubuntu on Windows”项目将可以让你从 Windows 启动菜单直接访问 Linux 下的 bash shell。只需要键入 bash ，然后回车，就会打开一个命令行窗口，里面运行着 /bin/bash，然后数以万计的来自 Ubuntu 软件库中的二进制程序就可以运行了，包括但不限于 apt、ssh、 rsync、 find、 grep、 vim、 emacs、 awk、 sed、 ruby、 tar、 sort、php、 mysql、 perl、 python、 wget、 md5sum、 gpg、 curl、 apache、 gcc、 diff、patch 等等。


“这是 Windows 上原生可用的完整 Ubuntu 环境，不是虚拟化或模拟器，这是打破常识的里程碑和通向新天地的里程碑，”Canonical 公司 CEO Mark Shuttleworth 说，“不管怎么说，我们很高兴将 Ubuntu 带到了 Windows ，以一种神奇的方式满足了 Windows 开发者探索 Linux 的需要。”


这个技术当前基于 Ubuntu 14.04 LTS 开发，可以从 Windows Store 中下载早期 beta 版本。有关该项目的进一步技术细节，我们会在之后的文章中进行探讨。
