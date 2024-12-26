---
layout: post
title:	"Fedora 25 Workstation 安装指南"
date:	2016-12-08 09:53:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Fedora]
---


在这篇教程中，我们将会走完在电脑上安装 Fedora 25 workstation 的每一步。该指南包括整个安装过程中的每一步截图，因此，请认真跟着操作。


![](/Asserts/Images//attachment/album/201612/07/210434pbzllsrlllscrlli.jpg)


#### Fedora 25 Workstation 有哪些新特性?


正如大家所期待的那样，Fedora 的这个最新版本在基础组件上做了很多的改变以及修复大量的 bug，除此之外，它带来了很多新的功能强大的软件，如下所示：


* GNOME 3.22，可以重命名多个文件，重新设计的键盘布局工具以及一些用户界面上的改进。
* 使用 Wayland 代替 X11 系统，以满足现代图形硬件设备。
* 支持 MP3 格式解码。
* Docker 1.12。
* Node.js 6.9.1。
* 支持 Rust 系统编程语言。
* 支持多个版本的 Python 编程语言，包括 Python2.6、2.7、3.3、3.4 和 3.5。
* 不再检查 GNOME Shell 扩展与当前的 GNOME Shell 版本的兼容性等等。


注意：如果电脑上已安装了前一个版本 Fedora 24，或许你可以考虑使用更简单的几个步骤[将 Fedora 24 升级到 Fedora 25](http://www.tecmint.com/upgrade-fedora-24-to-fedora-25-workstation-server/) 以避免全新的安装过程。


### 安装 Fedora 25 Workstation 版本


从下面的链接下载 ISO 系统镜像开始，本安装教程将使用 64 位的镜像来安装。


* [下载 Fedora 25 Workstation 64 位版本](https://download.fedoraproject.org/pub/fedora/linux/releases/25/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-25-1.3.iso)
* [下载 Fedora 25 Workstation 32 位版本](https://download.fedoraproject.org/pub/fedora/linux/releases/25/Workstation/i386/iso/Fedora-Workstation-Live-i386-25-1.3.iso)


下载完 Fedora 25 的系统镜像后，第一步是创建一个可启动设备（DVD 或 USB 设备），使用 [Unetbootin 和 dd 命令](http://www.tecmint.com/install-linux-from-usb-device/)来制作 USB 启动工具，或使用其它你想用的方法也行。


1、 创建完成启动设备后，插入并从该设备（DVD/USB）启动，此时，你应该看到如下图所示的 Fedora Workstation Live 的启动界面。


选择 “Start Fedora-Workstation-Live 25” 选项，然后单点回车。


![Fedora 25 Boot Menu](/Asserts/Images//attachment/album/201612/07/210530wqhs1s9yz8s9xax8.png)


*Fedora 25 启动菜单*


2、 接下来，你会进入到登录界面，单击“Live System User”以 Live 用户身份进入系统。


![Fedora 25 Live User Login](/Asserts/Images//attachment/album/201612/07/210531f6gez5mj999exse9.png)


*Fedora 25 Live 用户登录*


3、 登入系统后，几秒钟后桌面上会出现下面的欢迎界面，如果你想在安装前试用 Fedora 系统，单击 “Try Fedora”，否则单击 “Install to Hard Disk” 进入到全新安装过程。


![Fedora 25 Welcome Screen](/Asserts/Images//attachment/album/201612/07/210533sm7kkd4pahhd79bd.png)


*Fedora 25 欢迎界面*


4、 在下面的界面中，选择想要使用的安装语言，然后单击“<ruby> 继续 <rp>  （ </rp> <rt>  Continue </rt> <rp>  ） </rp></ruby>”按钮进入到安装总结页面。


![Select Installation Language Type](/Asserts/Images//attachment/album/201612/07/210534ykeoey3b37kokyc6.png)


*选择安装语言类型*


5、 下图是安装总结界面，显示默认的区域及系统设置内容。你可以根据自己的位置和喜好来定制区域及系统设置。


从键盘设置开始。单击“<ruby> 键盘 <rp>  （ </rp> <rt>  KEYBOARD </rt> <rp>  ） </rp></ruby>”进入到键盘布局自定义设置界面。


![Fedora 25 Installation Summary](/Asserts/Images//attachment/album/201612/07/210535ypzdodqo8lqz8d3p.png)


*Fedora 25 安装总结*


6、 在这个界面中，根据你电脑之前的设置使用`+`号来添加你需要的键盘布局，然后单击“<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>"返回到安装总结界面。


![Set Keyboard Layout](/Asserts/Images//attachment/album/201612/07/210536yamh4iaiu6qrqd5u.png)


*设置键盘布局*


7、 下一步，单击“<ruby> 时间与日期 <rp>  （ </rp> <rt>  TIME &amp; DATA </rt> <rp>  ） </rp></ruby>”调整系统时间和日期。输入所在地区和城市来设置时区，或者从地图上快速选择。


注意你可以从右上角启用或者停用网络时间同步。设置完系统时间和日期后，单击“<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>”返回到安装总结界面。


![Set System Timezone](/Asserts/Images//attachment/album/201612/07/210538civv6mad44am40pb.png)


*设置系统时区*


8、 返回到安装总结界面，单击“<ruby> 网络与主机名 <rp>  （ </rp> <rt>  NETWORK &amp; HOSTNAME </rt> <rp>  ） </rp></ruby>”设置网络和主机名。


主机名设置完成后，单击“<ruby> 应用 <rp>  （ </rp> <rt>  Apply </rt> <rp>  ） </rp></ruby>”来检查主机名是否可用，如果可用，单击“<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>”。


![Set Hostname for Fedora 25](/Asserts/Images//attachment/album/201612/07/210538gffz75b5j5ebf3bw.png)


*设置 Fedora 25 的主机名*


9、 此时，在安装总结界面，单击“<ruby> 安装目标 <rp>  （ </rp> <rt>  INSTALLATION DESTINATION </rt> <rp>  ） </rp></ruby>”来为系统文件划分安装空间。


在“<ruby> 其它存储选项 <rp>  （ </rp> <rt>  Other Storage Options </rt> <rp>  ） </rp></ruby>”上选择“<ruby> 我要配置分区 <rp>  （ </rp> <rt>  I will configure partitioning </rt> <rp>  ） </rp></ruby>”来执行手动分区，然后单击 “<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>” 前进至手动分区界面。


![Select Installation Destination Drive](/Asserts/Images//attachment/album/201612/07/210539nsi5ks0qjej7js0w.png)


*选择安装位置*


10、 下面是手动分区界面，选择“<ruby> 标准分区 <rp>  （ </rp> <rt>  Standard Partition </rt> <rp>  ） </rp></ruby>”为新的分区模式来安装。


![Manual Partitioning Selection](/Asserts/Images//attachment/album/201612/07/210539xpbbbu90tbq3b53q.png)


*手动配置分区*


11、 现在通过点`+`号增加一个挂载点来创建一个`/root`分区。


* 挂载点： /root
* 建议容量： 合适即可（比如 100 GB）


之后，单击“<ruby> 增加挂载点 <rp>  （ </rp> <rt>  Add mount point </rt> <rp>  ） </rp></ruby>”添加刚刚创建的分区/挂载点。


![Create New Root Partition](/Asserts/Images//attachment/album/201612/07/210540nghvb3ug7mdg7dhg.png)


*创建新的 Root 分区*


下图展示了 `/root` 分区设置。


![Root Partition Settings](/Asserts/Images//attachment/album/201612/07/210541vafk4agabokzeccs.png)


*Root 分区设置*


12、 下一步，通过`+`号创建<ruby> 交换分区 <rp>  （ </rp> <rt>  swap </rt> <rp>  ） </rp></ruby>


交换分区是硬盘上的一个虚拟的磁盘空间，用于临时存放那些当前 CPU 不使用的内存数据。


* 挂载点： swap
* 建议容量：合适即可（比如 4 GB）


单击“<ruby> 增加挂载点 <rp>  （ </rp> <rt>  Add mount point </rt> <rp>  ） </rp></ruby>”添加交换分区。


![Create Swap Partition](/Asserts/Images//attachment/album/201612/07/210542b7ljn7hnwnjnk4ws.png)


*创建交换分区*


![Swap Partition Settings](/Asserts/Images//attachment/album/201612/07/210543ka2k02e5e9bk7e0d.png)


*交换分区设置*


13、 创建完 `root` 分区和 `swap` 分区后，单击“<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>”按钮来查看这些要对磁盘进行的更改。单击 “<ruby> 接受调整 <rp>  （ </rp> <rt>  Accept Changes </rt> <rp>  ） </rp></ruby>” 允许执行所有的分区调整。


![Accept Partition Changes](/Asserts/Images//attachment/album/201612/07/210544x5ara4hzpaeihaaa.png)


*接受分区调整*


14、 你最后的安装总结内容应该跟下图显示的差不多。单击“<ruby> 开始安装 <rp>  （ </rp> <rt>  Begin Installation </rt> <rp>  ） </rp></ruby>”开始真正安装系统。


![Final Installation Summary](/Asserts/Images//attachment/album/201612/07/210545dlmm0nnpbml60b9e.png)


*最后的安装总结内容*


15、 系统文件安装开始后，你可以在下面的界面中，创建一个常用的系统用户，并为 root 账号设置密码。


![User Configuration Settings](/Asserts/Images//attachment/album/201612/07/210547feghg567mdnoh7gd.png)


*用户配置设置*


16、 之后，单击“<ruby> ROOT 密码 <rp>  （ </rp> <rt>  ROOT PASSWORD </rt> <rp>  ） </rp></ruby>”来设置 root 账号密码。像之前一样，单击“<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>”返回到用户配置界面。


![Set Root Account Password](/Asserts/Images//attachment/album/201612/07/210548q3kfzff3skbboaoe.png)


*设置 root 账号密码*


17、 之后，在用户配置界面单击“<ruby> 创建用户 <rp>  （ </rp> <rt>  USER CREATION </rt> <rp>  ） </rp></ruby>”按钮来创建一个常用的系统用户。你也可以勾选“<ruby> 将该用户作为管理员 <rp>  （ </rp> <rt>  Make the user administrator </rt> <rp>  ） </rp></ruby>”选项把该用户提升为系统管理员。


再次单击“<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>”按钮继续。


![Create System User Account](/Asserts/Images//attachment/album/201612/07/210549p3foisupggpig3os.png)


*创建系统用户账号*


18、 安装过程将会持续一段时间，你可以去休息会了。安装完成之后，单击“<ruby> 退出 <rp>  （ </rp> <rt>  Quit </rt> <rp>  ） </rp></ruby>”重启系统，并弹出你使用的启动设备。终于，你可以登录进入新的 Fedora 25 Workstation 了。 


![Fedora 25 Login Screen](/Asserts/Images//attachment/album/201612/07/210551zpnwepw1k1nkfnkd.png)


*Fedora 25 登录界面*


![Fedora 25 Workstation Desktop](/Asserts/Images//attachment/album/201612/07/210553h0lc82qqwy2x7m7u.png)


*Fedora 25 Workstation 桌面*


就写到这里吧！请在下面提出相关的问题并发表评论。




---


via: <http://www.tecmint.com/fedora-25-installation-guide/>


作者：[Aaron Kili](http://www.tecmint.com/author/aaronkili/) 译者：[rusking](https://github.com/rusking) 校对：[jasminepeng](https://github.com/jasminepeng)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
