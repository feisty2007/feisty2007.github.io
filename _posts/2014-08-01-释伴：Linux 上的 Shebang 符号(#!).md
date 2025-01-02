---
layout: post
title:	"释伴：Linux 上的 Shebang 符号(#!)"
date:	2014-08-22 10:16:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Shebang,释伴]
---


![](/Asserts/Images/album/201811/24/213153for8ck8kv98wl6kp.jpg)


使用 Linux 或者 unix 系统的同学可能都对 `#!` 这个符号并不陌生，但是你真的了解它吗？


![](/Asserts/Images/album/201408/22/110421y6evt7fsvd88pjxd.jpg)


本文将给你简单介绍一下 Shebang（“`#!`”）这个符号。


这个符号（`#!`）的名称，叫做“Shebang”或者“Sha-bang”。长期以来，shebang 都没有正式的中文名称。Linux 中国翻译组的 GOLinux 将其翻译为：**释伴**，即解释伴随行的简称，同时又是 shebang 的音译。


### 词源与历史


Shebang 的名字来自于 SHArp 和 bang，或 haSH bang 的缩写，用来指代 Shebang 中 `#!` 两个符号的典型 Unix 名称。 Unix 术语中，`#`号通常称为 sharp，hash 或 mesh；而`!`号则常常称为 bang。也有看法认为，shebang 名字中的 sh 来自于默认 shell —— Bourne shell 的名称 sh，因为常常使用 shebang 调用之。<sup class="reference" id="cite_ref-3"></sup>


在 2010 年版的 [Advanced bash scripting guide](http://tldp.org/LDP/abs/html/)（revision 6.2）中，shebang 被称为“sha-bang”，同时提到“也写作 she-bang 或 sh-bang”，但该文件中没有提到“shebang”这一形式。


[丹尼斯·里奇](http://zh.wikipedia.org/wiki/%E4%B8%B9%E5%B0%BC%E6%96%AF%C2%B7%E9%87%8C%E5%A5%87 "丹尼斯·里奇")在被问及他会如何称呼这一特性时，他答道：



> 
> 发信人："Ritchie, Dennis M (Dennis)\*\* CTR \*\*" <dmr@[redacted]>
> 
> 
> 收信人：<[redacted]@talisman.org>
> 
> 
> 日期：Thu, 19 Nov 2009 18:37:37 -0600
> 
> 
> 主题：RE: What do -you- call your #!<something> line?
> 
> 
> 我不记得我们曾经给它取过一个适当的名字。导入这一特性已经是相当晚了--我觉得我是从关于伯克利 Unix 的 UCB 会议上的某人那里得到的这一灵感；我可能是首先实现它的人之一，但这个创意是来自于别人的。
> 
> 
> 至于它的名字：可能是类似于“hash-bang”的英国风描述性文字，但我没有在任何场合使用类似宠物的名字来描述它。
> 
> 
> 此致,
> 
> 
> Dennis
> 
> 
> 


### 用途


Shebang 这个符号通常在 Unix 系统的脚本中第一行开头中写到，它指明了执行这个脚本文件的解释程序。


1. 如果脚本文件中没有 `#!` 这一行，那么它执行时会默认用当前 Shell 去解释这个脚本(即：`$SHELL` 环境变量）。


2. 如果`#!`之后的解释程序是一个可执行文件，那么执行这个脚本时，它就会把文件名及其参数一起作为参数传给那个解释程序去执行。


3. 如果`#!`指定的解释程序没有可执行权限，则会报错“bad interpreter: Permission denied”。如果`#!`指定的解释程序不是一个可执行文件，那么指定的解释程序会被忽略，转而交给当前的 shell 去执行这个脚本。


4. 如果`#!`指定的解释程序不存在，那么会报错“bad interpreter: No such file or directory”。注意：`#!`之后的解释程序，需要写其绝对路径（如：`#!/bin/bash`），它是不会自动到 $PATH 中寻找解释器的。


5. 当然，如果你使用 `bash test.sh` 这样的命令来执行脚本，那么`#!`这一行将会被忽略掉，解释器当然是用命令行中显式指定的 bash。
