---
layout: post
title:	"如何在Ubuntu上修复“Not Enough Free Disk Space On /boot”"
date:	2015-04-08 10:32:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,ubuntu tweak]
---


### 提问:如何在Ubuntu上修复“Not Enough Free Disk Space On /boot”错误？


今天，当我在升级Lubuntu 14.04的时候遇到了下面这个错误，但是很简单。



> 
> “Not Enough Free Disk Space On /boot”
> 
> 
> 


![](/Asserts/Images/album/201504/07/223403nw4q215kx8l2mqx7.png)


这是因为我的 /boot 分区被不再需要的旧内核与包塞满了。


### 回答:


我听说Ubuntu Tweak中的**Computer Janitor**功能可以删除不想要的垃圾文件。使用Computer Janitor，你可以将你的系统清理成像新安装的那样。Janitor会删除:


* 程序缓存（Firefox/Chrome 缓存、软件中心缓存）;
* 略缩图缓存;
* apt缓存;
* 旧内核;
* 包的配置;
* 不再需要的包。


如果你还没有安装这个工具，参考下面的链接


* **[如何安装和使用Ubuntu Tweak](http://linux.cn/article-3335-1.html)**


要删除不需要的垃圾文件，打开Ubuntu Tweak，点击 **Janitor** 选项。


![](/Asserts/Images/album/201504/07/223406r5cvkiazrirgp9gj.png)


选择你想要删除的文件的选框，并点击 **Clean** 按钮。


![](/Asserts/Images/album/201504/07/223409mglg01h0gh8dlgq4.png)


Janitor现在就开始清理你的系统了。


![](/Asserts/Images/album/201504/07/223412i2e2u07gpn3n22vf.png)


真酷！系统清理完成了。


![](/Asserts/Images/album/201504/07/223413dett0l608kl0gztc.png)


我重启启动了软件更新。这个没再遇到问题了。


![](/Asserts/Images/album/201504/07/223414oot7mbb7bsyv9vr7.png)


就是这样。当然也有其他的方法可以清理系统。但是，这个方法很容易学。我们可以只点击几次鼠标就可以清理系统。


干杯！




---


via: <http://www.unixmen.com/how-to-fix-not-enough-free-disk-space-on-boot-in-ubuntu/>


作者：[SK](https://www.unixmen.com/author/sk/) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
