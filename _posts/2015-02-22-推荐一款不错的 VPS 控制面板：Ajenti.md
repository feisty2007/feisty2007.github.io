---
layout: post
title:	"推荐一款不错的 VPS 控制面板：Ajenti"
date:	2015-02-09 10:51:00 +0800 
categories:	系统运维 linuxcn 
tags:	[linuxcn,Ajenti]
---


任何有经验的Linux人员都认为没有任何一款控制面板可以打败纯命令行界面来管理[虚拟主机](http://xmodulo.com/go/digitalocean)（VPS）。也有人争辩说好的控制面板还是应该有一席之地，因为顺滑的操作界面让常规管理操作通过点几下鼠标就可以完成。


至于控制面板，有那种充满浮华装饰的商业控制面板，也有各种免费的但也强大多功能的免费开源面板替代品。这之中的杰出代表是[Ajenti](http://ajenti.org/)控制面板。


Ajenti可以让你很简单地配置不同的常规服务程序，如Apache/nginx、Samba、BIND、Squid、MySQL、cron、防火墙等等，对管理常规的 VPS 实例可以节省大量的时间。对于生产环境，Ajenti同样提供了插件和平台来支持虚拟 web 主机管理和自定义 web UI开发。


Ajenti有[双重授权](http://ajenti.org/licensing);一个是针对个人、企业内部或者教育用途免费使用的AGPLv3。然而，如果你是一家托管企业或者硬件提供商，那么你需要购买商业授权来使用Ajenti作为商业服务。


### 在Linux上安装Ajenti


为了简化安装，Ajenti为主流Linux发行版提供了自己的仓库。安装Ajenti要做的就是配置目标仓库，并用默认包管理器来安装。


安装前会生成用于SSL的一个RSA密钥和证书，Ajenti会在8000端口监听HTTPS的web请求。如果你正在使用防火墙，你需要在防火墙中允许8000端口访问。为了安全，最好默认禁止8000端口的公开访问，并添加你的少数IP地址到白名单中。


#### 在Debian上安装Ajenti



```
$ wget http://repo.ajenti.org/debian/key -O- | sudo apt-key add -
$ sudo sh -c 'echo "deb http://repo.ajenti.org/debian main main debian" >> /etc/apt/sources.list'
$ sudo apt-get update
$ sudo apt-get install ajenti 

```

#### 在Ubuntu上安装Ajenti



```
$ wget http://repo.ajenti.org/debian/key -O- | sudo apt-key add -
$ sudo sh -c 'echo "deb http://repo.ajenti.org/ng/debian main main ubuntu" >> /etc/apt/sources.list'
$ sudo apt-get update
$ sudo apt-get install ajenti 

```

#### 在 CentOS/RHEL或者Fedora上安装Ajenti


在CentOS/RHEL上，首先[配置](http://linux.cn/article-2324-1.html)EPEL仓库，接着运行下面的命令。在Fedora上，直接使用下面的命令。



```
$ wget http://repo.ajenti.org/ajenti-repo-1.0-1.noarch.rpm
$ sudo rpm -ivh ajenti-repo-1.0-1.noarch.rpm
$ sudo yum install ajenti 

```

接着配置防火墙。


在Fedora或者CentOS/RHEL 7上：



```
$ sudo firewall-cmd --zone=public --add-port=8000/tcp --permanent
$ sudo firewall-cmd --reload 

```

在CentOS/RHEL 6上：



```
$ sudo iptables -I INPUT -p tcp -m tcp --dport 8000 -j ACCEPT
$ sudo service iptables save 

```

### 访问Ajenti web界面


在访问Ajenti的web界面前，先确保启动了ajenti服务。



```
$ sudo service ajenti restart 

```

直接在浏览器中输入https://<server-ip-address>:8000，你就会看到下面的Ajenti的登录界面。


![](/Asserts/Images/album/201502/09/105110g5eav8n5c4yahyvz.jpg)


默认的登录凭证是用户名“root”，密码“admin”。当你登录后，你会看到初始化的Ajenti菜单。


![](/Asserts/Images/album/201502/09/105114lmx25x22b2aj5jj3.jpg)


在左边面板的"SOFTWARE"选项下，你会看带一些已安装的服务。当你安装了任何Ajenti支持的服务端程序时，软件会在重启ajenti服务后被自动加入列表。



```
 $ sudo service ajenti restart 

```

### 通过Ajenti web界面管理VPS


Ajenti的web界面非常直观且易使用。下面是Ajenti功能的几个例子。


#### 可插入结构


Ajenti有许多特定应用的插件，这让AJenti可高度扩展化。当你在VPS上安装一款新软件时。相关的AJenti插件（如果有的话）会自动启用来管理软件。“Plugins”菜单会展示可用/启用的插件，以及和它们关联的软件。


![](/Asserts/Images/album/201502/09/105117c3a164fkwjmm8gi3.jpg)


#### 包管理


Ajenti提供了一个web界面来安装和升级VPS上的包。


![](/Asserts/Images/album/201502/09/105119c2475ke4ch7h7nzk.jpg)


#### 防火墙配置


Ajenti允许你用两种方法管理防火墙规则（使用iptables或者CSF）。一种方法是使用用户友好的web面板，另一种是直接编辑原始的防火墙规则。


![](/Asserts/Images/album/201502/09/105121xbe7iqbhha2pzi2e.jpg)


![](/Asserts/Images/album/201502/09/105123cdqbdczvkyozqck5.jpg)


#### 日志检查


你可以在Ajenti的web界面中浏览位于/var/log下的系统日志。


![](/Asserts/Images/album/201502/09/105125ha3facze7suxbka7.jpg)


#### 进程监控


你可以看见按照CPU和内存使用率排序的进程列表，如果需要的话，也可以干掉它们。


![](/Asserts/Images/album/201502/09/105127gcm7zainxn0sw1wa.jpg)


#### 终端访问


如果需要更低层面的VPS访问，Ajenti提供了基于web的终端界面，你在这可以输入Linux命令。你也可以像下面那样在一个面板中打开多个终端。


![](/Asserts/Images/album/201502/09/105129bhsuq5jqm7mi5jk5.jpg)


#### Apache Web服务管理


你可以编辑Apache配置文件，并管理apache2服务。


![](/Asserts/Images/album/201502/09/105131ve8ztwtcah5eeazj.jpg)


#### MySQL/MariaDB 管理


你可以访问MySQL/MariaDB服务并直接在上面执行原始SQL命令。


![](/Asserts/Images/album/201502/09/105132q1oaox1zoe8kxn17.jpg)


#### Squid 配置


你可以配置Squid代理服务器的ACL、HTTP访问规则，过滤端口。


![](/Asserts/Images/album/201502/09/105134ho76gof59jkontdn.jpg)


#### 启动服务管理


你可以浏览、启动、停止、重启已安装的服务。


![](/Asserts/Images/album/201502/09/105136cmjqi7ojqjg9rmf3.jpg)


### 总结


Ajenti是一款易于使用的服务器管理控制面板，可以加入你开发的[自定义插件](http://docs.ajenti.org/en/latest/dev/intro.html)。然而请记住，任何好的控制面板都不是阻止你学习在控制面板之后[VPS](http://xmodulo.com/go/digitalocean)里发生了什么的原因。一款好的面板会在你完全了解你正在做的事情时成会一款真正节省时间的利器，并且不依赖于控制面版来达成你所需要的目标。




---


via: <http://xmodulo.com/free-control-panel-for-vps.html>


作者：[Dan Nanni](http://xmodulo.com/author/nanni) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
