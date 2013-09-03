vim 脚本

###介绍

如果你定制任何软件以符合你的需要，通常情况下可以改变软件的设置来做到。
但是如果你想做的更高级的事情呢？
譬如在一个图像界面程序（GUI）里面，如何查看当前程序的主题？。
这个就是“脚本的范畴。脚本就是一种语言，让我们来决定当出现什么情况我们就采取动作集合。
vim里面有两种脚本语言-vim内置的脚本和一些具有黏合效应的语言（譬如Python、Perl等，当然运行这些语言需要安装vim的模块）。


本章节需要你熟悉一种脚本语言，否则你会觉得不知所云。
如果你想学习一种新的脚本语言，推荐‘byte ofPython’一书。

在vim里面有2种情况可以帮你定义功能（function)，功能是指你完成一遍以后，系统会按照某个步骤自动执行。
他们是宏和脚本。

###宏

使用宏，我们可以记录一个命令的序列，然后不同上下文中进行重放。

例如，假设有一些像这样的文本：

    tansen is the singer
    daswant is the painter
    todarmal is the financial wizard
    abul fazl is the historian
    birbal is the wazir


在这里需要如下更正：

1.更改句子的第一个字母为大写。

2.更改 'is' 为 'was'。

3.更改 'the' 为 'a'。

4.在每一行的末尾加上"in Akbar's court."。

在这里可以使用vim的正则表达式功能来进行更正，譬如可以使用":s/^\\w/\\u\\0/"把每一句的第一个字母变为大写。
但是我们需要撰写4个正则表达式才能完成，并且有时候正则表达式还会改动不需要改动的词语。

更好的方法是使用宏。

1、把光标移动到第一行的第一个字母。第一行的内容应该是：tansen is the singer。

2、按下qa，vim开始进行宏录制

3、使用gUL命令把第一个字母变为大写。

4、按下w，跳到下个单词

5、按下cw

6、把is改为was

7、按下Esc，进入正常模式

8、按下w，跳到下个单词

9、按下cw

10、把the改为a

11、按下Esc，进入正常模式

12、按下A，在行尾添加文字

13、输入”in Akbar's court.“

14、按下Esc，进入正常模式

15、按下q，停止宏录制

上面好像是一个很长的步骤，但是比起绞尽脑汁构思复杂的替换表达式，还是要简单一点！

第一行的内容应该变成了：

    Tansen was a singer in Akbar's court.
    
OK。现在我们把光标定位到第二行的第一个字母，然后按下@a，第二行的内容就会变成：

    Daswant was a painter in Akbar's court.
    
宏的奥义就是可以记录我们操作，然后重现出来，用在不同的地方，只确认操作类似即可！


###脚本基础

Vim 有内置的脚本语言，使用它您可以编写您自己的脚本，以决定"做"的东西，和操作的文本。

####动作

怎么改变Vim的主题（或者颜色）呢？只需输入：

    :colorscheme desert
    
在这里，我选用了我最喜欢的‘desert’主题。你通过输入‘colorscheme’然后按下tab键，vim会自动提示下一个可用的主题。

如何得到当前行的字符数？输入：

    ：echo strlen(getline("."))
    
特别注意`strlen`和`getline`，他们是“函数”。函数就是一个有名字的代码片段，我们可以通过名字来反复调用它的功能。
getline是获取某一行的文字，“。”代表当前行，strlen是获取文本(string)的长度(length)。echo就是把结果显示出来。
我们通过一级一级的调用，最终把结果当前行的文字长度来显示了出来。

Strlen(getline(".")) 被称为表达式。我们可以将结果存储到名为`变量`的表达式里面。
`变量`如同骑名称所暗示的 — — 它们是一个名称，代表某个值，并且值可以是发生变化的。

例如，我们可以这样存储长度：

    :let len = strlen(getline("."))
    :echo "We have" len "characters in this line."
    
如果你运行上面的命令，可能会得到下面的结果：

     We have 46 characters in this line.

特别注意，我们可以把变量在其他表达式里面使用。

vim里面有很多变量，譬如$开头的环境变量，&开头的配置变量，@开头的寄存器变量。

    :echo $HOME
    :echo &filetype
    :echo @a
    
输入":help funtion-list"可以看到很多的函数。

你也可以创建自己的函数：

    :function CurrentLineLength()
    :    let len = strlen(getline("."))
    :    return len
    :endfunction
    
现在输入下列命令：

    :echo CurrentLineLength()
    
然后就会看到当前行的字符统计。

同内置函数不同，自定义函数的名称应该以大写字母开头，而内置函数一般以小写字母开头。
如果你只是简单想调用某个函数，可以使用call命令。


####条件

如果你希望根据vi的运行环境来决定vi的主题，譬如在GUI下面是什么主题，而在终端模式是什么主题，怎么办？

    :if has("gui_running")
    :    colorscheme desert
    :else
    :    colorscheme darkblue
    :endif
    
