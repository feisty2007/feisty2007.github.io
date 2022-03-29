---
layout:   post
title:    "Mysql5-7root不能登录"
crawlertitle: "Mysql5-7root不能登录"
description:  "Mysql5-7root不能登录"
summary:  "Mysql5-7root不能登录"
date: 2022-3-29 14:33:4
categories:   软件
tags: [软件]
author:   "feisty2007"
---


### 起因

最近需要登录root账号，来修改一个账号的权限。

结果提示“Access dined root@localhost”.

开始以为密码不正确。

于是，开始重置密码。

### 重置mysql5.7 root密码 步骤

1、停止mysql

	sudo service mysql stop

2、修改m/etc/mysql/mysql.conf.d下面的my.cnf,增加下面语句

	 skip-grant-tables

3、重启mysql

	sudo service mysql restart

4、登录mysql

	mysql -u root

这样就无密码进入mysql，可以修改root密码了。

进行下面操作：

	use mysql;

	select host,user,authentication_string from user;

	update user set authentication_string = password('123456') where user = 'root';

5、注释掉my.cnf里面的skip-grant-tables语句

6、重启mysql

	sudo service mysql restart

### 依然不行的解决方法

这个时候，其实是Ubuntu里面mysql设置造成的。

Ubuntu里面，mysql的root用户默认认证方式-auth_socket.

它特点如下：

发现这种验证方式有以下特点：

	1、首先，这种验证方式不要求输入密码，即使输入了密码也不验证。这个特点让很多人觉得很不安全，实际仔细研究一下这种方式，发现还是相当安全的，因为它有另外两个限制；
	2、只能用 UNIX 的 socket 方式登陆，这就保证了只能本地登陆，用户在使用这种登陆方式时已经通过了操作系统的安全验证；
	3、操作系统的用户和 MySQL 数据库的用户名必须一致，例如你要登陆 MySQL 的 root 用户，必须用操作系统的 root用户登陆。

auth_socket 这个插件因为有这些特点，它很适合我们在系统投产前进行安装调试的时候使用，而且也有相当的安全性，因为系统投产前通常经常同时使用操作系统的 root 用户和 MySQL 的 root 用户。

当我们在系统投产后，操作系统的 root 用户和 MySQL 的 root 用户就不能随便使用了，

下面我们再次进入"skip-grant-tables"模式，切换一下root的验证方法：

	use mysql;

	select plugin from user where user='root'; #如果提示是auth_socket，就需要修改

	update user set plugin="mysql_native_password" where user='root';

至此，你的root账号应该可以登录！


