---
layout: post
title:	"硬核观察 #375 龙芯被指 LoongArch 的内核代码复制 MIPS 代码"
date:	2021-08-26 16:05:29 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,龙芯,Python,微软]
---


![](/Asserts/Images/album/202108/26/160415ncokoeac62fkdr0z.jpg)


### 龙芯被指 LoongArch 的内核代码复制 MIPS 代码


![](/Asserts/Images/album/202108/26/160426hvv8txgvuv2mgvft.jpg)


龙芯今年夏天推出了 3A5000 处理器，该处理器建立在龙芯的 LoongArch 指令集架构（ISA）上，龙芯将其描述为“一种新的 RISC ISA”。但 Linux 内核的上游维护者在审查 LoongArch 提交的代码时[质疑](https://lore.kernel.org/lkml/87pmu1q5ms.wl-maz@kernel.org/)，“你一直说 ‘不是 MIPS’，但我看到的只是 MIPS 代码的盲目复制。”在对提交的代码给出一些具体意见之后，维护者最后说，“从我审查的第一个版本以来，我没有看到太多进展。这仍然是同样过时的、破碎的 MIPS 代码，只是换了个名字而已。”据外媒 Phoronix [称](https://www.phoronix.com/scan.php?page=news_item&px=LoongArch-MIPS-Copy-Kernel)，LoongArch 的一些补丁确实是新的，但到目前为止还没有指出这些处理器的任何突破性的差异或令人兴奋的新功能，不幸的是，龙芯科技的公开文档也没有显示任何 ISA 差异等。



> 
> 如果龙芯不能拿出本质上不同的改进，估计会被内核社区拒绝。
> 
> 
> 


### IEEE 调查显示 Python 才是最流行的编程语言


![](/Asserts/Images/album/202108/26/160453g2rsbzuuszx71tzb.jpg)


根据 IEEE 的[研究](https://spectrum.ieee.org/top-programming-languages-2021)，Python、Java、C 和 C++ 是前四名编程语言。而通常在此类调查中名列前茅的 JavaScript 排在第五位。相比之下，StackOverflow 本月早些时候报告说，JavaScript 成为使用最多的语言。Redmonk 的分析师也把 JavaScript 放在首位，开发者工具公司 JetBrains 在其开发者生态系统状况调查中也是如此。IEEE 调查的[数据源](https://spectrum.ieee.org/ieee-top-programming-languages-design-methods-and-data-sources)来自 8 个来源的 11 个指标。IEEE 调查结果不同的原因可能是，虽然 JavaScript 可能是最受欢迎的语言，但它肯定不是搜索量最大或谈论最多的。



> 
> 不管最流行的到底是 Python 还是 JavaScript，至少该学会其中一种。
> 
> 
> 


### 微软将不再允许 Chromebook 用户安装原生安卓 Office 应用


![](/Asserts/Images/album/202108/26/160510bhoejhhcavikopxi.jpg)


从 9 月中旬开始，微软将建议想运行 Office 软件的 Chromebook 用户使用基于 Web 的 Office 应用，但将继续为其他安卓平台提供原生 Office 应用。微软解释说，网页版的应用程序“为 Chrome OS/Chromebook 用户提供了最优化的体验”。8 月 13 日，微软更新了其关于“[如何在 Chromebook 上安装和运行微软 Office](https://support.microsoft.com/en-us/office/how-to-install-and-run-microsoft-office-on-a-chromebook-32f14a23-2c1a-4579-b973-d4b1d78561ad)”的支持页面："安卓版本的 Office、Outlook、OneNote 和 OneDrive 目前在 Chromebook 上不被支持。“而在上周之前，同样的支持页面还建议 Chromebook 用户从 Google Play 商店安装 Office 应用程序的原生安卓版本。



> 
> 这是微软看 Chrome OS 十分不顺眼了啊。
> 
> 
>