运行原理如下：

* has()函数来检查某个特征当前计算机是否支持
* if来进行条件判断，如果为真就执行某个动作，如果为假，就执行“else”里面设定的动作。
* 注意，if的末尾需要一个endif来配对。
* 还有一个elseif语句，可以进行更多情况的判断。

vim也支持循环语句-“for”和“while”。

    :let i = 0
    :while i < 5
    :    echo i
    :    let i += 1
    :endwhile
    
结果如下：
    
    0
    1
    2
    3
    4
    
使用vim内置函数，也可以这样：
    :for i in range(5)
    :    echo i
    :endfor
    
* range()是一个内置函数，他可以产生一定范围的数组。
* break和continue也是被支持的。


####数据结构

vim支持数组和字典。你可以利用他们来建立复杂的程序。

    :let fruits = ['apple', 'mango', 'coconut']
    :echo fruits[0]
    " apple
    :echo len(fruits)
    " 3
    :call remove(fruits, 0)
    :echo fruits
    " ['mango', 'coconut']
    :call sort(fruits)
    :echo fruits
    " ['coconut', 'mango']
    :for fruit in fruits
    :   echo "I like" fruit
    :endfor
    " I like coconut
    " I like mango
    
在":help functon"里面你可以查看那些数组和字典操作函数。

###编写一个vim脚本

我们现在编写一个脚本，这个脚本被在vim启动时被载入，并且可以随时调用。
这跟我们前面编写脚本的方法有些不同。

现在我们试图解决一个简单的问题-如何让指定行的第一个字符都大写呢？
我们可以写一个函数来完成这个操作，它的名字就叫“capitalize”。

我们首先从一个脚本模版开始，我们输入下面的内容，并把它存为capitalize.vim：

    " Vim global plugin for capitalizing first letter of each word
    "       in the current line.
    " Last Change: 2008-11-21 Fri 08:23 AM IST
    " Maintainer: www.swaroopch.com/contact/
    " License: www.opensource.org/licenses/bsd-license.php
    
    if exists("loaded_capitalize")
        finish
    endif
    let loaded_capitalize = 1
    
    " TODO : The real functionality goes in here.
    
解释一下:

* 第一行解释脚本的用途
* 
* 第2-3行，“Last Change”可以让使用者来了解脚本的最后修改日期，“Maintainer”是维护者的信息，以便于如果出现问题或疑问，可以联系到作者！
* 
* “License”是可选的，但是还是强烈建议。如果你的脚本可能对于其他人很有用并且有相应的版权声明，别人可以根据你的版权情况来改进，或许有一天你自己也能受益！
* 
* 脚本是可以重复载入的。譬如你一个vim里面打开了二个html文件，html对应的代码高亮脚本会载入2次。为了避免代码运行2次，变量定义2次的情况出现，我们可以定义一个变量（这里是“loaded_capitalize”）来防止这种情况的发生。

现在开始撰写真正的功能。

我们来定义一个函数-capitalize来完成这个转换。它的功能是把字符串的首个字符大写，同时因为这是一个多行操作，我们把它定义为范围（range）函数。

    " Vim global plugin for capitalizing first letter of each word
    "       in the current line
    " Last Change: 2008-11-21 Fri 08:23 AM IST
    " Maintainer: www.swaroopch.com/contact/
    " License: www.opensource.org/licenses/bsd-license.php
    " Make sure we run only once
    if exists("loaded_capitalize")
        finish
    endif
    let loaded_capitalize = 1
    " Capitalize the first letter of each word
    function Capitalize() range
        for line_number in range(a:firstline, a:lastline)
            let line_content = getline(line_number)
            " Luckily, the Vim manual had the solution already!
            " Refer ":help s%" and see 'Examples' section
            let line_content = substitute(line_content, "\\w\\+", "\\u\\0", "g")
            call setline(line_number, line_content)
        endfor
    endfunction
    
    
工作原理

* firstline和latline代表选择的第一行和最后一行。
* 我们使用for来遍历所有的选择行
* 使用substitute()函数来进行一个查找替换操作。\\w\\+代表匹配的第一个单词，\\u代表要把单词进行字母首先操作，\\0代表\\w\\+匹配的单词
* setlne()把每一个修改完成的行修改到vim里面。

如何运行？

1、打开vim，输入下面的文字“this is a test.”。
2、输入“:source:capitalize.vim “,让vim载入这个脚本
3、输入”call Capitalize()“
4、文字就会变成”This Is A Test“。

