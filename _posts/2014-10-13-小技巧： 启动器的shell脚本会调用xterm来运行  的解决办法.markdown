---
layout: post
title:	"小技巧：&quot;启动器的shell脚本会调用xterm来运行&quot; 的解决办法"
date:	2014-10-21 14:52:00 +0800 
categories:	桌面应用 linuxcn 
tags:	[linuxcn,启动器,终端,xterm]
---


本文针对 Mate 1.8.1 桌面环境下，CentOS 7.0 (x86\_64) 和 ArchLinux 2014.10.01 (x86\_64) 版本，也同样适用于存在类似问题的其他发行版本。


![](/Asserts/Images//attachment/album/201410/19/212020xixigeswh5whdnni.png)


（我自己仅仅在这两种发行版本下使用）


### 问题提出


按照旧思路，在面板中添加启动器指向 .sh 脚本，以这个为例：



```
/home/myname/Scripts/pacman_Update.sh
```

![](/Asserts/Images//attachment/album/201410/19/212023tq6lphwmjjpypdqh.png)


但是运行时会默认调用 xterm 来运行。界面既不美观，也不习惯，更为麻烦的是不支持粘贴操作。


![](/Asserts/Images//attachment/album/201410/19/212024ygrzw5nnhccpx7hp.png)


### 解决办法


需要将启动器指向修改为：



```
/usr/bin/mate-terminal -x /bin/sh -c '/home/myname/Scripts/pacman_Update.sh'
```

并且启动类型需要设置为“应用程序”，而不是“终端上的程序”。


![](/Asserts/Images//attachment/album/201410/19/212026wwuvq333v73nzauf.png)


执行结果如下：


![](/Asserts/Images//attachment/album/201410/19/212027djiqwewh3s8wwwg3.png)


如果本文对您有所帮助，欢迎转载和分享，谢谢！
