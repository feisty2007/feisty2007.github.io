---
layout: post
title:	"Canonical解决了一个Ubuntu 14.04 LTS中的nginx漏洞"
date:	2014-09-28 09:22:27 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Ubuntu,Nginx,安全]
---



> 
> 用户应该更新他们的系统来修复这个漏洞！
> 
> 
> 


![](/Asserts/Images/album/201409/28/092111vcelq4agcxi7zzwi.jpeg)
**Canonical已经在安全公告中公布了这个影响到Ubuntu 14.04 LTS (Trusty Tahr)的nginx漏洞的细节。这个问题已经被确定并被修复了**


Ubuntu的开发者已经修复了nginx的一个小漏洞。他们解释nginx可能已经被利用来暴露网络上的敏感信息。


根据安全公告，“Antoine Delignat-Lavaud和Karthikeyan Bhargavan发现nginx错误地重复使用了缓存的SSL会话。攻击者可能利用此问题，在特定的配置下，可以从不同的虚拟主机获得信息“。


对于这些问题的更详细的描述，可以看到Canonical的安全[公告](http://www.ubuntu.com/usn/usn-2351-1/)。用户应该升级自己的Linux发行版以解决此问题。


这个问题可以通过在系统升级到最新nginx包（和依赖v包）进行修复。要应用该补丁，你可以直接运行升级管理程序。


如果你不想使用软件更新器，您可以打开终端，输入以下命令（需要root权限）：



```
sudo apt-get update
sudo apt-get dist-upgrade

```

在一般情况下，一个标准的系统更新将会进行必要的更改。要应用此修补程序您不必重新启动计算机。




---


via: <http://news.softpedia.com/news/Canonical-Closes-Nginx-Exploit-in-Ubuntu-14-04-LTS-459677.shtml>


作者：[Silviu Stahie](http://news.softpedia.com/editors/browse/silviu-stahie) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
