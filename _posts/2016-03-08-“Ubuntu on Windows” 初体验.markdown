---
layout: post
title:	"“Ubuntu on Windows” 初体验"
date:	2016-03-31 16:07:18 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Ubuntu]
---


在 Windows 10 中原生运行 Linux bash 和其它的 ELF 二进制程序？对，你没看错，这就是昨晚微软[宣布](/article-7177-1.html)的“Ubuntu on Windows”项目所披露的事实——而且，今天不是 4/1。


之前就有传闻说，微软在 [Windows 10 里暗藏神秘 Linux 子系统！](/article-6979-1.html)现在，传闻变成真的了。


![Ubuntu on Windows 10](/Asserts/Images/album/201603/31/160721hcwz5cbo2cgc40ez.jpg)


据该项目的合作方， Ubnutu 背后的 Canonical 公司的产品与战略负责人 [Dustin Kirkland](https://www.linkedin.com/in/dustinkirkland/) 说，他在几个月前听说这个疯狂的想法时也懵了，花费了不少工夫才理解这后面发生了什么。


本文带你揭开“Ubuntu on Windows”的神秘一角。


首先，让我们看看发生了什么？


1. 首先你得有个 Windows 10
2. 打开 Windows 开始菜单
3. 输入“bash” （没有引号），回车
4. 这会打开一个 cmd.exe 窗口
5. 运行 Ubuntu 的 /bin/bash
6. 宾果！你可以完全访问所有的 Ubuntu 用户空间了
7. 没错，这包括 apt、 ssh、 rsync、 find、 grep、 awk、 sed、 sort、 xargs、 md5sum、 gpg、 curl、 wget、apache、 mysql、 python、 perl、 ruby、 php、 gcc、 tar、 vim、 emacs、 diff、 patch 等等
8. 以及，Ubuntu 软件库中数以万计的 ELF 二进制程序中的绝大多数！


![Bash](/Asserts/Images/album/201603/31/151117fu333omffsp3o494.jpg)


“好吧，这是一个运行在虚拟机的 Ubuntu 吗？” 不！**这根本不是一个虚拟机**，不用在虚拟机中启动 Linux 内核，它就是 Ubuntu 的用户空间。


“哦，那是运行在容器里面啰？” 不不！**这也不是一个容器**，这是在 Windows 里面直接运行原生的 Ubuntu 二进制程序。


“嗯，就像 cygwin 那样？”不不不！cygwin 所包括的开源程序是以源代码重新编译后才能原生运行在 Windows 上。而这里，我们说的是一个比特都不差、校验值**完全一样的 Ubuntu 的 ELF 二进制程序可以直接运行在 Windows 下**！


... ...


“那么，这就像是模拟器一样么？”这就比较接近真相了，来自微软的一些尖端技术人员正在研究一种技术，可以**将 Linux 的系统调用实时地转换为 Windows 的系统调用**。你可以把它当成 Wine 的一种反向技术。微软将其称之为“<ruby> Windows 下的 Linux 子系统 <rt>  Windows Subsystem for Linux </rt></ruby>”，当然现在还没有开源。（我觉得网友 [delectate](https://linux.cn/space/23856/) 说的比较有趣，这个东西不如叫做 mine=microsoft's native emulator 。）


而且，根据 [Dustin Kirkland](https://www.linkedin.com/in/dustinkirkland/) 的[说法](http://blog.dustinkirkland.com/2016/03/ubuntu-on-windows.html)，使用跨平台的性能测试工具 sysbench 进行测试的结果发现，在 Windows 下运行这些原生的 ELF 二进制程序和在 Linux 下运行所消耗的 CPU 、内存和 IO 性能相当。对于这个结果，我表示非常的吃惊！


[Dustin Kirkland](https://www.linkedin.com/in/dustinkirkland/) 是该项目组的成员之一，他的体验可以让我们感受一下这个“超级神秘”的项目。


由于需要将整个 Ubuntu 的根文件系统打包到一个 Windows 应用软件包（.appx）中，这位已经十几年没有使用过 Windows 的老兄对微软开发工具十分陌生，在经过几个小时与 Visual Studio 的痛苦搏斗，制作了一堆各种尺寸的 png 图标，编辑了一打以上的 XML 文件后，他简直忍不住要将咖啡杯扔到该死的屏幕上了。


到最后，他终于寻求他所熟悉的 Linux 经验解决了这些问题。


按下 Windows 键，输入“bash”，回车！他发现这个要上载的根文件系统的内容放在 /mnt/c/Users/Kirkland/Downloads 下，只需要使用一个 cp -a 复制到目标位置即可，并用 find | xargs |rename 来批量更新文件名，用 grep| xargs | sed 搜索替换路径，用 convert 工具快速地批量缩放图标，简直不要太容易地搞定了这些工作，剩下的就只需要让 Visual Studio 自己干了，编译、上载到 Windows Store。搞定！


嗯，你也许从终端窗口中看到了 /mnt/c ，没错，这就是你的 Windows 下的 C: 盘，它们以读写模式直接挂载到 /mnt 下了。当然，你也可以在 Windows 下通过类似如下的路径访问 Ubuntu 的文件系统：C:\Users\Kirkland\AppData\Local\Lxss\rootfs\ 。


![文件系统](/Asserts/Images/album/201603/31/151003ljojc3jbkomm1mjm.jpg)


同时，如果需要 ssh 连接到其它的 Linux 上，你根本不用下载 putty，直接输入 ssh 即可：


![ssh](/Asserts/Images/album/201603/31/151329dupcfwbc1wppw8v6.jpg)


当然，你也可以使用 apt 来安装和更新软件包：


![apt](/Asserts/Images/album/201603/31/151425vz7crhkosobarzdt.jpg)


到目前为止，是不是所有的东西都可以完美工作了？还不全是。[LTP](https://github.com/linux-test-project/ltp) 测试中的大多数都没问题，但是有一些则还不行，主要是 tty 相关的部分，比如 byobu、screen、tmux 等还不能很好的工作，不过相信也快了。


另外，顺便提一句，当前这个子系统所采用的 Linux 镜像是 Ubuntu 14.04 LTS，等 16.04 LTS 发布后相信很快就会更新到 Windows Store 上。
