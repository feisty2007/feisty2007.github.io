---
layout: post
title: "vim 插件"
description: ""
category: blog
tags: [vim,byte of vim]
---
{% include JB/setup %}

###介绍

正如我们在前面章节所述，我们可以编写脚本来扩展vim的功能。我们把这些扩展或者功能叫做“插件”。

插件有下面几种：

+ vimrc
+ 全局插件
+ 文件类型插件
+ 代码高亮插件
+ 代码编译插件

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
	
