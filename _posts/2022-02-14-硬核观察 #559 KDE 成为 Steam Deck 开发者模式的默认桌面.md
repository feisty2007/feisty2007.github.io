---
layout: post
title:	"硬核观察 #559 KDE 成为 Steam Deck 开发者模式的默认桌面"
date:	2022-02-26 20:58:27 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,KDE,C语言,大型机]
---


![](/Asserts/Images/album/202202/26/205727o83br8ir43z8zufr.jpg)


![](/Asserts/Images/album/202202/26/205742eubjqkuikzkojvsb.jpg)


### KDE 成为 Steam Deck 开发者模式的默认桌面


Steam Deck 已经发货，[KDE Plasma](https://pointieststick.com/2022/02/25/this-week-in-kde-bugfixing-plasma-5-24/) 成为“开发者模式”下的默认桌面。对于 KDE 开发者来说，为了能顺利地在 Steam Deck 上运行，他们经历了忙碌的一周，进行了大量修复和改进。



> 
> 老王点评：虽然这不应该意外，因为 Steam Deck 是基于 Linux 的。
> 
> 
> 


![](/Asserts/Images/album/202202/26/205750xr45v8pn354pe57r.jpg)


### Linux 内核准备采用现代 C 语言标准


Linux 内核仍然采用的是 1989 版的 C 语言标准，它已有三十多年历史了。由于一些特性在 C89 中不支持，因此在处理一些问题时格外麻烦。Torvalds 说，内核代码一直停留在 C89 的原因之一是旧版本的 gcc 编译器会出现奇怪的问题，现在内核要求的 gcc 最低版本已经提高到了 v5.1，那些 bug 可能不再相关了。在讨论之后，他宣布将在下一个内核版本 5.18 中 [尝试下新的 C 语言标准](https://lwn.net/SubscriberLink/885941/01fdc39df2ecc25f/)。如果一切顺利，C 语言标准有望在下一个内核版本中迁移到 C11。



> 
> 老王点评：虽然 Linux 内核存在一些历史遗留问题，但是好在内核社区是一个活跃的社区，能不断前进。
> 
> 
> 


![](/Asserts/Images/album/202202/26/205812gli2scpp8d95o3z5.jpg)


### 富士通准备停止其大型机和 UNIX 业务


富士通将在 2030 年之前 [停止生产和销售其大型机系统](https://www.theregister.com/2022/02/25/fujitsu_signposts_the_end_for/)，并将在 2029 年底之前停止发售其 Unix 服务器系统。对这两个组合的支持服务将再持续五年。对于大多数富士通大型机客户来说，他们需要在这个期限之前将他们的大型机应用迁移到另一个平台上。



> 
> 老王点评：虽然这看起来很遥远，但对于大多数使用大型机的组织来说，大型机是一项巨大的长期投资，这对他们来说是一件大事。
> 
> 
>
