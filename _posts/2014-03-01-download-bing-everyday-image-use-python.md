---
layout: post
title: "下载Bing每日壁纸"
description: "Download Bing EveryDay Image use python"
category: Blog 
tags: [Python,Bing]
---
{% include JB/setup %}

Bing的背景非常优美，估计地球人都知道了。

闲来无聊，做个Python自动下载。

其实，最近发现[IFTTT](http://ifttt.com)是个好东西，可以自动到Bing壁纸存放到Dropbox里面。美中不足的是触发速度太慢了，几乎没启动过，哎！

Python借鉴了github的一个项目，使用Python2.7，代码如下：

	import datetime
	from urllib import urlopen, urlretrieve
	from xml.dom import minidom
	import os
	
	
	#变量:
	idx = '0' #设置日期: 0 = 今天, 1 = 昨天, ... 20.
	#存放路径
	# saveDir = 'D:/ProgrammingStuff/GitHub/bing-wallpaper/images/' #in Windows you might put two \\ at the end
	# saveDir = 'D:/Dropbox/Dropbox/BingImage/'
	saveDir = 'D:/BaiduYun/BingImage/'
	
	operatingSystem = 'windows' #windows or linux (gnome)
	
	
	
	#设为壁纸
	def setWindowsWallpaper(picPath):
	    cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' %picPath
	    os.system(cmd)
	    os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
	    return
	
	
	def setGnomeWallpaper(picPath):
	    os.system('gsettings set org.gnome.desktop.background picture-uri file://' + picPath)
	    return
	
	
	#取得XML配置文件
	usock = urlopen(
	    'http://www.bing.com/HPImageArchive.aspx?format=xml&idx=' + idx + '&n=1&mkt=ru-RU') #ru-RU, because they always have 1920x1200 resolution pictures
	xmldoc = minidom.parse(usock)
	#解析XML文件
	for element in xmldoc.getElementsByTagName('url'):
	    url = 'http://www.bing.com' + element.firstChild.nodeValue
	
	    #根据日期设定文件名
	    now = datetime.datetime.now()
	    picPath = saveDir + now.strftime('bing_wp_%m-%d-%Y') + '.jpg'
	
	    #下载图片
	    #设置为高分辨率的
	    if not os.path.isfile(picPath):
	        urlretrieve(url.replace('_1366x768', '_1920x1200'), picPath)
				#urlretrieve(url, picPath)
	    else:
	        print "File exists."
	
	    #设为壁纸代码:
	    # if operatingSystem == 'windows':
	        # setWindowsWallpaper(picPath)
	    # elif operatingSystem == 'linux' or operatingSystem == 'gnome':
	        # setGnomeWallpaper(picPath)

