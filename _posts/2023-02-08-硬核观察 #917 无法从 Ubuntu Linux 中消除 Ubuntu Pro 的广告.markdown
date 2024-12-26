---
layout: post
title:	"硬核观察 #917 无法从 Ubuntu Linux 中消除 Ubuntu Pro 的广告"
date:	2023-02-19 18:31:58 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,Ubuntu,Copilot,GNU]
---


![](/Asserts/Images/album/202302/19/183106qlpd0aodbfhadada.jpg)


![](/Asserts/Images/album/202302/19/183115f7aiba76rihkyaty.jpg)


### 无法从 Ubuntu Linux 中消除 Ubuntu Pro 的广告


在更新 Ubuntu 时，它会提示你安装 esm-apps 软件包，以通过 Ubuntu Pro 获得更多的安全更新。当然，你可以获得一个免费的 Ubuntu Pro 账户，为不超过 5 台的计算机获得更多安全支持。但是，如果你不想用它，也不想看到这个广告信息，你可能认为永久防止这些信息的方法之一是删除提供 Ubuntu Advantage 集成的软件包。但你不能这样做。正如 Ubuntu #1950692 错误所描述的，该软件包现在是核心的 ubuntu-minimal 元包的一个依赖关系，所以如果你删除它，它将会删除其他多个核心包。



> 
> **[消息来源：The Register](https://www.theregister.com/2023/02/17/ubuntu_advantage/)**
> 
> 
> 



> 
> 老王点评：就没有“免费”的午餐，但是 Canonical 一直将广告打到 Ubuntu 中，并且不能删除，总是有些失望。
> 
> 
> 


![](/Asserts/Images/album/202302/19/183126wr6xhfk6868vafrv.jpg)


### 新的 GitHub Copilot 将为开发者写出 40-60% 的代码


GitHub 更新了它的 Copilot 编码助手，变得更智能，它建议的代码的接受度从 2022 年 6 月的 27% 提升到现在的 46%，而 Java 代码的接受度甚至高达 61%。此外，它还新提供了一个漏洞过滤系统，以阻止不安全的编码模式，如 SQL 注入或硬编码凭证。新的漏洞扫描器使用大型语言模型来“接近静态分析工具的行为”，虽然不会像那样严格。



> 
> **[消息来源：Dev Class](https://devclass.com/2023/02/16/github-claims-new-smarter-copilot-will-block-insecure-code-writes-40-60-of-developer-output/)**
> 
> 
> 



> 
> 老王点评：就像大部分手工制品都会被机器淘汰，以后编码这种手工活早晚被替代。
> 
> 
> 


![](/Asserts/Images/album/202302/19/183140hr8e2jee3zyzb0hj.jpg)


### 非 GNU/Linux 的 Linux


有一些 Unix 极客坚持认为 Linux 应该正确地被称为 GNU/Linux，因为内核是用 GNU C 编译器构建的，所有东西都是针对 GNU C 库链接的，使用 GNU Coreutils，通常还有来自 GNU 项目的其他多个组件。[Chimera Linux](https://chimera-linux.org/) 是一个正在建设中的新发行版，它不仅是无 systemd 的，而且也是无 GNU 的。它的创建者希望在今年春天达到 alpha 测试。Chimera 用 LLVM 编译，使用与轻量级 Alpine Linux 发行版相同的 musl C 库和打包工具，新的 Dinit 初始化系统，用户空间其余的大部分都来自当前版本的 FreeBSD。



> 
> **[消息来源：The Register](https://www.theregister.com/2023/02/13/chimera_non_gnu_linux)**
> 
> 
> 



> 
> 老王点评：这说明 Linux 并不一定必须的 GNU 的，也可以是 Free 的。
> 
> 
>
