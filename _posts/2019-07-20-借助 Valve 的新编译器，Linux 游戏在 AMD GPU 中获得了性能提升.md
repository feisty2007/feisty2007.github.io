---
layout: post
title:	"借助 Valve 的新编译器，Linux 游戏在 AMD GPU 中获得了性能提升"
date:	2019-07-10 12:54:23 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,AMD,游戏]
---


Steam 寻求公众反馈以便为 AMD GPU 测试 ACO（一个新的 Mesa [着色器](https://en.wikipedia.org/wiki/Shader)编译器）已经有几天了。


目前，AMD 驱动程序使用 LLVM 作为着色器编译器。而 [Mesa](https://en.wikipedia.org/wiki/Mesa_(computer_graphics)) 则是一个开源的 [LLVM](https://en.wikipedia.org/wiki/LLVM) 的替代品。因此，在这种情况下，Valve 希望支持 AMD 显卡以提高 Linux 游戏在各种 Linux 发行版上的性能。


![](/Asserts/Images/album/201907/10/125425yshoefsnoodenmo2.png)


为了提高游戏性能，编译时间至关重要，使用新的 ACO 编译器，它将时间缩短了近 50％。 Valve 在其 [Steam 社区](https://steamcommunity.com/games/221410/announcements/detail/1602634609636894200)的帖子中解释了更多关于它的信息：



> 
> AMD OpenGL 和 Vulkan 驱动程序目前使用的着色器编译器是上游 LLVM 项目的一部分。该项目规模庞大，并且有许多不同的目标，游戏着色器的在线编译只是其中之一。这可能会导致不同的开发权衡，其中改进游戏特定功能比其他情况更难，特定于游戏的功能也经常被 LLVM 的开发人员因其他事情破坏。特别是，着色器编译速度就是这样一个例子：它在大多数其他场景中并不是一个关键因素，只能锦上添花。但是对于游戏来说，编译时间是至关重要的，而缓慢的着色器编译可能导致几乎无法播放的顿挫。
> 
> 
> 


### Linux 游戏真的有性能提升吗？


是的，没错。


这里的主要亮点是编译时间。如果着色器编译时间急剧减少，理论上应该会改善游戏的性能。


而且，根据[最初的基准报告](https://gist.github.com/pendingchaos/aba1e4c238cf039d17089f29a8c6aa63)，我们确实看到了一些重大改进。


![](/Asserts/Images/album/201907/10/125427vwi4fhihn4zbbdy3.png)


当然，游戏中的 FPS 改进并不是很大。但是，它在早期阶段仍然是一个很好的进步。


如果你对编译时间的改进感到好奇，下面是结果：


![](/Asserts/Images/album/201907/10/125428rlyipzpt93wsytck.png)


是的，即使大幅的编译时间减少也不会大幅影响游戏中的 FPS。但是，它仍然是一件大事，因为目前，这是一项正在进行中的工作。所以，我们可以有更多期待。


但是，还能做些什么呢？


好吧，ACO 还没完成。下面是为什么（在 Valve 中提到）：



> 
> 现在，ACO 只处理像素和计算着色器阶段。当其余的阶段实现时，我们预计编译时间将进一步减少。
> 
> 
> 


#### 总结


尽管我没有配备 AMD GPU，但我很有兴趣看到对 Linux 游戏场景的改进。


此外，随着事情进展，我们将期待更多的基准和报告。


你怎么看待？请在下面的评论中告诉我们你的想法。如果你有基本报告要分享，请告诉我们。




---


via: <https://itsfoss.com/linux-games-performance-boost-amd-gpu/>


作者：[Ankush Das](https://itsfoss.com/author/ankush/) 选题：[lujun9972](https://github.com/lujun9972) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
