---
layout: post
title:	"Linux 有问必答：在 Linux 如何更改文本文件的字符编码"
date:	2014-11-14 15:42:25 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,编码,iconv]
---



> 
> **问题**：在我的 Linux 系统中有一个编码为 iso-8859-1 的字幕文件，其中部分字符无法正常显示，我想把文本改为 utf8 编码。在 Linux 中, 有没有一个好的工具来转换文本文件的字符编码？
> 
> 
> 


正如我们所知道的那样，电脑只能够处理低级的二进制值，并不能直接处理字符。当一个文本文件被存储时，文件中的每一个字符都被映射成二进制值，实际存储在硬盘中的正是这些“二进制值”。之后当程序打开文本文件时，所有二进制值都被读入并映射回原始的可读字符。只有当所有需要访问这个文件的程序都能够“理解”它的编码，即二进制值到字符的映射时，这个“保存和打开”的过程才能很好地完成，这也确保了可理解数据的往返过程。


如果不同的程序使用不同的编码来处理同一个文件，源文件中的特殊字符就无法正常显示。这里的特殊字符指的是非英文字母的字符，例如带重音的字符（比如 ñ，á，ü）。


然后问题就来了： 1）我们如何确定一个确定的文本文件使用的是什么字符编码？ 2）我们如何把文件转换成已选择的字符编码？


![](/Asserts/Images//attachment/album/201411/14/154227jvuutdzqu9u9surr.jpg)


### 步骤一


为了确定文件的字符编码，我们使用一个名为 “file” 的命令行工具。因为 file 命令是一个标准的 UNIX 程序，所以我们可以在所有现代的 Linux 发行版中找到它。


运行下面的命令：



```
$ file --mime-encoding filename 

```

![](/Asserts/Images//attachment/album/201411/14/154230cgzc69w1mul3p9bp.jpg)


### 步骤二


下一步是查看你的 Linux 系统所支持的文件编码种类。为此，我们使用名为 iconv 的工具及 “-l” 选项（L 的小写）来列出所有当前支持的编码。



```
$ iconv -l 

```

iconv 工具是 GNU libc 库组成部分，因此它在所有 Linux 发行版中都是开箱即用的。


### 步骤三


在我们在我们的 Linux 系统所支持的编码里面选定了目标编码之后，运行下面的命令来完成编码转换：



```
$ iconv -f old_encoding -t new_encoding filename

```

例如，把 iso-8859-1 编码转换为 utf-8 编码：



```
$ iconv -f iso-8859-1 -t utf-8 input.txt 

```

![](/Asserts/Images//attachment/album/201411/14/154232a4q9di1i0pw0npns.png)


了解了我们演示的如何使用这些工具之后，你可以像下面这样修复一个受损的字幕文件：


![](/Asserts/Images//attachment/album/201411/14/154235p8b8gaw099a0o4g9.jpg)




---


via: <http://ask.xmodulo.com/change-character-encoding-text-file-linux.html>


译者：[wangjiezhe](https://github.com/wangjiezhe) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
