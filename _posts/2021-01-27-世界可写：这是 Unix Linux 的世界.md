---
layout: post
title:	"世界可写：这是 Unix/Linux 的世界"
date:	2021-01-17 12:32:00 +0800 
categories:	观点 linuxcn 
tags:	[linuxcn,Unix,权限]
---


![](/Asserts/Images/album/202101/17/123419bjsnqy3nsiyarjs3.jpg)


昨天发的一篇[新闻点评](/article-13021-1.html)中，提及了在 Ubuntu 21.04 中准备修复一个十多年的 Bug：将用户主目录的默认的“世界可写”权限取消，并对这条新闻吐槽了一番。


不料，这条新闻引来了一些意料之外的吐槽，大家在公众号、知乎、今日头条上看到这篇内容后，纷纷表示“**世界可写**”是机翻，是误读，应该翻译为“<ruby> 全局 <rt>  Global </rt></ruby>”。因此，我觉得有必要就此写点文字来说明一下。


说实话，我也是第一次看到“世界可写”这个翻译（这个翻译不是我发明的），初看之下有点诧异，但是细思之下，我认为，这个翻译还是颇有意思的。


<ruby> <a href="https://en.wikipedia.org/wiki/File-system_permissions#Traditional_Unix_permissions">  传统的 Unix 权限 </a> <rt>  traditional Unix permissions </rt></ruby>模型将用户分为三类：


* <ruby> <a href="https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_167">  属主 </a> <rt>  Owner </rt></ruby> 或 <ruby> 用户 <rt>  User </rt></ruby>类（`u`）：文件/目录的所有者
* <ruby> <a href="https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_173">  群组 </a> <rt>  Group </rt></ruby>类（`g`）：除所有者之外的文件/目录所属用户组的成员
* <ruby> <a href="https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_173">  其他 </a> <rt>  Other </rt></ruby>类（`o`）：“世界”上除以上二者外的其他人


对于 `chmod` 命令来说，我们有时候需要给这三类人都统一赋予一些权限，这种情况下，我们采用 `a` 来代表“<ruby> 全部 <rt>  All </rt></ruby>”，有时也称之为“<ruby> 世界 <rt>  World </rt> ”。这在各种文献中 <a href="https://man7.org/linux/man-pages/man1/chmod.1.html">  屡 </a> <a href="https://www.grymoire.com/Unix/Permissions.html">  见 </a> <a href="https://kb.iu.edu/d/abdb">  不 </a> <a href="https://www.ibm.com/support/pages/can-we-remove-world-writable-permissions-global-write-permission">  鲜 </a> 。</ruby>


对于“<ruby> 世界 <rp>  （ </rp> <rt>  World </rt> <rp>  ） </rp></ruby>”这个词汇，除看起来有点不太寻常，但是我觉得，这是一种 Unix 的古典黑客精神的幽默，可能是隐喻 Unix 机器里面就是一个世界吧，如果你连 Unix 用户都没有，那你就不是这个世界的。


Unix 世界只是 Unix 的<ruby> 世界 <rt>  World </rt></ruby>，从来不是<ruby> 全球 <rt>  Gloabl </rt></ruby>。


最后，“世界可写”万万要不得。022 赛高！
