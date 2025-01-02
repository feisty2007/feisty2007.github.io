---
layout: post
title:	"谷歌也不信任沃通的证书了，StartCom CA 一并受到同等处罚"
date:	2016-11-02 08:24:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,沃通,StartCom]
---


继 Mozilla 做出对<ruby> 沃通 <rp>  （ </rp> <rt>  WoSign </rt> <rp>  ） </rp></ruby>的[处罚决定](/article-7898-1.html)之后，谷歌也跟随了这一做法，从 Chrome 56 开始，不再信任沃通及被其收购的 StartCom 于 2016 年 10 月 21 日之后所颁发的证书。


此前， 苹果已经率先于 [9 月 30 日](https://support.apple.com/en-us/HT204132)将沃通的根证书[从证书存储库中移除](/article-7846-1.html)了。虽然沃通及其被其秘密收购的 StartCom 均存在不同程度的 CA 违规问题，但是苹果和 Mozilla 在最近的操作中都只对沃通采取了处罚，而谷歌的处置则更进一步，也同时对 StartCom 进行了同等处罚。


![](/Asserts/Images/album/201611/01/232735zu1qnbnnffbvf8mn.jpg)


谷歌在其[通告](https://security.googleblog.com/2016/10/distrusting-wosign-and-startcom.html)中说：



> 
> 谷歌已经查明了沃通和 StartCom 这两个 CA 没有维持对其作为 CA 的高标准预期，因此根据我们的[根证书策略](https://www.chromium.org/Home/chromium-security/root-ca-policy#TOC-Removal-of-Trust)，谷歌 Chrome 将不再信任它们。这个观点类似于苹果和 Mozilla 的根证书计划发出的最近公告。
> 
> 
> 


在 2016 年 8 月 17 日，谷歌接到了 GitHub 安全团队的通告，称沃通在没有得到他们授权的情况下签发了一个 GitHub 的证书。这促使 GitHub 安全团队和 Mozilla 合作对沃通进行了调查，发现了[沃通的若干违规签发证书的问题](https://wiki.mozilla.org/CA:WoSign_Issues)。该调查表明沃通有意地规避了浏览器限制（即对 SHA-1 签名证书的失效计划）和对 CA 的要求。更进一步的，还发现了另外一家 CA 公司 StartCom 也被沃通秘密收购，这违反了对 CA 公司被收购需要披露信息的要求。而且，沃通公司还替换了原 StartCom 的基础设施、人员、政策和签发系统。面对这种情况，沃通和 StartCom 管理层还尝试误导社区这两个公司之间的收购事实和关系。


谷歌于 10 月 31 日发布了 Chrome 56 的 Dev 渠道版本。谷歌决定从该版本的 Chrome 开始，不再信任沃通和 StartCom 于 2016 年 10 月 21 日之后签发的证书。在这个日期之前签发的证书依旧信任，但是之后，除非他们遵循 [Chrome 的证书透明策略](https://www.chromium.org/Home/chromium-security/root-ca-policy/CTPolicyMay2016edition.pdf?attredirects=0)，将只能对其已有客户的域名签发。按照计划，Chrome 56 将于 2017 年 1 月正式发布稳定版，因此在此之前，**使用这两个 CA 所签发证书的网站应该尽快迁移到其它被 Chrome 信任的 CA 所签发的证书下**。


沃通和 StartCom 的客户会发现他们的证书在 Chrome 56 中不再有效。并且，更严厉的是，谷歌还说：



> 
> 在接下来的 Chrome 版本中，还会进一步减少对这两个 CA 签发的证书的支持，直到最终完全移除对这两个 CA 的信任！
> 
> 
> 


并且称：



> 
> 沃通和 StartCom 的任何试图规避处罚的做法都将导致这两个 CA 被马上全部移除！
> 
> 
> 


沃通的证书在国内使用比较多，而 StartCom 的 StartSSL 证书则在全球范围内有广泛的使用，尤其是它的免费证书有很多个人网站在使用。鉴于 Chrome 在浏览器市场上已经占据了[一半左右的份额](/article-7534-1.html)，因此其带来的影响将是毁灭性的。


目前，主流浏览器里面，Mozilla 的 Firefox 、苹果的 Safari 和谷歌的 Chrome 都已经做出了相应的反应，但是我们目前还没见到微软对此的跟进和表态。似乎微软在 CA 策略方面一向比较散漫，因此，IE 和 Edge 浏览器的反应或许还需要一段时间，抑或不会采取措施。
