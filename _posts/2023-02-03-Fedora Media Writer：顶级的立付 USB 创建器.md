---
layout: post
title:	"Fedora Media Writer：顶级的立付 USB 创建器"
date:	2023-02-01 16:30:00 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,ISO,USB]
---



> 
> 关于安装和使用 Fedora Media Writer 从 Linux 和 Windows 创建立付 USB 的教程。
> 
> 
> 


![Fedora Media Writer](/Asserts/Images/album/202302/01/163445oc5x42zhhtbu2hhl.jpg)


### Fedora Media Writer


社区和 Fedora Linux 团队开发并维护了 [Fedora Media Writer 应用](https://github.com/FedoraQt/MediaWriter)。这个应用可以将任何 ISO 镜像写入你的闪存盘（U 盘）中。此外，Fedora Media Writer 还有直接从 Fedora 镜像中下载 ISO 文件的功能，前提是你有一个稳定的互联网连接。


此外，它还为你提供了一个下载选项列表：比如官方版本、新兴版本、定制版和实验室版本的镜像。


不仅如此，你还可以使用这个灵巧的工具将任何其他 ISO 镜像写入你的闪存。它不总是需要 Fedora ISO。


虽然有其他流行的工具可以用来创建 <ruby> 立付 <rt>  Live </rt></ruby> USB ，比如 [Etcher](https://www.debugpoint.com/2021/01/etcher-bootable-usb-linux/)、Ventoy 和 Rufus，但考虑到该团队是从主流 Fedora Linux 与贡献者一起开发的，你仍然可以尝试使用此程序。



> 
> **LCTT 译注**：特此说明一下使用 “立付” 一词作为 “Live” 的中文翻译。
> 
> 
> Live 原意多指“现场”、“实时”，在计算机环境中使用时也多引用此意。但对它的翻译就颇费神，因为无论是在 Live Patch，还是更多见的 Live USB/CD、Live Session，其实都不好翻译为“现场”、“实时”。
> 
> 
> 提议者之前曾经尝试创造了新的“[临场](/article-12854-1.html)”词汇，但是感觉有些不够达意。经过推敲，提议者再次推荐使用“立付”，在照顾发音的同时，取其“立时交付”之意。这样，Live USB/CD 可以译做 “立付 USB/CD”，Live Session 可以译做 “立付会话”。
> 
> 
> 详见我们发布的[《LCTT 术语词典》](/article-15496-1.html)。
> 
> 
> 


因此，综上所述，这里是 Fedora Media Writer 的快速功能亮点。


#### Fedora Media Writer 的功能摘要


* 适用于 Linux、Windows 和 macOS
* 直接下载 + 写入镜像到 USB 闪存
* 官方版本（Workstation、IoT、Server）下载
* 新兴版本（Silverblue、Kinoite）下载
* 定制版（KDE Plasma、Xfce 等）
* 实验室（Fedora Astronomy、Robotic 等）
* 可作为 Linux 发行版的 Flatpak 包
* 同时，可以将任何其他 ISO 镜像（非 Fedora）写入 U 盘。
* 能够格式化 U 盘，恢复 U 盘
* 基于 Qt


### 如何安装


#### Linux


Fedora Media Writer 以 Flatpak 的形式提供给 Linux 发行版。要在任何 Linux（如 Fedora、Ubuntu 或 Linux Mint）中安装它，请 [按照这个指南设置 Flatpak](https://flatpak.org/setup/)。


然后，点击下面的链接进行安装。这将启动你的 Linux 发行版的官方软件程序（如 <ruby> 发现 <rt>  Discover </rt></ruby>应用、GNOME <ruby> 软件 <rt>  Software </rt></ruby> 应用）。安装后，你可以通过应用程序菜单启动它。



> 
> **[以 Flatpak 形式安装 Fedora Media Writer](https://dl.flathub.org/repo/appstream/org.fedoraproject.MediaWriter.flatpakref)**
> 
> 
> 


#### Windows


如果你是一个计划迁移到 Linux（如 Fedora）的 Windows 用户，它是一个完美的工具。你需要从 GitHub 上下载 exe 安装程序（链接如下），并按照屏幕上的指示进行安装。



> 
> **[用于 Windows 的最新安装程序（exe）](https://github.com/FedoraQt/MediaWriter/releases/latest)**
> 
> 
> 


安装完成后，你可以从开始菜单启动它。


#### macOS


对于 macOS，你可以在上述链接中获取 dmg 文件。



> 
> **[用于 macOS 的最新安装程序（dmg）](https://github.com/FedoraQt/MediaWriter/releases/latest)**
> 
> 
> 


### 如何使用 Fedora Media Writer 在 Linux 中创建立付 USB


第一个页面给你两个主要选项。<ruby> 自动下载 <rt>  Download automatically </rt></ruby> 选项用于即时下载 ISO 镜像。第二个选项是直接从你的磁盘上写入已经下载的 ISO 文件。


如果你已经插上了 USB，你应该看到它是第三个选项。第三个选项是格式化并删除你 U 盘中的所有数据，并将其恢复到出厂设置。


此外，你也可以用这个工具来格式化你的 USB 闪存。你不需要任何命令或任何花哨的东西。需要注意的一点是，这个选项只有在你的 U 盘有数据时才可见。如果它已经被格式化了，该工具可以检测到它，但不会显示恢复它的选项！! ?


#### 自动下载和写入


![Fedora Media Writer - 第一个页面](/Asserts/Images/album/202302/01/163500ohe131x3248epxsu.jpg)


 


<ruby> 自动下载 <rt>  Download automatically </rt></ruby>选项为你提供了以下页面，可以从镜像中下载任何你想要的 Fedora ISO。这对很多人来说很有用，因为它消除了单独下载 ISO 文件、验证校验和等的麻烦。


![自动下载选项给了你这些选项](/Asserts/Images/album/202302/01/163518o54sr2d42njfzzaa.jpg)


在选择了发行版之后，最后的页面会给你版本（Fedora 36、35 等）和架构（x86、ARM 等）的选项。另外，你应该看到目标 USB。点击 “<ruby> 下载并写入 <rt>  Download &amp; Write </rt></ruby>”，开始这个过程。


![Fedora Media Writer 的最终写入页面](/Asserts/Images/album/202302/01/163526fiztloggeiee3esp.jpg)


#### 从磁盘上写入一个现有的 ISO 文件


当你选择 “<ruby> 选择 ISO 文件 <rt>  select .iso file </rt></ruby>” 时，你可以从系统中选择该文件。之后，选择目标 USB 驱动器，然后点击 “<ruby> 写入 <rt>  Write </rt></ruby>”，开始这个过程。


![通过 Fedora Media Writer 直接写入 ISO](/Asserts/Images/album/202302/01/163536sq0j902qjq33x838.jpg)


![写入进行中](/Asserts/Images/album/202302/01/163545u3m070gg2d0yg0g0.jpg)


![写入完成](/Asserts/Images/album/202302/01/163553t9h7sorehp77rrcv.jpg)


写入操作完成后，你可以看到如上所示的确认信息。在我的测试中，写一个大约 3GB 的 ISO 需要大约 3 到 4 分钟。


### 使用 Fedora Media Writer 在 Windows、macOS 中创建 LIVE USB


在 Windows 和 macOS 中使用这个工具的步骤是一样的，就像上面显示的 Linux 一样。你可以在安装后轻松找到快捷方式，并以同样的方式启动。


![在 Windows 11 中运行](/Asserts/Images/album/202302/01/163606z3kah1mzul3km3l9.jpg)


### 结束语


我希望本指南能帮助你在日常的 USB 写入工作中使用 Fedora Media Writer。另外，这个工具的好处是你可以用它来格式化/恢复你的 U 盘。你不再需要 GParted 或 GNOME <ruby> 磁盘 <rt>  Disks </rt></ruby> 应用了。


对于 Linux、Windows 和 macOS 用户来说，这是一个非常棒的程序。


加油。




---


via: <https://www.debugpoint.com/fedora-media-writer/>


作者：[Arindam](https://www.debugpoint.com/author/admin1/) 选题：[lkxed](https://github.com/lkxed) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
