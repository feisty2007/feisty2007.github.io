---
layout: post
title: "隐式声明与内建函数printf不兼容"
description: "why and how to do"
category: blog 
tags: [linux,c]
---

在linux 编译C文件的时候如果出现这个警告：'隐式声明与内建函数 ‘printf’ 不兼容',则只需要加入这两个头文件到C文件中就可以了！

      #include <stdio.h>
	#include <stdlib.h>


这时这个警告将不会出现!
