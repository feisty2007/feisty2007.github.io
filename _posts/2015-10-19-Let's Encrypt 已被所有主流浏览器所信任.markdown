---
layout: post
title:	"Let's Encrypt 已被所有主流浏览器所信任"
date:	2015-10-21 19:35:53 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Let’s Encrypt,HTTPS]
---


旨在让每个网站都能使用 HTTPS 加密的非赢利组织 Let’s Encrypt 已经得了 [IdenTrust](https://identrustssl.com/) 的交叉签名，这意味着其证书现在已经可以被所有主流的浏览器所信任。从这个里程碑事件开始，访问者访问使用了 Let’s Encrypt 证书的网站不再需要特别配置就可以得到 HTTPS 安全保护了。 


![](/Asserts/Images/album/201510/21/193557zacu8jp6xu9jxppj.png)


Let’s Encrypt 的两个中级证书 Let’s Encrypt Authority X1 和 Let’s Encrypt Authority X2 得到了交叉签名。Web 服务器需要在证书链中配置交叉签名，客户端会自动处理好其它的一切。


你现在可以[在此](https://helloworld.letsencrypt.org/)体验一下使用新的交叉签名的中级证书所签发证书的服务器。


![https://helloworld.letsencrypt.org/](/Asserts/Images/album/201510/21/192558yf9wg9uglwfyg969.jpg)


越来越多的重要的个人和商业信息在互联网上传递着，对它们的加密需求也越来越迫切。这就是创建 Let’s Encrypt 的目的，这次迈进的一大步将会把安全连接带到 web 世界的每一个角落。


Let’s Encrypt 项目获得了 Mozilla、思科、Akamai、IdenTrust 和 EFF 等组织的支持，由 Linux 基金会托管。它在9月中旬颁发了第一个证书，计划于11月16日向公众开放免费签名服务。
