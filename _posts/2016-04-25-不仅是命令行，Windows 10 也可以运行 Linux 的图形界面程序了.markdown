---
layout: post
title:	"不仅是命令行，Windows 10 也可以运行 Linux 的图形界面程序了"
date:	2016-04-12 21:53:18 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Windows 10]
---


正如大家所知道的，大多数 Linux 上的命令行二进制程序现在可以原生地运行在 Windows 10 里面了，这包括 Linux 上著名的 bash shell 以及很多重要的 Linux 程序，如：apt、ssh、 vim、 emacs、tar、 php、 perl、 python、 gcc 等等。


微软在 Build 2016 上[宣布这个新闻](/article-7177-1.html)后，很快就在其发布的 [Insider 预览版 14316](/article-7209-1.html) 上将这个功能展示给了迫不及待的粉丝们。根据微软当前的技术说明，目前除了部分命令行程序不能运行之外，还不支持 Linux 下的图形界面程序，比如 Firefox。


**然而，社区的智慧是无穷的！**


今天，我们“[发现](https://www.reddit.com/r/Windows10/comments/4ea4w4/fyi_you_can_run_gui_linux_apps_from_bash/)”了一种可以从 Windows 10 的 Bash 环境中启动图形界面的 Linux 程序的方法。一位名叫 [w2qw](https://www.reddit.com/user/w2qw) 的开发者找到了一个可以在 Bash 之外运行 X 服务器的方法，从而可以在 Windows 10 中运行原生的图形界面 Linux 程序了！


![](/Asserts/Images//attachment/album/201604/12/215326yomohrsw3q2vzhvj.png)


上图是从 Bash on Ubuntu on Windows 10 里面运行的 Firefox 和 Vim，还有 xeyes，看起来和 Windows 10 风格相当和谐 :D


要实现这个功能，你首先需要安装 [Xming X Server for Windows](https://sourceforge.net/projects/xming/)，然后在 Windows 10 的 Bash 中运行如下命令（你可以将 firefox 替换成你安装在 Bash 中其它图形界面的 Linux 程序）：



```
DISPLAY=:0 firefox
```

该开发者说，“显然，这要比原生的 Windows/Linux 应用慢一些，但是肯定比 VNC/X11 转发要快。”


[社区立刻被这个发现震惊了](https://www.reddit.com/r/Windows10/comments/4ea4w4/fyi_you_can_run_gui_linux_apps_from_bash/)，另外一些人表示也许可以在 Windows 中运行完整的 Linux 桌面，就如同有人[在 Windows 10 中编译运行了 Xfce 一样](https://www.reddit.com/r/unixporn/comments/4aokkr/xfce_xfce_running_in_windows10/)！！！Xfce —— 这可是很多 Linux 发行版的默认桌面环境！


![](/Asserts/Images//attachment/album/201604/12/215336sgfpbk5sl2pz2b8g.png)


面对这种脑洞大开的想法，笔者只能表示瞠目结舌，然而细思却有一定的道理。让我们期待有读者可以实现这个目标。
