---
layout: post
title:	"微软开源了一个更安全的 C 语言版本：Checked C"
date:	2016-06-18 18:15:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Checked,Checked C,微软]
---


微软开源了 [Checked C](https://github.com/Microsoft/checkedc) ，这是一个 C 语言的扩展版本，可以用于解决 C 语言中的一系列安全相关的隐患。正如其名字所示，Checked C 为 C 语言增加了检查。这个检查可以帮助开发者检查常见的编程错误，比如<ruby> 缓存区侵占 <rp>  （ </rp> <rt>  buffer overruns </rt> <rp>  ） </rp></ruby>、内存访问越界、不正确的类型转换等。这些编程错误往往是造成许多重大安全漏洞的根本原因，比如<ruby> 破壳漏洞 <rp>  （ </rp> <rt>  Shellshock </rt> <rp>  ） </rp></ruby>、<ruby> 心脏出血漏洞 <rp>  （ </rp> <rt>  Heartbleed </rt> <rp>  ） </rp></ruby>、<ruby> 沙虫 <rp>  （ </rp> <rt>  Sandworm </rt> <rp>  ） </rp></ruby>等。


![](/Asserts/Images//attachment/album/201606/18/181509d01gpq7ibpqbebb7.jpg)


Checked C 通过修改如何控制指针来解决这些问题，指针被程序员们用来定义他们的代码所操作的内存地址。


当指针数量一多，指针控制就往往容易忙中出乱。项目越大，跟踪它们就越困难。类似 Chromium、Firefox、Office、OpenSSL 以及其它的大型代码库在这方面都存在这样的问题，你可以从它们的变更日志中看到大量的这类问题修复。


“Checked C 允许程序员更好的描述他们想要如何使用指针，以及指针应该指向的内存范围”，微软[说](http://research.microsoft.com/en-us/projects/checkedc/default.aspx)，“这个信息可以用于在运行时环境中添加检测，以侦测错误的数据访问，而不是让错误悄悄的发生而无所察觉。”


### Checked C 给 C 语言添加了边界检查


Checked C 也将允许开发者检测到他们以为 C 语言有、而实际却没有的功能误用。按编程的说法来说，这个叫做“<ruby> 边界检查 <rp>  （ </rp> <rt>  bounds checking </rt> <rp>  ） </rp></ruby>”的功能，用于检查变量/指针是否在它的范围之内赋值。


C# 和 Rust 已经有这样的功能了，而且还不止于此。然而，不幸的是，被广泛使用的 C 和 C++ 却没有这样的功能。微软希望只需要对现有的 C/C++ 程序做最小的改动，利用 Checked C 就可以得到安全方面的改善，这样会吸引大量的开发者开始使用 Checked C。


Checked C 项目已经放到了 [GitHub](https://github.com/Microsoft/checkedc) 上。


这并不是微软第一次对基本编程语言做出来自己的演绎，之前，该公司的程序员们还创建了一个名为 TypeScript 的 JavaScript 的超集，它已经得到了广泛认可。
