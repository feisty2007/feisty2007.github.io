---
layout: post
title: "VIM移动（vim系列之一）"
description: ""
category: blog 
tags: [vim,byte of vim]
---

###介绍

一旦你开始写一些东西，编辑和修改需要移动输入位置就是家常便饭了。譬如，你正在写小说，突然你有一个新的灵感，但是当你把新灵感写完以后，如何快速回到你当前的编辑状态呢？


下面，我们来看一些vim的快速移动：

* 下个单词，按‘w'（next word）
* 下一个自然段，按"}"
* 移动到“h”字符第三次出现的地方，按"3fh"
* 向下移动35行，按“35j”
* 回到上次位置，输入Ctrl+o

首先，打开一个文件，命名为"chandrayaan.txt",输入下面内容：

	Chandrayaan-1 is India's first mission to the moon.Luanched by India's nation space agentcy the Indian Sapce Research Organisation(ISRO).The unmanned lunar exploration mission include a lunar orbiter and an impator. 
	The spacecraft was launched a modified version of the PSLV XL on 22 October 2008 from Satish Dhawan Space Centre,Sriharikota,Andhra Pradesh at 06:23 IST(00:52 UTC).


###VIM式移动

最基础的移动键是`hjkl`,这四个按键分别对于“上，下，左，右”，注意一些，它们在键盘上离你的右手位置并不远！

为什么不直接用键盘上的方向键呢？主要问题是他们在键盘上在另外一个区域，找到他们需要更多的移动你的手，缺乏效率！

记住，现在把你的右手手指放在jkl;上面，现在来看如何使用：

	h 左移
	j 下移
	k 上移
	l 右移

注意，我们可以通过在前面添加数字来表示重复多少次。譬如，`2j`表示下移2次。

打开“chandrayaan.txt”，开始实践吧：

+ 按下2j，你会看到光标下移了2次
+ 按下2k，往上移动，或者按下Ctrl+o，移动到原来位置
+ 按下5l，向右移动5次
+ 按下5h，向左移动5次

多尝试几次，你就会惊奇的发现这种操作方式是多么的高效！

当然，还有更多的惊喜。譬如：

'Home'（移动到行首） ^
'end'（移动到行尾） $
'PgUP'(翻到上一页） Ctr+b(backward)
'PgDn'(翻到下一页） Ctr+f(forward)

如果你知道行号，譬如50，你按下`50G`，vim会自动跳到第50行。如果只有`G`而没有数字，vim会跳到最后一行。怎么到第一行呢？“1G”即可。

下面试一下：
+ 移动到第一行，输入“1G”
+ 右移20个字符，输入“20l”
+ 移动到行首，输入“^”
+ 移动到行尾，输入“$”
+ 移动到最后一行，输入“G”

如何移动到屏幕中间呢？

+ 按下“H”（high），跳到屏幕最上面（high）的一行
+ 按下“M”（middle），跳到屏幕之间（middle）的一行
+ 按下“L”（low），跳到屏幕最下面（low）的一行

现在，你会发现，你的手基本上在一个特定的区域内移动。

###词语，行，段落

下面我们将往更广阔的区域来进发。首先我们来一个示例句子：

	The polar regions are of special interest,as they might contain ice.

我们来进行一系列操作，同时我们约定，以【】来标志光标位置。

首先，我们按下`^`:

	【T】he polar regions are of special interest,as they might contain ice.

可以看到光标位置在行首。

第二步，我们输入`w`，意思是移动到下一个词语(next 'w'ord):

	The 【p】olar regions are of special interest,as they might contain ice.

继续移动，输入`2w`:

	The polar regions 【a】re of special interest,as they might contain ice.

按下`e`,会移动到词语的末尾(‘e’nd)。

	The polar regions ar【e】 of special interest,as they might contain ice.

回退（'b'ackward)一个单词,按下`b`。输入2b，

	The polar 【r】egions are of special interest,as they might contain ice.

输入：help word-motions 可以看到更多内容。


现在看看段落移动，按下`）`。

	【C】handrayaan-1 is India's first mission to the moon.Luanched by India's nation space agentcy the Indian Sapce Research Organisation(ISRO).The unmanned lunar exploration mission include a lunar orbiter and an impator. The spacecraft was launched a modified version of the PSLV XL on 22 October 2008 from Satish Dhawan Space Centre,Sriharikota,Andhra Pradesh at 06:23 IST(00:52 UTC).

输入`）`：

	Chandrayaan-1 is India's first mission to the moon.【L】uanched by India's nation space agentcy the Indian Sapce Research Organisation(ISRO).The unmanned lunar exploration mission include a lunar orbiter and an impator. The spacecraft was launched a modified version of the PSLV XL on 22 October 2008 from Satish Dhawan Space Centre,Sriharikota,Andhra Pradesh at 06:23 IST(00:52 UTC).

很酷吧。按下“（”，你会看到光标又回到“C”。

现在多打几个自然段，输入“{”和“}”试验一下。

###书签

设想一下状况，你现在正在编辑某些东西，突然想到需要修改这个文档的另外一个部分，然后修改完成以后，如何快速回到之前编辑的地方呢？

在vim里面你可以，先用`ma`做个书签(m-mark,a代表你的标签名称，你可以使用a-zA-Z来命名，也就是说你可以做52个标签）。开始修改，譬如输入“199G“，到199行修改。修改完成以后，只需要“'a”,就会回到刚才你编辑的地方。

###跳转队列

你可以使用`Ctrl+o`来跳回你上次的光标所在地，使用`Ctrl+i`来跳回来。

###部分文字

有很多种方法，你可以把你需要操作的文本传递给vim的命令。譬如，你向把某一部分的文字转化一下大小写（vim可以用～键盘）。

输入下面的文字：

	Dapping means being determined about being determined and being passionate about being passionate.
	Be a dapper.

按下`v`进入“visual”模式，输入“ap”来选择一段（'a' 'p'aragraph)。按下“～”来转换一下。如果你想取消，按下Esc。

	Dapping means being determined about being determined and being passionate about being passionate.
	bE A DAPPER.

另外的选择命令包括，aw代表一个词语（a word),a"代表以"保卫的一段词语（譬如"this is a  quoted string"),ab代表一个块（a block).

查看 :help object_motions和 :help text-objects.

###总结

我们已经看到了VIM在光标移动方面提供的丰富特征。记住全部的每一个快捷键并不重要，更加重要的是，把你需要的快捷键转换为你手指的一种本能，只有这样，才能释放你的灵感，而不是如何使用VIM。
	
