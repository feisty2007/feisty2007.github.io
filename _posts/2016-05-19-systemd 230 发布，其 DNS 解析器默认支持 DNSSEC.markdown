---
layout: post
title:	"systemd 230 发布，其 DNS 解析器默认支持 DNSSEC"
date:	2016-05-24 08:26:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,systemd,DNSSEC]
---


Zbigniew Jędrzejewski-Szmek [宣布](https://lists.freedesktop.org/archives/systemd-devel/2016-May/036583.html) systemd 发布了 230 版本，这是一个主要更新版本。上个版本 systemd 229 发布于大约三个月前。


![](/Asserts/Images//attachment/album/201605/24/082657frrmfhqtc9y0r2ua.jpg)


本次更新主要的关注点是其 DNS 解析服务 systemd-resolved，现在它可以使用 DNSSEC 来校验解析结果了。正如你所知道的，systemd 的“魔爪”已经伸向了 GNU/Linux 中除了内核以外的各个基础部分，比如 DNS 解析器就是一个例子，它用于为系统内的 DNS 解析请求提供服务。在本次更新中，当使用“allow-downgrade”模式时，它会默认打开 DNSSEC 扩展。DNSSEC 是一个用于校验 DNS 解析数据是否安全的扩展，对于防范 DNS 欺诈有重要作用，只是到目前为止还有不少 DNS 服务器尚未支持，所以，你也可以在编译时通过增加“--with-default-dnssec=no”编译参数来关闭它。


“我们建议下游维护人员在开发期间打开该功能，并将发现的问题报告给上游，”Zbigniew Jędrzejewski-Szmek 说，“我们非常希望得到 DNSSEC 校验器的反馈，不管是哪种反馈。不过要注意，DNSSEC 支持可能在下游发行版的稳定版本中关闭，因为它可能会导致和一些 DNS 服务器及网络的不兼容。”


当然，systemd-resolved 并不是 systemd 初始化系统中唯一得到改进的部件，其它的部件也有不少改变。


systemd 230 不久之后将会进入到各个以 systemd 作为默认的初始化系统的 Linux 发行版之中。
