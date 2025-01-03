---
layout: post
title:	"理解 Linux 中的 shutdown、poweroff、halt 和 reboot 命令"
date:	2017-06-05 09:58:38 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,shutdown,poweroff,halt,reboot]
---


![](/Asserts/Images/album/201706/05/095810ydt5h18yh8etzhkx.jpg)


在本篇中，我们会向你解释 `shutdown`、`poweroff`、`halt` 以及 `reboot` 命令。我们会解释清楚当你用那些可用的选项执行的时候它们实际做了什么。


如果你想深入 Linux 服务器管理，那么为了有效和可靠的服务器管理，这些[重要的 Linux 命令](https://www.tecmint.com/60-commands-of-linux-a-guide-from-newbies-to-system-administrator/)你需要完全理解。


通常上，当你想要关闭或者重启你的机器时，你会运行下面之一的命令：


### shutdown 命令


`shutdown` 会给系统计划一个时间关机。它可以被用于停止、关机、重启机器。


你可以指定一个时间字符串（通常是 `now` 或者用 `hh:mm` 指定小时/分钟）作为第一个参数。额外地，你也可以设置一个广播信息在系统关闭前发送给所有已登录的用户。


重要：如果使用了时间参数，系统关机前 5 分钟，会创建 `/run/nologin` 文件。以确保没有人可以再登录。


`shutdown` 命令示例：



```
# shutdown
# shutdown now
# shutdown 13:20  
# shutdown -p now  ### 关闭机器
# shutdown -H now  ### 停止机器      
# shutdown -r09:35 ### 在 09:35am 重启机器

```

要取消即将进行的关机，只要输入下面的命令：



```
# shutdown -c

```

### halt 命令


`halt` 通知硬件来停止所有的 CPU 功能，但是仍然保持通电。你可以用它使系统处于低层维护状态。


注意在有些情况会它会完全关闭系统。下面是 `halt` 命令示例：



```
# halt             ### 停止机器
# halt -p          ### 关闭机器
# halt --reboot    ### 重启机器

```

### poweroff 命令


`poweroff` 会发送一个 ACPI 信号来通知系统关机。


下面是 `poweroff` 命令示例：



```
# poweroff           ### 关闭机器
# poweroff --halt    ### 停止机器
# poweroff --reboot  ### 重启机器

```

### reboot 命令


`reboot` 通知系统重启。



```
# reboot           ### 重启机器
# reboot --halt    ### 停止机器
# reboot -p        ### 关闭机器

```

就是这样了！如先前提到的，理解这些命令能够有效并可靠地在多用户环境下管理 Linux 服务器。你有一些额外的想法么？在评论区留言与我们分享。




---


作者简介：


Aaron Kili是一名 Linux 和 F.O.S.S 的爱好者，未来的 Linux 系统管理员、网站开发人员，目前是 TecMint 的内容创作者，他喜欢用电脑工作，并乐于分享知识。




---


via: <https://www.tecmint.com/shutdown-poweroff-halt-and-reboot-commands-in-linux/>


作者：[Aaron Kili](https://www.tecmint.com/author/aaronkili/) 译者：[geekpi](https://github.com/geekpi) 校对：[jasminepeng](https://github.com/jasminepeng)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
