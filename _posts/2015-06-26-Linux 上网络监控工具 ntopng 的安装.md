---
layout: post
title:	"Linux 上网络监控工具 ntopng 的安装"
date:	2015-06-21 08:53:00 +0800 
categories:	系统运维 linuxcn 
tags:	[linuxcn,ntopng,监控]
---


当今世界，人们的计算机都相互连接，互联互通。小到你的家庭局域网（LAN），大到最大的一个被我们称为互联网。当你管理一台联网的计算机时，你就是在管理最关键的组件之一。由于大多数开发出的应用程序都基于网络，网络就连接起了这些关键点。


这就是为什么我们需要网络监控工具。ntop 是最好的网络监控工具之一。来自[维基百科](http://en.wikipedia.org/wiki/Ntop)的知识“ntop是一个网络探测器，它以与top显示进程般类似的方式显示网络使用率。在交互模式中，它显示了用户终端上的网络状态。在网页模式中，它作为网络服务器，创建网络状态的HTML转储文件。它支持NetFlow/sFlowemitter/collector，这是一个基于HTTP的客户端界面，用于创建ntop为中心的监控应用，并使用RRD来持续存储通信数据”。


15年后的今天，你将见到ntopng——下一代ntop。


![](/Asserts/Images/album/201506/20/075824msdd31c1gfgs5tls.png)


### ntopng是什么


Ntopng是一个基于网页的高速通信分析器和流量收集器。Ntopng基于ntop，它运行于所有Unix平台、MacOS X和Windows。


### 特性


从[ntopng网站](http://www.ntop.org/products/ntop/)上，我们可以看到他们说它有众多的特性。这里列出了其中一些：


* 按各种协议对网络通信排序
* 显示网络通信和IPv4/v6的激活主机
* 持续不断以RRD格式存储定位主机的通信数据到磁盘
* 通过nDPI，ntop的DPI框架，发现应用协议
* 显示各种协议间的IP通信分布
* 分析IP通信，并根据源/目的地址进行排序
* 显示IP通信子网的矩阵（谁在和谁通信？）
* 报告按协议类型排序的IP协议使用率
* 生成HTML5/AJAX网络通信数据


### 安装的先决条件


Ntop为CentOS和**基于64位**Ubuntu预编译好了包，你可以在[它们的下载页面](http://www.nmon.net/packages/)找到这些包。对于32位操作系统，你必须从源代码编译。本文在**CentOS 6.4 32位**版本上**测试过**。但是，它也可以在其它基于CentOS/RedHat的Linux版本上工作。让我们开始吧。


#### 开发工具


你必须确保你安装了编译ntopng所需的所有开发工具，要安装开发工具，你可以使用yum命令：



```
# yum groupinstall ‘Development Tools’

```

#### 安装TCL



```
# yum install tcl

```

#### 安装libpcap



```
# yum install libpcap libpcap-devel

```

#### 安装Redis



```
# wget http://redis.googlecode.com/files/redis-2.6.13.tar.gz
# tar zxfv redis-2.6.13.tar.gz
# cd redis-2.6.13
# make 32bit
# make test
# make install

```

### 安装ntopng


#### 方法 1 ：



```
# wget http://sourceforge.net/projects/ntop/files/ntopng/ntopng-1.1_6932.tgz/download
# tar zxfv ntopng-1.1_6932.tgz
# cd ntopng-1.1_6932
# ./configure
# make
# make install 

```

#### 方法 2 ：


在我的CentOS 6.4上，我使用方法 1时收到了一个错误消息，错误消息内容如下：



```
./third-party/LuaJIT-2.0.2/src/libluajit.a : could not read symbols : File in wrong format

```

所以，我**切换**到了**SVN**来安装。对于此方法，需要联网，步骤如下：



```
# svn co https://svn.ntop.org/svn/ntop/trunk/ntopng/
# ./autogen.sh
# ./configure
# make
# make install

```

*由于ntopng是一个基于网页的应用，你的系统必须安装有工作良好的 Web 服务器*


### 为ntopng创建配置文件


如果一切都已安装完毕，那么我们该来运行它了。默认情况下，如果我们在./configure这一步没有明确修改安装文件夹的话，redis和ntopng将安装到/usr/local/文件夹。接下来，我们需要为ntopng创建配置文件。在本文中，我们使用vi作为文本编辑器。你也可以使用你所中意的文本编辑器来创建ntopng的配置文件。



```
# cd /usr/local/etc
# mkdir ntopng
# cd ntopng
# vi ntopng.start

```

放入这些行：



```
--local-network "10.0.2.0/24"
--interface 1

```



---



```
# vi ntopng.pid

```

放入该行：



```
-G=/var/run/ntopng.pid

```

保存这些文件，然后继续下一步。


### 运行ntopng


我们假定你已正确安装了网络服务器，那么下一步就是运行redis服务器。



```
# /usr/local/bin/redis-server

```

![Starting Redis Server](/Asserts/Images/album/201506/20/075838ysbolgbkodhzslbj.png)


然后，**运行**ntopng



```
# /usr/local/bin/ntopng

```

![Starting Ntopng](/Asserts/Images/album/201506/20/075839c7bwzll129blwb44.png)


### 测试ntopng


现在，你可以通过访问[http://yourserver.name:3000](http://yourserver.name:3000/)来测试ntopng应用，你将会看到ntopng登录页面。首次登录，你可以使用用户‘**admin**’和密码‘**admin**’。


![Ntop Login page](/Asserts/Images/album/201506/20/075840ku9ne4fxtuzufuv4.png)


仪表盘相当简洁。当你登入后，你将看到关于最高流量通信者页面。


![Ntopng Flow Talker](/Asserts/Images/album/201506/20/075840dsxvksg6ipkv6igv.png)


如果你点击右侧顶部的**流量菜单**，ntopng将会显示活动流量的更多细节。


![Ntopng Flows](/Asserts/Images/album/201506/20/075841ghzddw978uhtg3uz.png)


在**主机菜单**上，你可以看到连接到流的所有主机。


![Ntopng Hosts List](/Asserts/Images/album/201506/20/075841m8l8h3738khy73pk.png)


如果你点击**主机 > 交互**，ntop将显示一个漂亮的主机间的交互信息图表。


![Ntopng Hosts Interaction](/Asserts/Images/album/201506/20/075842nsgnffltsrrzcioi.png)


**仪表盘菜单**组成部分：


#### 顶级主机（发送+接收）


![Ntopng Hosts](/Asserts/Images/album/201506/20/075843j1cd8c4819w989rd.png)


#### 顶级应用协议


![Ntopng Apps](/Asserts/Images/album/201506/20/075843a9qzb2b4lu4zjp0u.png)


**界面菜单**将引领你进入更多内部菜单。包菜单将给你显示包的大小分布。


![Ntopng packets](/Asserts/Images/album/201506/20/075844f4qyukj42jmjkaqk.png)


**协议菜单**将为你显示使用了多少协议及其使用百分比。


![Ntopng protocol](/Asserts/Images/album/201506/20/075845c50nc945yx425xy2.png)


![Ntopng protocols - detail](/Asserts/Images/album/201506/20/075845lnqqc94v75xz1t27.png)


你也可以通过使用**历史活跃度菜单**查看活跃度。


![Ntopng Historical Activity](/Asserts/Images/album/201506/20/075846okphh8wek9wpetpw.png)


![Ntopng Historical Activity detail](/Asserts/Images/album/201506/20/075846xne0vbx0u0ulbnvt.png)


最后一项要点是，你也可以通过顶部右侧区域的**设置菜单**（齿轮图标的那一个）管理哪些用户可以访问ntopng。


![Ntopng Users](/Asserts/Images/album/201506/20/075846izpkjksjk5ryb81d.png)


Ntopng为你提供了一个范围宽广的时间线，从5分钟到1年都可以。你只需要点击你想要显示的时间线。图表本身是可以点击的，你可以点击它来进行缩放。


当然，ntopng能做的事比上面图片中展示的还要多得多。你也可以将定位和电子地图服务整合进来。在ntopng自己的网站上，有已付费的模块可供使用，如nprobe可以扩展ntopng可以提供给你的信息。更多关于ntopng的信息，你可以访问[ntopng网站](http://www.ntop.org/)。




---


via: <http://linoxide.com/monitoring-2/ntopng-network-monitoring-tool/>


作者：[Pungki Arianto](http://linoxide.com/author/pungki/) 译者：[GOLinux](https://github.com/GOLinux) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](https://linux.cn/) 荣誉推出
