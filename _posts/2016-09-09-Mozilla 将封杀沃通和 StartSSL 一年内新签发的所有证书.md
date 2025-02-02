---
layout: post
title:	"Mozilla 将封杀沃通和 StartSSL 一年内新签发的所有证书"
date:	2016-09-28 08:29:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,SSL,CA,沃通,StartSSL]
---


Firefox 浏览器背后的 Mozilla 基金会正在考虑对沃通（WoSign）及被其秘密收购的 StartCom（著名的 StartSSL 即其旗下产品）这两个 CA 一年内新签发的所有 SSL 证书进行封杀。


Mozilla 的工程师是在对这两个 CA 签发了一系列可疑的 SSL SHA-1 证书进行调查之后，宣布了这个禁令。


![](/Asserts/Images/album/201609/27/235231v37ur7524fndn4n6.jpg)


### 这两家 CA 试图规避 SHA-1 停用政策


该问题主要是因为各大主要浏览器厂商共同决定从 2016 年 1 月 1 日开始就停止接受采用陈旧的 SHA-1 签名算法的证书。而 Mozilla 指责沃通今年还在签发 SHA-1 签名的证书，并将签发日期倒填成去年 12 月份。


虽然 Mozilla 也允许一些其它的 CA 在 2016 年 1 月 1 日之后继续签发 SHA-1 证书，比如说[赛门铁克](http://news.softpedia.com/news/mozilla-gives-a-security-pass-to-the-people-it-shouldn-t-500986.shtml)，但是他们仅允许那些通过了复杂的审批流程的 CA 这样做，而显然沃通没有得到同意。


### 沃通秘密收购了 StartCom


此外，沃通似乎在否认其收购了以色列 CA 公司 StartCom。Mozilla 说，沃通已经于 2015 年 11 月 1 日百分百地收购了 StartCom。而另一方面，[据奇虎 360 称](http://www.solidot.org/story?sid=49774)，它共计持有 84% 的沃通股份。但是这些信息沃通此前都予以否认或拒绝发表意见。


此外，在 Mozilla 披露的技术细节中显示，StartCom 已经开始使用沃通的基础架构来签发新的证书了。而且，StartCom 也和沃通一样在 2016 年采用了倒填日期的手段来签发 SHA-1 证书。Mozilla 的安全工程师也展示了这种违例的案例细节。


Mozilla 的调查发现，一个和 GeoTrust CA 合作了多年的付费处理机构 Tyro 突然在 6 月中旬使用 StartCom 部署了一个 SHA-1 签名的证书，而此前该机构从未和 StartCom 有过合作。该证书看起来是在 2015 年 12 月 20 日签发的，而在同一个日期 StartCom 签发大量的 SHA-1 证书。Mozlla 发现这些证书部署于 2016 年中，这很不正常，这显然是采用倒填日期来规避 SHA-1 停用的策略。


这些问题以及其它的[更多问题](https://wiki.mozilla.org/CA:WoSign_Issues)让 Mozilla 决定在至少一年内不再信任沃通和 StartCom 的 SSL 证书。


### 或许会永久封杀


Mozilla 说这个临时封杀仅针对这两个公司最新签发的证书，不影响已经分发给他们的客户的证书。如果这两个公司在一年的封杀后没有通过一系列的检查，Mozilla 将准备封杀这两个公司的所有证书。


“许多人都在盯着 Web PKI 安全体系，如果发现了这样的倒填（不管是什么原因），Mozilla 会立即永久地取消对沃通和 StartCom 根证书的信任。”该[报告](https://docs.google.com/document/d/1C6BlmbeQfn4a9zydVi2UvjBGv6szuSB4sMYUcVrR8vQ/preview#)中说。


此外，Chrome 和其它产品的对它们的封杀也在计划中。“其它的浏览器厂商和根证书存储运营者也会做出他们自己的决定，我们在这个文档中摆出了这些信息，以便他们了解我们做出这个决定的原因，并可以据此做出他们的决定。”Mozilla 说。
