---
layout: post
title:	"你不一定知道，如何重置CentOS 7的Root密码"
date:	2014-10-07 10:07:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,密码,口令,CentOS 7]
---


重置Centos 7 Root密码的方式和Centos 6完全不同。让我来展示一下到底如何操作。


![](/Asserts/Images/album/201410/07/194634o9bqtl6nlmff6tin.jpg)


1 - 在启动grub菜单，选择编辑选项启动


![](/Asserts/Images/album/201410/07/000954z7v2dt7uv2z2rl3u.png)


2 - 按键盘e键，来进入编辑界面


![](/Asserts/Images/album/201410/07/000955zaja8raka0aq9frd.png)


3 - 找到Linux 16的那一行，将ro改为rw init=/sysroot/bin/sh


![](/Asserts/Images/album/201410/07/000956xg4lbr57dl5gilbg.png)


4 - 现在按下 Control+x ，使用单用户模式启动


![](/Asserts/Images/album/201410/07/000958hlbg5o7ss76595js.png)


5 - 现在，可以使用下面的命令访问系统



```
chroot /sysroot

```

6 - 重置密码



```
passwd root

```

7 - 更新系统信息



```
touch /.autorelabel

```

8 - 退出chroot



```
exit

```

9 - 重启你的系统



```
reboot

```

就是这样！




---


via: <http://www.unixmen.com/reset-root-password-centos-7/>


作者：M.el Khamlichi 译者：[su-kaiyao](https://github.com/su-kaiyao) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
