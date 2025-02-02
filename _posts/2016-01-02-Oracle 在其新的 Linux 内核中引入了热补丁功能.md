---
layout: post
title:	"Oracle 在其新的 Linux 内核中引入了热补丁功能"
date:	2016-01-11 08:38:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,内核,Linux]
---


Oracle 的 Michele Casey 宣布其 Unbreakable Enterprise Kernel (UEK) 4 发布！UEK 可用于 Oracle Linux 6 和 Oracle Linux 7 ，它们是基于 Centos 的衍生版。


![](/Asserts/Images/album/201601/11/153804mtebbxx85sbdu8xs.jpg)


UEK 4 带来了不少性能和功能方面的重大更新，包括 CPU 调度、自动 NUMA 平衡以及众所期待的<ruby> 内核热补丁 <rp>  （ </rp> <rt>  Real-Time Kernel Patching </rt> <rp>  ） </rp></ruby>功能。


UEK 4 中的内核热补丁功能来自于 Linux 内核 4.1 主线内核的 Ksplice 开源扩展，它可以让用户无需重启系统即可更新内核，这改进了系统安全和简化了云架构的管理。去年4月发布的 Linux 4.0 内核[合并了 Live Patching](/article-5272-1.html)，为实时内核打补丁功能提供了必要的内核模块 API 和用户空间 API/ABI。


除此之外，UEK 4 还带来了 LZ4 压缩算法、低延迟网络 polling等新的功能。以及在系统安全方面做了极大增强，包括新的随机数系统调用、内核地址空间随机化、对 SELinux 、nftables 等程序的更新等。
