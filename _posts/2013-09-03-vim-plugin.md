---
layout: post
title: "vim 插件"
description: ""
category: blog
tags: [vim,byte of vim]
---

###介绍

正如我们在前面章节所述，我们可以编写脚本来扩展vim的功能。我们把这些扩展或者功能叫做“插件”。

插件有下面几种：

1、vimrc

2、全局插件

3、文件类型插件

4、代码高亮插件

5、代码编译插件


你不但可以自己编写插件，当然可以下载别人的插件来使用。

###使用vimrc定制

当安装了一个新的Linx发行版，或者重装了Windows，我做的第一件事情都是把我的vimrc文件从备份里面恢复出来，然后再开始使用vim。为什么这样做很重要？因为vimrc文件里面的设定都会让我的vim使用感觉很习惯，更加得心应手。

有2个文件，你可以用来定制你的vim：

* %HOME%/_vimrc和%HOME%/_gvimrc(Windows平台）
* %HOME%/.vimrc和%HOME%/.gvimrc(Linux/BSD/Mac OS X平台） 

查看:help vimrc来查看你的系统vimrc文件的路径

vimrc和gvimrc文件可以包含任何vim命令。下面是我的vimrc文件的一部分：

	" My Vimrc file
	" Maintainer: www.swaroopch.com/contact/
	" Reference: Initially based on
	http://dev.gentoo.org/~ciaranm/docs/vim-guide/
	" License: www.opensource.org/licenses/bsd-license.php
	" Use Vim settings, rather then Vi settings (much better!).
	" This must be first, because it changes other options as a 	side
	effect.
	set nocompatible
	" Enable syntax highlighting.
	syntax on
	" Automatically indent when adding a curly bracket, etc.
	set smartindent
	" Tabs should be converted to a group of 4 spaces.
	" This is the official Python convention
	" (http://www.python.org/dev/peps/pep-0008/)
	" I didn't find a good reason to not use it everywhere.
	set shiftwidth=4
	set tabstop=4
	set expandtab
	set smarttab
	" Minimal number of screen lines to keep above and below the cursor.
	set scrolloff=999
	" Use UTF-8.
	set encoding=utf-8
	" Set color scheme that I like.
	if has("gui_running")
		colorscheme desert
	else
		colorscheme darkblue
	endif
	" Status line
	set laststatus=2
	set statusline=
	set statusline+=%-3.3n\  "buffer number
	set statusline+=%f\	"filename
	set statusline+=%h%m%r%w	"status flags
	set statusline+=\[%{strlen(&ft)?&ft:'none'}]	"file type
	set statusline+=%=	"right align remainder
	set statusline+=0x%-8B	"character value
	set statusline+=%-14(%l,%c%V%)	"line, character
	set statusline+=%<%P	"file position

	" Show line number, cursor position.
	set ruler

	" Display incomplete commands.
	set showcmd
	" To insert timestamp, press F3.
	nmap <F3> a<C-R>=strftime("%Y-%m-%d %a %I:%M %p")<CR><Esc>
	imap <F3> <C-R>=strftime("%Y-%m-%d %a %I:%M %p")<CR>
	" To save, press ctrl-s.
	nmap <c-s> :w<CR>
	imap <c-s> <Esc>:w<CR>a
	
	" Search as you type.
	set incsearch
	" Ignore case when searching.
	set ignorecase
	" Show autocomplete menus.
	Set wildmenu
	" Show editing mode
	set showmode
	" Error bells are displayed visually.
	set visualbell

注意，这些命令并没有以“：”开始。这是因为它假设这么命令都是在正常模式下面执行的。

我的gvimrc的一部分：

	 " Size of GVim window
	set lines=35 columns=99
	" Don't display the menu or toolbar. Just the screen.
	set guioptions-=m
	set guioptions-=T
	" Font. Very important.
	if has('win32') || has('win64')
		" set guifont=Monaco:h16
	"
	http://jeffmilner.com/index.php/2005/07/30/windows-vista-fonts-now-available/
	set guifont=Consolas:h12:cANSI
	elseif has('unix')
		let &guifont="Monospace 10"
	endif

通常情况下，vimrc文件的配置通常可以反映出你使用vim的时间。

###全局插件

全局插件用来提供全局性/通用性的功能。

全局插件可以存放在2个地方：

1、$VIMRUNTIME/plugin 来存储vim的官方插件。
2、安装你下载的插件，你可以使用自己的目录：
	* $HOME/.vim/plugin(Linux/BSD/Mac OS X)
	* %HOME%/vimfiles/plugin/ (Windows)
	* 查看 :help runtimepath来查看特定平台的插件目录信息

下面来看如何使用插件。

一个特别有用的插件是 Ansuman Mohanty编写的highlight_current_line.vim插件，顾名思义就是高亮显示当前行的一个插件。下载最新版本，然后放到上面的目录里面。

现在，重启vim，打开一个文件，你就看到效果了。

如果你不喜欢，删除那个文件，然后重启就可以了。

同样，我们可以把前面章节的related.vim和capitalize.vim文件放到插件目录里面，就不用每次都用source命令来载入了。你编写的任何插件都可以放到那个目录下面。

###文件类型插件

文件类型插件是针对某一种特定类型的文件。譬如C语言有自己的缩进格式、代码高亮甚至错误显示。

####使用文件类型插件

下面我们来尝试一个XML类型的插件。Xml是一个格式文档语言。譬如，你有下面一段文字：
	
	Iron Gods
	---------
		Ashok Banker's next book immediately following the Ramayana 	
		is said to be a novel tentatively titled "Iron Gods" scheduled to be published in
		2007. A contemporary novel, it is an epic hard science fiction story
		about a war between the gods of different faiths. Weary of the
		constant infighting between religious sects and their deities, God
		(aka Allah, Yahweh, brahman, or whatever one chooses to call the
		Supreme Deity) wishes to destroy creation altogether.

		A representation of prophets and holy warriors led by Ganesa, the
		elephant-headed Hindu deity, randomly picks a sample of mortals, five
		of whom are the main protagonists of the book--an American Catholic,
		an Indian Hindu, a Pakistani Muslim, a Japanese Buddhist, and a
		Japanese Shinto follower. The mortal sampling, called a 'Palimpsest'
		is ferried aboard a vast Dyson's Sphere artifact termed The Jewel,
		which is built around the sun itself, contains retransplanted cities
		and landscapes brought from multiple parallel Earths and is the size
		of 12,000 Earths. It is also a spaceship travelling to the end of
		creation, where the Palimpsest is to present itself before God to
		plead clemency for all creation.

		Meanwhile, it is upto the five protagonists, aided by Ganesa and a few
		concerned individuals, including Lucifer Morningstar, Ali Abu Tarab,
		King David and his son Solomon, and others, to bring about peace among
		the myriad warring faiths. The question is whether or not they can do
		so before the audience with God, and if they can do so peacefully--for
		pressure is mounting to wage one final War of Wars to end all war
		itself.

		(Excerpt taken from
		http://en.wikipedia.org/w/index.php?title=Ashok_Banker&oldid=86219280
		under the GNU Free Documentation License)

如果以XML格式来书写：

	<!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN" "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd">
	<article>

		<articleinfo>
			<author><firstname>Wikipedia Contributors</firstname></author>
			<title>Iron Gods</title>
		</articleinfo>
		<para>
			Ashok Banker's next book immediately following the Ramayana is
			said to be a novel tentatively titled "Iron Gods" scheduled to
			be published in 2007. A contemporary novel, it is an epic hard
			science fiction story about a war between the gods of
			different faiths. Weary of the constant infighting between
			religious sects and their deities, God (aka Allah, Yahweh,
			brahman, or whatever one chooses to call the Supreme Deity)
			wishes to destroy creation altogether.
		</para>
		<para>
			A representation of prophets and holy warriors led by Ganesa,
			the elephant-headed Hindu deity, randomly picks a sample of
			mortals, five of whom are the main protagonists of the
			book--an American Catholic, an Indian Hindu, a Pakistani
			Muslim, a Japanese Buddhist, and a Japanese Shinto follower.
			The mortal sampling, called a 'Palimpsest' is ferried aboard a
			vast Dyson's Sphere artifact termed The Jewel, which is built
			around the sun itself, contains retransplanted cities and
			andscapes brought from multiple parallel Earths and is the
			landscapes brought from multiple parallel Earths and is the
			size of 12,000 Earths. It is also a spaceship travelling to
			the end of creation, where the Palimpsest is to present itself
			before God to plead clemency for all creation.
		</para>
		<para>
			Meanwhile, it is upto the five protagonists, aided by Ganesa
			and a few concerned individuals, including Lucifer
			Morningstar, Ali Abu Tarab, King David and his son Solomon,
			and others, to bring about peace among the myriad warring
			faiths. The question is whether or not they can do so before
			the audience with God, and if they can do so peacefully--for
			pressure is mounting to wage one final War of Wars to end all
			war itself.
		</para>
		<sidebar>
			<para>
				(Excerpt taken from
				http://en.wikipedia.org/w/index.php?title=Ashok_Banker&amp;oldid=86219280
				under the GNU Free Documentation License)
			</para>
		</sidebar>
	</article>

可以看到XML格式的文档相当严谨。这意味可以轻松把xml文件转化为其它格式的文档，如PDF等可打印的格式。XML不好的一面是编写非常困难。

我们来看一下文件类型插件如何帮助编写XML文档的人。
1、首先把xmledit插件下载，然后放到 ~/.vim/ftpplugin/目录。
2、添加下面一行到vimrc里面：
	
	autocmd BufNewFile,BufRead *.xml source ~/.vim/ftplugin/xml.vim

特征注意根据操作系统来确定ftplugin目录的正确位置。	
3、打开vim，然后编辑一个名字为test.xml的文件。

4、输入"<"+"article"

5、现在输入">",看一下xmledit插件如何帮你自动填写article的闭合。差不多应该是这样：

	<article></article>
6、现在输入另外一个>，看xmledit如何帮助你输入更多的符号。文件应该看起来这样：
	
	<article>
	
	</article>

7、你应该看到光标也缩进到了正确的位置，你可以按照文档结构来输入更多的文字。

8、重复上面的步骤，直到输入完毕。

一个XML插件能够让你编写XML更容易，这正是文件类型插件的设计目标。

####编写一个文件类型插件

让我们尝试自己编写一个文件类型插件。

在前面的xmledit插件里面，你可能看到每一个xml文件都几乎有一个相同的开头。如果让vim自动插入这个标准开头呢？

先看一下我们的xml插件的标准开头的格式：

	<?xml version="1.0"?>
	<!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.5//EN"
          "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd">

所以，我们可以编写一个xmlheader.vim插件，让每新建一个xml文件，就会在开头插入上面的内容。首先，在~/.vmimrc文件里面插入一行：

	autocmd BufNewFile *.xml source ~/.vim/ftplugin/xmlheader.vim

现在我们要做的就是让xmlheader.vim插入上面2行：

	" Vim plugin to add XML header information to a new XML file
	call setline(1, '<?xml version="1.0"?>')
	call setline(2, '<!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML
		V4.5//EN" "http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd">')	

OK。现在重启Vim，然后输入:e test.xml(test.xml必须为新建文件)，就会看到这个文件的开头自动插入了我们的标准开头。


####语法高亮

前面我们已经看过一个XML文件，如果在编写xml的时候，不同的标签用不同的颜色表示，无疑我们就很容易看出语法错误。在vim里面，如果我们使用:set filetype=docbkxml，vim就会调用$VIMRUNTIME/syntax/docbkxml.vim.在这个文件里面定义了每一个xml标签所对应的的颜色。在vim里面有很多针对特定文件类型的语法定义文件。

#####使用语法高亮插件

实践一下。我们下载一个mkd.vim文件，这个一个markdown类型文件的语法定义插件。markdown是一种文本文件，它根据文件特征很容易转化成为HTML文件。

1、在vim里面打开一个名为“new_markdown.txt”的文件。

2、运行:set syntax=mkd

3、输入下面的内容：

	# Bengaluru
    
	The name **Bangalore** is an anglicised version of the city's name in
	    the Kannada language, Bengaluru.
	    
	    > A popular anecdote (although one contradicted by historical
		> evidence) recounts that the 11th-century Hoysala king Veera Ballala
		> II, while on a hunting expedition, lost his way in the forest.Tired
		> and hungry, he came across a poor old woman who served him boiled
	    > beans. The grateful king named the place _"benda kaal-ooru"_
	    > (literally, "town of boiled beans"), which was eventually
	    > colloquialised to "Bengaluru".
	    
	    ***
	    
	    (This information has been retrieved from
		[Wikipedia](http://en.wikipedia.org/wiki/Bangalore) under the GNU Free
	    Documentation License.)

4、你会看到所有Markdown里面的分段和关键词都高亮显示了。

#####编写一个语法高亮插件

现在我们尝试编写一个AniFormat格式的文件。

语法高亮插件一般涉及2个问题：找到需要高亮的词语和这些词语如何显示。

譬如，我们需要寻找以"b“作为开始和结束的语句，然后把b里面的内容进行黑体（bold）显示。怎么做呢？首先定义一个寻找模式（需要定义模式名称），然后根据模式来定义显示：

	:syntax match ourBold /<b>.*<\/b>/
	:highlight default ourBold term=bold cterm=bold gui=bold

第一行，我们定义了一个正则表达式，然后把匹配结果定义为一个名称"ourBold".
第二行定义如何高亮显示这个匹配。“default”表示可以在别的主题里面进行重新定义，ourBold是我们的名称，后面3个分别对应vim的三种运行环境：黑白终端、彩色终端和GUI窗口模式。

如何解决关键词的大小写问题呢？譬如我们可能习惯把“todo”写成“TODO”，可以这样：

	:syntax keyword ourTodo TODO FIXME XXX
	:hi def link ourTodo Todo

首先我们定义ourTodo有几个词语构成-TODO FIXME XXX等，然后把ourTodo链接到vim已经定义的Todo高亮模式。在vim里面有很多Todo这样已经预定义的关键词显示定义。

下面，我们定义一个以code开始和结束的语句的高亮显示：

	:syn region amiCode excludenl start=/\[code\]/ end=/\[\/code\]/
	:hi def link amiCode Identifier

首先，我们定义了一个以code开始（start）和（end）的一个区域，然后把这个区域链接到Identifier预定义。

下面，我们来定义其它部分：

	" Vim syntax file for AmiFormat
	" Language: AmiFormat
	" Version: 1
	" Last Change: 2006-12-28 Thu
	" Maintainer: www.swaroopch.com/contact/
	" License: www.opensource.org/licenses/bsd-license.php
	" Reference: http://orangoo.com/labs/AmiNation/AmiFormat/

	"""""""""" Initial Checks """"""""""""""""""""""""""""""""""""""""""""
	" To be compatible with Vim 5.8. See `:help 44.12`
	if version < 600
	    syntax clear
	elseif exists("b:current_syntax")
	    " Quit when a (custom) syntax file was already loaded
	    finish
	endif
	"""""""""" Patterns """"""""""""""""""""""""""""""""""""""""""""""""""
	" Emphasis
	syn match amiItalic /<i>.\{-}<\/i>/
	syn match amiBold /<b>.\{-}<\/b>/
	" Todo
	syn keyword amiTodo TODO FIXME XXX
	" Headings
	syn match amiHeading /^h[1-6]\.\s\+.\{-}$/
	" Lists
	syn match amiList /^\s*\*\s\+/
	syn match amiList /^\s*\d\+\.\s\+/
	" Classes
	syn match amiClass /^\s*%(\w\+).*%/
	syn match amiClass /^\s*%{.*}.*%/
	" Code
	syn region amiCode excludenl start=/\[code\]/ end=/\[\/code\]/
	" HTML
	syn region amiEscape excludenl start=/\[escape\]/ end=/\[\/escape\]/
	" Link
	syn match amiLink /".\{-}":(.\{-})/
	" Image
	syn match amiImage /!.\{-}(.\{-})!/
	"""""""""" Highlighting """"""""""""""""""""""""""""""""""""""""""""""
	hi def amiItalic term=italic cterm=italic gui=italic
	hi def amiBold term=bold cterm=bold gui=bold

	hi def link amiHeading Title
	hi def link amiTodo Todo
	hi def link amiList PreProc
	hi def link amiClass Statement
	hi def link amiCode Identifier
	hi def link amiEscape Comment
	hi def link amiLink String
	hi def link amiImage String
	"""""""""" Finish """"""""""""""""""""""""
	" Set syntax name
	let b:current_syntax = "amifmt"

学习更多的vim语法高亮，可以参考:

1 :help syntax

2 :help usr_44.txt

3 :help group-name

4 :help pattern-overview

5 :help mysyntaxfile

6 :help new-filetype
