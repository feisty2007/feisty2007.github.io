---
layout: post
title: "三分钟建立Github博客"
description: "利用现成模版，如何快速建立Blog"
category: blog
tags: [Github,blog]
---
{% include JB/setup %}

###1、建立一个新的Gibhub代码库

到[Github](https://github.com)建一个新的代码库，名字必须为username.github.io，其中username为你的gibhub用户名。

###2、安装Install Jekyll-Bootstrap

进入shell，输入下面代码：

	$ git clone https://github.com/plusjade/jekyll-bootstrap.git USERNAME.github.io
	$ cd USERNAME.github.io
	$ git remote set-url origin git@github.com:USERNAME/USERNAME.github.io.git
	$ git push origin master

###3、完成

等待几分钟，这段时间里面github会自动编译你的上传，然后在浏览器里面输入username.github.com，你的Github博客就魔法般的出现了。

###更多阅读

原文英文地址：[这里](http://jekyllbootstrap.com/)
