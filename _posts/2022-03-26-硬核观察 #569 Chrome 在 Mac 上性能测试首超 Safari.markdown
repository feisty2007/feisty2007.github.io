---
layout: post
title:	"硬核观察 #569 Chrome 在 Mac 上性能测试首超 Safari"
date:	2022-03-08 18:36:50 +0800 
categories:	硬核观察 linuxcn 
tags:	[linuxcn,Chrome,Mac,Linux,x86]
---


![](/Asserts/Images/album/202203/08/183545ikdz31z9dkfctktf.jpg)


![](/Asserts/Images/album/202203/08/183555zzrwv6mfc6go729z.jpg)


### Chrome 在 Mac 上性能测试首超 Safari


[谷歌今天宣布](https://www.macrumors.com/2022/03/07/chrome-faster-safari-speedometer-benchmark/)，在 Mac 上的最新版 Chrome 浏览器 Chrome 99 在 Speedometer 测试中首次超过 Safari，得分超过 300。Speedometer 是苹果 WebKit 团队开发的网页响应测试工具，模拟用户与网页之间的各种交互。谷歌表示，自 M1 Mac 发布后，Chrome 在这期间速度提升了 43%，在图形处理方面，Chrome 浏览器比 Safari 快 15%。



> 
> 老王点评：性能是越来越好，内存占用是越来越多。
> 
> 
> 


![](/Asserts/Images/album/202203/08/183606cd3fsj5alaedje55.jpg)


### Linux 发现严重的 “Dirty Pipe” 本地提权漏洞


安全研究人员发现了一个被称为 [Dirty Pipe](https://dirtypipe.cm4all.com/) 的 Linux 本地提权漏洞，其概念验证利用代码也一同被披露。该漏洞在内核 5.8 中被引入。正常登录的用户或正在运行的流氓程序可以利用它来获得 root 权限；恶意应用程序也可以利用它来接管有漏洞的安卓设备。这个错误可以被滥用来添加或覆盖敏感的只读文件中的数据，例如从 `/etc/passwd` 中删除 root 密码，允许系统中的任何人获得超级用户权限，或者暂时改变一个 setuid 二进制文件来授予 root 权限。



> 
> 老王点评：一般来说，Linux 发行版都会很快打上补丁，不过安卓往往要慢得多。
> 
> 
> 


![](/Asserts/Images/album/202203/08/183626fk33m7cxa4iw4mmf.jpg)


### Fedora 鼓励放弃支持 32 位 x86 软件包


Fedora 已经很久没有专注于 32 位 x86（i686）硬件支持了，但仍在继续构建一些 i686 软件包，但其中一些软件包没有被使用。为了释放构建/编译阶段的资源和减轻软件包维护者的负担，正在开发中的 Fedora 37 [鼓励](https://www.phoronix.com/scan.php?page=news_item&px=Fedora-37-Stop-Unused-i686-Pkgs) 软件包维护者放弃末端或未使用的 32 位 x86 软件包。但这一变化不会影响对 multilib 的支持，或其他软件包依赖的 i686 软件包。



> 
> 老王点评：32 位硬件该落幕了。
> 
> 
>
