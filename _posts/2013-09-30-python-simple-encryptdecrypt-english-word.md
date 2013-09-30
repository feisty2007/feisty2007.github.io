---
layout: post
title: "python简单加/解密字符串"
description: ""
category: blog
tags: [ python,加解密]
---
{% include JB/setup %}

###原理

这是一个非常简单的python加解密模块，原来如下：

1、产生一个a-z的列表

2、定义一个偏移量

3、查找需要加密字符串的每一个字符在列表中的位置，然后加上偏移量，得到一个数值。如果这个数值小于列表的长度，就输出列表数值的字符，如果大于，就减去数值，继续输出


###代码

	# -*- coding: cp936 -*-

	# Python简单英语加密

	# 产生[a..z]的字符列表字典
	def gen_dict():
	    i= ord('a')
	    ilen=26
	    dict1 = []
	    for j in range(0,ilen):
	        dict1.append(chr(i+j))
	    return dict1





	#特殊字符处理
	def spec_char(c):
	    s_char=[',',' ','!','.','?']

	    if c in s_char:
	        return True
	    else:
	        return False

	#加密函数
	def encrypt_word(word):
	    dict2=[]
	    dict1=gen_dict()
	    ilen=26
	    for c in word:
	        #if dict1.contain
	        if spec_char(c):
	            dict2.append(c)
	            continue
	        i_sum=13 #定义偏移量，如h为7，则加密为20，为u
	        pos=dict1.index(c)
	        i_sum=i_sum+pos

	        #超过字典上线，就从头开始，既-26
	        if i_sum>=ilen:
	            i_sum = i_sum -ilen

	        dict2.append(dict1[i_sum])

	    entry_pass="".join(dict2)
	    return entry_pass

	# 解密函数
	def decrypt_word(word):
	    dict3 = []
	    dict1=gen_dict()
	    ilen=26
	    for c in word:
	        if spec_char(c):
	            dict3.append(c)
	            continue
	        isum=13

	        pos=dict1.index(c)
	        isum=pos-isum

	        if isum<0:
	            isum = isum + ilen

	        dict3.append(dict1[isum])

	    decode_pass="".join(dict3)
	    return decode_pass

	# main
	if __name__ == '__main__':
	    word1='hello,how are you?' #需要加密的字符串
	    e1=encrypt_word(word1)
	    print e1 #e1='uryyb,ubj ner lbh?'
	    e2=decrypt_word(e1)
	    print e2

###后记

来自《Hacking Secret Clipers with Python》第一章的例子。