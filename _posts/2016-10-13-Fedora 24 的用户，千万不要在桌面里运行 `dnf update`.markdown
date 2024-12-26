---
layout: post
title:	"Fedora 24 的用户，千万不要在桌面里运行 `dnf update`"
date:	2016-10-06 20:58:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Fedora,dnf]
---


前几天，Fedora 项目组的 Adam Williamson [发布一则服务公告（PSA）](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/7ULAG243UNGTOSL6URGNG23GC4B6X5GB/)，提醒 Fedora 社区在内部更新过程中出现了严重问题！


许多 Fedora 24 的用户报告称，从 4 日起，当他们在桌面中运行 `dnf update` 命令，通过官方软件仓库更新软件时会遇到 “duplicated packages” 和 “kernel updates not working” 等错误。


![](/Asserts/Images/album/201610/06/205757x4a43qqavau64a4p.jpeg)


经过一些调查，Williamson 得出结论在 dnf update 过程中存在一个 bug，会导致图形界面，比如 GNOME 或 KDE，甚至整个 X Window 系统（X11）崩溃，但是这与用户的硬件配置和安装的软件有关。


“当崩溃发生时，更新进程会被杀死以至于不能完整结束，这就是为什么会得到 ‘duplicated packages’ 或其它的奇怪错误的原因”，Adam Williamson 说，“我在努力和报告者配合调查原因，希望能够解决它，但是，此刻，**不要在桌面里面运行 `dnf update` !**”


所以，如果你正在使用 Fedora 24 操作系统，当你在使用 KDE、GNOME、Xfce 等桌面环境时，千万不要执行 `dnf update` 命令。你可以通过按下 Ctrl+Alt+F3 切换到文本模式来执行它，或者使用离线更新系统。


截止到现在，该 bug 仍无修复完成的通知。
