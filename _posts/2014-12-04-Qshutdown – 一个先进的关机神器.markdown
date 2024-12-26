---
layout: post
title:	"Qshutdown – 一个先进的关机神器"
date:	2014-12-02 11:25:00 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,关机,qshutdown]
---


qshutdown是一个QT程序，用于让计算机在指定时间或者在几分钟后关机/重启/挂起/睡眠。对于那些只在特定时间使用计算机工作的人而言，可能很有用。


![](/Asserts/Images/album/201412/02/112507qi3zg403dg4qr5c4.png)


qshutdown将在最后70秒时显示3次警告提醒。（如果设置了1分钟或者“本地时间+1”，它只会显示一次。）


该程序使用qdbus来发送关机/重启/挂起/睡眠请求到gnome或kde会话管理器，或者到HAL或DeviceKit，而如果这些都没有工作，那么就会使用‘sudo shutdown -P now’命令进行关机（注意，当发送请求到HAL或DeviceKit，或者使用shutdown命令时，会话不会被保存。如果使用shutdown命令，该程序只会被关机或重启）。所以，如果在shutdown或reboot时间到时却什么都没发生，这就意味着用户缺少使用shutdown命令的权限。


在这种情况下，你可以进行以下操作：


粘贴以下信息到终端：“EDITOR:nano sudo -E visudo”并添加此行：“\* ALL = NOPASSWD:/sbin/shutdown”这里\*替换为你的“用户名”或“%组名”。


倒计时最大计数为1440分钟（24小时）。配置文件（和日志文件）位于~/.qshutdown，配置文件为：qshutdown.conf。


对于管理员：


在将qshutdonw.conf中的Lock\_all选项设置为true后，用户将不能修改设置。如果你使用“sudo chown root -R ~/.qshutdown”和“sudo chmod 744 ~/.qshutdown/qshutdown.conf”命令修改qshutdown.conf的权限后，用户将不能修改配置文件。


### Ubuntu中安装Qshutdown


打开终端，然后运行以下命令



```
sudo apt-get install qshutdown

```

### 屏幕截图


![](/Asserts/Images/album/201412/02/112509lgae532eajy2zjd4.png)


![](/Asserts/Images/album/201412/02/112511javmwnjizcwjjdbt.png)


![](/Asserts/Images/album/201412/02/112513z0sssxto6xgo6bm6.png)




---


via: <http://www.ubuntugeek.com/qshutdown-an-avanced-shutdown-tool.html>


作者：[ruchi](http://www.ubuntugeek.com/author/ubuntufix) 译者：[GOLinux](https://github.com/GOLinux) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
