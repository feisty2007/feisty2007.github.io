---
layout: post
title:	"微软发布 Linux 下的 SQL Server 公众预览版"
date:	2016-11-17 21:33:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,微软,数据库,SQL Server]
---


微软发布了它的下一个版本的 SQL Server 数据库的公众预览版，同时支持 Linux 和 Windows。


![](/Asserts/Images//attachment/album/201611/17/213226blpr367yaaafzaaw.jpg)


在今年 3 月，微软发布过 SQL Server for Linux 的一个[内部预览版](/article-7082-1.html)。同时，微软官方说 SQL Server for Linux 是 SQL Server for Windows 版本的一个子集，将可以运行在 Ubuntu 上或作为 Docker 镜像运行（后来补充说内部预览也支持 Red Hat 的 RHEL）。该公司官方称用户购买的 SQL Server 将可以用在 Windows 服务器或 Linux 上，此后不久还说该版本的 SQL Server for Linux 和 for Windows 实际上是同一个。 


不过，就在今天（美国时间 11 月 16 日），微软将 SQL Server Next 定位为既可以运行在 Linux ，也可以运行在 Windows 上的一个产品。


微软官方称，运行在 Linux 上和运行在 Windows 上的 SQL Server Next 基于同一份代码基，“有些功能存在平台差异，比如说 Linux 上的文件路径不同于 Windows”，但是这不是两个完全不同的产品。运行在 Linux 上的 SQL Server Next 拥有“关系型数据库引擎的所有主要功能”，这包括堆内在线事务处理（OLTP）、堆内列存储、透明数据加密、全程加密、行级安全等等。


SQL Server for Linux 的公众预览版支持 Ubuntu、Red Hat 的 RHEL、SUSE 的 SLES，也将很快出现在 Azure 虚拟机中和 [Docker Hub](http://hub.docker.com/r/microsoft/mssql-server-linux) 上。不过，微软依旧说，支持 Linux 和 Windows 的 SQL Server 的正式版仍然会要到明年中期才能发布。


Linux 下的 SQL Server 公众预览版可以从微软的 [SQL Server on Linux 网站](https://www.microsoft.com/en-us/sql-server/sql-server-vnext-including-Linux)上下载到。 


众所周知，使用开源软件的公司不会将其自由而强大的 MariaDB 或 MySQL 数据库方案用 SQL Server 来替代，但是微软的 SQL Server 承诺支持 Docker 容器，并允许选择数据类型和开发语言，对于某些场景来说，使用 SQL Server 可以节省成本，提升性能，并增强灵活性。在今年 3 月份发布内部预览版之后，微软宣布有超过 8000 家公司已经在第一周内注册尝试了 SQL Server for Linux，其中位列财富 500 强里的公司超过一半都参与了试用。
