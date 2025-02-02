---
layout: post
title:	"ngxtop：在命令行实时监控 Nginx 的神器"
date:	2014-06-16 15:00:00 +0800 
categories:	软件开发 linuxcn 
tags:	[linuxcn,]
---


Nginx网站服务器在生产环境中[运行](http://xmodulo.com/2014/01/compile-install-nginx-web-server.html)的时候需要进行实时监控。实际上，诸如[Nagios](http://xmodulo.com/2013/12/monitor-common-services-nagios.html), Zabbix, Munin 的网络监控软件是支持 Nginx 监控的。


如果你不需要以上软件提供的综合性报告或者长期数据统计功能，只是需要一种快速简便的办法去监控 Nginx 服务器的请求的话，我建议你采用一个叫 [ngxtop](https://github.com/lebinh/ngxtop) 的命令行工具。


你马上就会发现 ngxtop 从界面和名称都借鉴了著名的top命令。ngxtop 是通过分析 Nginx 或者其他的日志文件，使用类似 top 命令的界面实时展示出来的。你可以说你知道的其他高端监控工具，但是在简洁这方面 ngxtop 无疑是最好的。简单就意味着不可替代。


本指南中，我将介绍如何使用 ngxtop 实时监控 Nginx 网站服务器。


### Linux 上安装 ngxtop


首先在 Linux 系统中安装依赖库[pip](http://ask.xmodulo.com/install-pip-linux.html)（LCTT译注：ngxtop是用python编写的）。


然后使用如下命令安装 ngxtop。



```
$ sudo pip install ngxtop

```

### ngxtop 使用


基本使用方法如下：



```
ngxtop [options]
ngxtop [options] (print|top|avg|sum) <var>
ngxtop info

```

这里是一些通用选项。


* **-l** : 指定日志文件的完整路径 (Nginx 或 Apache2)
* **-f** : 日志格式
* **--no-follow**: 处理当前已经写入的日志文件，而不是实时处理新添加到日志文件的日志
* **-t** : 更新频率
* **-n** : 显示行号
* **-o** : 排序规则(默认是访问计数)
* **-a ..., --a ...**: 添加表达式(一般是聚合表达式如： sum, avg, min, max 等)到输出中。
* **-v**: 输出详细信息
* **-i** : 只处理符合规则的记录


以下是一些内置变量，他们的含义不言自明。


* body*bytes*send
* http\_referer
* http*user*agent
* remote\_addr
* remote\_user
* request
* status
* time\_local


### 使用 ngxtop 监控 Nginx


ngxtop 默认会从其配置文件 (/etc/nginx/nginx.conf) 中查找 Nginx 日志的地址。所以，监控 Nginx ，运行以下命令即可：



```
$ ngxtop

```

这将会列出10个 Nginx 服务，按请求数量排序。


显示前20个最频繁的请求：



```
$ ngxtop -n 20

```

![](/Asserts/Images/album/201406/16/133347yossqqn79yj4xdzr.jpg)


获取Nginx基本信息：



```
$ ngxtop info

```

![](/Asserts/Images/album/201406/16/133349me6x7pa71tg7chy3.jpg)


你可以自定义显示的变量，简单列出需要显示的变量。使用 "print" 命令显示自定义请求。



```
$ ngxtop print request http_user_agent remote_addr

```

![](/Asserts/Images/album/201406/16/133352ht00nx7fnz07fvq0.jpg)


显示请求最多的客户端IP地址



```
$ ngxtop top remote_addr

```

![](/Asserts/Images/album/201406/16/133354fypepynimipnnyyv.jpg)


显示状态码是404的请求



```
$ ngxtop -i 'status == 404' print request status

```

![](/Asserts/Images/album/201406/16/133357orc6q1voa44v65vg.jpg)


除了Nginx，ngtop 还可以处理其他的日志文件，比如 Apache 的访问文件。使用以下命令监控 Apache 服务器:



```
$ tail -f /var/log/apache2/access.log | ngxtop -f common

```



---


via: <http://xmodulo.com/2014/06/monitor-nginx-web-server-command-line-real-time.html>


译者：[shipsw](https://github.com/shipsw) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
