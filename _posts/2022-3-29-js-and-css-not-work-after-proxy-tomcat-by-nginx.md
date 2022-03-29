---
layout:   post
title:    "解决nginx部署https后，原tomcat部署的javaweb项目http不能正常加载js、css资源问题"
crawlertitle: "解决nginx部署https后，原tomcat部署的javaweb项目http不能正常加载js、css资源问题"
description:  "解决nginx部署https后，原tomcat部署的javaweb项目http不能正常加载js、css资源问题"
summary:  "解决nginx部署https后，原tomcat部署的javaweb项目http不能正常加载js、css资源问题"
date: 2022-3-29 14:16:25
categories:   软件
tags: [软件]
author:   "feisty2007"
---


### 一、配置tomcat的server.xml文件

1、 修改1

	<Connector port="7080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="7443" 
			   proxyPort="443"/>//加一个proxyPort="443"代理端口

2、修改2
在host标签里加一句

	<Valve className="org.apache.catalina.valves.RemoteIpValve"  
				remoteIpHeader="X-Forwarded-For"  
				protocolHeader="X-Forwarded-Proto"  
				protocolHeaderHttpsValue="https"/>

### 二、修改nginx配置文件

		proxy_set_header Host      $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_redirect http:// $scheme://; #做https跳转
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	    proxy_set_header X-Forwarded-Proto  $scheme; #反向代理时透传给后端tomcat，用户使访问协议，tomcat后面也需要添加配置接收此参数
         client_max_body_size 100m;




