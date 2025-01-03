---
layout: post
title:	"硬核观察 #790 Canonical 在 apt 命令中为其 Ubuntu Pro 打广告"
date:	2022-10-15 18:52:00 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,Ubuntu,无人机,PostgreSQL]
---


![](/Asserts/Images/album/202210/15/185110hg00ssie3ihey9g0.jpg)


![](/Asserts/Images/album/202210/15/185118xeokk5qx0prp0oco.jpg)


### Canonical 在 apt 命令中为其 Ubuntu Pro 打广告


之前我们 [报道](/article-15120-1.html) 过，Canonical 公司提供的 Ubuntu Pro 支持现在可供多达五台机器免费使用，为这些机器提供十年的支持服务。这本来是一件好事，但如果你从命令行用 `apt` 命令更新时，你就会看到 Canonical 发布的宣传这项免费服务的广告。这让一些用户非常恼火。Canonical 在自作主张向 Ubuntu 用户显示广告方面“劣迹斑斑”。上一次在服务器的登录屏幕中显示了促销信息，而在十年前，它还在桌面搜索结果中显示了亚马逊的广告。



> 
> **[消息来源：The Register](https://www.theregister.com/2022/10/13/canonical_ubuntu_ad/)**
> 
> 
> 



> 
> 老王点评：我觉得，可能 Canonical 的初衷或许是好的，但是这种侵入式广告的方式太糟糕。或许，Ubuntu 应该在其桌面版和服务器版中专门提供一个通告服务，以使关注 Ubuntu 相关信息的人可以主动订阅。
> 
> 
> 


![](/Asserts/Images/album/202210/15/185129jwrira0v3i0x343a.jpg)


### 黑客利用无人机，通过 Wi-Fi 远程渗透了金融公司内网


安保人员在美国东海岸一家专注于私人投资的金融公司的大楼顶层发现了两架 DJI 无人机，一架虽然炸机但仍在运行，而另一架实现了安全着陆。两架无人机上被加装了渗透套件，包含一台树莓派、GPD 迷你笔记本电脑、4G 调制解调器、Wi-Fi 设备、几块电池，以及一套网络渗透测试设备。攻击者利用该装置拦截了该公司员工的凭据，利用员工 MAC 地址和访问凭据、从屋顶侵入了该公司的内网。



> 
> **[消息来源：The Register](https://www.theregister.com/2022/10/12/drone-roof-attack/)**
> 
> 
> 



> 
> 老王点评：这真是无孔不入，之前曾经有黑客靠近办公室渗透 Wi-Fi 的，现在居然连无人机都用上了。
> 
> 
> 


![](/Asserts/Images/album/202210/15/185142j73dprboyugtomdo.jpg)


### PostgreSQL 15 发布


新版本进一步改进了性能，主要新特性包括：支持 SQL MERGE 命令；改进内存中和磁盘上的排序性能，最高提升 400%；启用了 Zstd 和 LZ4 压缩支持，并支持写前日志文件；支持 pg\_basebackup 期间执行服务器端压缩；等等。



> 
> **[消息来源：Phoronix](https://www.phoronix.com/news/PostgreSQL-15-Released)**
> 
> 
> 



> 
> 老王点评：我当时学习的第一个开源数据库就是 PG，可惜后来它的风头被 MySQL 抢走了，但是实际上 PG 更优秀。
> 
> 
>
