---
layout: post
title:	"使用DNSCrypt来加密您与OpenDNS之间的通信"
date:	2014-06-22 12:04:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,DNS,DNSCrypt,OpenDNS]
---


**正如SSL能将HTTP通信变为加密过的HTTPS通信，DNSCrypt, 物如其名， 是一款能加密您电脑与OpenDNS之间的通信的小神器。**


[DNSCrypt](http://dnscrypt.org/)刚问世的时候，官方公布它只是一款Mac才能用的工具，但根据最近一篇由OpenDNS发的[文章](https://blog.opendns.com/2012/02/16/tales-from-the-dnscrypt-linux-rising/)表明，虽然还没有用户界面，但其实当Mac版DNSCrypt推出的时候源码已经放到了Github上了， Linux的用户也可以安装以及使用哦！（LCTT译注：目前已经有[DNSCrypt WinClient](https://github.com/Noxwizard/dnscrypt-winclient)、[DNSCrypt Windows Service Manager](http://simonclausen.dk/projects/dnscrypt-winservicemgr/)、[DNSCrypt OSXClient](https://github.com/alterstep/dnscrypt-osxclient) 和 [DNSCrypt Tools for Linux](http://opendesktop.org/content/show.php/DNScrypt+Tools?content=164488) 等第三方图形界面客户端出现。）


![](/Asserts/Images/album/201406/22/120418fl7qql4tz24yfzsl.jpg)


### 为神马要使用 DNSCrypt?


**DNSCrypt可以加密您电脑与OpenDNS服务器的所有通信，加密可以防止中间人攻击，信息窥觑，DNS劫持。更能防止网络供应商对某些网站的封锁。**


这是世界上第一款加密DNS通信的工具，虽然TOR可以加密DNS的请求，但毕竟它们只是在出口节点加密而已。



> 
> 这款工具并不需要对域名或其工作方式做任何的改变，它只是提供了个该工具的用户与机房里的DNS服务器之间的加密方式而已。
> 
> 
> 


您可以在[GitHub](https://github.com/opendns/dnscrypt-proxy)的[OpenDNS DNSCrypt](http://www.opendns.com/technology/dnscrypt/)页面阅读更多的相关信息。


### 如何在Linux使用DNSCrypt


首先下载安装[DNSCrypt](http://download.dnscrypt.org/dnscrypt-proxy/) (LCTT译注，安装过程不详述，请参照官网描述)， 然后在Terminal里输入这个命令:



```
sudo /usr/sbin/dnscrypt-proxy --daemonize
```

然后把您的DNS服务器调成"127.0.0.1" - 在GNOME界面下的话，只要到Network Connections（网络连接）选项然后选择"Edit"并在"DNS servers"输入"127.0.0.1"就好了。如果您用的是DHCP的话，请选择Automatic (DHCP) addresses only"， 这样的话才能输入DNS服务器。然后只要重连网络便可。


![](/Asserts/Images/album/201406/22/120239uzijojill1ll4ee0.png)


您可以访问这条[链接](http://www.opendns.com/welcome)来测试您连接到了OpenDNS了没。


如果您想设置开机启动DNSCrypt，可以自建一个init的脚本，如果您用的是Ubuntu，可以参考下面的。


**Arch Linux的用户可以通过[AUR](http://aur.archlinux.org/packages.php?ID=54702)来安装DNSCrypt-proxy** （内含rc.d脚本）


### Ubuntu下的DNSCrypt


如果您想在Ubuntu设置开机启动，您可以使用这个[Upstart脚本](http://webupd8.googlecode.com/files/dnscrypt-0.2.tar.gz)。


注： 在Ubuntu 12.04版在127.0.0.1有个本地的DNS cache 服务器（dnsmasq）在跑，所以已经把改脚本改成让DNSCrypt使用127.0.0.2了， 所以按照上面的教程，应该把127.0.0.1换成127.0.0.2了。


要安装此脚本请使用以下的指令（要首先解压下下来的压缩文件）：



```
sudo cp dnscrypt.conf /etc/init/
sudo ln -s /lib/init/upstart-job /etc/init.d/dnscrypt

```

然后用这个指令来启动:



```
sudo start dnscrypt

```

现在DNSCrypt就应该是开机自启了，如果您想停止的话，可以使用：



```
sudo stop dnscrypt

```

[下载DNSCrypt](https://github.com/opendns/dnscrypt-proxy/downloads) (.deb、 .rpm以及源码都可供下载哦！)




---


via: <http://www.webupd8.org/2012/02/encrypt-dns-traffic-in-linux-with.html>


译者：[213edu](https://github.com/213edu) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
