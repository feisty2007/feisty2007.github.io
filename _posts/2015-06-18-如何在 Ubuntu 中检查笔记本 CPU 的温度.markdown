---
layout: post
title:	"如何在 Ubuntu 中检查笔记本 CPU 的温度"
date:	2015-06-24 08:46:00 +0800 
categories:	桌面应用 linuxcn 
tags:	[linuxcn,温度]
---


![](/Asserts/Images//attachment/album/201506/23/234719y9wqlm8ww27wo55h.png)


夏天到了，笔记本过热是最近一个常见的问题。监控硬件温度或许可以帮助你诊断笔记本为什么会过热。本篇中，我们会**了解如何在Ubuntu中检查CPU的温度**。


我们将使用一个GUI工具[Psensor](http://wpitchoune.net/blog/psensor/)，它允许你在Linux中监控硬件温度。用Psensor你可以：


* 监控cpu和主板的温度
* 监控NVidia GPU的文档
* 监控硬盘的温度
* 监控风扇的速度
* 监控CPU的利用率


Psensor最新的版本同样提供了Ubuntu中的指示小程序，这样使得在Ubuntu中监控温度变得更加容易。你可以选择在面板的右上角显示温度。它还会在温度上过阈值后通知。


### 如何在Ubuntu 15.04 和 14.04中安装Psensor


在安装Psensor前，你需要安装和配置[lm-sensors](http://www.lm-sensors.org/)，这是一个用于硬件监控的命令行工具。如果你想要测量磁盘温度，你还需要安装[hddtemp](https://wiki.archlinux.org/index.php/Hddtemp)。要安装这些工具，运行下面的这些命令:



```
sudo apt-get install lm-sensors hddtemp

```

接着开始检测硬件传感器：



```
sudo sensors-detect

```

要确保已经工作，运行下面的命令：



```
sensors

```

它会给出下面这样的输出：



```
acpitz-virtual-0
Adapter: Virtual device
temp1: +43.0°C (crit = +98.0°C)

coretemp-isa-0000
Adapter: ISA adapter
Physical id 0: +44.0°C (high = +100.0°C, crit = +100.0°C)
Core 0: +41.0°C (high = +100.0°C, crit = +100.0°C)
Core 1: +40.0°C (high = +100.0°C, crit = +100.0°C)

```

如果一切看上去没问题，使用下面的命令安装Psensor：



```
sudo apt-get install psensor

```

安装完成后，在Unity Dash中运行程序。第一次运行时，你应该配置Psensor该监控什么状态。


![](/Asserts/Images//attachment/album/201506/23/234720sgi4oj6z7jyjt7gy.jpg)


### 在面板显示温度


如果你想要在面板中显示温度，进入**Sensor Preferences**:


![](/Asserts/Images//attachment/album/201506/23/234721raf5xjtuasuukhqu.jpg)


在 **Application Indicator** 菜单下，选择你想要显示温度的组件并勾上 **Display sensor in the label** 选项。


![](/Asserts/Images//attachment/album/201506/23/234723wccmmbomehr91btb.jpg)


### 每次启动启动Psensor


进入 **Preferences->Startup** 并选择 **Launch on session startup** 使每次启动时启动Psensor。


![](/Asserts/Images//attachment/album/201506/23/234723skznw6slnkrs4u84.jpg)


就是这样。你所要做的就是在这里监控CPU温度。你可以时刻注意并帮助你找出使计算机过热的进程。




---


via: <http://itsfoss.com/check-laptop-cpu-temperature-ubuntu/>


作者：[Abhishek](http://itsfoss.com/author/abhishek/) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](https://linux.cn/) 荣誉推出
