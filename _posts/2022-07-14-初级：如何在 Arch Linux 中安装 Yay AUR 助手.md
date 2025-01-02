---
layout: post
title:	"初级：如何在 Arch Linux 中安装 Yay AUR 助手"
date:	2022-07-20 16:41:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,Arch Linux,AUR,Yay]
---


![](/Asserts/Images/album/202207/20/164144qgavhpzf6h67a2q7.jpg)



> 
> 这个初学者指南解释了在 Arch Linux 中安装 Yay AUR 助手的步骤。
> 
> 
> 


Yay 是 “Yet Another Yogurt” 的缩写（LCTT 校注：Yogurt 是另外一个已经停止维护的 AUR 助手）。从技术上讲，它是用 [Go 编程语言](https://golang.org/) 编写的 [pacman](https://wiki.archlinux.org/index.php/pacman) 封装器和 AUR 助手。它是当今最流行的 [Arch 用户仓库（AUR）](https://wiki.archlinux.org/index.php/Arch_User_Repository) 助手。使用 Yay，你可以利用庞大的 Arch 用户软件包库并轻松编译和安装任何软件。


它可以自动执行许多包管理任务，例如搜索、动态解决依赖关系、编译和构建包，当然还有在 AUR 发布包。


让我们看看如何在 Arch Linux 或任何基于 Arch 的发行版（如 Manjaro）中安装 Yay。安装 Arch Linux 后，你可以通过 pacman 包管理器从三个主要的 Arch 官方仓库安装包。但是在全新的 Arch Linux 安装后，默认情况下不会安装 Yay。因此，你需要手动安装它以利用 AUR。


本指南涵盖以下主题：


* 在 Arch Linux 中安装 Yay
* 在 Manjaro 中安装 Yay
* 如何在 Arch Linux 和 Manjaro 中使用 Yay 安装包
* 一些 Yay 的技巧


### 在 Arch Linux 中安装 Yay


#### 先决条件


打开终端并运行以下命令。出现提示时提供管理员密码。这些步骤需要 [base-devel](https://aur.archlinux.org/packages/meta-group-base-devel/) 包和 git 包进行编译和安装。



```
sudo pacman -S base-devel

```


```
sudo pacman -S git

```

![Install git](/Asserts/Images/album/202207/20/164145l9j59ui588e8g453.png)


#### 安装 Yay


`yay` 包在 Arch 仓库中有两个版本，如下所示。


* [yay](https://aur.archlinux.org/packages/yay/) – 稳定版
* [yay-git](https://aur.archlinux.org/packages/yay-git/)– 开发版


对于本指南，我使用了稳定版。现在，进入 `/opt` 目录并克隆 git 仓库。



```
cd /opt
sudo git clone https://aur.archlinux.org/yay.git

```

![clone the yay repo](/Asserts/Images/album/202207/20/164146rurac0drl21m0u8f.png)


更改源目录的所有者。将 `debugpoint` 替换为你的用户名。



```
sudo chown -R debugpoint:users ./yay

```

如果你不知道用户或组，可以使用以下示例查找用户和组。



```
id debugpoint

```

进入目录并编译。



```
cd yay

```


```
makepkg -si

```

这样就完成了 Arch Linux 中 Yay 的安装。


![Install yay in Arch Linux](/Asserts/Images/album/202207/20/164146jece5s5bmqbfbbhn.png)


### 在 Manjaro 中安装 Yay


如果你使用 Manjaro Linux，`yay` 包可以在社区仓库中找到。你可以在 Manjaro 中使用以下命令轻松安装。



```
pacman -Syyu  
pacman -S yay

```

现在，让我们看看如何使用 Yay 安装任何软件包，以及一些基本的 `yay` 用法。


### 如何使用 Yay 安装包


首先在 AUR 网站上搜索安装任何应用以获取包名。例如，要安装 [featherpad](https://aur.archlinux.org/packages/featherpad-git/) 文本编辑器，请运行以下命令。



```
yay -S featherpad

```

安装后，你可以在应用菜单中找到应用启动器。


![Install a sample application (featherpad) using yay](/Asserts/Images/album/202207/20/164147iz3eune98x88e385.png)


### 一些 Yay 的技巧


你还可以使用 yay 进行许多调整和系统操作。下面是一些示例。


**刷新系统包并升级**：



```
yay -Syu

```

**使用包的开发版本并升级（运行此命令时要小心）**：



```
yay -Syu --devel --timeupdate

```

**删除任何包（例如，featherpad）**：



```
yay -Rns featherpad

```

**快速获取系统统计信息**：


![system stat using yay](/Asserts/Images/album/202207/20/164148p5zugqu78cvvwgz6.png)



```
yay -Ps

```

我希望这个初学者指南能帮助你在 [Arch Linux](https://www.debugpoint.com/tag/arch-linux/) 中安装 Yay，然后使用 Yay 安装包，并执行不同的系统操作。




---


via: <https://www.debugpoint.com/install-yay-arch/>


作者：[Arindam](https://www.debugpoint.com/author/admin1/) 选题：[lkxed](https://github.com/lkxed) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
