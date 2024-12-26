---
layout: post
title:	"新手指南： 手把手教你安装 Ubuntu 和 Fedora"
date:	2016-06-06 12:15:00 +0800 
categories:	桌面应用 linuxcn 
tags:	[linuxcn,Ubuntu,安装,Fedora]
---


Linux 由于开源，所以具备可定制性，因此衍生了许多发行版。Ubuntu 和 Fedora 算是其中对新手比较友好的两个发行版，主要是其安装较为简单，用户群多，有问题搜索出相关的信息或者找前辈解决。此文为 Linux 新手准备，通过展示整个安装过程来使 Linxu 新手完成安装 Ubuntu 或 Fedora ，也恳请各位前辈指出不足之处。


![](/Asserts/Images//attachment/album/201606/06/213747wj6puk60zct54n18.jpg)


### 阅读建议


* 本文将包含 Ubuntu 和 Fedora 两个发行版的安装，请先通篇浏览全文，再决定安装哪个发行版，并且配图有相应的文字说明，请不要忽视。
* 如果你是一位新手，强烈建议使用虚拟机操作；如果你相信自己可以解决问题，也可使用 `ultraiso` 、`USBWriter` 和 `dd`命令写入 U 盘，进行实体机安装，此处不详述。
* 有任何问题都可以加入 `Linux中国-新手村` QQ 群提问，QQ 群号 `198889109` ，验证信息 `LINUX` 。


### Ubuntu 简介


Ubuntu 是一个基于 Debian 的 GNU/Linux 操作系统，支持 X86 、64以及 PPC 架构。Ubuntu 每隔六个月发布一个版本，即每年的四月和十月，本文使用的是 `15.04 64-bit` 版本。Ubuntu 对于新手应该是比较友好的一个 Linux 发行版，中文本地化也做的不错，有开箱即用的感觉。因为 Ubuntu 近几年用户群的增加，多了很多对于新手有用的资料，因此不用担心遇到问题无法解决，善用搜索和提问，将使你更快速地成长。


更多 Ubuntu 的介绍请移步：[Ubuntu 17.04 (Zesty Zapus)/Ubuntu 16.04.2 LTS (Xenial Xerus)](/article-3238-1.html "Ubuntu 17.04 (Zesty Zapus)/Ubuntu 16.04.2 LTS (Xenial Xerus) ")  。


### Fedora 简介


Fedora 是一个由 Fedora 社区开发的 Linux 发行版，由 Red Hat 公司赞助。可以将 Fedora 看成是 Red Hat Linux 个人使用的代替，由于有 Red Hat 公司的支持，Fedora 的功能非常完善，还分为 WORKSTATION 、SERVER 和 CLOUD 版本。本文使用的是 **Fedora 22 WORKSTATION （工作站）**，Fedora 22 已经将包管理器从 `YUM` 改为 `DNF` ，因此建议学习者直接学习 `DNF` 。


更多 Fedora 的介绍请移步：[Fedora 27](/article-3237-1.html "Fedora 27") 。


### 本文环境


* **注意*****：*****本文下载链接直达官方下载，并且不断更新，以使****新的 Linux 用户可以用上最新的发行版，且文中的安装步骤基本不因版本的更替而改变。**
* Windows 8.1 64-bit
* [VirtualBox-5.2.4](/article-5794-1.html) [点此下载](http://download.virtualbox.org/virtualbox/5.2.4/VirtualBox-5.2.4-119785-Win.exe)
* Ubuntu 16.04 LTS 64-bit [点此下载](http://releases.ubuntu.com/16.04.3/ubuntu-16.04.3-desktop-amd64.iso)
* Ubuntu 16.04 LTS 32-bit 适合配置较低的用户使用 [点此下载](http://releases.ubuntu.com/16.04.3/ubuntu-16.04.3-desktop-i386.iso)
* Fedora 27 64-bit [点此下载](https://download.fedoraproject.org/pub/fedora/linux/releases/27/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-27-1.6.iso)
* Fedora 25 32-bit 适合配置较低用户使用 [点此下载](https://mirrors.ustc.edu.cn/fedora/releases/25/Workstation/i386/iso/Fedora-Workstation-Live-i386-25-1.3.iso)


更多 Linux 发行版的下载，可以看这里：[Linux 下载](/article-4130-1.html "Linux 下载") 。


### Ubuntu 安装


#### 1.新建与加载盘片


当你安装完 VirtualBox 后，打开你应该会看到下面这样的界面


![VirutalBox](/Asserts/Images//attachment/album/201507/26/230210cemyywweqgwwceeo.png)


点击新建后会出来如下图所示的界面，一般如图填写即可，内存可酌情填写


![新建虚拟电脑](/Asserts/Images//attachment/album/201507/26/230211ag6ggpqdxhh2x7gg.png)


下一步将创建虚拟硬盘，如图所示，默认位置为 C 盘，如果你不想在 C 盘创建，请确保你选择的盘格式为NTFS


![创建虚拟硬盘](/Asserts/Images//attachment/album/201507/26/230211upm7dd7dsztd6223.png)


创建完成后，请点 `设置` 如图加载 ISO 文件


![加载 ISO 文件](/Asserts/Images//attachment/album/201507/26/230212foxososp75skz2h3.png)


#### 2.安装 Ubuntu


点击**启动** ，会开机，进入如下界面


![开始安装](/Asserts/Images//attachment/album/201507/26/230212tfy6afa0yy7lqyh0.png)


![安装选项](/Asserts/Images//attachment/album/201507/26/230212ok12zd1dz4egei4t.png)


这里请注意，如果你与笔者一样使用虚拟机，强烈建议选择 **清除整个磁盘并安装 Ubuntu** ，但如果你要装到实体机与 Windows 形成双系统时，请选择 **其他选项** ，但这要求你对 Linxu 有一定的了解且具备一定的基础进行分区操作，注意不要覆盖 Windows 的 C 盘，此处由于篇幅原因，不再详述。


![安装类型](/Asserts/Images//attachment/album/201507/26/230213zchehg7hrj7fyfr2.png)


如图，进行用户设定，**计算机名** 是主机名，**用户名** 是登录时用的账户名称，**密码** 则是你所设 **用户名** 的登录密码，请务必记牢。


![添加用户](/Asserts/Images//attachment/album/201507/26/230213p4b2tq55ae4sjz22.png)


这一步之后会选择时区，直接点下一步即可，键盘选择如下图


![选择键盘布局](/Asserts/Images//attachment/album/201507/26/230213ca443s4r4z3srelr.png)


配置选择已完成，接下来请耐心等待安装过程，如图，请不要点击 **SKIP**


![安装中](/Asserts/Images//attachment/album/201507/26/230214o692qht9i9tkffk6.png)


耐心等待安装完成，然后会重启进入系统，用你上面配置的用户名和密码登录，请注意最好不要登录 `root` ，你可以用 `sudo` 命令来获取相应的权限，下图是展示成果：


![安装完成](/Asserts/Images//attachment/album/201507/26/230214ssckxph4fho4hhee.png)


### Fedora 安装


#### 1.新建与加载盘片


请参考上面的 Ubuntu 部分。


#### 2.安装 Fedora


点击 **启动**，会开机，进入如下界面,如图操作


![开始安装](/Asserts/Images//attachment/album/201507/26/230214oydrj7ce1761f4gs.png)


接下来依然是如图操作


![安装到硬盘](/Asserts/Images//attachment/album/201507/26/230215ximhv3r9a2f9qizf.png)


然后是选择语言，选择完后进入如图界面


![安装信息摘要](/Asserts/Images//attachment/album/201507/26/230215k99mdfwl3jp3kldz.png)


配置安装位置，这里请注意，如果你与笔者一样使用虚拟机，强烈建议选择 **自动配置分区** ；但如果你要装到实体机与 Windows 形成双系统时，请选择 **我要配置分区** ，但这要求你对 Linxu 有一定的了解且具备一定的基础进行分区操作，注意不要覆盖 Windows 的 C 盘，此处由于篇幅原因，不再详述。


![选择安装目标](/Asserts/Images//attachment/album/201507/26/230216zk1obsqmz7bxmz6q.png)


下一步将创建 `root` 和 **日常使用账户** ，`root` 账户有最大的管理权限，你甚至可以将整个系统删除，所以使用 `root` 账户请务必小心，**日常使用账户** 应作为你的习惯使用账户，必要时只需使用 `sudo` 命令暂时提升权限即可，更多说明如图所示


![创建用户和密码](/Asserts/Images//attachment/album/201508/16/212331r2wdmvrucvcmgrv2.png)


`root` 配置只需创建密码即可，下图是 **日常使用账户** 配置


![创建用户](/Asserts/Images//attachment/album/201507/26/230216dvc0clb4zic4nej8.png)


配置完后将回到之前的界面，请耐心等待安装，如图


![安装中](/Asserts/Images//attachment/album/201507/26/230217el3bnhonpaofbfnp.png)


安装完成，点击 **退出** 后，进入的依然是 Live CD 环境，请先关机，再执行下一步


![安装完成，退出关机](/Asserts/Images//attachment/album/201507/26/230219xagjlgkgqurqvivi.png)


由于 Fedora 未自动卸载盘片，因此需要手动卸载盘片，否则将再次进入 Live CD 环境，请如图操作


![卸载盘片](/Asserts/Images//attachment/album/201507/26/230219krn2uf1sjs5fzooo.png)


接下来则是点击 **启动** 进入你的 Fedora ，使用你上面设置的用户名和密码登录，请注意最好不要登录 `root` ，你可以用 `sudo` 命令来获取相应的权限，下图是展示成果


![安装成功](/Asserts/Images//attachment/album/201507/26/230220nl17l2zmyi1iyz11.png)


### 参考资料




---


* [Ubuntu-Wikipedia](https://zh.wikipedia.org/wiki/Ubuntu)
* [Fedora-Wikipedia](https://zh.wikipedia.org/wiki/Fedora)
