---
layout: post
title:	"Linux/Unix 桌面趣事：ASCII 艺术水族箱"
date:	2015-12-30 15:25:00 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,ASCIIQuarium]
---


你可以在你的终端中使用 ASCIIQuarium 安全地欣赏海洋的神秘了。它是一个用 perl 写的 ASCII 艺术水族箱/海洋动画。


### 安装 Term::Animation


首先你需要安装名为 Term-Animation 的perl模块。打开终端（选择程序 > 附件 > 终端），并输入：



```
$ sudo apt-get install libcurses-perl
$ cd /tmp
$ wget http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/Term-Animation-2.4.tar.gz
$ tar -zxvf Term-Animation-2.4.tar.gz
$ cd Term-Animation-2.4/
$ perl Makefile.PL && make && make test
$ sudo make install

```

### 下载安装 ASCIIQuarium


接着在终端中输入：



```
$ cd /tmp
$ wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz
$ tar -zxvf asciiquarium.tar.gz
$ cd asciiquarium_1.0/
$ sudo cp asciiquarium /usr/local/bin
$ sudo chmod 0755 /usr/local/bin/asciiquarium

```

### 我怎么观赏 ASCII 水族箱?


输入下面的命令：



```
$ /usr/local/bin/asciiquarium

```

或者



```
$ perl /usr/local/bin/asciiquarium

```

![Fig.01: ASCII Aquarium](/Asserts/Images//attachment/album/201512/25/152912u4yng3yg4ggr3z3e.png)


*ASCII 水族箱*


### 相关媒体







### 下载：ASCII Aquarium 的 KDE 和 Mac OS X 版本


[点此下载 asciiquarium](http://www.robobunny.com/projects/asciiquarium/html/)。如果你运行的是 Mac OS X，试下这个可以直接使用的已经打包好的[版本](http://habilis.net/macasciiquarium/)。对于 KDE 用户，试试基于 Asciiquarium 的[KDE 屏幕保护程序](http://kde-look.org/content/show.php?content=29207)




---


via: <http://www.cyberciti.biz/tips/linux-unix-apple-osx-terminal-ascii-aquarium.html>


作者：Vivek Gite 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
