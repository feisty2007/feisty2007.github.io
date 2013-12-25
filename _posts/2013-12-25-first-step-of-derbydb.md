---
layout: post
title: "JAK Derby 初体验"
description: ""
category: blog 
tags: [Java,Derby]
---
{% include JB/setup %}




####前提

本文JDK的版本是1.7.0_05，在这个版本里面自带了Derby数据库，因此如果有一个可以运行的JDK就可以了。

在此之前，需要设置好一些java的运行变量，譬如JAVA_HOME等。

####Derby的位置

在我的Win7计算机里面，DerbyDB的位置在JAVA_HOME的db子目录下面。在这个目录里面有bin和lib目录。

bin里面是一些批处理文件。

lib里面是DerbyDB的jar文件。

####启动DerbyDB服务器

进入bin目录，运行startNetworkServer.bat，就可以启动数据库服务器了。

运行stopNetworkServer.bat关闭数据库。

####数据库交互

#####准备工作

DerbyDB里面有一个交互式的shell，名字叫ij，我们在这里可以运行它来对数据库进行一些操作。

在bin里面其实有ij.bat运行，我们这里为了演示，自己定义一个ij的运行。

首先，我们要自己定义一个数据库，名字叫CoreJava，然后里面建立一个数据表。

这里，建立2个文件，一个是数据库定义文件，名字叫corejava.properties:
    
      ij.driver=org.apache.derby.jdbc.ClientDriver
      ij.protocol=jdbc:derby://localhost:1527/
      ij.database=COREJAVA;create=true
  
第一行，定义jdbc驱动
第二行，说明DerbyDb的数据库服务器地址和端口
第三行，定义数据名称，create=true表示如果Database不存在，就建立一个

OK.利用上面的properties文件，我们来启动ij,为了以后启动方便，我们可以编写一个cmd文件：

    java -jar lib/derbyrun.jar ij -p corejava.properties
  
#####数据操作

运行上面的cmd文件，就进入了DerbyDB的交互Shell。
提示

    ij>
  
如果是第一次使用，可以输入help来看一下帮助。

    ij>help;
  
注意，别忘记了;,ij以这个来代表命令的结束。

好了。因为我们已经定义了Database的名字。如果没有定义，可以使用：

    CONNECT 'jdbc:derby://localhost:1527/corejava;create=true';
  
来定义。

现在就可以使用SQL语句了。

建立一个数据表：

    create table greetings (msg char(20));
  
插入一条记录：

    insert into greetings values ('hello,java!');
  
显示记录：

    select * from greetings
  

#####退出

在ij里面输入：

    ij>exit;
  
就会断开和数据库的连接。

####补充

更多资料，可以查看Apache的Derby站点的[文档](https://builds.apache.org/job/Derby-docs/lastSuccessfulBuild/artifact/trunk/out/getstart/index.html)。

  

