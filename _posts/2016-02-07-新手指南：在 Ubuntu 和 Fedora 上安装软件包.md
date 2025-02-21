---
layout: post
title:	"新手指南：在 Ubuntu 和 Fedora 上安装软件包"
date:	2016-02-05 08:15:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,安装软件,编译]
---


新进入 Linux 世界的朋友们，也许你已经[下载好了 Linux 的安装 ISO](/article-4130-1.html)，并且[安装好了你的 Linux](/article-5893-1.html) ，那么接下来，你也许希望安装一些 Linux 上用的软件。开始你可能会使用图形界面的软件中心来安装，有时候也需要使用命令行来安装，或者甚至需要自己去编译一个二进制出来——这是多么神奇的一件事啊。


那么我们今天就讲一讲如何在 Linux 上安装软件包。


本文将从 **GUI 软件中心**、**包管理器**、**在线仓库安装**，**本地安装**，**源码安装** 一一为你讲解有关安装软件包需要注意的事项。 


![](/Asserts/Images/album/201508/16/222746e5vh38d7ey3leyps.jpg)


### 本文环境


* Ubuntu 15.04 64-bit
* Fedora 22 64-bit


### 安装目标


* wget 它是一个用于从网络上下载文件的简单自由软件，在下文我们也会用到 wget 进行下载某些文件。


### 相关概念


* **源** ：我们安装程序可以从 **远程仓库** 或 **本地仓库** 获取，这个 **仓库** 就是我们程序的来源，因此可以称为 **源** 。
* **包管理器** ：顾名思义 **包管理器** 是用来管理软件包的，用这个工具我们可以轻松的从仓库中安装、卸载程序。不同的发行版有不同的包管理器，Ubuntu 使用 `apt-get` 而 Fedora 22使用 `dnf`。
* **源码** ： 程序的原始代码，未经过编译，通过编译源码也可以生成程序。


### 图形界面的软件中心


#### Ubuntu 软件中心


当我们处于图形界面（ GUI ：Graphical User Interface) 时，Ubuntu 为我们提供了一个图形界面的安装工具，称为 **Ubuntu 软件中心**，通过这个软件中心，我们可以像 Windows 一样通过点击几个按钮，轻松实现软件包安装。下图为打开软件中心之后的图，左边是一些分类，下面则是一些推荐的软件包。


![Ubunutu 软件中心](/Asserts/Images/album/201508/16/222807duvefmvtekrvmzae.png)


点击已安装可以查看安装在本机的软件包，并且可以在此管理它们，如图选中 Firefox 并点击卸载，此时会提示你输入密码，输入完成且正确就会卸载你所选的程序。


![已安装](/Asserts/Images/album/201508/16/222808pglctdclc3gd3f5t.png)


接下来在搜索框搜索 `wget` 你可以看到如图所示的东西，并且只需点击安装并正确输入密码即可。


![安装新程序](/Asserts/Images/album/201508/16/222808pglctdclc3gd3f5t.png)


#### Fedora 软件中心


点开如图所示的图标就可以打开 Fedora 的软件中心。


![Fedora 软件中心](/Asserts/Images/album/201508/16/222808i3dn7zuy4c27zvc4.png)


打开后界面如图，分类在最下面


![软件中心](/Asserts/Images/album/201508/16/222809pxyzebmzsmhwheei.png)


点开上图的扫雷，显示如下，点击 **安装** ，静候即可


![安装新程序](/Asserts/Images/album/201508/16/222809ke0uhd9e3zqw7h39.png)


现在转到 **已安装** ，我们可以看到刚刚安装的扫雷，点击 **移除** ，就可以删除了。


![移除程序](/Asserts/Images/album/201508/16/222809e9plrmmzu1p1pukr.png)


如果你遇到下图，只需要输入你的密码即可。


![认证](/Asserts/Images/album/201508/16/222810mc3rd4sasqabmqcz.png)


### 使用包管理器安装


#### 1.换源




