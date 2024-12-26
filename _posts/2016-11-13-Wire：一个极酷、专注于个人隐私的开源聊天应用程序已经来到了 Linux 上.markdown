---
layout: post
title:	"Wire：一个极酷、专注于个人隐私的开源聊天应用程序已经来到了 Linux 上"
date:	2016-11-08 10:16:49 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,Wire]
---


![](/Asserts/Images//attachment/album/201611/08/101545s8plpwfmy8hd8wvh.jpeg)


回到大约两年前，一些曾开发 [Skype](https://www.skype.com/en/) 的开发人员发行了一个漂亮的新聊天应用个程序：[Wire](https://wire.com/)。当我说它漂亮的时候，只是谈论它的“外貌”。Wire 具有一个许多其他聊天应用程序所没有的整洁优美的“外貌”，但这并不是它最大的卖点。


从一开始，Wire 就推销自己是[世界上最注重隐私的聊天应用程序](http://www.ibtimes.co.uk/wire-worlds-most-private-messaging-app-offers-total-encryption-calls-texts-1548964)。无论是文本、语音电话，还是图表、图像等基本的内容，它都提供端到端的加密。


WhatsApp 也提供‘端到端加密’，但是考虑一下它的所有者 [Facebook 为了吸引用户而把 WhatsApp 的数据分享出去](https://techcrunch.com/2016/08/25/whatsapp-to-share-user-data-with-facebook-for-ad-targeting-heres-how-to-opt-out/)。我不太相信 WhatsApp 以及它的加密手段。


使 Wire 对于我们这些 FOSS（自由/开源软件）爱好者来说更加重要的是，几个月前 [Wire 开源了](http://www.infoworld.com/article/3099194/security/wire-open-sources-messaging-client-woos-developers.html)。几个月下来我们见到了一个用于 Linux 的 beta 版本 Wire 桌面应用程序。


除了一个包装器以外，桌面版的 Wire 并没有比 web 版多任何东西。感谢 [Electron 开源项目](http://electron.atom.io/)提供了一种开发跨平台桌面应用程序的简单方式。许多其他应用程序也通过使用 Electron 为 Linux 带去了一个本地桌面应用程序，包括 [Skype](https://itsfoss.com/skpe-alpha-linux/)。


### WIRE 的特性：


在我们了解有关 Linux 版 Wire 应用程序的更多信息之前，让我们先快速看一下它的一些主要特性。


* 开源应用程序
* 针对所有类型内容的全加密
* 无广告，无数据收集，无数据分享
* 支持文本，语音以及视频聊天
* 支持群聊和群电话
* [音频过滤器](https://medium.com/colorful-conversations/the-tune-for-this-summer-audio-filters-eca8cb0b4c57#.c8gvs143k)（不需要吸入氦元素，只需要使用过滤器就可以用有趣的声音说话）
* 不需要电话号码，可以使用邮箱登录
* 优美、现代化的界面
* 跨平台聊天应用程序，iOS，Android，Web，Mac，Windows 和 Linux 客户机均有相应版本
* 欧洲法保护（欧洲法比美国法更注重隐私）


Wire 有一些更棒的特性，尤其是和[Snapchat](https://www.snapchat.com/)类似的音频过滤器。


### 在 Linux 上安装 WIRE


在安装 Wire 到 Linux 上之前，让我先警告你它目前还处于 beta 阶段。所以，如果你遇到一些故障，请不要生气。


Wire 有一个 64 位系统可使用的 .deb 客户端。如果你有一台 [32 位或者 64 位系统](https://itsfoss.com/32-bit-64-bit-ubuntu/)的电脑，你可以使用这些技巧来找到它。你可以从下面的链接下载 .deb 文件。


* [下载 Linux 版 Wire [Beta]](https://wire.com/download/)


如果感兴趣的话，你也可以看一看它的源代码：


* [桌面版 Wire 源代码](https://github.com/wireapp/wire-desktop)


这是 Wire 的默认界面，看起来像 [elementary OS Loki](https://itsfoss.com/tag/elementary-os-loki/):


![](/Asserts/Images//attachment/album/201611/08/101614uo2woz4qzymfg2w5.jpeg)


你看，他们甚至还弄了一个机器人：）


你已经开始使用 Wire 了吗？如果是，你的体验是什么样的？如果没有，你将尝试一下吗？因为它现在是[开源的](https://itsfoss.com/tag/open-source)并且可以在 Linux 上使用。




---


via: <https://itsfoss.com/wire-messaging-linux/>


作者：[Abhishek Prakash](https://itsfoss.com/author/abhishek/)  译者：[ucasFL](https://github.com/ucasFL) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
