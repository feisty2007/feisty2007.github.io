---
layout: post
title:	"如何在 vmware esxi 5.5 中开放 VNC 端口"
date:	2015-06-17 20:59:00 +0800 
categories:	系统运维 linuxcn 
tags:	[linuxcn,VNC]
---


![](/Asserts/Images//attachment/album/201506/18/154855fksg81zozwcpwoph.png)


1、编辑/etc/vmware/firewall/service.xml 



```
vi /etc/vmware/firewall/service.xml 
```

2、在该文件重中倒数第二行开始添加以下内容：



```
<!-- Firewall configuration information for VNC --> 
<service id='0040'>
    <id>VNC</id>
    <rule id='0000'>
      <direction>inbound</direction>
      <protocol>tcp</protocol>
      <porttype>dst</porttype>
      <port>
        <begin>40000</begin>
        <end>60000</end>
      </port>
    </rule>
    <enabled>true</enabled>
    <required>false</required>
 </service> 
```

3、执行以下命令以使配置文件生效：



```
esxcli network firewall refresh
```

4、查看是否已经生效：



```
esxcli network firewall ruleset list | grep VNC
VNC                  true
```