每次都要输入”call Capitalize()“，显然有些麻烦，我们可以把它绑定到vim快捷键上面。

    " Vim global plugin for capitalizing first letter of each word
    " in the current line
    " Last Change: 2008-11-21 Fri 08:23 AM IST
    " Maintainer: www.swaroopch.com/contact/
    " License: www.opensource.org/licenses/bsd-license.php
    
    " Make sure we run only once
    if exists("loaded_capitalize")
        finish
    endif
    let loaded_capitalize = 1
    
    " Refer ':help using-<Plug>'
    if !hasmapto('<Plug>Capitalize')
        map <unique> <Leader>c <Plug>Capitalize
    endif
    noremap <unique> <script> <Plug>Capitalize <SID>Capitalize
    noremap <SID>Capitalize :call <SID>Capitalize()<CR>
    
    " Capitalize the first letter of each word
    function s:Capitalize() range
        for line_number in range(a:firstline, a:lastline)
            let line_content = getline(line_number)
            " Luckily, the Vim manual had the solution already!
            " Refer ":help s%" and see 'Examples' section
            let line_content = substitute(line_content, "\\w\\+", "\\u\\0", "g")
            call setline(line_number, line_content)
        endfor
    endfunction
    
    
* 首先我们把函数名从 'Capitalize' 改变为 's:Capitalize' 。这表示这是一个脚本范围内的函数，不能被其它脚本调用。
* 使用map来定义了一个快捷键
* Leader通常是\
* Plug代表我们里面有一个Capitalize函数
* 每一个脚本都有一个SID，我们可以用SID+Capitalize来调用Capitalize函数

现在就可以使用“\\c“快捷键来调用我们的脚本功能了。

如果你的脚本出现运行错误，你可以使用v:errmsg来查看最后的出错信息

###使用外部语言

许多人并不喜欢学习vim script，而是更倾向于使用他们已经学会的语言，来为vim编写插件。
vim支持Pytho、Perl、Ruby等许多语言。

在这一节，我们用Python来编写一个简单的插件，其它语言也能达到同样的功效。

正如前面所说，如果你对Python，向你推荐我的另外一个书：byte of Python。

首先，我们测试了一下vim是否支持Python：

    :echo has("python")
    
如果返回1，我们就可以继续了。如果没有，就需要安装一下。

假设您要编写一篇博客,通常情况下人们总是希望自己的博客能吸引更多的人阅读，而
搜索引擎通常可以做到这一点。
所以，如果你加入了一个关键词 （譬如“ C V 拉曼 ”，著名的印度物理学家，诺贝尔奖得主），就可以通过关键词来让更多的人从搜索引擎找到你的博客。例如，如果人们开始寻找 ' c v 拉曼 '，他们可能还搜索
拉曼效应，他们就可能找到你的博客文章。

怎么找到关键词呢？很简单，用Yahoo!搜索。

首先，我们来看Python怎么找到当前行，然后再当前行加入关键词！

    " Vim plugin for looking up popular search queries related
    "       to the current line
    " Last Updated: 2008-11-21 Fri 08:36 AM IST
    " Maintainer: www.swaroopch.com/contact/
    " License: www.opensource.org/licenses/bsd-license.php
    " Make sure we run only once
    if exists("loaded_related")
        finish
    endif    
    let loaded_related = 1
    
    " Look up Yahoo Search and show results to the user
    function Related()
        python <<EOF
            import vim
            print 'Length of the current line is', len(vim.current.line
        EOF
    endfunction

主要的架构和vimscipt的架构差不多。

主要的区别在于<<EOF和EOF中间的Python代码，Python解释器会运行这些代码，并把执行结果传送回vim。其它语言也是类似的。

现在你可以打开vim，运行一下，跟vimscipt的结果是一样的。


现在，我们完成工作的核心部分。Yahoo提高了一个Web服务，可以使用Python来调用。

    " Vim plugin for looking up popular search queries related
    " to the current line
    " Last Updated: 2008-11-21 Fri 08:36 AM IST
    " Maintainer: www.swaroopch.com/contact/
    " License: www.opensource.org/licenses/bsd-license.php
    " Make sure we run only once
    if exists("loaded_related")
        finish
    endif
    let loaded_related = 1
    " Look up Yahoo Search and show results to the user
    function Related()
    python <<EOF
    import vim
    from yahoo.search.web import RelatedSuggestion
    search = RelatedSuggestion(app_id='vimsearch', query=vim.current.line)
    results = search.parse_results()
    msg = 'Related popular searches are:\n'
    i = 1
    for result in results:
        msg += '%d. %s\n' % (i, result)
        i += 1
    print msg
    EOF
    endfunction

特别注意，这个脚本以vim的当前行文本作为目标，我们可以输入任何内容。

1、运行:source related.vim

2、输入c v raman

3、运行:call Related()

4、输出应该类似于下面：

     Related popular searches are:
     1. raman effect
     2. c v raman india
     3. raman research institute
     4. chandrasekhara venkata raman
     

###总结

我们已经如何使用vim内置脚本语言和其它脚本语言，他们为vim提供了无限的可扩展性！

请多细节，请查看:help eval, :help python-commands, :help perl-using 和 :help ruby-commands。









    
    

    












