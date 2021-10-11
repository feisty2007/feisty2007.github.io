#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from datetime import datetime
import os


now=datetime.now()

title = input("title:")
crawlertitle = input("crawlertitle:")
if crawlertitle=='':
	crawlertitle = title
summary = input("summary:")

categories = input("category(Blog):")
if categories=='':
	crawertitle = 'Blog'

tags = input("tags:")
if tags == '':
	tags = '心情'
author = "feisty2007"


today = now.strftime("%Y-%m-%d")
file_title = "-".join(title.split(" "))
target_file_name = today + "-" + file_title + ".md"

with open(target_file_name,'w') as f:
	f.write("---"+os.linesep);
	f.write("title: \""+title+"\""+os.linesep);
	f.write("crawlertitle: \""+crawlertitle+"\""+os.linesep);
	f.write("summary: \""+summary+"\""+os.linesep);
	f.write("date: "+str(now)+os.linesep);
	f.write("categories: \""+categories+"\""+os.linesep);
	f.write("tags: \""+tags+"\""+os.linesep);
	f.write("author: \""+author+"\""+os.linesep);
	f.write("---"+os.linesep);

print("write "+target_file_name+" ok!")

