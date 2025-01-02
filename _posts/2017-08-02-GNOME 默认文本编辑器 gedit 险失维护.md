---
layout: post
title:	"GNOME 默认文本编辑器 gedit 险失维护"
date:	2017-08-09 13:26:00 +0800 
categories:	观点 linuxcn 
tags:	[linuxcn,gedit,GNOME]
---


或许是出于疲倦，也有可能是出于对 GNOME 应用开发体系的不满，GNOME 桌面环境默认的文本编辑器、核心应用之一的 gedit 的开发者前几天宣布不再维护它了。它的最新稳定版本是 3.22。


![](/Asserts/Images/album/201708/09/132604qdnsxsiz070iio44.png)


gedit 开发者 Sébastien Wilmet [在邮件列表中说](https://mail.gnome.org/archives/gedit-list/2017-July/msg00001.html)：



> 
> “gedit 不再维护，我已将其添加到此维基页面： <https://wiki.gnome.org/Apps/Unmaintained> 
> 
> 
> 有没有感兴趣接手 gedit 维护的开发者？”
> 
> 
> 


庆幸的是，gedit 在“无维护”页面呆了几天后，[就有两位新的维护者加入了维护行列](https://wiki.gnome.org/Apps/Gedit)，我们可以不用担心 gedit 就此消亡——虽然“当前的 GTK+ 3 已经稳定，就是不维护，不出意外的话 gedit 也可以持续工作很长时间”。


gedit 是 GNOME 的默认编辑器，但其实它在 Linux 上的编辑器家族里面并不是很出彩，只能说是中规中矩、简单而轻量级罢了。但是可能也正是因为这个原因，才让大家忽视了这些默不出声的应用也是需要人来关爱的。


gedit 初次发布于 1999 年，而今已经有 18 岁了，但是它的开发者却一直不多，功能和特性的增加也不大，而且，几年前曾经历一次 UI 的较大变更，变更后的 UI 变成非常难用，所以使用者对此也颇有腹诽。但是可能是由于下面的原因，参与维护的人很少：



> 
> “另外， gedit 的核心是用 C 写的（为了支持 Mac OS X ，还有一点 Objective-C），一些插件是用 Vala 或 Python 写的。如果你要接手 gedit 的维护，你需要和这四种语言打交道（还不算构建系统）。 Python 代码是没编译的，所以如果重构 gedit 核心的话，可能需要移植所有的插件（python 代码也不如 C 代码那么便于 grep），不过至少 Vala 有个编译器，虽然我不推荐它。”
> 
> 
> 


所以，这可能真的会让维护者头大。


此外，Sébastien Wilmet 对 GNOME 生态的开发也颇有抱怨：



> 
> “如果 gedit 死了，我认为这对于所有的 GTK+ 应用都是一个教训：要写更多的库，并在几个类似应用之间共享且一同维护它们。GtkSourceView 仍在维护，但是 gedit 所用的代码要超过了 GtkSourceView。在我给 GtkSourceView 贡献代码前， gedit 里面就有 8000 行以上的代码来保存和载入文件（只是后端，不算前端）。你显然不会认为只有 gedit 需要在用 GtkSourceView 时使用载入和保存文件吧？其它的文本编辑器呢？比如 Anjuta （也有很大一个不再维护的代码库），而且现在 gnome-builder 还在犯同样的错误（在它的角落里面开发了许多文本编辑器功能；你真的认为 Vim 模式只在 gnome-builder 中有用？！）
> 
> 
> 这事不只是文本编辑器的事，我们造了多少个音乐播放器的轮子？照片管理器呢？IRC/聊天客户端呢？天气预报呢？等等~”
> 
> 
> 


好吧，或许是该正视这个问题的时刻了，毕竟只有良好的开发环境，才有丰富的应用生态，只有丰富的应用生态，才能大量的使用者。
