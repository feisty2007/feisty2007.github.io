---
layout: post
title:	"Enlightenment E20 发布"
date:	2015-12-03 07:33:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Enlightenment]
---


![](/Asserts/Images/album/201512/02/220827i9pyzhgkep79yxjk.jpg)


E20 的开发已经告一段落了。在这 441 天期间，50 位以上的开发者提交了 1890 个补丁。报告了 25 个以上的 Coverity 分析问题，解决了 165 个问题（根据提交信息得知）。bug 汇报之王 [@ApB](https://phab.enlightenment.org/p/ApB/) 共提交了 231 个问题，虽然只有其中 70% 得到了解决，但是依然为我们帮了大忙。


非常感谢每位做出贡献的人，无论是提交补丁、撰写文档、汇报问题还是简单地在 IRC 上提供反馈。


### 新版本亮点


* 对 [Wayland](https://git.enlightenment.org/core/enlightenment.git/tree/README.wayland) 的完整支持
* 新的屏幕管理架构和对话框
* 新的声音混音器架构及部件
* Elementary 替换了许多内部部件
* 改进了 FreeBSD 支持
* Geolocation 模块


完整的更新日志 [在此](https://git.enlightenment.org/core/enlightenment.git/tree/NEWS?id=v0.20.0)。


### 下载




|  |  |
| --- | --- |
| **链接** | **SHA256** |
| [Enlightenment DR 0.20.0 GZIP](http://download.enlightenment.org/rel/apps/enlightenment/enlightenment-0.20.0.tar.gz) | 2e59533d5576e7c96a40af0885540aa0990b4a5a60b578cf990f6bc5daa365a9 |
| [Enlightenment DR 0.20.0 XZ](http://download.enlightenment.org/rel/apps/enlightenment/enlightenment-0.20.0.tar.xz) | bb5f257dc91f67f321c5960556e8c4029ce9a42aace3e3d4d880986d418d9157 |


### 构建和依赖


如果你已经安装了 EFL 和 Elementary，你也许应该在编译安装它们之前，删除它们的头文件和库文件，以避免出现编译冲突。请以下列顺序编译这些依赖：


1. [EFL](https://phab.enlightenment.org/diffusion/EFL) （[说明](https://git.enlightenment.org/core/efl.git/tree/README)）
2. [Elementary](https://phab.enlightenment.org/diffusion/ELM) （[说明](https://git.enlightenment.org/core/elementary.git/tree/README)）
3. [Emotion Generic Players](https://phab.enlightenment.org/diffusion/EGP) （[说明](https://git.enlightenment.org/core/emotion_generic_players.git/tree/README)）
4. [Evas Generic Loaders](https://phab.enlightenment.org/diffusion/EGL) （[说明](https://git.enlightenment.org/core/evas_generic_loaders.git/tree/README)）


**注意：** E20 依赖于 EFL **v1.15.2** 及更新版本来支持 X11 混合，如需要支持 Wayland 则需要1.16。
