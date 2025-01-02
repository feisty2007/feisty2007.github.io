---
layout: post
title:	"Github Atom 你所不知道的一些事"
date:	2015-02-04 21:12:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Github Atom,Node.js,io.js]
---


GitHub 开发的文本编辑器 Atom 最近刚刚发布了[0.177.0版](https://github.com/atom/atom/releases/tag/v0.177.0)。在这次更新里面，也许有一些你所不知道的 Atom 的趣事。


![](/Asserts/Images/album/201502/04/211217et78ssd2otjttstu.png)


### Atom 是基于 Chrome 开发的


Atom 是完全基于web技术实现的。底层的架构是基于Chromium(是的就是Google Chrome浏览器的Chromium架构)，所有的窗口都是一个本地渲染的网页。


当我们按下快捷键 Alt+Command+I 时，就可以看到熟悉的Chrome浏览器的调试界面了。


本次 0.177.0 版本是基于 Chrome 40 所开发的。


![](/Asserts/Images/album/201502/04/211220k2ftk16d01dl0uuo.png)


### 弃 Node.js 而用 io.js


Atom 之前是采用了 node.js 来访问文件系统和包管理。这样就让Atom的包管理具有很强的灵活性和可扩展性。面对浩如烟好的npm资源，Atom 的可配置型也变得异常突出。


本次发布的0.177.0版，其中一个引入注目的变化是从 Node.js 切换到了 io.js。


io.js是Node.js的分支，Node.js社区发生分裂后由核心开发者在去年12月[创建的](http://www.solidot.org/story?sid=42171)，已经发布了[v1.1版](https://iojs.org/)，目前开发非常活跃。Atom是切换到io.js的一个重量级项目。


另外，也使用了 [6to5](http://6to5.org/) 的 JavaScript 预处理器。