| 发行版 | 换源方法 |
| --- | --- |
| Ubuntu | [阿里云镜像配置请参考这里](http://mirrors.aliyun.com/help/ubuntu) |
| [USTC镜像配置请参考这里](https://lug.ustc.edu.cn/wiki/mirrors/help/ubuntu) |
| Fedora | [阿里云镜像配置请参考这里](http://mirrors.aliyun.com/help/fedora) |
| [USTC镜像配置请参考这里](https://lug.ustc.edu.cn/wiki/mirrors/help/fedora) |


换源是为了提升下载速度，上文的概念已经提到了，我们安装软件是从远程仓库下载安装的，自然这个远程仓库的网络连通必须要好，并且下载速度要可观。


#### 2.更新源


更换了源的文件后，还需要更新本地数据库信息，以便与远程仓库信息一致。




| 发行版 | 包管理工具 | 参数 | 示例 | 解释 |
| --- | --- | --- | --- | --- |
| Ubuntu | apt-get | update | sudo apt-get update | 取回更新的软件包列表信息 |
| Fedora | dnf | check-update | sudo dnf check-update | 取回更新的软件包列表信息 |


#### 3.安装软件包




| 发行版 | 包管理工具 | 类型 | 参数 | 示例 | 解释 |
| --- | --- | --- | --- | --- | --- |
| Ubuntu | apt-get | 远程仓库 | install | sudo apt-get install packagename | 安装软件包 |
| Fedora | dnf | 远程仓库 | install | sudo dnf install packagename | 安装软件包 |
| Ubuntu | dpkg | 本地deb包 | -i | sudo dpkg -i filename.deb | 安装本地二进制deb包 |
| Fedora | rpm | 本地rpm包 | -i | sudo rpm -i filename.rpm | 安装本地二进制rpm包 |


#### 4.卸载软件包




| 发行版 | 包管理工具 | 参数 | 示例 | 解释 |
| --- | --- | --- | --- | --- |
| Ubuntu | apt-get | remove | sudo apt-get remove packagename | 卸载软件包 |
| Fedora | dnf | remove | sudo dnf remove packagename | 卸载软件包 |
| Ubuntu | dpkg | -r | sudo dpkg -r packagename | 卸载软件包 |


#### 5.升级所有软件包




| 发行版 | 包管理工具 | 参数 | 示例 | 解释 |
| --- | --- | --- | --- | --- |
| Ubuntu | apt-get | upgrade | sudo apt-get upgrade | 升级所有软件包 |
| Fedora | dnf | upgrade | sudo dnf upgrade | 升级所有软件包 |


#### 6.其它参数




| 发行版 | 包管理工具 | 参数 | 示例 | 解释 |
| --- | --- | --- | --- | --- |
| Ubuntu  | apt-get  | purge | sudo apt-get purge packagename | 卸载并清除软件包的配置 |
| source | apt-get source packagename | 下载源码包文件 |
| clean | sudo apt-get clean | 删除所有已下载的包文件 |
| download | apt-get download packagename | 下载指定的二进制包到当前目录 |
| --help | apt-get --help | 获取帮助 |
| Fedora  | dnf  | clean | sudo dnf clean | 清除旧缓存 |
| makecache | sudo dnf makecache | 生成新缓存 |
| -h | dnf -h | 获取帮助 |


### 从源码编译安装


有些时候我们会发现有的软件包并没有包含在软件仓库中，也没有可用的二进制包，这时候我们可以尝试从源码编译安装，我在此处仍以`wget` 为例，示范如何编译，并解决编译遇到的问题


以下环境为 **Ubuntu 15.04**



```
$ mkdir buildwget #构建目录
$ cd buildwget
$ wget http://ftp.gnu.org/gnu/wget/wget-1.16.tar.xz         #下载源码包
$ sudo apt-get remove wget  #为了后面的测试，先把 wget 卸载了
$ xz -d wget-1.16.tar.xz  #解压 xz 文件
$ tar -xvf wget-1.16.tar #解档 tar 文件
$ cd wget-1.16
$ ls                     #列出文件
ABOUT-NLS   ChangeLog.README  GNUmakefile   maint.mk     po       util
aclocal.m4  configure         INSTALL       Makefile.am  README
AUTHORS     configure.ac      lib           Makefile.in  src
build-aux   COPYING           m4            msdos        testenv
ChangeLog   doc               MAILING-LIST  NEWS         tests
```

上面的文件就是我们将要编译的源文件，其中有个特别要注意的就是 `INSTALL`，我们要养成一个习惯，多看 `INSTALL` 文件，这个文件会告诉我们怎么编译，编译时需要注意什么？但由于此处的编译较简单，所以 `INSTALL` 也没有提到什么特别重要的事情。


按照 `INSTALL` 我们先执行 `./configure`



```
$ ./configure
```

如果出现如下的错误



```
configure: error: --with-ssl=gnutls was given, but GNUTLS is not available.
```

错误提示说，给定的 `SSL` 是 `gnutls` 但是却不可用（因为没有安装），因此我们安装并指定 `openssl` 为 `wget` 的 `SSL` 。



```
$ sudo apt-get install openssl 
$ sudo apt-get install libssl-dev
$ ./configure --with-ssl=openssl
```

如果没有问题，执行完后应该显示如下



```
configure: Summary of build options:

  Version:           1.16
  Host OS:           linux-gnu
  Install prefix:    /usr/local
  Compiler:          gcc
  CFlags:            -g -O2 
  LDFlags:           
  Libs:              -lssl -lcrypto -ldl -lz 
  SSL:               openssl
  Zlib:              yes
  PSL:               no
  Digest:            yes
  NTLM:              yes
  OPIE:              yes
  Debugging:         yes
```

然后进行编译



```
$ make
```

会输出很多编译信息，不要担心，如果最后没有报错而停止，则编译成功，接下来进行安装



```
$ sudo make install
```

试试是不是 `wget` 命令又出来了？源码安装遇到问题，我们要善于搜索，提问和解决，根据报错内容进行相应的编译调整，缺少的依赖装上，一般就可以成功。 


### 总结


本文主要为新手讲解了 **Ubuntu** 和 **Fedora** 安装软件包的一些方法， 相较之前的版本，本次更改由繁化简，并且以表格的形式给出参数和命令，要熟练和体会这些命令到底是干嘛的，还必须亲自敲一敲，去理解这个命令的作用。从源码编译安装，则展示了一个遇到问题，解决问题的过程，由于编译 `wget` 较简单，此处也未遇到特别难处理的问题，但这清晰的展示了一个编译安装的过程，遇到错误，我们不要害怕，而要认真阅读给出的错误信息，借此搜索，提问，寻求解答。另外 Linux 下遇到问题首先要自己善于去搜索，提问，解决问题得到答案并归纳总结，不然是很难学到知识的。
