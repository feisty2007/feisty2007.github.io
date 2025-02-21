---
layout: post
title:	"你现在可以在 Arch Linux 上安装 Unity 7.6 桌面了"
date:	2022-12-04 11:31:13 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Unity]
---



> 
> 想在 Arch Linux 上试试 Unity 吗？现在可以了！
> 
> 
> 


![](/Asserts/Images/album/202212/04/113114x15r1rq321pwk2pz.png)


Unity Desktop 是由 Canonical 构建的经典桌面环境，它从 2010 年到 2017 年是 Ubuntu 的一部分，但为了支持 GNOME 而放弃。


我们认为它永远被杀死了。但它卷土重来。


今年早些时候，自 2016 年 5 月上次更新以来，经过长达 6 年的时间，Unity 的改进版本发布了。


开发由一位年轻的开发人员 [Rudra Saraswat](https://about.ruds.io) 带头，他也是 [Ubuntu Unity](https://about.ruds.io) 的创建者，它现在是 Ubuntu 的官方版本。


Unity 7.6 的发布标志着大量改进的到来。


而且，更进一步，Unity 7.6 已可用于 Arch Linux。开发者提到：



> 
> 此移植基于 chenxiaolong （于 2011-2016 年维护）的早期成果 Unity-for-Arch。
> 
> 
> 


### 在 Arch Linux 上试用 Unity 7.6


![unity on arch linux](/Asserts/Images/album/202212/04/113115fh8i92nn85i1vnsn.jpg)


首先，你必须确保你已经安装了 Arch Linux。


然后你可以按照以下步骤在 Arch Linux 上运行 Unity 7.6：


安装 [Paru](https://itsfoss.com/paru-aur-helper/)，它是一个 AUR 助手。


使用 `paru -S unity-installer-arch` 安装名为 `unity-installer-arch` 的脚本。


在 TTY/终端窗口中运行 `unity-installer-arch`。


选择 “<ruby> 安装 Unity 桌面 <rt>  Install Unity desktop </rt></ruby>”。


将默认显示管理器更改为 `lightdm`。


使用 `unity-greeter` 作为默认登录界面。


我的同事 Sreenath 尝试了一下，在安装过程中，由于多重依赖冲突，他不得不从全新的 Arch 开始。


对你来说可能有所不同，但请记住这一点。如果你不想花时间在这上面，你可能想试试 [Ubuntu Unity](https://ubuntuunity.org)。


### 总结


对于 Unity 桌面爱好者来说，这是一件好事。更多发行版可能会考虑使用带有 Unity 桌面的变体。


你想让那发生吗？


? 你是 Unity 桌面的用户吗？想试试看么？在评论区分享你的观点。




---


via: <https://news.itsfoss.com/unity-arch-linux/>


作者：[Sourav Rudra](https://news.itsfoss.com/author/sourav/) 选题：[lkxed](https://github.com/lkxed) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
