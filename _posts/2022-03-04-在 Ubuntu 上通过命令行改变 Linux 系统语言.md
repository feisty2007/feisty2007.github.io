---
layout: post
title:	"在 Ubuntu 上通过命令行改变 Linux 系统语言"
date:	2022-03-13 22:39:43 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,语言,locale]
---



> 
> 这是一个快速教程，展示了在 Ubuntu 和其他 Linux 发行版上从命令行改变语言的步骤。
> 
> 
> 


![](/Asserts/Images/album/202203/13/223937s17qtqz931grud89.jpg)


事实上，我一直在写西班牙语的文章。如果你没有访问过它并且/或你是一个讲西班牙语的人，请访问 [It's FOSS en Español](https://es.itsfoss.com/) 并查看所有西班牙语的 Linux 内容。


你可能想知道我为什么要和你分享这件事，这是因为这篇文章以这个新页面为例。


在新安装 [你喜欢的 Linux 发行版](https://itsfoss.com/best-linux-beginners/) 时，系统会要求你选择一种主语言。有些人，比如说我，后来会考虑把这个语言改成新的，尽管这并不频繁。


你看，我必须同时用西班牙语和英语进行截屏。这就成了一个问题，因为我只有一台电脑，而更换用户对我来说不是一个快速的解决方案。


这就是为什么我想和你分享这个快速技巧，我将告诉你如何在终端中用两行简单的文字改变你的主系统语言。


让我们开始吧！


### 从终端改变 Linux 系统语言


假设你想把你的主语言从英语改为西班牙语。


确认你将哪种语言设置为默认语言（主语言）。为此，让我们使用 `locale` 命令。



```
locale

```

你应该看到像这样的东西：



```
team@itsfoss:~$ locale
LANG=en_US.UTF-8
LANGUAGE=
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=

```

在这里你可以看到主语言是英语。现在要改变它，请按以下方式使用 `dpkg` 命令：



```
sudo dpkg-reconfigure locales

```

当你运行之前的命令，你应该在终端看到下面的页面：


![sudo dpkg reconfigure locales](/Asserts/Images/album/202203/13/223944kfhxblxa1ih3b8vv.png)


在这里，你应该**使用向上和向下的箭头移动**直到你到达所需的语言。在我的例子中，我想要西班牙语，更具体地说，是墨西哥西班牙语，因为我是墨西哥人。


不是所有的语言都有这个选项，但如果你的语言有，请选择 [UTF-8](https://en.wikipedia.org/wiki/UTF-8)。


找到你的语言后，**按空格键来标记**，然后**回车**。


![Selecting your language](/Asserts/Images/album/202203/13/223944uk6y7dk9hicek7m0.png)


最后，在最后一个窗口中，通过使用箭头键移动到该语言并按下**回车键**，选择该新语言作为你的默认语言。


![Setting new language as default](/Asserts/Images/album/202203/13/223944ul2qcevy2iivhzkl.png)


完成后，你应该在你的终端看到这样的信息：



```
Generating locales (this might take a while)...
    en_US.UTF-8... done
    es_MX.UTF-8... done
Generation complete.

```

这就完成了！现在你能够直接从终端改变你的默认语言，次数不限。


如果你对这个话题有任何疑问，请在评论区告诉我们。




---


via: <https://itsfoss.com/change-locales-linux/>


作者：[Marco Carmona](https://itsfoss.com/author/marco/) 选题：[lujun9972](https://github.com/lujun9972) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
