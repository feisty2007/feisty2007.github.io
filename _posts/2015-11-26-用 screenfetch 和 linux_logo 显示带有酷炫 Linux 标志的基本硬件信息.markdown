---
layout: post
title:	"用 screenfetch 和 linux_logo 显示带有酷炫 Linux 标志的基本硬件信息"
date:	2015-11-02 09:52:00 +0800 
categories:	桌面应用 linuxcn 
tags:	[linuxcn,screenfetch,linux_logo]
---


想在屏幕上显示出你的 Linux 发行版的酷炫标志和基本硬件信息吗？不用找了，来试试超赞的 screenfetch 和 linux\_logo 工具。


![Linux Logo](/Asserts/Images//attachment/album/201511/01/230001y3s98ro26295ta9f.jpg)


### 来看看 screenfetch 吧


screenFetch 是一个能够在截屏中显示系统/主题信息的命令行脚本。它可以在 Linux，OS X，FreeBSD 以及其它的许多类Unix系统上使用。来自 man 手册的说明：



> 
> 这个方便的 Bash 脚本可以用来生成那些漂亮的终端主题信息和用 ASCII 构成的发行版标志，就像如今你在别人的截屏里看到的那样。它会自动检测你的发行版并显示 ASCII 版的发行版标志，并且在右边显示一些有价值的信息。
> 
> 
> 


#### 在 Linux 上安装 screenfetch


打开终端应用。在基于 Debian 或 Ubuntu 或 Mint 的系统上只需要输入下列 [apt-get 命令](http://www.cyberciti.biz/tips/linux-debian-package-management-cheat-sheet.html)：



```
$ sudo apt-get install screenfetch

```

![](/Asserts/Images//attachment/album/201511/01/230228p7if3cl27nh9zzf0.jpg)


*图一：用 apt-get 安装 screenfetch*


如果源里面没有这个软件，可以采用如下方法：



```
wget https://github.com/KittyKatt/screenFetch/archive/master.zip
unzip master.zip
sudo mv screenFetch-master/screenfetch-dev /usr/bin/screenfetch
```

#### 在 Mac OS X 上安装 screenfetch


输入下列命令：



```
$ brew install screenfetch

```

![](/Asserts/Images//attachment/album/201511/01/230229fs635gs5505w5k0g.jpg)


*图二：用 brew 命令安装 screenfetch*


#### 在 FreeBSD 上安装 screenfetch


输入下列 pkg 命令：



```
$ sudo pkg install sysutils/screenfetch

```

![](/Asserts/Images//attachment/album/201511/01/230231kl87dwsl750m0wal.jpg)


*图三：在 FreeBSD 用 pkg 安装 screenfetch*


#### 在 Fedora 上安装 screenfetch


输入下列 dnf 命令：



```
$ sudo dnf install screenfetch

```

![](/Asserts/Images//attachment/album/201511/01/230232ln4v994fu1fqvp2q.jpg)


*图四：在 Fedora 22 用 dnf 安装 screenfetch*


#### 我该怎么使用 screefetch 工具？


只需输入以下命令：



```
$ screenfetch

```

这是不同系统的输出：


![](/Asserts/Images//attachment/album/201511/01/230233w92d45x9bbtb7x21.jpg)


*Fedora 上的 Screenfetch*


![](/Asserts/Images//attachment/album/201511/01/230235x5ihd1qrq7e8hj1i.jpg)


*OS X 上的 Screenfetch*


![](/Asserts/Images//attachment/album/201511/01/230236b5ayn5uas6646yae.jpg)


*FreeBSD 上的 Screenfetch*


![](/Asserts/Images//attachment/album/201511/01/230237d3ru6tpt620640t6.jpg)


*Debian 上的 Screenfetch*


#### 获取截屏


要获取截屏并保存成文件，输入：



```
$ screenfetch -s

```

你会看到一个文件 ~/Desktop/screenFetch-\*.jpg。获取截屏并直接上传到 imgur，输入：



```
$ screenfetch -su imgur

```

**输出示例：**



```
                 -/+:.          veryv@Viveks-MacBook-Pro
                :++++.          OS: 64bit Mac OS X 10.10.5 14F27
               /+++/.           Kernel: x86_64 Darwin 14.5.0
       .:-::- .+/:-``.::-       Uptime: 3d 1h 36m
    .:/++++++/::::/++++++/:`    Packages: 56
  .:///////////////////////:`   Shell: bash 3.2.57
  ////////////////////////`     Resolution: 2560x1600 1920x1200
 -+++++++++++++++++++++++`      DE: Aqua
 /++++++++++++++++++++++/       WM: Quartz Compositor
 /sssssssssssssssssssssss.      WM Theme: Blue
 :ssssssssssssssssssssssss-     Font: Not Found
  osssssssssssssssssssssssso/`  CPU: Intel Core i5-4288U CPU @ 2.60GHz
  `syyyyyyyyyyyyyyyyyyyyyyyy+`  GPU: Intel Iris
   `ossssssssssssssssssssss/    RAM: 6405MB / 8192MB
     :ooooooooooooooooooo+.
      `:+oo+/:-..-:/+o+/-      

Taking shot in 3.. 2.. 1.. 0.
==>  Uploading your screenshot now...your screenshot can be viewed at http://imgur.com/HKIUznn

```

你可以访问 <http://imgur.com/HKIUznn> 来查看上传的截屏。


### 再来看看 linux\_logo


linux\_logo 程序生成一个彩色的 ANSI 版企鹅图片，还包含一些来自 /proc 的系统信息。


#### 安装


只需按照你的 Linux 发行版输入对应的命令：


#### Debian/Ubutnu/Mint



```
# apt-get install linuxlogo   ### 注意名字略微不同

```

#### CentOS/RHEL/旧版 Fedora



```
# yum install linux_logo

```

#### Fedora Linux v22+ 或更新版本



```
# dnf install linux_logo

```

#### 运行它


只需输入下列命令：



```
$ linux_logo

```

![](/Asserts/Images//attachment/album/201511/01/230238zgh6gy2aoirkh4e6.jpg)


*运行 linux\_logo*


#### 等等，还有更多！


你可以用这个命令查看内置的标志列表：



```
$ linux_logo -f -L list

```

**输出示例：**



```
Available Built-in Logos:
    Num Type    Ascii   Name        Description
    1   Classic Yes aix     AIX Logo
    2   Banner  Yes bsd_banner  FreeBSD Logo
    3   Classic Yes bsd     FreeBSD Logo
    4   Classic Yes irix        Irix Logo
    5   Banner  Yes openbsd_banner  OpenBSD Logo
    6   Classic Yes openbsd     OpenBSD Logo
    7   Banner  Yes solaris     The Default Banner Logos
    8   Banner  Yes banner      The Default Banner Logo
    9   Banner  Yes banner-simp Simplified Banner Logo
    10  Classic Yes classic     The Default Classic Logo
    11  Classic Yes classic-nodots  The Classic Logo, No Periods
    12  Classic Yes classic-simp    Classic No Dots Or Letters
    13  Classic Yes core        Core Linux Logo
    14  Banner  Yes debian_banner_2 Debian Banner 2
    15  Banner  Yes debian_banner   Debian Banner (white)
    16  Classic Yes debian      Debian Swirl Logos
    17  Classic Yes debian_old  Debian Old Penguin Logos
    18  Classic Yes gnu_linux   Classic GNU/Linux
    19  Banner  Yes mandrake    Mandrakelinux(TM) Banner
    20  Banner  Yes mandrake_banner Mandrake(TM) Linux Banner
    21  Banner  Yes mandriva    Mandriva(TM) Linux Banner
    22  Banner  Yes pld     PLD Linux banner
    23  Classic Yes raspi       An ASCII Raspberry Pi logo
    24  Banner  Yes redhat      RedHat Banner (white)
    25  Banner  Yes slackware   Slackware Logo
    26  Banner  Yes sme     SME Server Banner Logo
    27  Banner  Yes sourcemage_ban  Source Mage GNU/Linux banner
    28  Banner  Yes sourcemage  Source Mage GNU/Linux large
    29  Banner  Yes suse        SUSE Logo
    30  Banner  Yes ubuntu      Ubuntu Logo

Do "linux_logo -L num" where num is from above to get the appropriate logo.
Remember to also use -a to get ascii version.

```

查看 aix 的标志，输入：



```
$ linux_logo -f -L aix

```

查看 openbsd 的标志：



```
$ linux_logo -f -L openbsd

```

或者只是随机看看一些 Linux 标志：



```
$ linux_logo -f -L random_xy

```

你[可以像下面那样结合 bash 的循环来显示不同的标志](http://www.cyberciti.biz/faq/bash-for-loop/)，输入：


![](/Asserts/Images//attachment/album/201511/01/230241p2ut2tyjjzrtcqq8.gif)


*动图1： linux\_logo 和 bash 循环，既有趣又能发朋友圈耍酷*


### 获取帮助


输入下列命令：



```
$ screefetch -h
$ linux_logo -h

```

**参考**


* [screenFetch 主页](https://github.com/KittyKatt/screenFetch)
* [linux\_logo 主页](https://github.com/deater/linux_logo)




---


via: <http://www.cyberciti.biz/hardware/howto-display-linux-logo-in-bash-terminal-using-screenfetch-linux_logo/>


作者：Vivek Gite 译者：[alim0x](https://github.com/alim0x) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
