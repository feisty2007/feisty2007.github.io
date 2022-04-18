---
layout:   post
title:    "U8Debug打开"
crawlertitle: "U8Debug打开"
description:  "U8Debug打开"
summary:  "U8Debug打开"
date: 2022-4-18 10:35:20
categories:   软件
tags: [软件]
author:   "feisty2007"
---

1、log4net

U8使用log4net作为日志工具，请打开相关设置！

门户在EnterprisePort.exe.config里面，需要把：

	<root>
      <level value="DEBUG"/>
      <appender-ref ref="LogFileAppender"/>
    </root>

把value改成DEBUG,默认为error。

具体模块需要设置不同xml文件。

		U8MPool.exe.config-生产模块
		U8SCMPool.exe.config-进出口模块

2、打开U8M（生产模块的配置文件）\U8M\U8M_Objects_App.Client，

	<object id="RuntimeConfigProvider" type="UFSoft.U8.U8M.Base.ObjectImpl.RuntimeConfigProvider,UFSoft.U8.U8M.Base.ObjectImpl" singleton="true" lazy-init="true">
	<property name="Configuration">
      <dictionary key-type="string" value-type="string">
        <entry key="Assembly_SqlCmdCollection" value="UFSoft.U8.U8M.SQLCmdCollection"/>
        <entry key="Assembly_DefaultSqlCmdNameSpace" value="UFSoft.U8.U8M.SQLCmdCollection"/>
        <entry key="Assembly_BESchema" value="UFSoft.U8.U8M.BESchema"/>
        <entry key="Assembly_UIPSchema" value="UFSoft.U8.U8M.UIP.Schema"/>
        <entry key="XmlFile_BFConfig" value="UFSoft.U8.BusinnessComponents.Services.Config.xml"/>
      	<entry key="ShowException" value="false"/>
        <entry key="ReferenceCheck" value="false"/>
        <entry key="UIPTaskRecord" value="false"/>
        <entry key="DTFDataXmlLog" value="false"/>
        <entry key="BizNotifyEnabled" value="true"/>
      </dictionary>
    </property>
	</object>
	
	
特别注意：

	<entry key="ShowException" value="false"/>

把**value**改**true**，U8就会显示c#的具体error！，比较直观！

3、U8 sql跟踪器名称

在ApplicationName设置为

	U8M%

里面会有

	U8M.Server 服务器执行脚本
	U8M.Client 客户端执行Sql

开始即可，比较直观！


