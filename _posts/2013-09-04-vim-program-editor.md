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

###易于编码

####自动完成

在vim7里面最希望添加的功能是“自动完成”-根据上下文提供选择输入。譬如，你使用了一个名字很长的变量，并且需要经常使用他，你可以使用快捷键告诉vim，vim会自动补充剩余的其它内容。

vim在这里使用文件类型插件来完成这个功能，一般在ftplugin/language-complete.vim里面，譬如pythoncomplete.vim。

一个简单的Python例子：

	def hello():
    	print 'hello world'
	def helpme():
    	print 'help yourself'	

 当开始输入代码时候，输入“he”，然后按下ctrl-x ctrl-o，vim会出现提示，帮助你完成输入。

 如果出现 E764:Option 'Omnifunc' is not set错误，可以运行 :runtime! autoload/pythoncomplete.vim来载入插件。

 为了避免每一个都需要输入，在~/.vimrc里面添加一行：

 	autocmd FileType python runtime! autoload/pythoncomplete.vim

vim默认使用第一个提示，可以使用ctrl-n或者ctrl-p来选择。

如果你不想使用，按下Esc。

在 :help new-omni-completion来查看语言支持（包括C、Html、Javascript、PHP、Python、Ruby、SQL、XML等）。

我一般使用Ctrl-space来代替Ctrl-x ctrl-o，可以在vimrc里面配置：

	imap <c-space> <c-x><c-o>

####使用代码片度

代码片度就是你经常使用的一小段程序代码。你也可以通过插件来插入。这里，我们使用SnippetEmu插件。

1、下载snippetsEmu插件。

2、如果~/.vim/after目录不存在，就建立这个目录。

3、通过vim命令行启动插件。譬如 gvim snippy_bundles.vba

4、运行 :source %。“vimball”就会解压文件到目录。

5、使用snippy_plugin.vba重复上面的步骤。

现在使用：

1、打开文件test.py

2、输入def,然后按Tab

3、你会看到snippetsEmu已经产生了Python函数的构架。大概如下：

	def <{fname}>(<{args}>):
    	"""
    	<{}>
    	<{args}>"""
    	<{pass}>
    	<{}>

4、把光标移动到函数的名称，fname

5、输入名称

6、按下Tab键会自动跳到函数的参数字段。

7、输入函数注释，譬如：Just say Hi

8、按下Tab键，输入： print 'Hello World

9、按下Tab

10、函数完成

结果如下：

	def test():
	    """
	    Just say Hi
	    """
	    print 'Hello World'


####自建代码片段

怎么建立我们自己的代码片段呢？

譬如ActionScript3里面，我经常需要输入下面类似的代码：

	private var _foo:Object;
	public function get foo():Object
	{
	    return _foo;
	}
	public function set foo(value:Object)
	{
	    _foo = value;
	}	

这是一个非常简单的getter/setter变量封装代码。问题是经常我们需要这样封装很多这样的变量，每次都需要这样类似的代码。让我们看如何使用代码片度自动完成。

SnippetEmu使用st来代表一个标签的开始，et来代表一个标签的结束。

譬如下面的例子：

	exec "Snippet pubfun public function
	".st.et.":".st.et."<CR>{<CR>".st.et."<CR>}<CR>"	

这是~/.vim/after/ftplugin/actionscript_snippets.vim里面的一行。

现在新建一个名字为test.as的文件，输入pubfun,按下Tab，就会产生：

	public function <{}>:<{}>
	{
    
	}	

按下Tab键就可以在函数名称和返回参数之间切换，进行输入。

回到前面的问题，下面是我们getter/setter的解决方法：

	exec "Snippet getset private var _".st."name".et.";<CR><CR>public
	function get ".st."name".et."():".st."type".et."<CR>{<CR><tab>return
	_".st."name".et.";<CR>}<CR><CR>public function set
	".st."name".et."(value:".st."type".et.")<CR>{<CR><tab>_".st."name".et."
	= value;<CR>}<CR>"
	 Note

1、把上面一行加入到~/.vim/after/ftplugin/actionscript_snippets.vim。

2、现在新建一个名字为test.as的文件

3、输入getset,按下Tab，就会产生：

	private var _<{name}>;
	public function get <{name}>():<{type}>
	{
	        return _<{name}>;
	}
	public function set <{name}>(value:<{type}>)
	{
	        _<{name}> = value;
	}

4、输入color，然后按下Tab。

5、输入Number，按下Tab，代码会变成：

	private var _color;
	public function get color():Number
	{
	        return _color;
	}
	public function set color(value:Number)
	{
	        _color = value;
	}	

看看我们降低了多少次键盘敲击！只需一行，就在vim里面产生了11行的代码。

根据实际需要，我们可以更多的实用代码片段。

###IDE

