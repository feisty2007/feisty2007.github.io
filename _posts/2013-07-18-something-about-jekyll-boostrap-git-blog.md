---
layout: post
title: "Jekyll boostrap Github blog二三事"
description: "几个方法，让你的Github Blog更专业 "
category: blog 
tags: [Github,blog]
---
{% include JB/setup %}

###前提

本文都是基于利用[Jekyll boostrap](http://jekyllbootstrap.com/)建立的Github 博客，建立，你可以参考[这篇文章](http://feisty2007.github.io/blog/2013/07/18/zero-to-hosted-jekyll-blog-in-3-minutes/)。


###如何改变theme

[Jekyll bootstrap](http://jekyllbootstrap.com/)提供了几个theme,你可以在它的[theme](http://themes.jekyllbootstrap.com/)里面浏览，进行选择，同时可以点击  `install theme` 来获得改变本地theme的rake代码，执行一下就可以了。

###添加Disqus评论系统

Jekyll bootstrap建立的站点，自动利用[Disqus](https://disqus.com/)建立评论系统，你可以在`_config.yaml`里面配置disqus的账号，如下：

	 comments :
     provider : disqus
     disqus :
     	short_name : 你的disqus账号

不然，使用缺省账号，系统会出现一些推荐信息，如同小广告一样，非常讨厌！


###添加“分享到新浪等国内网站”的按钮

我们这里利用“[分享道](http://shareto.com.cn/share.html)”来实现这个功能。

具体是在_includes/themes/twitter/post.html文件里面的

	content

下面添加下面内容，twitter对应于你现在的theme名称：

	<!-- ShareTo Button BEGIN -->
    <a class="shareto_button" href="http://shareto.com.cn/share.html"><img src="http://s.shareto.com.cn/btn/lg-share-cn.gif" width="125" height="21" alt="分享道" style="border:0"/></a>
    <script type="text/javascript" src="http://s.shareto.com.cn/js/shareto_button.js" charset="utf-8"></script>
    <!-- ShareTo Button END -->

然后在每一个Blog下面就会显示"分享"链接了，在这篇文章后面你应该可以看到实际效果！

###狗尾续貂

按照上面方法，你的Blog会更干净，更专业！