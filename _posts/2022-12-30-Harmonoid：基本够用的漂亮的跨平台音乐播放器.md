---
layout: post
title:	"Harmonoid：基本够用的漂亮的跨平台音乐播放器"
date:	2022-12-27 17:37:21 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,音乐播放器]
---


![](/Asserts/Images/album/202212/27/173656kmq05d54llttls55.jpg)


幸运的是，[Linux 的优秀开源音乐播放器](https://itsfoss.com/best-music-players-linux/) 并不缺乏。过去我们已经介绍了多种选择。


在这里，我重点介绍一款免费使用（但不是自由开源软件），可用于多种平台（包括 Linux、Windows 和 Android）的音乐播放器。


### Harmonoid：Material Design 的直观用户体验


![harmonoid player](/Asserts/Images/album/202212/27/173721q24r46ypryr42nkg.png)


Harmonoid 是用 Dart 语言编写的。它利用 [libmpv](https://github.com/mpv-player/mpv/tree/master/libmpv) 和 [mpv](https://mpv.io) 在桌面平台上实现媒体播放功能。


它提供了一个优秀的用户界面。并且不使用 electron.js。所以，如果你讨厌 Electron，你可以试试这个。


通常，你会在 Android 上看到应用具有 Material Design UI。如果你不知道，Material 是谷歌的开源设计系统。


![harmonoid player info](/Asserts/Images/album/202212/27/173721t5j8v1t51vgkm0oe.png)


没有多少创作者将它用于桌面应用。作为一种改变，Harmonoid 具有 Material Design 用户体验，可以同时做到快速和直观。


这让 Harmonoid 为 Linux 用户呈现了独特的用户体验。动画感觉流畅且易于导航，并提供大量有价值的功能来帮助管理你的音乐库。


![harmonoid url](/Asserts/Images/album/202212/27/173722hbxf7srpd7q7x3b3.png)


如果你想要一个有良好 UI 和功能集的音乐播放器，我建议你尝试一下 Harmonoid。


### Harmonoid 的特点


![harmonoid player options](/Asserts/Images/album/202212/27/173722apx5wtpmtz45ftfu.png)


[Harmonoid](https://harmonoid.com) 可能看起来像一个简单的音乐播放器，但它包含了一些最有价值的功能。他们包括：


* 跟唱功能，你可以找到歌词，或者你可以手动添加它们
* 编辑歌曲详细信息，包括艺术家、年份、流派、曲目编号、专辑和标题
* 轻松分类和排序你的音乐列表
* 一个快速搜索功能来找到你要找的东西
* 缓存元数据以在你每次加载时提供快速体验
* 与 Windows 和 Linux 的良好集成支持
* 支持在 Discord 中展示，可以显示你的音乐以及插图和播放按钮
* 调整音乐的速度、音量和音高
* 原始元数据读取器可读取你库中任何文件或歌曲的标签
* 播放由 MPV 提供
* .LRC 文件兼容性
* 支持在线 URL（YouTube）和广播流
* 跨平台
* 多位艺术家支持
* 深色/浅色模式


除了这些之外，还有一些小功能可以发挥很大的作用，例如**无缝播放和上下文菜单集成，并且它通常是一个轻量级应用**。


Harmonoid 应该非常适合想要同时播放音乐或整理收藏的用户。我会说它提供了两全其美的方法。


![harmonoid settings](/Asserts/Images/album/202212/27/173723gx9mi5xo4hh56909.png)


### 在 Linux 上安装 Harmonoid


你可以从其 [下载页面](https://harmonoid.com/downloads) 获取 .deb/.rpm 包并将其安装在基于 Ubuntu 的发行版或 Fedora 上。


此外，你需要使用以下命令安装 mpv 和 libmpv（对于 Ubuntu）：



```
sudo apt install mpv lipmpv-dev

```

确保安装这些软件包可以让你用 Harmonoid 处理所有类型的文件进行播放。


你还可以在 [AUR](https://aur.archlinux.org/packages/harmonoid-bin) 上找到基于 Arch 的发行版的 Harmonoid。要探索有关该播放器的更多信息，请访问其 [GitHub 页面](https://github.com/harmonoid/harmonoid)和[官方网站](https://harmonoid.com)。


你是否尝试过 Harmonoid 在你的 Linux 系统上播放和整理音乐？ 你最喜欢的 Linux 音乐播放器是什么？ 在下面的评论中让我知道你的想法。




---


via: <https://itsfoss.com/harmonoid/>


作者：[Ankush Das](https://itsfoss.com/author/ankush/) 选题：[lkxed](https://github.com/lkxed) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
