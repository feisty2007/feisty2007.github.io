---
layout: post
title: "vim 程序员的编辑器"
description: ""
category: blog
tags: [vim,byte of vim]
---
{% include JB/setup %}

###简介

Vim在程序员当中被广泛使用。因为易用易扩展，vim成为编写大量代码的好帮手。这丝毫不应该让人诧异。

###简单入门

vim最容易帮助你的特征是其代码高亮功能。它会让你编写代码更快，避免出错，更容易“看清”代码。

####代码高亮

如果你正在编写一个vim高亮文件，你可以运行:set filetype=vim，就会看到vim会给你的文件着色。如果你编辑Python程序，就允许:set filetype=python.

你可以在$VIMRUNTIME/syntax/目录下面看到vim支持的语言类型。

####智能缩进

有经验的程序员一般都会按照程序结构来进行缩进，以便更容易看清程序的结构和来龙去脉。vim会帮你做到这一点。

如果你希望下一行和本行缩进到一个水平，请使用:set autoindent。

如果你希望一段文字自动缩进，可以使用:set smartindent设定。注意：缩进行为根据编程语言的不同而不同。


####跳跃

如果你的程序有“{}”包围的一段文字，你可以按%来跳到当前{或者}对应的}和{。

####Shell命令

你可以在vim内部使用:!来运行Shell命令。

譬如，如果你的操作系统支持date命令，那么你运行:!date 就会看到当前日期。

这个功能非常实用，如果你想在文件夹里面查找某个文件，就可以使用:!ls 或者:!dir。

如果希望进入shell，就输入:sh。

我们可以利用这个功能来进行一些编辑操作。譬如你想排序当前编辑的文件，你可以使用:!sort来进行，并把结果输出到屏幕。

####跳转

有几种方法可以在代码之间跳跃：

* 把光标放到代码里面的文件上面，然后按下gf就会打开文件。

* 把光标放到局部变量上面，按gd就会返回到变量的声明处。gD可以查找全局变量。

* 使用]]。

查看:help 29.3, :help 29.4, 和:help 29.5会看到更多信息。

###浏览代码

####文件系统
使用:Vex 或者 :Sex在vim内部打开所需文件。

####ctags

我们已经看懂如何简单的在一个文件内部进行移动查看，如何在不同的文件之间来回移动呢？这里，我们可以使用标签（tags）。

这里使用taglist.vim插件。

1、安装Exuberant ctags。

2、安装taglist.vim.

3、运行:TlistToggle打开标签列表窗口。现在你就可以看到程序的东西-宏、类型定义、变量定义和函数。

4、你可以使用:tag foo来跳到foo的定义。

5、把光标放到任何一个符号上面，按下Ctrl-l就可以跳到它的定义。ctrl-t跳转回来。

6、使用ctrl w ]来一个分割窗口里面产科一个符号的定义。

7、使用:tnext,:tprev,:tfirst,:tlast在不同的tag直接移动。

现在exuberant Ctags支持33种编程语言，并且非常容易扩展来支持更多的语言。

####cscope

为了支持不同的文件之间查找，需要一个程序-cscope。但是人如其名，这个程序只支持C语言。

1、安装cscope。请查看:help cscope-info和:help cscope-win32。

2、拷贝cscope_maps.vim到~/.vim/plugin/ 目录。

3、到程序目录，运行 cscope -R -b来建立你的程序数据库。

4、重启Vim，并打开一个程序文件。

5、运行:cscope show 会看到，一个cscope连接已经建立。

6、运行:cscope find synbol foo来查找foo，也可以缩写成 :cs f s foo。

还可以：

* 查找定义 :cs f g

* 查找此函数调用的函数 :cs f d

* 查找调用此函数的函数 : cs f c

* 查找文本 :cs f t

* 以egrep方式查找 :cs f e

查看 :help cscope-suggestions来查看更多cscope使用建议。

另外,the Source Code Obedience插件非常值得使用，它提供了很多有用的cscope/ctags访问快捷键。

同时如果我们使用C语言，cvim插件将非常值得推荐。


###编译

在前面章节，我们已经看到 :make，这里不再重复。





