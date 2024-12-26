---
layout: post
title:	"微软允许 OEM 对 Windows 10电脑不提供关闭 Secure Boot 的选项"
date:	2015-03-23 14:05:51 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,UEFI,Secure Boot,Windows 10]
---


用户[可能将无法](http://arstechnica.com/information-technology/2015/03/windows-10-to-make-the-secure-boot-alt-os-lock-out-a-reality/)在Windows 10电脑上安装其它操作系统了，微软不再要求OEM在UEFI 中提供的“关闭 Secure Boot”的选项。


微软最早是在Designed for Windows 8认证时要求OEM的产品必须支持UEFI Secure Boot。Secure Boot 被设计用来防止恶意程序悄悄潜入到引导进程。问题是如果其它的操作系统，比如 Linux，没有Secure Boot的有效签名它们将无法安装。幸好微软要求电脑必须有一个UEFI设置可以关闭Secure Boot的保护。


![](/Asserts/Images//attachment/album/201503/23/140556th82323l23xmmdzs.png)


**但现在微软改变了做法，允许OEM 厂商不提供该设置，这样用户将无法安装没有签名的替代操作系统。**


Windows 10 对 OEM 厂商所提供 UEFI 的要求如下：


* 必须支持 UEFI，兼容版本2.31
* 对于 Windows 10 Desktop：OEM 厂商可以选择是否允许用户关闭 Secure Boot
* 对于 Windows 10 Mobile：OEM 厂商必须不能允许用户关闭 Secure Boot
* UEFI Secure Boot 数据库必须按照 Windows 10 硬件需求来配置
* PCR 必须实现 TCG TrEE EFI 协议
