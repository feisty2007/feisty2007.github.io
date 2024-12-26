---
layout: post
title:	"Dropbox原生Linux客户端首次展示Qt界面"
date:	2014-07-25 14:21:00 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,Dropbox]
---


**Dropbox原生Linux客户端的最新试验版首次展示了全新的Qt界面。**


Dropbox表示这次的UI重写，将同时应用到Windows和Linux，将修复“大量”长期遗留下来的错误和问题。这个跨平台的工具也将整体提升性能。


在全新的设置向导和登录界面（见下面的图片）旁边是几个重新设计过的启动画面。


![Login Screen ](/Asserts/Images/album/201407/25/142130ygx66ggbzfbf6xvb.jpg)


登录界面


![Setup Screen](/Asserts/Images/album/201407/25/142132gu7l62lxuvku7c6e.jpg)


设置界面


![Congratulations Screen ](/Asserts/Images/album/201407/25/142133mj7j0mejjm9vk9vs.jpg)


欢迎界面


### 目前还不稳定


Dropbox开发人员提醒参与测试的人，目前大部分新界面“还很粗糙”，在使用中可能会碰到大量的界面问题。新界面还不能配合一些辅助工具一起工作，例如屏幕阅读器。


![](/Asserts/Images/album/201407/25/142135qxuw61t643336116.jpg)


新UI使用了（目前）系统自带的Qt界面主题。它本身也不算很丑，不过在Ubuntu桌面上看起来不怎么合适，特别是和之前的版本比较。据说内存占用也变多了，在空闲情况下有时候会从60MB一下子跳到178MB。那些使用低端设备的人应该忍耐一下试用这个版本的诱惑－至少在这个特别的问题解决之后。


Dropbox 2.11.0 (试验版本) for Linux的完整改动日志：


* 用Qt重写了Windows & Linux界面
* 在移动和重命名文件后会尝试识别
* 新的设置／登录体验
* 更快上传小文件
* 新的启动画面


### 下载Dropbox Linux Build 2.11.x


想尝鲜的话，可以通过下面的链接下载和你系统对应的安装包。


* [Dropbox Experimental (64bit) Offline Linux Installer](https://d1ilhw0800yew8.cloudfront.net/client/dropbox-lnx.x86_64-2.11.0.tar.gz)
* [Dropbox Experimental (32bit) Offline Linux Installer](https://d1ilhw0800yew8.cloudfront.net/client/dropbox-lnx.x86-2.11.0.tar.gz)


下载完后，解压到主目录。它默认是隐藏的，所以打开终端，’cd‘到‘.dropbox-dist/dropbox-lnx‘目录下，然后运行‘./dropbox start‘。


演示Dropbox终端操作的gif动画：


![](/Asserts/Images/album/201407/25/142137dha5bqlvqzlkklbq.gif)




---


via: <http://www.omgubuntu.co.uk/2014/07/dropbox-experimental-linux-build-qt-rewrite>


原文作者：[Joey-Elijah Sneddon](https://plus.google.com/117485690627814051450/?rel=author) 译者：[zpl1025](https://github.com/zpl1025) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
