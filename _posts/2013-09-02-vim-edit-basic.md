---
layout: post
title: "vim编辑基础"
description: ""
category: blog 
tags: [vim,byte of vim]
---
{% include JB/setup %}

###介绍

下面，将介绍vim的基础编辑命令，包括读/写文件、剪切/复制/粘贴、撤销/重复和搜索。

###文件的读写

####Buffers（内存）

当你编辑文件的时候，vim会把文件的内容从硬盘加载到计算机的内存里面。也就是说文件的一个拷贝副本会被放在计算机内存里面，当你进行了修改，修改会立刻体现出来。当你编辑完成，你必须保存文件，以便让vim把内存里面的文件存储到硬盘上（因为计算机内存一旦vim退出，vim所使用的内存就立刻被操作系统转为它用了，要么清空，要么存储其它内容，这就意味着你的修改就消失了。而硬盘则是相对比较固定的存储，只要文件不擅长或者硬盘硬件不损坏，文件的内容就会永久存在）。存储文件内容的内存空间就被成为“Buffer”。其实这个概念在所有的文字编辑器里面都是通用的。

现在，打开Vim，输入“Hello world",并且存为`hello.txt`.如果你不知道怎么做，翻看一下前面的章节。

####Swap(交换区）

现在你可能注意到在`hello.txt`的同目录下面存在一个名为`hello.txt.swp`的文件出现了。使用下面的命令，来看一下你的swap文件的名字：

	:swapname

这个文件是什么？vim会维护一个内存景象的备份文件，以防止因为计算机崩溃等原因所导致的编辑丢失。也就是说在你最后一次保存文件的时候，vim会进行一次备份。备份文件叫做'swap file'.vim会一直自动维护这个文件。查看`:help swap-file`浏览更多细节。

####保存文件

现在进行一个小小的修改，按～键来改变一下光标位置字符的大小写，你会发现Vim会标记这个文件已经被修改（在GUI版本的vim里面，在标题栏的文件名旁边会出现一个“+”）。现在你可以打开其它编辑器，查看一下文件是否已经修改（一般是没有）。因为现在vim只是改变了buffer的内容，而并没有把改动写入到硬盘）。

现在我们可以通过下面的命令，把修改写入到硬盘：

	:write

注意：
	为了保存方便，你可以在.vimrc里面建立一个快捷键：
	
	" To save Ctrl-s
	nmap <c-s> :w<CR>
	imap <c-s> <Esc>:w<CR>a

现在保存文件按一下Ctrl+s就可以了。

####工作目录

默认情况下，vim启动是会把你的HOME目录作为起始目录，然后所有的文件操作都是在这个目录里面工作。

如果想打开其它目录的文件，你可以使用下面的命令：

	:e ../tmp/test.txt
	:e c:\\shoppig\\monday.txt

或者切换vim的工作目录：
	
	:cd ../tmp

:cd是c‘hang di’rectory的缩写

如果你不知道当前目录，可以使用：

	:pwd

:pwd是p'rint w'orking d'irectory的缩写。

###剪切、拷贝和粘贴

同普通桌面（譬如windows，KDE）不同，vim使用不同的术语：

普通桌面	vim         操作键
cut         delete        d
copy        yank          y
paste       paste         p

在普通情况下，“cut”（剪切）文本的意思是删除当前文本然后把它保存到剪贴板里面。在vim里面，cut意味着从文件的buffer里面删除文本，然后把它保存到vim的“寄存器”里面。在vim里面有很多寄存器可以选择，但同样必须删除当前文本。

同“剪切”类似，在普通桌面里面，拷贝就是把文本存储到剪贴簿里面，vim是把它存储到“寄存器”里面。

Paste（粘贴），vim的意义同普通桌面相同。

我们已经知道vim的“剪切、拷贝和粘贴”的操作，但如何制定要操作的文本呢？我们在前面的章节已经讲述过了。

下面，我们来举一个例子。

在vim里面输入下面的文字：

	This is the rthe first paragraph.
	This is the second line.

	This is the second paragraph.

现在把光标定位到第一行的开头位置，提示，你可以使用`1G`和行内移动命令来完成，譬如‘^’。

现在，我们看下，`rthe`单词明显是一个错误单词，我们需要把`r`删除。按下3w往后移动到rthe单词。

现在删除`r`.

命令分2部分。

操作       对象
delete   一个字符
d         1

所以，我们输入`d1`就可以了。

现在我们发现第一行变成了这个样子：
	
	This is the the first paragraph.	

'the'单词出现了2次，如何改正呢？

使用下面的命令：
操作       对象
Delete   单词
d        w

所以，我们输入'dw'就可以了，沃！是不是非常的简单优美？优美之处在于可以通过不同的组合就可以完成不同的操作。

如何来完成删除一行呢？很简单，‘dd“命令就是。

在我们的例子里面是这样的：

	This is the first paragraph.
	This is the second line.

	This is the second paragraph.	

使用‘j’键来跳到下一行，然后使用“dd”命令来删除当前行。这时文本变成了：

	This is the first paragraph.


	This is the second paragraph.	

现在，我们看下如何进行vim式的拷贝-》yank？

操作      目标
yank    当前段
y       ap

OK，vim会拷贝当前段落。

现在拷贝完成，如何粘贴呢？按`p`。

你会看到：

	This is the first paragraph.
	This is the first paragraph.


	This is the second paragraph.	

