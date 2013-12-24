---
layout: post
title: "install canon iR2320 under ubuntu 12.04 LTS"
title: "在Ubuntu 12.04下面安装Canon iR2320一体机"
description: ""
category: blog
tags: [ubuntu,iR2320]
---
{% include JB/setup %}


###下载驱动

从[Canon iR2320驱动页面](http://support-cn.canon-asia.com/P/ZH/search?category=%E5%A4%8D%E5%90%88%E6%9C%BA&series=%E9%BB%91%E7%99%BD%E6%95%B0%E7%A0%81%E4%BD%8E%E9%80%9F%E5%A4%8D%E5%90%88%E6%9C%BA&model=iR+2320L&menu=Download&filter=0)下载Linux版本的驱动程序

### 安装

运行Debian下面的Deb文件

### 命令行配置

	/usr/sbin/lpadmin -p CANON-iR2320 -m CNCUPSIR2320ZK.ppd -v lpd://10.10.4.252/CANON-iR2420 -E

###打印测试成功
