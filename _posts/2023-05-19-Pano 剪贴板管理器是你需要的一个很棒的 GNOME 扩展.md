---
layout: post
title:	"Pano 剪贴板管理器是你需要的一个很棒的 GNOME 扩展"
date:	2023-05-22 15:23:19 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,剪贴板]
---



> 
> 一个灵巧的剪贴板管理器，提供视觉丰富的界面和有价值的选项。
> 
> 
> 


![pano clipboard manager](/Asserts/Images/album/202305/22/152319d7gk44zem6moemvy.jpg)


你知道，有一种比 `Ctrl+C`/`Ctrl-V` 更好的方法来处理剪贴板文本。不，我不是在谈论使用右键单击菜单。


我是指使用一个**合适的剪贴板管理器**。而且，不仅仅是一个普通的剪贴板管理器，而是一个非常有用的东西。如果你喜欢，我相信它将成为 [Linux 上必不可少的应用程序](https://itsfoss.com/essential-linux-applications/?ref=news.itsfoss.com) 之一。


认识 Pano 剪贴板管理器。让我告诉你它能做什么。


### Pano 剪贴板管理器：概述 ⭐


![a screenshot of how pano looks on gnome](/Asserts/Images/album/202305/22/152320yxryoppfcvyptoxp.jpg)


Pano 是一个**易于使用且高度可定制的剪贴板应用**，它在一个非常紧凑的包中提供了一些很好的实用程序（以 GNOME 扩展的形式）。


它可以让你存储任何东西，从文本和表情符号，一直到颜色。


正如你在上面看到的，**复制的内容根据其类型进行分类，并在界面中整齐排列。**


除此之外，当你复制某些内容时，它会显示一个漂亮的通知，其中包含复制内容的简短预览。


![a screenshot showing the notification feature of pano](/Asserts/Images/album/202305/22/152320tvcc4rskkxc0q7yx.png)


该扩展**最近进行了更新**，进行了全面的视觉改造，并重新设计了托盘图标、占位符图像等。


你现在可以在配置菜单中调整 Pano 的高度，以及自定义背景颜色和不透明度、调整内容类型、字体大小等。


![pano customization options](/Asserts/Images/album/202305/22/152322u2oo25yoseh6ok2e.png)


但是，当我的同事 Shivam 试用 Pano 时，他发现它**还会将密码从 Bitwarden** 复制到剪贴板。


我必须说，这是 Pano 的一个失误。它应该有排除特定应用的选项，如密码管理器。尽管如此，你应该是安全的，因为它没有云同步连接。


除此之外，这里有一些快捷方式可以在使用 Pano 时派上用场：


* 使用 `super+shift+V` 来切换 Pano。
* 使用 `ctrl+super+shift+V` 来进入隐身模式，以处理那些隐私剪贴板文本。
* 使用 `←` 和 `→` 箭头键在项目之间导航。
* 使用 `↑` 和 `↓` 箭头键将焦点放在搜索框和项目上。
* 使用 `Ctrl+S` 将处于输入焦点的项目添加到收藏夹。


对于更多这样的快捷方式，你可以参考它的 [GitHub 仓库](https://github.com/oae/gnome-shell-pano?ref=news.itsfoss.com)。


让我们继续。


Linux 和 GNOME 有类似的应用可以提供此类功能，比如 [CopyQ](https://itsfoss.com/copyq-clipboard-manager/?ref=news.itsfoss.com)。


但 Pano 提供的功能**有点不同**，尤其是在如此紧凑的包中。


### ? 获取 Pano 剪贴板管理器


你可以从 [Gnome 扩展网站](https://extensions.gnome.org/extension/5278/pano/?ref=news.itsfoss.com) 获取 Pano，或单击下面的下载按钮获取它：



> 
> **[Pano 剪贴板管理器](https://extensions.gnome.org/extension/5278/pano/?ref=news.itsfoss.com)**
> 
> 
> 


请记住，它需要两个依赖项，[libgda](https://gitlab.gnome.org/GNOME/libgda?ref=news.itsfoss.com) 和 [gsound](https://wiki.gnome.org/Projects/GSound?ref=news.itsfoss.com) 才能工作，这可以使用以下命令完成：



```
sudo apt install gir1.2-gda-5.0 gir1.2-gsound-1.0

```

你还可以参考我们关于 [使用 GNOME 扩展](https://itsfoss.com/best-gnome-extensions/?ref=news.itsfoss.com) 的指南来启用它。




---


via: <https://news.itsfoss.com/pano-clipboard-manager/>


作者：[Sourav Rudra](https://news.itsfoss.com/author/sourav/) 选题：[lkxed](https://github.com/lkxed/) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
