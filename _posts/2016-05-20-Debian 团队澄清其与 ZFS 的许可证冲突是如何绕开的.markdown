---
layout: post
title:	"Debian 团队澄清其与 ZFS 的许可证冲突是如何绕开的"
date:	2016-05-16 15:42:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,ZFS,Debian]
---


之前，我们报道过 [Debian 中支持了 ZFS 文件系统](/article-7341-1.html)的新闻。Debian 社区对此表示了欢迎，但是也有人指出，ZFS 支持之所以迟迟不能加入到 Debian 中是由于 ZFS 许可证与 <ruby> Debian 自由软件指南 <rp>  （ </rp> <rt>  Debian Free Software Guidelines </rt> <rp>  ） </rp></ruby>之间的冲突。


今天早些时候，我们联系到了 Debian 公关团队的 Donald Norwood，他告诉我们， ZFS for Linux 没有放到 Debian GNU/Linux 的主软件仓库中，而是放到了另外一个名为 “contrib”的仓库中。


“ZFS 放到了 /contrib/ 下，而没有放到 /main/ 下，原因是因为当前的 ZFS 许可证同 <ruby> Debian 自由软件指南 <rp>  （ </rp> <rt>  Debian Free Software Guidelines </rt> <rp>  ） </rp></ruby>存在冲突。因此，用户可以从其中下载源代码编译而不是直接下载二进制。”，Donald Norwood 说。


![](/Asserts/Images//attachment/album/201605/16/154250zmxevc8mmgkk3i4g.jpg)


### Debian 中的 ZFS 实现与 Ubuntu 中的那个不同


似乎有些人误解 Debian GNU/Linux 中的 ZFS 实现是来自 Ubuntu 16.04 中的 ZFS 实现，而据 <ruby> Software Freedom Conservancy <rp>  （ </rp> <rt>  自由软件管理委员会 </rt> <rp>  ） </rp></ruby> 称，[Ubuntu 中的 ZFS 实现违反了 GPL 许可证](https://sfconservancy.org/blog/2016/feb/25/zfs-and-linux/)。Debian 的 ZFS 软件包虽然[包含了一些来自 Ubuntu 的补丁](https://tracker.debian.org/news/767790)，但是是以源代码的方式提供的，所以实质上绕开了 GPL 许可证的冲突。（注：据网友指正，此处语言有修饰。）


如果你想在你的 Debian GNU/Linux 中体验一下 ZFS，你可以从 contrib 仓库中下载最新的 zfs-linux 软件包。


更多关于 Debian 中的 ZFS 的细节，可以查看[此处](https://bits.debian.org/2016/05/what-does-it-mean-that-zfs-is-in-debian.html)。
