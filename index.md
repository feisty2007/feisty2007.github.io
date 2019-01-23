---
layout: page
title: 风轻云淡
tagline: 
---
{% include JB/setup %}

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

微博 : [提子的碎碎念](http://weibo.com/516132346)


微信平台: 

<img src="/assets/images/weixin.jpg" width="215" height="215" />
    
<br/>


## To-Do

<br/>
乐观的心态，愉快的生活，共勉！


