---
bg: "owl.jpg"
layout: page
title: "About"
crawlertitle: "Why and how this blog was created"
permalink: /about/
summary: "About this blog"
active: about
---

听任庭前花开花落,坐看天上云卷云舒.

<br/>

## 闲言碎语

<br/>

<ul class="posts">
  {% for post in site.categories.blog limit:10 %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
    <li><a href="{{BASE_PATH}}/archive.html">全部存档</a></li>
</ul>




## 印象笔记

<br/>

Email: [camark@sina.cn](mailto:camark@sina.cn)
a
    
<br/>


## To-Do

<br/>
乐观的心态，愉快的生活，共勉！
<br />

This is the base Jekyll theme. You can find out more info about customizing your Jekyll theme, as well as basic Jekyll usage documentation at [jekyllrb.com](http://jekyllrb.com/)

You can find the source code for the Jekyll new theme at:
{{site.twitter_username}} /
[jekyll-new](https://github.com/jglovier/jekyll-new)

You can find the source code for Jekyll at
{{site.github_username}} /
[jekyll](https://github.com/jekyll/jekyll)
