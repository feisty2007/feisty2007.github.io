---
layout: post
title:	"如何在VirtualBox中的Linux客户机系统间共享磁盘"
date:	2014-06-02 12:36:00 +0800 
categories:	桌面应用 linuxcn 
tags:	[linuxcn,]
---


在本教程中，让我来给你们展示一下如何在VirtualBox中的两个Linux客户机系统间共享一个磁盘。


本教程对于那些想配置一下并玩玩GFS或者集群的人来说还是很有帮助的。


下图是VirtualBox的标准界面：


![](/Asserts/Images/album/201406/02/063725keo2zw424zolo2lo.png)


第一个客户系统机CentOS1：


![](/Asserts/Images/album/201406/02/063726q46t2ucujqv33cfu.png)


第二个客户机系统CentOS2：


![](/Asserts/Images/album/201406/02/063727h010ir5alkl7iknz.png)


给第一台机器添加额外的磁盘：


![](/Asserts/Images/album/201406/02/063728xyz356n90293cggr.png)


点击文件->虚拟介质管理器（Control+D）打开虚拟介质管理器界面：


![](/Asserts/Images/album/201406/02/063729pf4zpny4xzlyyv2p.png)


设置磁盘为可共享（Shareable）：


![](/Asserts/Images/album/201406/02/063730cgly7iwhzd7w9h5h.png)


在客户机CentOS 2上，你可以添加现有磁盘，该磁盘在CentOS1客户机系统之前已经创建好：


![](/Asserts/Images/album/201406/02/063731j8pg2896xt1p2jg6.png)


完成后，你可以重启第二个客户机系统，并检查驱动器是否已经添加：


![](/Asserts/Images/album/201406/02/063733fbaceo9e9aeadoab.png)


大功告成。




---


via: <http://www.unixmen.com/share-disks-virtualbox-linux-guest-os/>


译者：[GOLinux](https://github.com/GOLinux) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
