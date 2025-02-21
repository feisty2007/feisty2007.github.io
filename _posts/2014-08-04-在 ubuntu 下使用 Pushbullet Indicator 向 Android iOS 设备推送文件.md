---
layout: post
title:	"在 ubuntu 下使用 Pushbullet Indicator 向 Android/iOS 设备推送文件"
date:	2014-08-05 15:04:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,ubuntu,Pushbullet]
---


[![](https://camo.githubusercontent.com/deb2c456f1d8536ab7b8875371df51acc3807ba6/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c6c65745f4c6f676f672e6a7067)](https://camo.githubusercontent.com/deb2c456f1d8536ab7b8875371df51acc3807ba6/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c6c65745f4c6f676f672e6a7067)


[Pushbullet](https://www.pushbullet.com/)是一款iOS和Android设备与桌面系统互相传输文件、链接、图片的APP应用,Pushbullet可以在任何装有Firefox或Chrome 浏览器的操作系统上安装使用。


如果你不是浏览器扩展插件的粉丝，却依然想使用桌面应用**Pushbullet in Ubuntu 14.04**的话，你可以使用由 [Atareao](http://www.atareao.es/)开发 的**Pushbullet Indicator**。 Pushbullet Indicator 小应用正在开发阶段，并不具备官方windows桌面版应用的所有功能， 但是已经足够大家入门使用了。


### 在Ubuntu 14.04 和 Linux Mint 17 下安装Pushbullet Indicator小应用


打开一个终端，并且使用以下命令



```
sudo add-apt-repository ppa:atareao/atareao
sudo apt-get update
sudo apt-get install pushbullet-indicator

```

以上个人软件包不支持运行在Ubuntu 13.10.版本


### 在Ubuntu 14.04 和 Linux Mint 17 下使用Pushbullet Indicator小应用


* 创建一个[Pushbullet](https://www.pushbullet.com/)账号
* 在Android/iOS设备上安装Pushbullet
* 在Ubuntu 或者Linux Mint系统安装Pushbullet Indicator小应用以后，运行。第一次启动时，会提供一些Pushbullet账号连接的选项。如图：


[![](https://camo.githubusercontent.com/1e6de8add4c7a0954664b9242e0510b1f4aec44d/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c6c65745f496e64696361746f725f73746172742e706e67)](https://camo.githubusercontent.com/1e6de8add4c7a0954664b9242e0510b1f4aec44d/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c6c65745f496e64696361746f725f73746172742e706e67)


* 当连接完成时，你也应该从下图设备标签中命名你的设备。如果你想Pushbullet在每次开机时自动启动，你可以在从preference设备中
* 点击打开Autostart按钮自动启动(如上图所示)
* 当你做完这一步，你会看见 Pushbullet indicator 小应用出现在Unity panel。


[![](https://camo.githubusercontent.com/e319c20609cfee98e2384438d6b83395f1bd6bfd/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5573655f5075736862756c6c65745f696e64696361746f725f5562756e74752e6a706567)](https://camo.githubusercontent.com/e319c20609cfee98e2384438d6b83395f1bd6bfd/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5573655f5075736862756c6c65745f696e64696361746f725f5562756e74752e6a706567)


* 点击indicator，选择想要向其发送数据的智能手机（已经连接到你的Pushbullet的设备）


[![](https://camo.githubusercontent.com/425431a16ccd304e20a574c65734022f077dd030/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c6c65745f496e64696361746f725f496e5f5562756e74752e706e67)](https://camo.githubusercontent.com/425431a16ccd304e20a574c65734022f077dd030/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c6c65745f496e64696361746f725f496e5f5562756e74752e706e67)


* 你将会在其他设备上接收到一个接收文件的通知。然后，你可以通过Pushbullet app应用获取所有的通知消息。
* 安卓设备也可以接到来电、短信和其他类型的通知。
* 如果你从你的移动设备向桌面发送一个文件的话，你将会接到以下通知。


[![](https://camo.githubusercontent.com/a89fc6ab7b7d939cf0502a88eba66f9eed1df85c/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c65745f496e64696361746f725f4e6f74696669636174696f6e2e6a706567)](https://camo.githubusercontent.com/a89fc6ab7b7d939cf0502a88eba66f9eed1df85c/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30372f5075736862756c65745f496e64696361746f725f4e6f74696669636174696f6e2e6a706567)


* 这些文件不会自动的保存在某个目录下。获取其他设备发送来的文件，可以去indicator目录查看最后推送（Show last push），显示你最后推送的。点击下载文件到你选择的目录中。


### 为Pushbullet安装Nautilus扩展


另一个可选的建议，你可以为Pushbullet安装Nautilus扩展，使它可以通过右键目录直接发送文件。使用以下命令安装。



```
sudo apt-get install nautilus-pushbullet

```

但是，在重启后你必须重新授权。


请在评论区分享你使用Pushbullet Indicator小应用的经验,朋友们,再见.


[![](https://camo.githubusercontent.com/833227653e92ff2977eb611656595583f49d0fd2/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d696e636c756465732f696d616765732f736d696c6965732f69636f6e5f736d696c652e676966)](https://camo.githubusercontent.com/833227653e92ff2977eb611656595583f49d0fd2/687474703a2f2f697473666f73732e697473666f73732e6e6574646e612d63646e2e636f6d2f77702d696e636c756465732f696d616765732f736d696c6965732f69636f6e5f736d696c652e676966)




---


via: <http://itsfoss.com/pushbullet-indicator-ubuntu/>


作者：[Abhishek](http://itsfoss.com/author/Abhishek/) 译者：[lfzark](https://github.com/lfzark) 校对：[Caroline](https://github.com/carolinewuyan)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
