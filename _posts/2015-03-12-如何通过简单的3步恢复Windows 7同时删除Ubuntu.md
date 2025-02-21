---
layout: post
title:	"如何通过简单的3步恢复Windows 7同时删除Ubuntu"
date:	2015-03-29 10:02:00 +0800 
categories:	桌面应用 linuxcn 
tags:	[linuxcn,双引导,Windows,Ubuntu]
---


### 说明


写这篇文章对我来说是一件奇怪的事情，因为我通常都是提倡安装Ubuntu而卸载Windows的。


让今天写这篇文章更加奇怪的是，我决定在微软决定终止对Windows7的主流支持的这一天来写。


那么为什么我现在要写这篇文章呢？


到目前为止我曾经在很多场合被问到如何从一个装有Windows7或Windows8的双系统中删除Ubuntu系统，因此写这篇文章就变得有意义了。


我在圣诞节期间浏览了人们在我文章中的留言，感觉是时候把缺失的文章写完同时更新一下那些比较老的又需要关注的文章了。


我打算把一月份剩下的时间都用在这上面。这是第一步。如果你的电脑上安装了Windows7和Ubuntu双系统，同时你不想通过恢复出厂设置的方式恢复Windows7系统，那么请参考该教程。(注意：对于Windows8系统，有一个独立的教程)


### 删除Ubuntu系统需要的步骤


1. 通过修复Windows启动项来删除Grub
2. 删除Ubuntu系统所在分区
3. 扩展Windows系统分区


### 备份系统


在你开始之前，我建议为你的系统保留一个备份。


我建议你不要放弃备份的机会，但也不要使用微软自带的工具。


