---
layout: post
title:	"一条命令在Manjaro/Arch Linux上安装Sublime Text 3"
date:	2014-05-23 14:07:11 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,Sublime Text,Arch Linux]
---


[Sublime Text 3](http://www.sublimetext.com/3)目前还处于beta测试状态，目前最新的版本为Build 3059。 这个教程中我们将通过AUR安装Sublime Text 3 build 3059。


![](/Asserts/Images/album/201405/23/140713qs0jssqk707o31h1.png)


打开终端并运行下列命令, 选择是否(Y/N)继续安装（这里选择Y）。



```
sudo yaourt -S sublime-text-dev

```

![](/Asserts/Images/album/201405/23/140715hgl1lcebt2s34ugl.png)



```
loading packages...
resolving dependencies...
looking for inter-conflicts...
Packages (1): sublime-text-dev-3.3059-1
Total Installed Size: 16.02 MiB
:: Proceed with installation? [Y/n] y
(1/1) checking keys in keyring           [########################################] 100%
(1/1) checking package integrity         [########################################] 100%
(1/1) loading package files              [########################################] 100%
(1/1) checking for file conflicts        [########################################] 100%
(1/1) checking available disk space      [########################################] 100%
(1/1) installing sublime-text-dev        [########################################] 100%
 ------------------------------------------------------------------------------
==> sublime-text-dev install/upgrade note:
 ------------------------------------------------------------------------------
 To disable in-application reminders about new Sublime Text dev versions,
 add the following setting to your User Preferences file:
 "update_check": false
------------------------------------------------------------------

```

![](/Asserts/Images/album/201405/23/140717g17ldii31f6i286i.png)




---


via: <http://www.unixmen.com/install-sublime-text-3-build-3059-manjaroarch-linux/>


译者：[alim0x](https://github.com/alim0x) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
