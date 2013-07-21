---
layout: post
title: "Fedora Core 19边走边写"
description: "每一个人都期待一个新的旅程，这次从Fedora core 19开始！"
category: blog 
tags: [Fedora Core，Linux]
---
{% include JB/setup %}

###闲言碎语


其实操作系统没有那么重，特别是PC上面的操作系统。因为现在PC上面无论Windows还是Linux，Web都围绕着我们。在Web上面，有可以让我们写的东西，还有长短可以选择，长篇大论可以写成博客，短小精悍的可以写成微薄，任君选择。而且可以自由选择写作地点，譬如坐在公交上面来一张帮助老太太的美好青年，在高山峡谷来一张云天绿树，也可以在家每天习惯像写日记一样写一篇，地点同样随心所欲，更何况是大便时、吃饭前等无数的碎片时间。

无论如何，我们处在了一个联网的时代，PC并不是我们的唯一，Iphone、Andriod等平台同样百花齐放。Windows有的时候也就显得不是那么必须了，其实真的想想除了游戏，其它的操作系统那一样不能完成，反正都是Web。

###前话

操作系统都有权限的概念，因此下面的东西都是在su状态下面进行的。

当然你可以直接用su命令进入root上帝模式，进行操作，当然很爽，其实我就是这么做的。

另外你比较严谨，也可以使用su -c模式来运行操作。

下面的东西很有用，嗯嗯，仔细看！

###目录

* 国内的YUM源
* Flash的安装
* Chrome浏览器的安装
* Grub2缺省操作系统的制度


####国内的YUM源

国内的YUM源，推荐163和搜狐2个网站的开源站点。

163的Url：http://mirrors.163.com/.help/fedora.html

在这里可以使用wget来下载。


wget http://mirrors.163.com/.help/fedora-163.repo

wget http://mirrors.163.com/.help/fedora-updates-163.repo

下载完成以后，放在/etc/yum.repos.d/

搜狐的Url:http://mirrors.sohu.com/help/fedora.html

同样可以用weget下载：

wget http://mirrors.sohu.com/help/fedora-sohu.repo

wget http://mirrors.sohu.com/help/fedora-updates-sohu.repo

####Flash的安装
其实Adobe有自己的YUM源，只需要安装以下，把Adobe的YUM源加入一下，然后就方便的安装软件了！

命令如下：

rpm -Uvh http://linuxdownload.adobe.com/adobe-release/adobe-release-i386-1.0-1.noarch.rpm

rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux

然后安装FlashPlayer：

yum install flash-plugin nspluginwrapper alsa-plugins-pulseaudio libcurl

yum install AdobeReader_chs # _chs表示简体中文版，英文版为AdobeReader_enu

####Chrome浏览器的安装

这个比较简单。从Google直接下载Chrome的RPM安装包就可以了！



####Grub2缺省操作系统

查找Windows系统
cat /boot/grub2/grub.cfg |grep Windows
result:-

menuentry "Windows 7 (loader) (on /dev/sda1)" --class windows --class os {
Set Windows menuentry as default (only entry mentioned in either " or ' from above command)

用grub2-set-default设置，参数为启动项的名称
grub2-set-default "Windows 7 (loader) (on /dev/sda1)"

查看设置结果：

grub2-editenv list

如果结果正确，写入配置文件，用grub2-mkconfig命令
grub2-mkconfig -o /boot/grub2/grub.cfg

####最后

说真的，有的时候，我被某些东西给震惊了，就在我安装FC19的小时以内。华丽的界面、如风的安装速度，当然很震惊！

当我安装完成以后，结果给我来个黑屏，这是要闹那样！

我换了几个操作系统，包括Ubuntu、Linux Mint等，全部黑屏。后来我才发现，不是黑屏了，是系统一启动，系统屏幕的亮度就不知道为什么调节到了最低，跟黑屏一样。

于是，我就按下了休眠快捷键，然后唤醒，然后桌面就出现了。

我不知道一个初学者如何面对这种情况，特别是一个心怀热忱的Linux初学者，最后会以怎样马娘或者沮丧的态度离开。

是啊。至少Ubuntu8、FC8的时候，我们的老爷机器还能启动，这么多年过去了，TMD这就是Linux桌面技术的进步，这就是GNOME3、Uubntu那些成要做操作系统手机的人做成的翔。

发了阵牢骚，FC19凑合着用吧，反正操作系统也不是那么重要是不是，怎么不是玩啊！


Edit By [MaHua](http://mahua.jser.me)