[点击查看如何使用Macrinum Reflect备份你的驱动](http://linux.about.com/od/LinuxNewbieDesktopGuide/ss/Create-A-Recovery-Drive-For-All-Versions-Of-Windows.htm)


如果Ubuntu中有你希望保存的数据，现在就登录进去然后将数据保存到外部硬盘驱动器，USB驱动器或者DVD中。


### 步骤1 - 删除Grub启动菜单


![](/Asserts/Images/album/201503/27/220313nuchiyp1pc1im1hu.jpg)


当你启动系统的时候你会看见一个与上图类似的菜单。


要想删除这个菜单直接进入Windows系统，你必须修复主引导记录。


要达到这个目的，我将向你展示如何创建一个系统恢复盘，如何从恢复盘中启动以及如何修复主引导记录。


![](/Asserts/Images/album/201503/27/220336nbnfensbyw9yynzh.png)


按下“开始”按钮，搜索“备份和还原”。点击出现的图标。


将会打开一个与上图一样的窗口。


点击“创建系统修复光盘”。


你需要一个[空的DVD盘](http://www.amazon.co.uk/gp/product/B0006L2HTK/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=B0006L2HTK&linkCode=as2&tag=evelinuse-21&linkId=3R363EA63XB4Z3IL)。


![](/Asserts/Images/album/201503/27/220453ciig9yafp9o1aima.png)


将空的DVD盘插入到驱动器中然后从下拉列表中选择你的DVD驱动器。


点击“创建光盘”。


将光盘留在电脑中并重启电脑，当出现从CD中启动的消息的时候按下键盘上的“回车”键。


![](/Asserts/Images/album/201503/27/220516cukd89qtab9dbja9.jpg)


屏幕上会出现“系统恢复选项”。


它会要求你选择你的键盘布局方式。


从列表中选择合适的选项，然后点击“下一步”。


![](/Asserts/Images/album/201503/27/220616bj7jiohovq20kljh.jpg)


下一个界面让你选择你想修复的操作系统。


或者你可以使用早先保存的系统镜像恢复系统。


选中上面的选项然后点击“下一步”。


![](/Asserts/Images/album/201503/27/220648bgtn2m82y8wbxyrz.jpg)


现在你将会看到一个有修复硬盘和恢复您的系统等选项的界面。


你需要做的是修复主引导记录，而这可以通过领命提示符来完成。


点击“命令提示符”。


![](/Asserts/Images/album/201503/27/220714eb76tgjx29rjgjbw.jpg)


现在只需要把下面的命令输入到命令提示符中：



```
bootrec.exe /fixmbr

```

接下来将会出现一条消息，提示操作已经成功完成。


你现在就可以关闭命令提示符窗口了。


点击“重启”按钮然后取出DVD。


你的电脑就会直接启动进入Windows7系统了。


### 步骤 2 - 删除Ubuntu分区


![](/Asserts/Images/album/201503/27/220737u9utkku459daew4w.png)


要删除Ubuntu你需要使用Windows系统提供的“磁盘管理”工具。


按下“开始”按钮然后在搜索框中输入“创建和格式化磁盘分区”。将会出现一个与上图类似的窗口。


现在上面我的屏幕将不再和你的一模一样了，不过也不会相差太多。你会看到第0块磁盘有101MB的未分配空间，另外还有4个分区。


这101MB的空间是之前我安装Windows7时犯的一个错误。驱动器C是Windows7系统，下一个分区(46.57GB)是Ubuntu的根分区。287G的分区是/HOME分区，8G的分区是交换空间。


对于Windows系统来说，我们真正需要的只有驱动器C，所以剩下的是可以删掉的。


**注意: 注意一下.你的磁盘上可能有恢复分区。 不要删除恢复分区。它们应该有专门的卷标，文件系统也许是NTFS或FAT32**


![](/Asserts/Images/album/201503/27/220807j337lt30ios735ot.png)


在你希望删除的分区上单击右键(例如：root,home和swap分区),然后从弹出的菜单中点击“删除卷”。


**(不要删除任何NTFS或者FAT32文件系统的分区！)**


对于剩下的两个分区重复执行上面的操作。


![](/Asserts/Images/album/201503/27/220834kulv03zsq6q0ml6e.png)


分区被删除后你将会有很大的一片空闲区域。右键点击空闲区域然后选择删除。


![](/Asserts/Images/album/201503/27/220845p70cz7v4q0f7sju9.png)


现在你的磁盘将包含驱动器C和一大片没有分配的空间。


### 步骤 3 - 扩展Windows分区


![](/Asserts/Images/album/201503/27/220908p5cpc695yppki9r8.png)


最后一步是扩展Windows以便于将它再变成一个大的分区。


右键点击Windows分区(C盘)，然后选择“扩展卷”。


![](/Asserts/Images/album/201503/27/220938mk4ddl0nui4u8ffx.png)


当出现左面的窗口的时候点击“下一步”。


![](/Asserts/Images/album/201503/27/220951utig8akoeaye6o1o.png)


接下来是一个向导界面，在这里你可以选择扩展到那个盘，同时修改扩展的大小。


默认情况下，向导界面将显示它能从未分配区域中获取的最大的磁盘空间数。


接受默认的选项，然后点击“下一步”。


![](/Asserts/Images/album/201503/27/221011sszcubppzxggjws6.png)


最后的界面展示了你在前一个界面中的选择结果。


点击“结束”进行磁盘扩展。


![](/Asserts/Images/album/201503/27/221119nzez7u47p764fx6z.png)


从上图中你可以看到，我的Windows分区占据了整个磁盘(除了我之前安装Windows的时候偶然创建的101MB的空间)。


### 总结


![](/Asserts/Images/album/201503/27/221154bj4iw4ppmop9qex1.png)


这就是全部内容。一个致力于Linux的网站刚刚向你展示了如何移除Linux然后用Windows7取而代之。


有任何疑问可以在下面评论区留言。




---


 


via: <http://www.everydaylinuxuser.com/2015/01/how-to-recover-windows-7-and-delete.html>


作者：Gary Newell 译者：[Medusar](https://github.com/Medusar) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
