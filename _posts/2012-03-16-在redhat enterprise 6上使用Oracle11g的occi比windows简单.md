---
layout: post
title:	"在redhat enterprise 6上使用Oracle11g的occi比windows简单"
date:	2012-03-31 08:42:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,redhat,oracle,occi,windows]
---


 在redhat enterprise 6 上安装了Oracle11g后，使用occi编程比windows里使用visual studio.net 里使用occi简单得多


1）在oracle官网下载instantclient\_11\_2 把那个sdk也下载了解压到这个文件夹中


2）进入instantclient\_11\_2 进行：ln -sf libclntsh.so.11.1 libclntsh.so ln -sf libocci.so.11.1 libocci.so


3) 把$ORACLE\_HOME/network/admin/下的文件拷贝到instantclient\_11\_2中


4)配置环境变量，编辑.bash\_profile加上


export ORACLE\_HOME=$ORACLE\_HOME:/instantclient\_11\_2


export LD\_LIBRARY\_PATH=/instantclient\_11\_2:$LD\_LIBRARY\_PATH


export TNS\_ADMIN=/instantclient\_11\_2


 在编译你的occi程序时：


g++ -I /instantclient\_11\_2/sdk/include -L /instantclient\_11\_2 yourocci.cxx -locci -lclntsh -o yourocci
