---
layout: post
title:	"Bottles：在 Linux 上轻松安装 Windows 应用程序"
date:	2022-02-19 15:45:15 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Bottles,Windows,虚拟环境]
---



> 
> 随着最新发布的更新，Bottles 正在成为一个近乎完美的解决方案，无需任何特别的努力就可以在 Linux 上安装 Windows 应用程序。
> 
> 
> 


![](/Asserts/Images/album/202202/19/154515zeh5iixzaklhc35l.png)


你可以 [使用 Wine 在 Linux 上安装 Windows 应用程序](https://itsfoss.com/use-windows-applications-linux/)，但它并不适用所有的应用程序。此外，它还需要你手动配置东西。那么，有什么简单的选择呢？


虽然 [CrossOver](https://news.itsfoss.com/crossover-21-1-0-release/) 一直在尽力使这个过程更容易，但还另一个解决方案：Bottles。


随着 Bottles 的最新发布，它的目标是更加顺滑地以最小的调整来运行你喜欢的 Windows 应用程序。


### Bottles 2022.2.14 的新变化


该版本带来了一些新功能、改进和大量的错误修复。让我强调一下以下关键变化：


#### 安装程序


以下是开发者对新功能的介绍：



> 
> 这些是由 Bottles 解释的指令集，以重现程序的安装。这个过程是由维护者写在清单文件中的，他们能够按照同样的步骤安装程序。
> 
> 
> 


![](/Asserts/Images/album/202202/19/154516ikllxak554z49kck.png)


简单来说，这些一键式安装程序会自动安装软件，而不需要你手动调整什么。这类似于 [Lutris](https://lutris.net/) 帮助游戏玩家安装一个需要大量调整的游戏。


目前只有不多的几个安装程序，主要是第三方游戏启动程序。用户如果想安装像 Origin 这样的程序，可以简单地在他们的首选“瓶子”中进入安装程序部分，点击下载按钮。（LCTT 译注：“瓶子”指一个虚拟环境。）


开发人员还承诺，你可以期待很快有更多的安装程序。


#### 一个专门的应用程序商店


为了展示可用的安装程序，他们在其官方网站上推出了一个 [应用商店](https://usebottles.com/appstore/)。它包含了所有可用安装程序的列表和必要的信息，如依赖性、配置和支持的架构。用户可以期待更多有用的功能，如评论功能很快就会到来。


![](/Asserts/Images/album/202202/19/154517by59resoy15g1eer.png)


需要注意的一点是，并不是所有的安装程序都能完美无缺地工作。因此，开发者引入了一种叫做“等级”的东西，指的是安装的程序的顺利工作的程度。分级范围从铜级到白金级，与 Wine 的兼容性评级方式非常相似。


用户可以放心，每个安装程序至少都可以运行该程序并执行程序所需完成的主要功能。但除非安装程序被评为白金级，否则用户应该对错误、图形故障和崩溃的出现有所预期。此外，安装程序也会与还原点一起工作。


#### 新的搜索栏


拥有多个“瓶子”的用户现在可以使用全新的搜索功能来寻找特定的“瓶子”。请注意，它在默认情况下是隐藏的，如果你至少安装了 10 个“瓶子”，就会自动启用。


![](/Asserts/Images/album/202202/19/154518sgd7whwwai1pv0ah.png)


我觉得，作为搜索栏的基本功能应该已经实现了，总比没有强！


#### “瓶子”的自定义路径


以前，用户不能为“瓶子”设置自定义路径。在这个版本中，用户可以在偏好部分中实现这一功能。如果用户的存储空间不足，并计划使用一个单独的驱动器，这非常有帮助。


请注意，Flatpak 用户得专门为 Bottles 启用权限，以访问 Flatpak 环境之外的任何位置。你也可以试试 [Flatseal 来管理 Flatpak 的权限](https://itsfoss.com/flatseal/)。


#### 改进和错误修复


除了主要的功能升级外，还有一些有用的全面改进，一些值得强调的有：


* 可用于非 Flapak 软件包的运行环境，可通过首选项中的核心部分安装。
* 用户现在能够使用内置的任务管理器终止正在进行的进程。
* 用户还可以从位于上下文菜单中的终端中启动程序。
* 已经有了对 Gamescope 和 dxvk-async 组件的支持。


这个版本中也修复了各种基本的错误。其中包括 Flatpak 版本中游戏模式的修复，以及 DXVK 版本的改变，删除了初始备份。


你可以参考他们的 [官方发布说明](https://usebottles.com/blog/release-2022.2.14/) 来了解更多的技术细节。


### 总结


Bottles 的目标是成为每个运行 Windows 软件的 Linux 用户的必备应用。而且，有了所有这些改进，它看起来很有前景！


安装程序的增加应该对很多用户有极大的帮助。你怎么看？请在下面的评论中告诉我你的想法。




---


via: <https://news.itsfoss.com/bottles-2022-2-14-release/>


作者：[Rishabh Moharir](https://news.itsfoss.com/author/rishabh/) 选题：[lujun9972](https://github.com/lujun9972) 译者：[wxy](https://github.com/wxy) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
