---
layout: post
title:	"RHEL (Red Hat Enterprise Linux，红帽企业级 Linux) 7.3 安装指南"
date:	2016-12-27 09:40:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,RHEL,CentOS]
---


RHEL 是由红帽公司开发维护的开源 Linux 发行版，可以运行在所有的主流 CPU 架构中。一般来说，多数的 Linux 发行版都可以免费下载、安装和使用，但对于 RHEL，只有在购买了订阅之后，你才能下载和使用，否则只能获取到试用期为 30 天的评估版。


![](/Asserts/Images//attachment/album/201612/27/095245gsx00qssvhq2chzb.png)


本文会告诉你如何在你的机器上安装最新的 RHEL 7.3，当然了，使用的是期限 30 天的评估版 ISO 镜像，请自行到 <https://access.redhat.com/downloads> 下载。


如果你更喜欢使用 CentOS，请移步 [CentOS 7.3 安装指南](/article-8048-1.html)。


欲了解 RHEL 7.3 的新特性，请参考 [版本更新日志](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7-Beta/html/7.3_Release_Notes/chap-Red_Hat_Enterprise_Linux-7.3_Release_Notes-Overview.html)。


#### 先决条件


本次安装是在支持 UEFI 的虚拟机固件上进行的。为了完成安装，你首先需要进入主板的 EFI 固件更改启动顺序为已刻录好 ISO 镜像的对应设备（DVD 或者 U 盘）。


如果是通过 USB 介质来安装，你需要确保这个可以启动的 USB 设备是用支持 UEFI 兼容的工具来创建的，比如 [Rufus](https://rufus.akeo.ie/)，它能将你的 USB 设备设置为 UEFI 固件所需要的 GPT 分区方案。


为了进入主板的 UEFI 固件设置面板，你需要在电脑初始化 POST (<ruby> 通电自检 <rp>  （ </rp> <rt>  Power on Self Test </rt> <rp>  ） </rp></ruby>) 的时候按下一个特殊键。


关于该设置需要用到特殊键，你可以向主板厂商进行咨询获取。通常来说，在笔记本上，可能是这些键：F2、F9、F10、F11 或者 F12，也可能是 Fn 与这些键的组合。


此外，更改 UEFI 启动顺序前，你要确保<ruby> 快速启动选项 <rp>  （ </rp> <rt>  QuickBoot/FastBoot </rt> <rp>  ） </rp></ruby>和 <ruby> 安全启动选项 <rp>  （ </rp> <rt>  Secure Boot </rt> <rp>  ） </rp></ruby>处于关闭状态，这样才能在 EFI 固件中运行 RHEL。


有一些 UEFI 固件主板模型有这样一个选项，它让你能够以传统的 BIOS 或者 EFI CSM (<ruby> 兼容支持模块 <rp>  （ </rp> <rt>  Compatibility Support Module </rt> <rp>  ） </rp></ruby>) 两种模式来安装操作系统，其中 CSM 是主板固件中一个用来模拟 BIOS 环境的模块。这种类型的安装需要 U 盘以 MBR 而非 GPT 来进行分区。


此外，一旦在你的 UEFI 机器中以这两种模式之一成功安装好 RHEL 或者类似的 OS，那么安装好的系统就必须以你安装时使用的模式来运行。而且，你也不能够从 UEFI 模式变更到传统的 BIOS 模式，反之亦然。强行变更这两种模式会让你的系统变得不稳定、无法启动，同时还需要重新安装系统。


### RHEL 7.3 安装指南


1、 首先，下载并使用合适的工具刻录 RHEL 7.3 ISO 镜像到 DVD 或者创建一个可启动的 U 盘。


给机器加电启动，把 DVD/U 盘放入合适驱动器中，并根据你的 UEFI/BIOS 类型，按下特定的启动键变更启动顺序来启动安装介质。


当安装介质被检测到之后，它会启动到 RHEL 的 grub 菜单。选择“Install red hat Enterprise Linux 7.3” 并按回车继续。


![RHEL 7.3 Boot Menu](/Asserts/Images//attachment/album/201612/27/094049h66v0fggajja5106.jpg)


*RHEL 7.3 启动菜单*


2、 之后屏幕就会显示 RHEL 7.3 欢迎界面。该界面选择安装过程中使用的语言 (LCTT 译注：这里选的只是安装过程中使用的语言，之后的安装中才会进行最终使用的系统语言环境) ，然后按回车到下一界面。


![Select RHEL 7.3 Language](/Asserts/Images//attachment/album/201612/27/094050zkr4408n0r18ezk4.png)


*选择 RHEL 7.3 安装过程使用的语言*


3、 下一界面中显示的是安装 RHEL 时你需要设置的所有事项的总体概览。首先点击<ruby> 日期和时间 <rp>  （ </rp> <rt>  DATE &amp; TIME </rt> <rp>  ） </rp></ruby>并在地图中选择你的设备所在地区。


点击最上面的<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby> 按钮来保持你的设置，并进行下一步系统设置。


![RHEL 7.3 Installation Summary](/Asserts/Images//attachment/album/201612/27/094051eur0q0pqgaai2fiq.png)


*RHEL 7.3 安装概览*


![Select RHEL 7.3 Date and Time](/Asserts/Images//attachment/album/201612/27/094052pq46p6jwvxhlhfxj.png)


*选择 RHEL 7.3 日期和时间*


4、 接下来，就是配置你的<ruby> 键盘 <rp>  （ </rp> <rt>  keyboard </rt> <rp>  ） </rp></ruby>布局并再次点击<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby> 按钮返回安装主菜单。


![Configure Keyboard Layout](/Asserts/Images//attachment/album/201612/27/094052fseeahsppvt6nz9z.png)


*配置键盘布局*


5、 紧接着，选择你使用的<ruby> 语言支持 <rp>  （ </rp> <rt>  language support </rt> <rp>  ） </rp></ruby>，并点击<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>，然后进行下一步。


![Choose Language Support](/Asserts/Images//attachment/album/201612/27/094053fc6sndiq10rqf01q.png)


*选择语言支持*


6、 <ruby> 安装源 <rp>  （ </rp> <rt>  Installation Source </rt> <rp>  ） </rp></ruby>保持默认就好，因为本例中我们使用本地安装 (DVD/USB 镜像)，然后进行<ruby> 软件集选择 <rp>  （ </rp> <rt>  Software Selection </rt> <rp>  ） </rp></ruby>。


此处你可以选择<ruby> 基本环境 <rp>  （ </rp> <rt>  base environment </rt> <rp>  ） </rp></ruby>和<ruby> 附件 <rp>  （ </rp> <rt>  Add-ons </rt> <rp>  ） </rp></ruby>。由于 RHEL 常用作 Linux 服务器，<ruby> 最小化安装 <rp>  （ </rp> <rt>  Minimal Installation </rt> <rp>  ） </rp></ruby>对于系统管理员来说则是最佳选择。


对于生产环境来说，这也是官方极力推荐的安装方式，因为我们只需要在 OS 中安装极少量软件就好了。


这也意味着高安全性、可伸缩性以及占用极少的磁盘空间。同时，通过购买<ruby> 订阅 <rp>  （ </rp> <rt>  subscription </rt> <rp>  ） </rp></ruby> 或使用 DVD 镜像源，这里列出的的其它环境和附件都是可以在命令行中很容易地安装。


![RHEL 7.3 Software Selection](/Asserts/Images//attachment/album/201612/27/094054ggjii7n4tjwjdj41.png)


*RHEL 7.3 软件集选择*


7、 万一你想要安装预定义的基本环境之一，比方说 Web 服务器、文件 & 打印服务器、架构服务器、虚拟化主机、带 GUI 的服务器等，直接点击选择它们，然后在右边的框选择附件，最后点击<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby> 结束这一步操作即可。


![Select Server with GUI on RHEL 7.3](/Asserts/Images//attachment/album/201612/27/094054rzyyrabcyjzjpa65.png)


*选择带 GUI 的服务器*


8、 在接下来点击<ruby> 安装目标 <rp>  （ </rp> <rt>  Installation Destination </rt> <rp>  ） </rp></ruby>，这个步骤要求你为将要安装的系统进行分区、格式化文件系统并设置挂载点。


最安全的做法就是让安装器自动配置硬盘分区，这样会创建 Linux 系统所有需要用到的基本分区 (在 LVM 中创建 `/boot`、`/boot/efi`、`/(root)` 以及 `swap` 等分区)，并格式化为 RHEL 7.3 默认的 XFS 文件系统。


请记住：如果安装过程是从 UEFI 固件中启动的，那么硬盘的分区表则是 GPT 分区方案。否则，如果你以 CSM 或传统 BIOS 来启动，硬盘的分区表则使用老旧的 MBR 分区方案。


假如不喜欢自动分区，你也可以选择配置你的硬盘分区表，手动创建自己需要的分区。


不论如何，本文推荐你选择自动配置分区。最后点击<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby> 继续下一步。


![Choose RHEL 7.3 Installation Drive](/Asserts/Images//attachment/album/201612/27/094055jsjzjudpjdpbgsjh.png)


*选择 RHEL 7.3 的安装硬盘*


9、 下一步是禁用 Kdump 服务，然后配置网络。


![Disable Kdump Feature](/Asserts/Images//attachment/album/201612/27/094056al5i85v6ivbiyni6.png)


*禁用 Kdump 特性*


10、 在<ruby> 网络和主机名 <rp>  （ </rp> <rt>  Network and Hostname </rt> <rp>  ） </rp></ruby>中，设置你机器使用的主机名和一个描述性名称，同时拖动 Ethernet 开关按钮到 `ON` 来启用网络功能。


如果你在自己的网络中有一个 DHCP 服务器，那么网络 IP 设置会自动获取和使用。


![Configure Network Hostname](/Asserts/Images//attachment/album/201612/27/094057v4tivv1sugg1vp1p.png)


*配置网络主机名称*


11、 如果要为网络接口设置静态 IP，点击<ruby> 配置 <rp>  （ </rp> <rt>  Configure </rt> <rp>  ） </rp></ruby>按钮，然后手动设置 IP，如下方截图所示。


设置好网络接口的 IP 地址之后，点击<ruby> 保存 <rp>  （ </rp> <rt>  Save </rt> <rp>  ） </rp></ruby>按钮，最后切换一下网络接口的 `OFF` 和 `ON` 状态已应用刚刚设置的静态 IP。


最后，点击<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby> 按钮返回到安装设置主界面。


![Configure Network IP Address](/Asserts/Images//attachment/album/201612/27/094058dz70x7j0leleu02w.png)


*配置网络 IP 地址*


12、 最后，在安装配置主界面需要你配置的最后一项就是<ruby> 安全策略配置 <rp>  （ </rp> <rt>  Security Policy </rt> <rp>  ） </rp></ruby>文件了。选择并应用<ruby> 默认的 <rp>  （ </rp> <rt>  Default </rt> <rp>  ） </rp></ruby>安全策略，然后点击<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby>返回主界面。


回顾所有的安装设置项并点击<ruby> 开始安装 <rp>  （ </rp> <rt>  Begin Installation </rt> <rp>  ） </rp></ruby>按钮来启动安装过程，这个过程启动之后，你就没有办法停止它了。


![Apply Security Policy for RHEL 7.3](/Asserts/Images//attachment/album/201612/27/094058hl4ekr60d1lzs2y4.png)


*为 RHEL 7.3 启用安全策略*


![Begin Installation of RHEL 7.3](/Asserts/Images//attachment/album/201612/27/094059wf8vzuzfto0o2mlu.png)


*开始安装 RHEL 7.3*


13、 在安装过程中，你的显示器会出现<ruby> 用户设置 <rp>  （ </rp> <rt>  User Settings </rt> <rp>  ） </rp></ruby>。首先点击<ruby> Root 密码 <rp>  （ </rp> <rt>  Root Password </rt> <rp>  ） </rp></ruby>为 root 账户设置一个高强度密码。


![Configure User Settings](/Asserts/Images//attachment/album/201612/27/094100i15vi14r7nnmrrnm.png)


*配置用户选项*


![Set Root Account Password](/Asserts/Images//attachment/album/201612/27/094101vftvnne42chhgcmz.png)


*设置 Root 账户密码*


14、 最后，创建一个新用户，通过选中<ruby> 使该用户成为管理员 <rp>  （ </rp> <rt>  Make this user administrator </rt> <rp>  ） </rp></ruby>为新建的用户授权 root 权限。同时还要为这个账户设置一个高强度密码，点击<ruby> 完成 <rp>  （ </rp> <rt>  Done </rt> <rp>  ） </rp></ruby> 返回用户设置菜单，就可以等待安装过程完成了。


![Create New User Account](/Asserts/Images//attachment/album/201612/27/094102gk22lvblltn6lk4o.png)


*创建新用户账户*


![RHEL 7.3 Installation Process](/Asserts/Images//attachment/album/201612/27/094103ri7vp8j9jffpkfxi.png)


*RHEL 7.3 安装过程*


15、 安装过程结束并成功安装后，弹出或拔掉 DVD/USB 设备，重启机器。


![RHEL 7.3 Installation Complete](/Asserts/Images//attachment/album/201612/27/094103qddbf0fldldd22d8.png)


*RHEL 7.3 安装完成*


![Booting Up RHEL 7.3](/Asserts/Images//attachment/album/201612/27/094104c6dwvrbzyn8i8ryw.png)


*启动 RHEL 7.3*


至此，安装完成。为了后期一直使用 RHEL，你需要从 Red Hat 消费者门户购买一个订阅，然后在命令行 [使用订阅管理器来注册你的 RHEL 系统](http://www.tecmint.com/enable-redhat-subscription-reposiories-and-updates-for-rhel-7/)。




---


作者简介:


![](/Asserts/Images//attachment/album/201612/27/094106f65usas6ytbz3tjx.jpg)Matei Cezar


我是一个终日沉溺于电脑的家伙，对开源的 Linux 软件非常着迷，有着 4 年 Linux 桌面发行版、服务器和 bash 编程经验。


 




---


via: <http://www.tecmint.com/red-hat-enterprise-linux-7-3-installation-guide/>


作者：[Matei Cezar](http://www.tecmint.com/author/cezarmatei/) 译者：[GHLandy](https://github.com/GHLandy) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
