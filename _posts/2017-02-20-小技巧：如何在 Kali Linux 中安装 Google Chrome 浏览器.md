---
layout: post
title:	"小技巧：如何在 Kali Linux 中安装 Google Chrome 浏览器"
date:	2017-02-16 07:23:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Chrome]
---


### 介绍


**目的**


我们的目标就是在 Kali Linux 上安装好 Google Chrome Web 浏览器。同时，请参阅附录为可能出现的问题进行排查。


**要求**


需要获得已安装 Kali Linux 或者 Live 系统的特权。


**困难程度**


容易。


**惯例**


* `#` - 给定命令需要以 root 用户权限运行或者使用 `sudo` 命令
* `$` - 给定命令以常规权限用户运行


![](/Asserts/Images/album/201702/14/232701gpotypfrrtsy1t4i.jpg)


### 步骤说明


**下载 Google Chrome**


首先，使用 `wget` 命令来下载最新版本的 Google Chrome 的 debian 安装包。



```
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

```

**安装 Google Chrome**


在 Kali Linux 安装 Google Chrome 最容易的方法就是使用 `gdebi`，它会自动帮你下载所有的依赖包。



```
# gdebi google-chrome-stable_current_amd64.deb

```

**启动 Google Chrome**


开启一个<ruby> 终端 <rp>  （ </rp> <rt>  terminal </rt> <rp>  ） </rp></ruby>，执行 `google-chrome` 命令来启动 Google Chrome 浏览器。



```
$ google-chrome

```

### 附录


<ruby> 非法指令 <rp>  （ </rp> <rt>  Illegal Instruction </rt> <rp>  ） </rp></ruby>


当以 root 用户特权来运行 `google-chrome` 命令是，会出现<ruby> 非法指令 <rp>  （ </rp> <rt>  Illegal Instruction </rt> <rp>  ） </rp></ruby> 错误信息。因为通常情况下，Kali Linux 默认情况下的默认用户是 root 用户，我们需要创建一个虚的非特权用户，比如 `linuxconfig`，然后使用这个用户来启动 Google Chrome 浏览器。如下：



```
# useradd -m -d /home/linuxconfig linuxconfig
# su linuxconfig -c google-chrome

```

**libappindicator1 包未安装**



```
dpkg: dependency problems prevent configuration of google-chrome-stable:
 google-chrome-stable depends on libappindicator1; however:
  Package libappindicator1 is not installed.

```

使用 `gdebi` 命令来安装 Google Chrome 的 debian 包可以解决依赖问题。参阅上文。 


![在 Kali Linux 中以普通用户启动 google chrome](/Asserts/Images/album/201702/14/232723ld9fa4o9fssnkmy5.jpg)




---


译者简介：


[GHLandy](http://GHLandy.com) —— 生活中所有欢乐与苦闷都应藏在心中，有些事儿注定无人知晓，自己也无从说起。




---


via: <https://linuxconfig.org/how-to-install-google-chrome-browser-on-kali-linux>


作者：[Lubos Rendek](https://linuxconfig.org/how-to-install-google-chrome-browser-on-kali-linux) 译者：[GHLandy](https://github.com/GHLandy) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