vim在插件的帮助下也可以完成IDE的一些功能。

####项目管理插件

Project插件可以帮助vim完成项目管理任务。

1、下载project插件

2、解压到~/.vim/目录

3、运行 :helptags ~/.vim/doc/

4、从http://www.vim/org/subversion.php下载vim源代码

5、运行 ：Project命令，就会出现一个侧边栏，类似于项目管理窗口。

6、运行2个\ 和 c。

7、输入下面配置

* Name 输入'vim7_src'
* Directory，选择vim7源代码目录
* CD同Directory
* Filter，输入*h,*c

8、你会看到侧边栏窗口里面出来了文件列表

9、使用j/k在文件列表里面浏览，输入enter来主窗口打开文件。  

这样就提高了非常类似于IDE界面的体验，同其它IDE需要繁琐的路径指定和配置文件，Project显得相当直接有效。

####直接运行vim文本

EvalSelection.vim提高了直接运行vim选择代码的能力，inc-python.vim也可以而且更简单。


####SCM集成

如果你希望从版本管理系统里面签出文件,你可以使用perforce插件，还有CVS/SVN/SVK/Git插件。

####补充

vim IDE更详细的解说，可以参阅：

* Vim Tip: Using vim as an IDE all in one

* C++/Python Vim+IDE plugins list

有很多特定类型的编程语言插件值得使用。譬如Python：

* SuperTab 允许你使用tab来自动完成。

* python-calltips会在底部显示一个完成列表。最酷的是还显示每一个可能输入的文档。

* VimPdb 运行你在vim内部调试Python


###编写你自己的插件

你可以根据自己的需要来编写vim插件。譬如，你又下面的需求：

	编写一个插件，可以根据当前单词来打开浏览器查看相关信息。

我的实现大体如下：

	" Add the following lines to your ~/.vimrc to enable online documentation
	" Inspiration: http://vim.wikia.com/wiki/Online_documentation_for_word_under_cursor
	function Browser()
	    if has("win32") || has("win64")
			let s:browser = "C:\\Program Files\\Mozilla Firefox\\firefox.exe -new-tab"
	    elseif has("win32unix") " Cygwin
			let s:browser = "'/cygdrive/c/Program\ Files/Mozilla\Firefox/firefox.exe' -new-tab"
	    elseif has("mac") || has("macunix") || has("unix")
	        let s:browser = "firefox -new-tab"
	    endif
	    return s:browser
	endfunction

	function Run(command)
	    if has("win32") || has("win64")
	        let s:startCommand = "!start"
	        let s:endCommand = ""
	    elseif has("mac") || has("macunix") " TODO Untested on Mac
	        let s:startCommand = "!open -a"
	        let s:endCommand = ""
	    elseif has("unix") || has("win32unix")
	        let s:startCommand = "!"
		  let s:endCommand = "&"
		    else
		        echo "Don't know how to handle this OS!"
		        finish
		    endif
		let s:cmd = "silent " . s:startCommand . " " . a:command . " " .
		s:endCommand
		    " echo s:cmd
		    execute s:cmd
	endfunction

	function OnlineDoc()
		    if &filetype == "viki"
		        " Dictionary
		let s:urlTemplate = "http://dictionary.reference.com/browse/<name>"
		    elseif &filetype == "perl"
		let s:urlTemplate = "http://perldoc.perl.org/functions/<name>.html"
		    elseif &filetype == "python"
		let s:urlTemplate =
		"http://www.google.com/search?q=<name>&domains=docs.python.org&sitesearch=docs.python.org
		    elseif &filetype == "ruby"
		let s:urlTemplate = "http://www.ruby-doc.org/core/classes/<name>.html"
		    elseif &filetype == "vim"
		let s:urlTemplate =
		"http://vimdoc.sourceforge.net/search.php?search=<name>&docs=help"
		    endif
		    let s:wordUnderCursor = expand("<cword>")
		let s:url = substitute(s:urlTemplate, '<name>', s:wordUnderCursor, 'g')
		    call Run(Browser() . " " . s:url)
	endfunction
	
	noremap <silent> <M-d> :call OnlineDoc()<CR>
	inoremap <silent> <M-d> <Esc>:call OnlineDoc()<CR>a

###访问数据库

使用dbext.vim插件，你可以访问超过10种数据库系统，包括Oracle、MySQL、PostgreSQL、Sybase和SQLite等。最好的地方是这个插件可以帮助你在PHP、Perl、Java里面编辑SQL语句，甚至可以直接执行代码里面的SQL语句。


###总结

上面我们看到了，如何通过插件和设定来帮助编程。如果需要，我们就可以自己编写一个插件来实现这个特征。

强力推荐Stack Overflow和Peteris Krumins的博客，那里有更多相关内容。






	









