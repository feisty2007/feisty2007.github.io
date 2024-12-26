---
layout: post
title:	"Red Hat Enterprise Linux 7.4"
date:	2016-12-27 08:43:00 +0800 
categories:	Linux 发行版 linuxcn 
tags:	[linuxcn,Linux,发行版,RHEL,CentOS]
---


![](/Asserts/Images//attachment/album/201407/09/100614ja4za9oppkot39vt.png)


### 简介


Red Hat Enterprise Linux 是 Red Hat 公司的 Linux 发行版，面向商业市场，包括大型机。红帽公司从 Red Hat Enterprise Linux 5 开始对企业版 Linux 的每个版本提供 10 年的支持。而 Red Hat Enterprise Linux 常简称为 RHEL。


Red Hat Enterprise Linux 大约 3 年发布一个新版本。


### 下载


RHEL 是商业版本，并不提供免费下载和使用。需要购买 Red Hat 公司的商业服务才能合法取得，并得到商业支持。


可以使用 RHEL 的开源衍生版本来取得除了商业支持之外一样的软件，比如：CentOS。


### 安装


* [RHEL 7.3 安装指南](/article-8067-1.html)


### 发行


最初，Red Hat Enterprise Linux 基于 Red Hat Linux，但使用较为保守的发布周期。后来版本都是基于 Fedora。大约每六个版本的 Fedora 会有一个新版本的 Red Hat Enterprise Linux 发布，因此：


* Red Hat Linux 6.2 → Red Hat Linux 6.2E
* Red Hat Linux 7.2 → Red Hat Enterprise Linux 2.1
* Red Hat Linux 9 → Red Hat Enterprise Linux 3
* Fedora Core 3 → Red Hat Enterprise Linux 4
* Fedora Core 6 → Red Hat Enterprise Linux 5
* Fedora 12 → Red Hat Enterprise Linux 6
* Fedora 19 → Red Hat Enterprise Linux 7


### 当前版本


* Red Hat Enterprise Linux 当前的最新版本是 7.4。
* Red Hat Enterprise Linux 7 当前仅支持 64 位CPU：64-bit AMD、64-bit Intel、IBM POWER7 和 POWER8、IBM System z。可以将32位操作系统作为虚拟机运行，包括之前的RHEL版本。
* 包含 Kernel 3.10 版本，支持 swap 内存压缩可保证显著减少 I/O 并提高性能，采用 NUMA (统一内存访问) 的调度和内存分配，支持 APIC (高级程序中断控制器) 虚拟化，全面的 DynTick 支持，将内核模块列入 黑名单，kpatch 动态内核补丁 (技术预览) 等等。
* 存储和文件系统方面，RHEL 7.0 使用 LIO 内核目标子系统，支持快速设备为较慢的块设备提供缓存，引进了 LVM 缓存 (技术预览)，将 XFS 作 为默认的文件系统。
* 引进网络分组技术作为链路聚集的捆绑备用方法，对 NetworkManager 进行大量改进，提供动态防火墙守护进程 firewalld，加入 DNSSEC 域名系统安全扩展，附带 OpenLMI 用来管理 Linux 系统提供常用的基础 设施，引进了可信网络连接功能 (技术预览)等。
* 对 KVM (基于内核的虚拟化) 提供了大量改进，诸如使用 virtio-blk-data-plane 提高快 I/O性能 (技术预览)，支持 PCI 桥接，QEMU 沙箱，多队列 NIC， USB 3.0 支持 (技术预览) 等。
* 引入 Linux 容器 Docker。
* 编译工具链方面，RHEL 7.0 包含 GCC 4.8.x、glibc 2.17、GDB 7.6.1。
* 包含 Ruby 2.0.0、Python 2.7.5、Java 7 等编程语言。
* 包含 Apache 2.4、MariaDB 5.5、PostgreSQL 9.2 等。
* 在系统和服务上，RHEL 7.0 使用 systemd 替换了 SysV。
* 引入 Pacemaker 集群管理器，同时使用 keepalived 和 HAProxy 替换了负载均衡程序 Piranha。
* 此外，还对安装程序 Anaconda 进行了重新设计和增强，并使用 引导装载程序 GRUB 2。


### 历史


![](/Asserts/Images//attachment/album/201712/14/155511uct53mc0n8mxtpc8.png)


#### 派生版本


派生版本有 CentOS，Scientific Linux 及 Oracle Linux 等。


各版本比较：




|  |  |  |  |
| --- | --- | --- | --- |
|  | 免费下载 | 免费使用 | 技术支持 (商业) |
| RHEL | 否 | 否 | 付费 |
| CentOS | 是 | 是 | 不提供 |
| Scientific Linux | 是 | 是 | 不提供 |
| Oracle Linux | 要求简单登记 | 是 | 付费 |


注：部分资料来自维基百科。
