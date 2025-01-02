---
layout: post
title:	"硬核观察 #364 Debian 11 “Bullseye” 正式发布"
date:	2021-08-15 12:00:12 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,Debian,Hurd,摩尔斯码]
---


![](/Asserts/Images/album/202108/15/115907n91vwmffa61qrzb5.jpg)


### Debian 11 “Bullseye” 正式发布


![](/Asserts/Images/album/202108/15/115920p9kyiuy9n8jziksv.jpg)


经过两年多的开发，Debian 11 “Bullseye” 已经[正式发布](https://www.debian.org/News/2021/20210814)。这个版本是一个长期支持版本，将支持 5 年。主要亮点有：Linux 5.10 LTS 内核；首次支持 exFAT 文件系统；超过 59000 个软件包，其中有 11000 个新软件包；支持控制组 v2；默认编译器 GCC 从 8.3 升级到 GCC 10.2；LLVM Clang 从 7.0 升级到 11.0；支持六种桌面环境。



> 
> 这是给 Debian 拥趸们的礼品。
> 
> 
> 


### GNU Hurd 微内核的非官方移植 GNU/Hurd 2021 发布


![](/Asserts/Images/album/202108/15/115939djururcccjab1jp3.jpg)


[Debian GNU/Hurd](https://lists.debian.org/debian-hurd/2021/08/msg00040.html) 仍然是一个非官方的移植版本，是基于 Debian 11.0 的源代码结合 GNU Hurd 微内核。鉴于目前 Hurd 的限制，Debian GNU/Hurd 2021 仍然只是适用于i386，硬件支持仍然很差，基本上只能用于虚拟机中。



> 
> GNU 项目哪里都好，就是这个内核一直没啥用。
> 
> 
> 


### 网络钓鱼攻击使用莫尔斯码来绕过电子邮件过滤系统


![](/Asserts/Images/album/202108/15/115958tba14b9mbb111v68.jpg)


微软[披露](https://www.zdnet.com/article/this-unique-phishing-attack-uses-morse-code-to-hide-its-approach/)了一个网络钓鱼攻击集团的内部技术，他们使用“拼图”技术加上莫尔斯码的破折号和圆点等不寻常的特征来隐藏其攻击。通过邮件发送的 HTML 附件被分成几个部分，然后用各种机制进行编码，包括像莫尔斯码这样古老而不寻常的加密方法，以隐藏这些攻击片段。这个附件就像一个拼图： HTML 文件的各个部分在代码层面上可能是无害的，只有当这些片段被组合在一起并被正确解码时，才会显示出恶意。



> 
> 别看摩尔斯码古老，还真是简单而不引人注意。
> 
> 
>
