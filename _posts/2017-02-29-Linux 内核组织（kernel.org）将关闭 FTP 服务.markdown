---
layout: post
title:	"Linux 内核组织（kernel.org）将关闭 FTP 服务"
date:	2017-02-01 08:00:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Linux,内核,FTP]
---


<ruby> <a href="https://www.kernel.org/">  Linux 内核组织 </a> <rp>  （ </rp> <rt>  Linux Kernel Organization </rt> <rp>  ） </rp></ruby>（kernel.org） 是一家建立于 2002 年的加利福尼亚公共福利公司，其目的是公开地免费分发 Linux 内核和其它开源软件。它接受 Linux 基金会的管理，包括技术、资金和人员支持，用以维护 [kernel.org](https://www.kernel.org/) 的运营。


![](/Asserts/Images/album/201701/31/230456loylh656v67oa1aa.jpg)


Linux 内核组织是 Linux 内核发布的官方场所，在其站点上可以找到 Linux 内核的各个版本，包括最早的 1.0 到最新的 4.x 内核。其所提供的内核获取方式多种多样，包括：


* [HTTP](https://www.ietf.org/rfc/rfc2616.txt) <https://www.kernel.org/pub/>
* [GIT](https://git-scm.com/) <https://git.kernel.org/>
* [RSYNC](https://rsync.samba.org/) rsync://rsync.kernel.org/pub/


以及 FTP 方式，然而，现在他们[决定停止](https://kernel.org/shutting-down-ftp-services.html) FTP 方式的下载了。


最初，早在 1998 年的时候， [Linux 内核组织](http://kernel.org/)就提供了以 FTP 服务为基础的内核代码获取方式，除了可以直接通过 FTP 进行下载以外，还可以通过 HTTP 协议封装来访问 FTP 资源，甚至，还允许通过 NFS 和 SMB/CIFS 来将他们的 FTP 资源挂载为本地分区。


![](/Asserts/Images/album/201701/31/223911knuau6uz7u4i08k4.jpg)


不过，不久之后，他们发现提供一个公开的 NFS/CIFS 服务器看起来并不是一个好主意，不仅仅是因为这两种服务在慢速网络时表现很糟糕，而且它们本身也存在严重的安全隐患。因此于当年年底时停止了对 NFS 和 SMB/CIFS 的支持。


而现在，基于如下考虑：


* FTP 服务需要在防火墙和负载均衡设备上做额外的配置和调整
* FTP 服务器不支持缓存和加速器，这严重影响了性能
* 大多数的相关软件缺乏维护和更新


因此，在服务了 19 年之后，Linux 内核组织决定彻底终止 FTP 服务器上剩下的 FTP 服务了。Linux 内核组织所有的 FTP 服务都将在今年内关闭，为了减少影响，关闭分为两个阶段：


1. <ftp://ftp.kernel.org/> 服务将于 2017 年 3 月 1 日终止
2. <ftp://mirrors.kernel.org/> 服务将于 2017 年 12 月 1 日终止


不过，如果你有任何疑问，欢迎联系 [ftpadmin@kernel.org](mailto:ftpadmin@kernel.org) 。
