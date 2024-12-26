---
layout: post
title:	"Linux有问必答:如何在CentOS或者RHEL上启用Nux Dextop仓库"
date:	2014-09-24 10:59:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,RPM,Nux Dextop,仓库]
---



> 
> **问题**: 我想要安装一个在Nux Dextop仓库的RPM包。我该如何在CentOS或者RHEL上设置Nux Dextop仓库？
> 
> 
> 


[Nux Dextop](http://li.nux.ro/download/nux/dextop/)是一个面对CentOS、RHEL、ScientificLinux的含有许多流行的桌面和多媒体相关的包的第三方RPM仓库（比如：Ardour，Shutter等等）。目前，Nux Dextop桌面对CentOS和RHEL 6/7可用。


![](/Asserts/Images//attachment/album/201409/23/220317wy5564bf9wev66gv.png)


要在CentOS或者RHEL上启用Nux Dextop，遵循下面的步骤。


首先，要知道Nux Dextop被设计与EPEL仓库共存。因此，你需要在使用Nux Dexyop仓库前先[启用 EPEL](http://xmodulo.com/2013/03/how-to-set-up-epel-repository-on-centos.html)。


启用EPEL后，用下面的命令安装Nux Dextop仓库。


在 CentOS/RHEL 6.\* 上:



```
$ sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el6/x86_64/nux-dextop-release-0-2.el6.nux.noarch.rpm

```

在 CentOS/RHEL 7 上 :



```
$ sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm

```

现在验证Nux Dextop仓库是否已经成功安装：



```
$ yum repolist 

```

![](/Asserts/Images//attachment/album/201409/23/220004j7uyf3oevmfze8ef.jpg)


### 对于 Repoforge/RPMforge 用户


据作者所说，目前已知Nux Dextop会与其他第三方库比如Repoforge和ATrpms相冲突。因此，如果你启用了除了EPEL的其他第三方库，强烈建议你将Nux Dextop仓库设置成“default off”（默认关闭）状态。就是用文本编辑器打开/etc/yum.repos.d/nux-dextop.repo，并且在nux-desktop下面将"enabled=1" 改成 "enabled=0"。



```
$ sudo vi /etc/yum.repos.d/nux-dextop.repo 

```

![](/Asserts/Images//attachment/album/201409/23/220035z0nadhrgqop0zhrg.jpg)


无论何时当你从Nux Dextop仓库安装包时，显式地用下面的命令启用仓库。



```
 $ sudo yum --enablerepo=nux-dextop install <package-name> 

```



---


via: <http://ask.xmodulo.com/enable-nux-dextop-repository-centos-rhel.html>


译者：[geekpi](https://github.com/geekpi) 校对： [wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
