---
layout: post
title:	"CentOS Linux 7 发布滚动构建版"
date:	2014-12-07 10:40:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,滚动构建版,CentOS]
---


CentOS上周五宣布，CentOS Linux 的滚动构建版正式发布！这次发布包括了用于安装介质的CentOS Linux 7 的 ISO和通用的云镜像两种版本。


CentOS Linux 滚动构建版包括了从初始发布时到快照发布之间推送到 [mirror.centos.org](http://mirror.centos.org) 的所有更新。这些更新包括了 CentOS Linux 的安全更新、错误修复、功能增强以及常规更新。使用这个版本安装的机器将包括之前所有已经发布的更新，和使用 yum 更新的没有什么不同。所有的 rpm/yum 库仍旧存储在 [mirror.centos.org](http://mirror.centos.org) 上，位置和内容都没有变化。


我们将在每个月底前发布一个滚动更新版本。每个发布版本的名字都包括一个时间戳和用于区分所包括内容的构建标记。如 20141129\_02 的文件名表示它包括了发布在 [mirror.centos.org](http://mirror.centos.org) 上的截止到 2014年11月29日在内的所有内容，而且是滚动周期中的第二次构建。所有的构建版本都会公开发布到 [buildlogs.centos.org/](http://buildlogs.centos.org/) 上，但是只有通过了 QA 和测试的才会标记为“发布”，并放到 [buildlogs.centos.org/rolling/](http://buildlogs.centos.org/rolling/) 下。我们也会在需要时（用于开发和测试）在不同的时间点上构建临时构建版本，这些临时构建版本不会当成通用发布版本，但是仍然可以公开得到。


因为需要测试这些镜像，所以这些版本的发布时间总是和它们的时间戳（及内容截止时间）有点延迟。我们希望尽可能的自动化这个过程来缩短这个时间差，但是终究还需要一点时间。


每个滚动周期，我们都希望能以滚动方式增加更多的内容。在紧接着的下一个周期（2014/12）我们会发布 CentOS Linux 7 的 Live 镜像的滚动构建版本，然后是 CentOS Linux 6的。


现在我们没有计划在这个滚动发行周期中包括 CentOS 5。


为了便于统一和交流，发布的介质将以其所包括的内容时间为标识，而不是以发布的时间为准。比如这次在12月发布的是2014/11月底的滚动构建版本。


其它的镜像，如容器及厂商特定的镜像，将和主 CentOS Linux 介质的滚动周期同步开始，不过如果需要的话，也许会迭代的更快。特别兴趣小组（Special Interest Groups - <http://wiki.centos.org/SpecialInterestGroup>   
）也希望让他们的介质和安装器的发布尽量与滚动时间线同步。 


最后，我要强调的是，**滚动发行版可以在出现类似心脏流血、破壳漏洞和狮子狗等重大安全漏洞时尽快提供解决方案**。


![](/Asserts/Images/album/201407/09/104559risei9g95hrarm1e.png)




---


### CentOS Linux 发行版安装介质:


文件： CentOS-7-x86\_64-DVD-20141129\_02.iso  
Sha256校验： 85a46c62b5bfc701678bef7854bb73af4ccfb840dfcbfb2f9b2189e08fe9438c


文件： CentOS-7-x86\_64-Everything-20141129\_02.iso  
Sha256校验： f9fdd8b12c9529a1e3bf7628ebee964b2aeb9fd66540de7b369e0fde6f7a4236


文件： CentOS-7-x86\_64-Minimal-20141129\_02.iso  
Sha256校验：e1338d13178f1c66c17386b7ced0b1459c677ff9a1cf095ac4db377234cc03fa


以下符号链接总是指向最新的滚动发行版本：


<http://buildlogs.centos.org/rolling/7/isos/x86_64/CentOS-7-x86_64-DVD.iso>   
- -> CentOS-7-x86\_64-DVD-20141129\_02.iso


<http://buildlogs.centos.org/rolling/7/isos/x86_64/CentOS-7-x86_64-Everything.iso>   
- -> CentOS-7-x86\_64-Everything-20141129\_02.iso


<http://buildlogs.centos.org/rolling/7/isos/x86_64/CentOS-7-x86_64-Minimal.iso>- -> CentOS-7-x86\_64-Minimal-20141129\_02.iso


每次测试通过并发布后，这些符号链接都会指向到最新的滚动发行版本。


### 云和实例镜像：


CentOS Linux 7 通用云镜像包括了 Extras/ 库中的云初始化部分。这个镜像有多种格式及不同的内容。云镜像发布在： <http://cloud.centos.org/centos/7/images/> 


文件： CentOS-7-x86\_64-GenericCloud-20141129\_01.qcow2  
描述：这是一个基准镜像。  
大小： 944 MB  
Sha256校验： 7710ffdd497cf00fc72c22a3fa7cc7adb3424d3542521ca8fbe19eba9ded403f


文件： CentOS-7-x86\_64-GenericCloud-20141129\_01.qcow2c  
描述：和上面的镜像内容一样，但是通过qemu qcow2 内部压缩设置运行，适合于开发和测试，它的 I/O 性能较低，所以不适合在产品环境中使用。  
大小： 399MB  
Sha256校验：db42e4fb9565e75f0acbe6b54a5b8822f3f1e9783fb1a553e1552c72ceaff8df


文件： CentOS-7-x86\_64-GenericCloud-20141129\_01.qcow2.xz  
描述：这是一个标准的 qcow2 文件，通过 xz 压缩工具运行，适合于产品环境中使用。  
大小： 266MB  
Sha256校验：9b0b38c48a24164c15c33625972b87835501b6994c3ee894f6b79ce40e7d5e54


文件： CentOS-7-x86\_64-GenericCloud-20141129\_01.raw  
描述： 这是一个原始格式的文件，没有使用 qcow2 镜像格式。它可以用“qemu-img convert”转换成其它的格式。  
大小： 8GB.  
Sha256校验：2e643310bdb3cda775905408dbfe378a5eed04e91db193165178afc5ed5492b8


以下符号链接总是指向最新的滚动发行版本：


<http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2>   
- -> CentOS-7-x86\_64-GenericCloud-20141129\_01.qcow2  
<http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2c>   
- -> CentOS-7-x86\_64-GenericCloud-20141129\_01.qcow2c  
<http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.qcow2.xz>   
- -> CentOS-7-x86\_64-GenericCloud-20141129\_01.qcow2.xz  
<http://cloud.centos.org/centos/7/images/CentOS-7-x86_64-GenericCloud.raw>   
- -> CentOS-7-x86\_64-GenericCloud-20141129\_01.raw


每次测试通过并发布后，这些符号链接都会指向到最新的滚动发行版本。


更多的信息请加入我们的 centos-devel 邮件列表（ <http://lists.centos.org/> ）。
