---
layout: post
title:	"下一代独立式 GNU/Linux 应用打包格式 Flatpak 发布"
date:	2016-06-24 10:31:26 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Flatpak,XDG-App,Snap]
---


GNOME 项目组的 Allan Day [正式发布](http://flatpak.org/press/2016-06-21-flatpak-released.html)了 Flatpak。


![](/Asserts/Images/album/201606/24/103127a774ydcqgr6u76bq.jpg)


这并不是我们第一次提及 Flatpak，你可能已经知道它是一个无依赖关系的、跨发行版的软件打包框架，它可以让用户在多个基于 Linux 内核的操作系统上使用各种桌面应用程序。有些人可能记得 Flatpak 之前的名字叫做 XDG-App。


Flatpak 是应 GNU/Linux 和开源软件开发者所需而出现的，可以让他们在多个桌面平台、操作系统上发行软件时，不用花费几个小时乃至几天来为各个主要 Linux 发行版进行打包工作。


Flatpak 的首席开发者 Alexander Larsson 说，“Linux 上的应用开发者总是不能直接接触到他们的用户，但是 Flatpak 改变了这种情况，开发者们现在能够真正知道他们的用户要的是什么。这次 Flatpak 的发布让这一切变为现实。”


### 以安全为主导的设计


据 Flatpak 开发团队称，几个重要的开源项目已经为其支持的操作系统以 .flatpak 格式发布了他们的应用，这些开源项目包括 LibreOffice、InkScape、GIMP、MyPaint 和 Darktable。作为 GNOME 项目开发的一部分，几个来自 GNOME 家族的应用也会以 Flatpak 格式打包。


我们之前刚刚说过，[即将发布的 LibreOffice 5.2 办公套件将采用 Flatpak 格式打包](http://news.softpedia.com/news/libreoffice-5-2-beta-now-available-as-a-flatpak-for-common-linux-distributions-504773.shtml)，支持各种常见的发行版，包括 Arch Linux、Debian、Ubuntu、Fedora、Mageia 和 Gentoo 等。 此外，图形化软件包管理器“GNOME 软件”也[支持](http://news.softpedia.com/news/gnome-software-package-manager-has-just-received-support-for-flatpak-packages-504397.shtml) Flatpak 格式。


但最棒的是，Flatpak 是围绕安全进行设计的，它为用户提供了沙盒技术，打包在其中的应用软件只能访问 Flatpak 容器内部和宿主库以及操作系统接口。


“下一个 Flatpak 主要版本将全部都是沙盒化的”， Alexander Larsson 在 Flatpak 的[官方声明](http://flatpak.org/press/2016-06-21-flatpak-released.html)中说，“应用作者会在沙盒中看到一套与操作系统交互的更完整界面。”


要更多了解 Flatpak，请访问其[官网](http://flatpak.org/getting.html)，你可以找到在上述提及的 GNU/Linux 操作系统中的安装建议。如果尚不支持你的操作系统，也不用担心，Flatpak 正在不断支持其它的发行版，相信很快就能看到。
