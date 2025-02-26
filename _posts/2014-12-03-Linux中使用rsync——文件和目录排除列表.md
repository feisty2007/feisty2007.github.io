---
layout: post
title:	"Linux中使用rsync——文件和目录排除列表"
date:	2014-12-23 11:10:00 +0800 
categories:	系统运维 linuxcn 
tags:	[linuxcn,rsync]
---


**rsync**是一个十分有用，而且十分流行的linux工具。它用于备份和恢复文件，也用于对比和同步文件。我们已经在前面的文章讲述了[如何在Linux下使用rsync](http://linux.cn/article-4503-1.html)，而今天我们将增加一些更为有用的rsync使用技巧。


![](/Asserts/Images/album/201412/22/211129pzu2cgsd7dlz933t.jpg)


### 排除文件和目录列表


有时候，当我们做大量同步的时候，我们可能想要从同步的文件和目录中排除一个文件和目录的列表。一般来说，像设备文件和某些系统文件，或者像临时文件或者缓存文件这类占据不必要磁盘空间的文件是不合适同步的，这类文件是我们需要排除的。


首先，让我们创建一个名为“excluded”的文件（当然，你想取什么名都可以），然后将我们想要排除的文件夹或文件写入该文件，一行一个。在我们的例子中，如果你想要对根分区进行完整的备份，你应该排除一些在启动时创建的设备目录和放置临时文件的目录，列表看起来像下面这样：


![rsync excluded](/Asserts/Images/album/201412/22/211143ws9i3xolll2kxzq3.jpg)


然后，你可以运行以下命令来备份系统：



```
$ sudo rsync -aAXhv --exclude-from=excluded / /mnt/backup

```

![rsync exclude file](/Asserts/Images/album/201412/22/211145q99j2h1hhtgwa92i.jpg)


### 从命令行排除文件


你也可以从命令行直接排除文件，该方法在你要排除的文件数量较少，并且在你想要将它写成脚本或加到crontab中又不想脚本或cron依赖于另外一个文件运行时十分有用。


例如，如果你想要同步/var到一个备份目录，但是你不想要包含cache和tmp这些通常不会有重要内容的文件夹，你可以使用以下命令：



```
$ sudo rsync -aAXhv --exclude={"/var/cache","/var/tmp"} /var /home/adrian/var

```

![rsync exclude](/Asserts/Images/album/201412/22/211148tdy8rm7adndvy8d1.jpg)


该命令易于在脚本或cron中使用，也不会依赖其它文件。




---


via: <http://linoxide.com/linux-command/exclude-files-rsync-examples/>


作者：[Adrian Dinu](http://linoxide.com/author/adriand/) 译者：[GOLinux](https://github.com/GOLinux) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
