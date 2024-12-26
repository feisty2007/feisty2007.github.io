---
layout: post
title:	"Linux 安全性被鄙视，OpenBSD 6.0 为了安全而抛弃了 Linux 兼容层"
date:	2016-07-27 17:59:22 +0800 
categories:	观点 linuxcn 
tags:	[linuxcn,OpenBSD,Linux,安全]
---



> 
> 最新版本的 OpenBSD 6.0 将关闭潜在的安全漏洞——比如其 Linux 兼容层。
> 
> 
> 


OpenBSD，这个 BSD 家族里面最重要的变种之一将在今年九月份[发布](https://www.openbsd.org/60.html)新的 6.0 版本。它通常被视作 Linux 的一个替代品，以没有专有软件而闻名，并由于其默认情况下比其它的操作系统更安全，以及对[用户安全](http://www.infoworld.com/article/2624916/government/openbsd-chief-believes-contractor-tried-to-write-back-doors.html)的[高度警惕](http://www.infoworld.com/article/2617852/open-source-software/openbsd-founder-calls-red-hat-and-canonical--traitors--to-open-source.html)而广泛受到赞誉。由于其在开发过程中的安全理念，许多软件路由器和防火墙项目都是基于 OpenBSD 而开发的。


![](/Asserts/Images//attachment/album/201607/27/175705d47mme5e0gag45nm.jpg)


在这次 OpenBSD 新版本中安全相关的最大变化是其移除了对 Linux 模拟的支持。在之前的 OpenBSD 版本中，Linux 应用可以通过一个[兼容层](https://www.openbsd.org/papers/slack2k11-on_compat_linux.pdf)直接运行在 BSD 中，但是在最新的 OpenBSD 6.0 的[发布公告](https://www.openbsd.org/60.html)中称，由于“安全改进”而移走了该子系统。


OpenBSD 中有一些软件是以附加的二进制软件包方式提供的，OpenBSD 的维护者们会尽量提供对这些软件的支持，但是他们不会像对待其操作系统一样对这些软件的安全性进行筛选。由于现在很多流行应用的最新版本都可以直接运行在 OpenBSD 中，比如说 Chromium 和 Firefox 浏览器，这意味没有 Linux 兼容层也不要紧。


出于安全考虑，OpenBSD 还抛弃了 [systrace](http://man.openbsd.org/OpenBSD-5.9/systrace) 系统安全实施策略工具。之前版本的 OpenBSD 包括它，但是并没有用它来管理任何重要的东西。[systrace](http://man.openbsd.org/OpenBSD-5.9/systrace) 被[视为不安全已经有段时间](https://www.lightbluetouchpaper.org/2007/08/06/usenix-woot07-exploiting-concurrency-vulnerabilities-in-system-call-wrappers-and-the-evil-genius/)了，所以在这次的 OpenBSD 发行版中它也将被抛弃。


作为安全增强的一部分，还[移除了“usermount”选项](http://undeadly.org/cgi?action=article&sid=20160715125022)，它允许非特权用户挂载文件系统。OpenBSD 项目负责人 Theo de Raadt 说 usermount “允许任何不当的程序调用 mount/umount 系统调用”，这意味着“在提供该功能的前提下，任何用户都没有办法保持其系统的安全性和可靠性的预期。”




在发布于今年三月份的 OpenBSD 的前一个版本 5.9 中，它提供了一些自己的安全改进。比如以特权用户身份运行程序的 sudo 被替换成 [doas](http://www.openbsd.org/faq/faq10.html#doas)，这个新的程序使用了更简化和潜在问题更少的配置机制。这种为了安全而做的改变在 Linux 世界会更难见到，而 OpenBSD 则通过让其[代码不断采用新的技术](http://www.openbsd.org/papers/pruning.html)而展示了其在安全方面的努力和进步。
