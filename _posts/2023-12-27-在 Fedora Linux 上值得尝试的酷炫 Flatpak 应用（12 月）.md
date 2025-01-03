---
layout: post
title:	"在 Fedora Linux 上值得尝试的酷炫 Flatpak 应用（12 月）"
date:	2023-12-10 17:40:15 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,Flatpak]
---


![Daimar Steiner 摄](/Asserts/Images/album/202312/10/174017x1hvhu5jhutyvyjc.jpg)


本文介绍了 Flathub 中可用的项目以及安装说明。


[Flathub](https://flathub.org) 就是为所有 Linux 发行版提供应用程序的平台，其由 Flatpak 支持，确保 Flathub 上的应用能在绝大多数 Linux 发行版上运行。


请参阅 [Flatpak 入门](https://fedoramagazine.org/getting-started-flatpak/)，并按照 [flatpak 网站](https://flatpak.org/setup/Fedora)的指南激活 Flathub 作为你的 Flatpak 供应商。


### Live Captions


Live Captions 是一款为 Linux 桌面提供实时自动字幕的应用。目前仅提供英语。其他语言可能会产生乱码或错误的语音翻译。


主要特性：


* 使用友好的界面
* 基于深度学习，为本地桌面/麦克风音频添加字幕
* 不需要 API 密钥、不依赖专有服务/组件、无追踪、无数据收集、不使用互联网权限
* 支持调整字幕字体、字体大小，以及进行大小写转换
* 不确定的文本会显示为暗色（此功能可进行设置）。


老实说，直到最近有人推荐我才知道这个应用，我感到非常惊讶。这对于有听力问题的人来说确实很有帮助。正如此类软件的常见情况，模型需要培训，而项目通常需要反馈。


Live Captions 需要良好的硬件才能正常运行，但不需要专业的 GPU。


该项目被标记为安全，因为它不需要特殊许可：


![](/Asserts/Images/album/202312/10/174017vq5yj4okxcc9xcfj.png)


你可以通过单击网站上的安装按钮或手动使用以下命令来安装 “Live Caption”：



```
flatpak install flathub net.sapples.LiveCaptions

```

### Pencil2D


[Pencil2D](https://flathub.org/apps/org.pencil2d.Pencil2D) 是一个 2D 动画创建程序，可让你使用位图和矢量图形轻松创建手绘图形。


主要特性：


* 轻量设计
* 支持光栅和矢量图
* 跨平台兼容
* 自由开源


请注意，该项目被标记为“潜在不安全”，因为它可以访问你的文件系统：


![](/Asserts/Images/album/202312/10/174017o5yqdlpndcoil56o.png)


你可以通过单击网站上的安装按钮或手动使用以下命令来安装 “Pencil2D”：



```
flatpak install flathub org.pencil2d.Pencil2D

```

**Pencil2D 也在 Fedora 的仓库中以 RPM 形式提供**


### Frog


[Frog](https://flathub.org/apps/com.github.tenderowl.frog) 是一款应用，它可以帮助你从图片、网站、视频和二维码中提取文本。


主要特性：


* 提取二维码和条形码：能够快速捕获、提取并转译二维码和条形码。
* 你可以直接拖放图像到 Frog 窗口中提取文本，无需进行截图。
* 支持大量语言：Frog 支持多种语言，甚至包括那些它以前不支持的语言。
* 隐私：Frog 使用门户网站尊重你的隐私


请注意，该项目被标记为“潜在不安全”，因为它可以访问你的主文件夹：


![](/Asserts/Images/album/202312/10/174017jx23ff1c0w2oc22f.png)


你可以通过单击网站上的安装按钮或手动使用以下命令来安装 “Frog”：



```
flatpak install flathub com.github.tenderowl.frog

```

### PDF Arranger


[PDF Arranger](https://flathub.org/apps/com.github.jeromerobert.pdfarranger) 是一个小型应用，它可以帮助用户使用交互式直观的图形界面合并或拆分 PDF 文档并旋转、裁剪和重新排列其页面。


其简明的界面和易于使用的功能都非常出色。


请注意，该项目被标记为“潜在不安全”，因为它可以访问你的文件系统：


![](/Asserts/Images/album/202312/10/174018po8hcs4h11wkqzw1.png)


你可以通过单击网站上的安装按钮或使用以下命令手动安装 “PDF Arranger”：



```
flatpak install flathub com.github.jeromerobert.pdfarranger

```

**PDF Arranger 也在 Fedora 的仓库中以 RPM 形式提供。**




---


via: <https://fedoramagazine.org/fedora-linux-flatpak-cool-apps-to-try-for-december/>


作者：[Eduard Lucena](https://fedoramagazine.org/author/x3mboy/) 选题：[lujun9972](https://github.com/lujun9972) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
