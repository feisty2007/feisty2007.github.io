---
layout: post
title:	"DebianFork 将发布没有 systemd 的 Debian 分支"
date:	2014-11-29 01:09:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,systemd,Debian,debianfork,Devuan]
---


编者按：Debian 8 Jessie的 init 系统默认使用 systemd，这一选择在社区引发了大量争议，导致了技术委员会的[多名成员辞职](http://linux.cn/article-4256-1.html)。现在，“老兵 Unix 管理员”宣布要创建一个新的不使用 sytemd 的 [Debian 分支](http://debianfork.org/)。这群 Unix 哲学拥护者们请求外界[捐赠](http://debianfork.org/donate.html)支持他们的新使命。


以下内容来自 debianfork.org 的相关内容：




---


// 更新： 项目名称正式命名为：[Devuan](https://devuan.org/)。


![](/Asserts/Images//attachment/album/201411/29/010211lt44nnckfkzakd4m.png)


#### 我们是谁？！


我们是老兵 Unix 管理员（Veteran Unix Admins），我们非常关注 Debian GNU/Linux 在 systemd 上的分歧，并且决定分支（fork）Debian 项目。


#### 为什么我们要这样做？


我们中的一些人是上游开发者，一些人是专业的系统管理员：我们每天都要和 Debian 打各种交道。


我们不想被强迫使用 systemd 来替代传统的 UNIX sysvinit 初始化系统，因为 systemd 背离了 UNIX 哲学。


我们考虑采用贴近 sysvinit 的架构，而不是那种破坏了“做一件事，把它做好”的原则、带着数十个紧密耦合的二进制文件和不透明的日志的东西。


#### 有比创建分支更好的解决方案么？


不幸的是，目前没有！


在下一代的 Debian v.8 "Jessie" 发行版中，默认的初始化系统将是 systemd，它将挟裹着一堆紧密纠缠的东西来到。


我们需要分离这些依赖的牵扯，从所有受到影响的软件包中清除这些，并提供相应的替代品。我们所要创建的分支的稳定性是目前阶段所要考虑的首要重点。


#### 你觉得为什么会走到了这一步？


现在的 Debian 项目的领导者受到了 GNOME 开发者太多的影响，而且在项目中考虑了太多的桌面需求的因素，而 Debian 用户却大多数是精通技术的系统管理员。


而且，今天 Debian 正逐渐背离自己最初愿景，也是开源软件的基石：用户至上。这到底是怎么了？所谓的“do-ocracy”开发者和包维护者正在给用户强加他们的选择。


#### 你可以说一下你对 systemd 的意见吗？


套用一下 Eric S. Raymond 在这个问题上的看法，我们认为 systemd 很容易就会发生嬗变，进而臃肿不堪、最后变成了那种讨厌的纠结在一起的毛球。


我们希望能够用可以阅读的 shell 脚本来控制系统的启动，因为可读性能够给我们这些有能力的人更多的控制和洞悉。我们认为，在一个守护进程中集中控制服务、socket、设备、挂载等等，是对传统的 UNIX 哲学的一记响亮耳光。


某些支持 systemd 的人对此的快速回应可以在 [forkfedora.org](https://web.archive.org/web/20141020161905/http://forkfedora.org/) （已经关闭，需要翻墙才能看历史归档）上看到。这个页面突出了两者之间的根本不同：systemd 也许对于配置 init 来说很简单，但是它增加了 init 过程中的不透明度。在 systemd 中很明确是这样的：可以通过更少的变量来调整，而通过远超 sysvinit 大小的程序将大部分细节隐藏在一个巨大的二进制程序里面。 



```
  ls -lH /sbin/init
  sysvinit: -rwxr-xr-x 1 root root 36992 Jul 14  2013 /sbin/init
  systemd: -rwxr-xr-x 1 root root 1317632 Sep  1 14:41 /sbin/init
# 你也许认为我不够强大，但是你也太胖了！
```

可以说 systemd 的安全模式更多的依赖于开发者和包维护者，而不怎么指望系统管理员。作为 Debian 用户，我们只是希望不要被强迫必须如此，看看 [CTTE 关于这个问题的投票就会知道](https://news.ycombinator.com/item?id=7203364)，我们相信这样下去会越来越多的听到用户要求：**放开那个 Init ！不要和 systemd 和它的那堆零碎纠缠在一起。**


#### 你们能坚持多久？


这不是比谁的胡子更长，放心，毛茸茸的不总是绵羊！


#### 概括一下计划?


“放开那个 Init”（ Init Freedom），这是我们的承诺，我们会建立一个 Debian 项目的分支，创建一个新的基础发行版。


这需要一些时间，我们会一步步来。


首先我们会配合 Debian 8 "Jessie" 的发布，给当前的 Debian 用户平滑升级提供一个完整的解决方案。


如果你也需要这个，请帮助我们： [捐赠](http://debianfork.org/donate.html) 或者参与进来。


#### 我们需要谈谈。


当然，您可以写电子邮件给 [VUA@debianfork.org](mailto:VUA@debianfork.org) 。


我们也有一些人聚集在 IRC ， Freenode 频道号是 #debianfork ，欢迎加入。


[可以订阅邮件列表](https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/dng)。喜欢的话来发布意见吧，不管是什么。


#### 只有你们这些家伙吗？


不是，有很多用户都对 systemd 有意见。


有一篇文章是对这个问题的很好的介绍： [Systemd: Linux 世界末日的预兆](http://www.infoworld.com/article/2608798/Asserts/Images/-center/systemd--harbinger-of-the-linux-apocalypse.html)。


有个 [boycott systemd](http://boycottsystemd.org/) 网站也有一些相关的资料。那里有个叫做 [uselessd](http://uselessd.darknedgy.net/) 的 “systemd 分支”，有些不错的地方和许多笑点（lulz）。


还有人提出了一个 [当世界 systemd 了](http://the-world-after-systemd.ungleich.ch/)之后的撤退战略。


在维基百科的 [systemd reception](http://en.m.wikipedia.org/wiki/Systemd#Reception) 章节也有一些对其提出的批评意见。


#### 谢谢你做的这些，我怎么帮助你们？


老兵 Unix 管理员（Veteran Unix Admins）的一个小型的核心小组正在积极建设分支的相关框架和一些用于开发的基础设施。


这时的捐赠有助于我们确定可以在基础架构上投入多少以及人们的对我们的预期。


如果你会捐赠，那么[来吧](http://debianfork.org/donate.html)。


如我们现在做的，我们会在此一直更新我们的项目进展。


#### 对于你做的这些，人们是怎么看的?


下面是我们收到的一些邮件（略，请参照[原链接](http://debianfork.org/)），我们会匿名发表这些信息，除非你申明不用。


我们会保密你的邮件地址，并会通知你我们的下一步进展。
