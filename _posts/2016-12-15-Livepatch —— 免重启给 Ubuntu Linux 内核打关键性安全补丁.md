---
layout: post
title:	"Livepatch —— 免重启给 Ubuntu Linux 内核打关键性安全补丁"
date:	2016-12-01 10:33:00 +0800 
categories:	系统运维 linuxcn 
tags:	[linuxcn,Ubuntu,补丁,实时补丁,Livepatch]
---


![](/Asserts/Images/album/201612/01/103248f6kpmxoko1mfi6yw.png)


如果你是一个在企业环境中维护关键性系统的系统管理员，你肯定对以下两件事深有感触：


1) 很难找个停机时间去给系统安装安全补丁以修复内核或者系统漏洞 。如果你工作的公司或者企业没有适当的安全策略，运营管理可能最终会优先保证系统的运行而不是解决系统漏洞。 此外，内部的官僚作风也可能延迟批准停机时间。我当时就是这样的。


2) 有时候你确实负担不起停机造成的损失，并且还要做好用别的什么方法减小恶意攻击带来的的风险的准备。


好消息是 Canonical 公司最近针对 Ubuntu 16.04 (64位版本 / 4.4.x 内核)　发布了 Livepatch 服务，它可以让你不用重启就能给内核打关键性安全补丁。 对，你没看错：使用 Livepatch 你不用重启就能使 Ubuntu 16.04 服务器系统的安全补丁生效。


### 注册 Ubuntu Livepatch 账号


要运行 Canonical Livepatch 服务你先要在这里注册一个账号 <https://auth.livepatch.canonical.com/>，并且表明你是一个普通用户还是企业用户（付费）。 通过使用令牌，所有的 Ubuntu 用户都能将最多 3 台不同的电脑连接到 Livepatch 服务：


![Canonical Livepatch Service](/Asserts/Images/album/201612/01/103304x2y6zxlkk5ylm6l2.png)


*Canonical Livepatch 服务*


下一步系统会提示你输入你的 Ubuntu One 凭据，或者你也可以注册一个新账号。如果你选择后者，则需要你确认你的邮件地址才能完成注册：


![Ubuntu One Confirmation Mail](/Asserts/Images/album/201612/01/103305fcbbrtj6tttlbtmz.png)


*Ubuntu One 确认邮件*


一旦你点了上面的链接确认了你的邮件地址，你就会回到这个界面：<https://auth.livepatch.canonical.com/> 并获取你的 Livepatch 令牌。


### 获取并使用 Livepatch 令牌


首先把分配给你账号的这个唯一的令牌复制下来：


![Canonical Livepatch Token](/Asserts/Images/album/201612/01/103305edoib4ljjhgjodij.png)


*Canonical Livepatch 令牌*


然后打开终端，输入：



```
$ sudo snap install canonical-livepatch

```

上面的命令会安装 livepatch 程序，下面的命令会为你的系统启用它。



```
$ sudo canonical-livepatch enable [YOUR TOKEN HERE]

```

如果后一条的命令提示找不到 `canonical-livepatch` ，检查一下 `/snap/bin` 是否已经添加到你的路径， 或者把你的工作目录切换到 `/snap/bin` 下执行也行。



```
$ sudo ./canonical-livepatch enable [YOUR TOKEN HERE]

```

![Install Livepatch in Ubuntu](/Asserts/Images/album/201612/01/103306evw4i153a89ia4an.png)


*在 Ubuntu 中安装 Livepatch*


之后，你可能需要检查应用于内核的补丁的描述和状态。幸运的是，这很简单。



```
$ sudo ./canonical-livepatch status --verbose

```

如下图所示：


![Check Livepatch Status in Ubuntu](/Asserts/Images/album/201612/01/103306alazeevauub688z7.png)


*检查补丁安装情况*


在你的 Ubuntu 服务器上启用了 Livepatch，你就可以在保证系统安全的同时把计划内的外的停机时间降到最低。希望 Canonical 的这个举措会在管理上给你带来便利，甚至更近一步带来提升。


如果你对这篇文章有什么疑问，欢迎在下面留言,我们会尽快回复。




---


via: <http://www.tecmint.com/livepatch-install-critical-security-patches-to-ubuntu-kernel>


作者：[Gabriel Cánepa](http://www.tecmint.com/author/gacanepa/) 译者：[Yinux](https://github.com/Yinux) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
