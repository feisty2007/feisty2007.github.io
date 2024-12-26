---
layout: post
title:	"一个月内发现的第六起 Linux DDoS 木马"
date:	2016-09-17 20:04:19 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,木马,DDoS]
---


Linux 用户又有一个木马需要苦恼了，就像以往一样，这些坏蛋大多部署在被劫持的 Linux 系统上，并在接受到命令后发起 DDoS 攻击。


发现了这件事的 Dr.Web 的安全研究人员说，木马似乎是通过<ruby> 破壳漏洞 <rp>  （ </rp> <rt>  Shellshock </rt> <rp>  ） </rp></ruby>感染的这些 Linux 机器——现在仍然有很多设备没有补上这个漏洞。


![](/Asserts/Images/album/201609/17/200421kbihtjm4r43vidil.png)


该木马被命名为 [Linux.DDoS.93](http://vms.drweb.com/virus/?_is=1&i=8598428)，它首要会修改 /var/run/dhcpclient-eth0.pid 这个文件，并通过它在计算机启动时运行。如果该文件不存在，就会自己创建一个。


当该木马运行起来以后会进行初始化，它会启动两个进程，一个用于与 C&C （控制）服务器通讯，另外一个用于确保木马的父进程一直运行。


### 该木马启动 25 个子进程进行 DDoS 攻击


当控制该木马网络的攻击者发起攻击命令时，这个木马会启动 25 个子进程来进行 DDoS 攻击。


当前，该木马可以发出 UDP 洪泛（针对随机或特定端口），TCP 洪泛（简单的包，或给每个包随机增加至多 4096 字节的数据）和 HTTP 洪泛（通过 POST、GET 或 HEAD 请求）。


而且，该木马还能自我更新、自我删除、终止自己的进程、ping、从 C&C 服务器下载和运行文件。


### 当它发现某些名字时会关闭


这个木马还包括一个功能，如果在扫描计算机内存并列出活动的进程时发现如下字符串会关闭自己：



```
privmsg
getlocalip
kaiten
brian krebs
botnet
bitcoin mine
litecoin mine
rootkit
keylogger
ddosing
nulling
hackforums
skiddie
script kiddie
blackhat
whitehat
greyhat
grayhat
doxing
malware
bootkit
ransomware
spyware
botkiller
```

这些字符串大多数与信息安全领域有关，似乎是为了防止安全研究人员的反向工程研究，或者是为了避免感染该恶意软件作者自己的机器。


在感染过程中，该木马也会扫描它的旧版本，并会关闭旧版本然后安装一个新的。这意味着这是一个自动更新系统，该木马的最新版本总是会出现在被感染的机器上。


Linux 是过去一个月以来最热门的木马攻击平台，在最近 30 天内，安全研究人员已经发现、分析和曝光了其它五个 Linux 木马： [Rex](http://news.softpedia.com/news/rex-linux-trojan-can-launch-ddos-attacks-lock-websites-mine-for-cryptocurrency-507486.shtml)、[PNScan](http://news.softpedia.com/news/pnscan-linux-trojan-resurfaces-with-new-attacks-targeting-routers-in-india-507617.shtml)、[Mirai](http://news.softpedia.com/news/mirai-ddos-trojan-is-the-next-big-threat-for-iot-devices-and-linux-servers-507964.shtml)、 [LuaBot](http://news.softpedia.com/news/luabot-is-the-first-botnet-malware-coded-in-lua-targeting-linux-platforms-507978.shtml) 和 [Linux.BackDoor.Irc](http://news.softpedia.com/news/new-linux-trojan-discovered-coded-in-mozilla-s-rust-language-508135.shtml)。
