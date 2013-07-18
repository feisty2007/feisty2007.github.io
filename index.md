---
layout: page
title: 风轻云淡
tagline: 
---
{% include JB/setup %}

听任庭前花开花落,坐看天上云卷云舒.

一个人懒到连自家院子的落叶都不扫！成天坐在那儿看天上的云彩！无所事事！
## 印象笔记

在 `脑部记忆` 更新一下我的数据:
    
     记录 : 生物 =)
     名字 : camark
     email: camark@sina.cn
     微博 : 提子的碎碎念 (http://weibo.com/516132346)
     博客 : Ubuntu高地 (http://hi.baidu.com/camark)

上面的数据，随时清除，无需保留！
    
## 闲言碎语

列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## To-Do

无论如何，生活还是要继续，爱你所爱，扯我之淡，如此而已！


