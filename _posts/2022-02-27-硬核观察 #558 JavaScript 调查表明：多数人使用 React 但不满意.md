---
layout: post
title:	"硬核观察 #558 JavaScript 调查表明：多数人使用 React 但不满意"
date:	2022-02-25 15:31:00 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,React,eBPF,挖矿]
---


![](/Asserts/Images/album/202202/25/153023ak88zcsmmoscs4k4.jpg)


![](/Asserts/Images/album/202202/25/153036r6tkbokt9dvh96g6.jpg)


### JavaScript 调查表明：多数人使用 React 但不满意


从专门 [针对 JavaScript 的 2021 年度调查](https://2021.stateofjs.com/en-US/demographics/)中可以发现，在 JavaScript 框架和库方面，React 的使用率继续领先，其次是 Angular 和 Vue.js。React 的满意度明显下降，在 Vue.js、Solid 和 Svelte 之后排名第四。Solid 在满意度方面排名第一，在兴趣方面排名第二，即使在实际使用它的人方面排名倒数第二。



> 
> 老王点评：这个调查报告还披露了很多信息，值得一看。
> 
> 
> 


![](/Asserts/Images/album/202202/25/153047tkdtr6rmfy6fzkgd.jpg)


### 声称恢复 GPU 挖矿性能的工具实际上是恶意软件


一些英伟达的新显卡带有性能限制，以减少该显卡对加密货币矿工的吸引力。大量的 GPU 显卡被用来挖矿，使得游戏玩家和其他人很难获得这种硬件，而且导致价格昂贵。前两天，有网站介绍了一个用于可以打开 RTX 显卡的加密货币挖掘性能限制。不过，[第二天他们发现](https://www.tomshardware.com/news/nvidia-rtx-lhr-unlocker-malware)“该工具非但没有解决挖矿性能上限的问题，反而使主机系统感染了恶意软件”。目前还不清楚该恶意软件到底是做什么的，可能是键盘记录、信息窃取，也有可能是加密货币挖掘。



> 
> 老王点评：真是哭笑不得的事情。好吧，现在没人和玩家们抢新显卡了。
> 
> 
> 


![](/Asserts/Images/album/202202/25/153122x4oobdco3g4g3wia.jpg)


### 红帽扩展 eBPF 用于输入设备的 HID 子系统


在内核中运行沙盒程序的 eBPF 非常有用，它已经超越了起源于网络子系统中的最初的 BPF，它对其他领域，如安全、追踪和内核内 JIT 虚拟机等也非常实用。红帽发出了 [一组补丁](https://www.phoronix.com/scan.php?page=news_item&px=Linux-eBPF-For-HID) 为 HID 设备引入了 eBPF 支持。其中一个非常有用的领域是用于有问题或奇怪的设备，这可以将修复放在一些外部仓库中，并作为 eBPF 程序在启动时加载，以避免需要创建新的内核，而经历漫长的上下游过程。



> 
> 老王点评：如果你还没有了解过 eBFP，建议了解一下，它已经越来越强大重要了。
> 
> 
>
