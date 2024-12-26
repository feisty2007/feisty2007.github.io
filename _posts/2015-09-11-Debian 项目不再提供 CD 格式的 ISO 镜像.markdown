---
layout: post
title:	"Debian 项目不再提供 CD 格式的 ISO 镜像"
date:	2015-09-17 07:36:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Debian,镜像]
---


debian-cd 项目负责人 Stephen McIntyre [今天在Debian邮件列表中](https://lists.debian.org/debian-devel-announce/2015/09/msg00004.html)对近日召开的 DebConf15 大会上的 Debian CD BoF会议进行了摘要总结。


该消息说，自即将发布的 Debian GNU/Linux 9.0 (Stretch) 版本开始，今后 Debian GNU/Linux 系统不再生成 CD 套装的 ISO 镜像，但是会依旧生成 DVD 和蓝光镜像。


![](/Asserts/Images/album/201509/16/220934y7hh0u15wupm22g1.jpg "cdr.jpg")


当前 debian-cd 项目会生成大量的各种镜像，包括：


* CD
* DVD
* 非自由的网络安装镜像（包括非自由的固件包）
* 非自由的固件打包


debian-live 团队使用 live-build 创建的在线镜像（Live image）


* 包括非自由的固件的镜像


openstack-debian-images 生成的 Openstack 镜像


所有这些都是在 pettersson 上构建的，这是一台托管在 umu.se 的大型中央化的 CD 构建机。


对于新的发行版和测试版本，会停止构建它的完整 CD 套装（针对 90% 以上的系统架构）。同时，也会停止构建针对不同桌面的可选的 CD1 。不过，会继续构建 DVD 和蓝光镜像，DVD#1 也可以继续用于 4GB 的 USB 存储棒。


网络安装镜像会继续构建，这个又小又方便的镜像还有很多人用。对于旧的发行版，会继续构建 CD 套装和可选的 CD1 （Wheezy 和 Jessie），这个不会半途而废。