特别注意，yap会拷贝段落下面的空行。

实践上，p的大小写也有不同的含义（记得前面的i和I,a和A吗？）

p（小写） 粘贴到光标后面
p（大写） 粘贴到光标前面

有了上面的基础，我们可以把他们组合完成更加高级的操作。

怎么交换2个字符的位置？输入`xp`

* x->删除当其字符
* p->拷贝到当前字符后面

怎么交换2个单词的位置，输入`dwwP`

* d-> 删除
* w->一个单词
* w->移动到下一个单词
* P->粘贴到当前字符前面

重要的不是死记硬背这些操作技巧，而是深入理解这些操作的内涵，把变为你指尖的自然而然的敲击，无需思考，浑然天成！

###标记位置

假设，你正在编写文件的某个部分，突然你想到可能需要对前面的某一个部分内容进行修改。现在摆在你面前的问题是，如果你修改完成，如何回到当前的位置？vim有这个功能吗？mark（标记）可以帮助你。

你可以按下'm'然后按下‘a-zA-Z’里面的一个字母，譬如按下a，就会产生一个名字为‘a’的标记位置。

做好标记以后，你就可以随时返回这个位置。


###时光机器（撤销/重复）

假设，你现在正在修改一个文件，你想退回到从前的内容。Udno撤销就是你需要做的。如果你需要重复刚才的动作，redo就是你的工具。

假设有下面的文字：

	I have coined a phrase for myself-'Cut to the G'
	1.Concentrate
	2.Understand
	3.Think
	4.Get Things done
	Step 4 is eventually what gets you moving,but Step 2 and 3 are equally
	import.As Abraham Lincoin once said "If I had eight hours to chop down a 
	tree,I'd spend six hours sharping my axe."And to get to this staage,you need to
	do Step 1 which boils down to one thing - It's all in mind.That's why it's so
	hard.

现在，开始编辑第一行：

* 按下S来替换整行
* 输入“After much thought ,I have coined a new phrase to help me solidify my approach:"
* 键入Esc

现在看一下是不是好很多？

现在按下`u`来撤销一下修改，你会看到“I have coined a phrase for myself-'Cut to the G'”又重新出现了。按下`ctrl-r`，第一句就会变成“After much thought ,I have coined a new phrase to help me solidify my approach:”。

特别注意，vim的撤销和重复是没有次数限制的，但是从节省内存的角度来讲，通常使用`undolevels`参数来设定次数。

现在，我们看一下vim的“撤销/重复”的一些高级功能。在某种意义上，vim并不是一个编辑器那么简单，你可以把它当成一个“时光机器”。

譬如：
	
	:earlier 4m

会把你的编辑状态恢复到4分钟以前。

这个功能的强大之处在于把包含你所有的“撤销/重复”操作，也就是在这4分钟以内的所有操作。

同时，你也可以使用前进状态：

	:later 45s

就会把你带到某个时间段的45秒后的状态。

或者你干脆可以退回5步：

	:undo 5

你可以使用下面命令来查看退回列表：

	:undolist

查看“:help undolist”会看到更多解释。


###一个本地搜索引擎

vim内置一个搜索引擎，可以帮助你找到你需要的内容。下面我们测试一下。

回到前面熟悉的一段文字：

	I have coined a phrase for myself-'Cut to the G'
	1.Concentrate
	2.Understand
	3.Think
	4.Get Things done
	Step 4 is eventually what gets you moving,but Step 2 and 3 are equally
	import.As Abraham Lincoin once said "If I had eight hours to chop down a 
	tree,I'd spend six hours sharping my axe."And to get to this staage,you need to
	do Step 1 which boils down to one thing - It's all in mind.That's why it's so
	hard.

现在，假如我们想查找“step”这个单词，在正常模式下，我们输入“/step”然后回车，vim就会自动带我们到发现“step”的位置。输入‘n’会往后查找，输入‘N’会往前查找。

如果你只知道一部分内容或者记忆比较模糊呢？vim会提供什么帮助呢？你可以开启下面的选项：

	set incsearch

你也可以配置搜索的时候，忽略大小写：

	set ignorecase

或者使用

	set smartcase

当‘smartcase’配置为“on”的时候：

* 假如你搜索/step，vim会不分大小写来搜索‘step’，譬如会搜索到‘Step’，“Stephen”、“stepbrother"等等。
* 如果你搜索/Step，它只会搜索以“Step”为开头的单词，譬如“Step”、“Stephen”，而不会搜索“stepbrother”、“misstep”。

现在我们已经了解了vim的基本搜索，其实探索一下vim搜索的真正威力。首先，vim并不是仅仅可以进行单词搜索，它的搜索方式可以是“表达式”搜索。表达式可以让你制定搜索文字的类型，而不是仅仅是这个单词的外观。

譬如，你就是想仅仅“step”这个单词，而不是“steps”或者“footstep”里面的step。你可以使用"/\<step\>"。

类似的，如果你想搜索“step+数字”这种单词，你可以使用“step/\d\+”来进行搜索。

详细内容，你可以使用帮助“:help pattern”。

###总结

我们上面探索了很多vim的一些日常编辑命令。我们应该多多实践，重复练习。重要的不是记住这些命令的每一个参数和细节。如果你知道这些命令，并且根据需要知道在哪里找到更多帮助，那么就会变成一个合格的vimmer。

现在，出发开始你的编辑旅程吧！



	
