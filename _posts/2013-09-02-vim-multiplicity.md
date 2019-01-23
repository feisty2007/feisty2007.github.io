---
layout: post
title: "vim里面的多个"
description: ""
category: blog 
tags: [vim,byte of vim]
---

###介绍

这个章节，我们探索vim如何帮助在一个文件的不同部分之间、不同的文件之间，不同的窗口和不同的标签页之间，让我们更平滑的进行工作。最后，学习一下如何管理文件。

###使用折叠来分段

如果你在阅读一片非常长的文档，能否集中精力观看其中一部分，而把其它部分“折叠”起来呢？

这在vim里面叫做“folding”。

我们来看下面的一个结构化的文档，它按照层次进行缩进排列：
	
	Book I

		The Shadow of the Past

			Three Rings for the Elven-kings under the sky,
			Seven for the Dwarf-lords in their halls of stone,
			Nine for Mortal Men doomed to die,
			One for the Dark Lord on his dark throne
			In the Land of Mordor where the Shadows lie.
			One Ring to rule them all, One Ring to find them,
			One Ring to bring them all and in the darkness bind them
			In the Land of Mordor where the Shadows lie.

		Three is Company

			The Road goes ever on and on
			Down from the door where it began.
			Now far ahead the Road has gone,
			And I must follow, if I can,
			Pursuing it with weary feet,
			Until it joins some larger way,
			Where many paths and errands meet.
			And whither then? I cannot say.

输入万这段文字以后，运行`:set folmethod=indent`,把光标移动到你希望折叠的地方，按下`zc`，你会看到文字是如何“折叠”起来的。输入`zo`,文字就会打开。

出于个人喜好，我喜欢用“空格”键来打开和折叠文本。这个可以在vimrc里面配置。

zo和zc默认代表a'lternate between o'pening and c'losing a folder.

如果你喜欢用空格，可以这样：

	:noremap <space> za

###多个缓冲区(Buffers)

如果你希望在一个vim里面同时编辑多个文件怎么办？

我们知道，vim会把文件载入到缓冲区里面。vim同时可以建立多个缓冲区。所以你可以在vim里面同时打开多个文件，并且自由切换。

我们看下面2个文件，part1.txt和part2.txt:

#####part1.txt

	I have coined a phrase for myself - 'CUT to the G':
	1.Concentrate
	2.Understand
	3.Think
	4.Get Things Done

#####part2.txt

	step 4 is eventually what gets you moving, but Steps 2 and 3 		
	are equally mportant. As Abraham Lincoln once said "If I had 		
	eight hours to chop down a tree, I'd spend six hours sharpening my axe." 
	And to get to this stage,
	you need
	to do Step 1 which boils down to one thing - It's all in the mind.
	That's why
	it's so hard.
	
现在运行“:e part1.txt”和“:e part2.txt".现在你注意到第二个文件在打开编辑。如何切换到第一个文件呢？这种情况下，你可以输入"b 1"来切换到缓冲区（b'uffer)到‘1’号；或者运行“:e part1.txt”来切换。

你可以运行“：buffers”来查看所以正在编辑的文件，或者使用“：ls”来列出（list）所有的buffer's。

当你关闭vim，所有的缓冲区会自动关闭，你唯一要关心的是你是否保存了你的改动。但是，如果你希望手工关闭一个缓冲区，可以使用bd1来关闭（d'elte)‘1’号缓冲区（b‘uffer）。

查看“:help buffer-list”获取更多帮助。

###多个窗口

我们已经看到如何同时编辑多个文件，但是如果我们希望同时查看2个文件怎么办？譬如，你写了一本书，你可以能需要参考第一章节的内容来继续撰写第二章节的内容。或者只是希望在2个不同的文件之间拷贝。

在vim里面，我们使用“视图”来编辑不同的缓冲区。vim把这些视图称之为“窗口”。

下面我们继续使用前面章节的part1.txt和part2.txt.

首先，使用“:e part1.txt”打开第一个文件。下面我们通过把窗口分割成2个窗口来打开一个新的缓冲区，使用“：new”。现在你可以在新的缓冲区里面进行任何编辑操作，但是不能保存，这是因为你还没有为这个缓冲区关联一个文件，这里，你可以是‘:w test.txt’来保存缓冲区。

怎么在不同的窗口之间移动呢？使用Ctrl+w+(移动键)，移动键包括“hjkl”或者任何箭头。Ctrl+w里面的w代表操作对象是windows.

一个特别的快捷键是ctrl-w ctrl-w，它可以在所有的窗口之间来回切换。

如果你希望查看一个文件的不同部分，你可以使用":sp"命令来把窗口分割(split)开来。这里他们对应的同一个buffer，所以改动一个窗口，另外一个窗口的内容也随着改变。“ctrl-w s"同“:sp"命令的效果相同。

如果你希望竖直分割窗口，可以使用“vsp”或者“ctrl-w v”.关闭窗口，使用“:q”。

现在我们已经学会了如何打开和使用多个窗口，现在看一些进一步的玩法：

* 现在你正在查看一个水平分割的窗口，你希望交换一下上下2个窗口的位置。怎么办，使用"ctrl -w r"来旋转(r'otate)一个就可以了。

* 希望把当前窗口放到最上层，使用ctrl-w K.

* 希望调整一个窗口的大小。使用:resize 10来让窗口扩大10行。

* 希望当前窗口调整到足够大？使用ctrl-w _.想象一下_的作用就是把其它窗口变得足够小。

查看“:help windows”获得更多细节。

###多标签

如果你使用Firefox，你会对其多标签系统非常熟悉。vim也有类似的东东。

运行":tabnew"来打开一个新的标签页，新标签页会自动建立一个新的缓冲区。怎么切换呢？使用:tabnext或:tabprev来切换到下一个/上一个标签。使用:tabclose来关闭标签页。

还可以使用：tabmove 1来移动一个标签到第1的位置。


###总结

vim提供了多种方式来同时编辑不同的文件-多个缓冲区、多窗口、多变迁。如何使用这些特征，取决于你的习惯。最好按照实际情况，来选择使用哪一种方式，让编辑更舒服自然！





	




	



	
