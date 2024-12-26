---
layout: post
title:	"修复 Shell 脚本在 Ubuntu 中的默认打开方式"
date:	2015-11-22 17:58:16 +0800 
categories:	桌面应用 linuxcn 
tags:	[linuxcn,shell,脚本]
---


![](/Asserts/Images//attachment/album/201511/22/175818bng2njj12j1nm3g2.jpg)


当你双击一个脚本（.sh文件）的时候，你想要做的是什么？通常的想法是执行它。但是在Ubuntu下面却不是这样，或者我应该更确切地说是在Files（Nautilus）中。你可能会疯狂地大叫“运行文件，运行文件”，但是文件没有运行而是用Gedit打开了。


我知道你也许会说文件有可执行权限么？我会说是的。脚本有可执行权限但是当我双击它的时候，它还是用文本编辑器打开了。我不希望这样，如果你遇到了同样的问题，我想你也许也想要这样。


我知道你或许已经被建议在终端下面执行，我知道这个可行，但是这不是一个在GUI下不能运行的借口是么？


这篇教程中，我们会看到**如何在双击后运行shell脚本。**


#### 修复在Ubuntu中shell脚本用文本编辑器打开的方式


shell脚本用文件编辑器打开的原因是Files（Ubuntu中的文件管理器）中的默认行为设置。在更早的版本中，它或许会询问你是否运行文件或者用编辑器打开。默认的行为在新的版本中被修改了。


要修复这个，进入文件管理器，并在菜单中点击**选项**：


![](/Asserts/Images//attachment/album/201511/22/175819v5mj0tk4mmebwnuk.png)


接下来在<ruby> 文件选项 <rp>  （ </rp> <rt>  Files Preferences </rt> <rp>  ） </rp></ruby>中进入<ruby> 行为 <rp>  （ </rp> <rt>  Behavior </rt> <rp>  ） </rp></ruby>标签中，你会看到<ruby> 可执行的文本文件 <rp>  （ </rp> <rt>  Executable Text Files </rt> <rp>  ） </rp></ruby>选项。


默认情况下，它被设置成“<ruby> 在打开时显示文本文件 <rp>  （ </rp> <rt>  View executable text files when they are opend </rt> <rp>  ） </rp></ruby>”。我建议你把它改成“<ruby> 每次询问 <rp>  （ </rp> <rt>  Ask each time </rt> <rp>  ） </rp></ruby>”，这样你可以选择是执行还是编辑了，当然了你也可以选择“<ruby> 在打开时云可执行文本文件 <rp>  （ </rp> <rt>  Run executable text files when they are opend </rt> <rp>  ） </rp></ruby>”。你可以自行选择。


![](/Asserts/Images//attachment/album/201511/22/175819y0egonhccdg34bpn.png)


我希望这个贴士可以帮你修复这个小“问题”。欢迎提出问题和建议。




---


via: <http://itsfoss.com/shell-script-opens-text-editor/>


作者：[Abhishek](http://itsfoss.com/author/abhishek/) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
