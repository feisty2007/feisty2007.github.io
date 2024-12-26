---
layout: post
title:	"如何让 Linux 机器加入 Windows 的 AD 域"
date:	2016-08-19 08:43:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,活动目录]
---


对于帐户统一管理系统或软件来说，在 Linux 下你可能知道 NIS、OpenLDAP、samba 或者是 RedHat、IBM 的产品，在 Windows 下当然就是最出名的<ruby> 活动目录 <rp>  （ </rp> <rt>  Active Directory </rt> <rp>  ） </rp></ruby>（AD）了，这里就来探讨一下如何让 Linux 的计算机加入 AD 域。


![](/Asserts/Images/album/201608/18/220956ztyx4r8o0706jr06.jpg)


首先，先简单介绍一下 AD 域。自 Windows 2000 以来，AD 一直是 Windows 的身份验证和目录服务，AD 基于 LDAP 实现其功能，其使用 DNS 进行主机名的解析，使用 Kerberos V5 进行用户身份验证，使用 LDAP V3 进行统一的帐户管理。


目标：在 AD 域中，将 Linux 服务器加入 AD，以使 Domain Admins 用户组成员可以登录操作 Linux 服务器，不需要在 Linux 服务器中单独创建帐户。


环境：一台 Windows Server 2012 R2 操作系统的服务器，安装有 AD 并作为<ruby> 域控制器 <rp>  （ </rp> <rt>  Domain Controller </rt> <rp>  ） </rp></ruby>（DC），同时也作为 DNS 服务器和时间服务器；一台 RedHat Enterprise Linux 6.x 的服务器，请自行配置好网络及 YUM 源。有关 AD 域服务器的搭建，由于比较简单，请自行查阅资料完成，这里不再详述。


这里以 Windows 服务器地址为 192.168.2.122，域名为 contoso.com，主机名为 ad.contoso.com；Linux 服务器地址为 192.168.2.150，主机名为 lemon20.contoso.com。


**1、安装所需软件：**



```
# yum -y install samba samba-client samba-common samba-winbind samba-winbind-clients krb5-workstation ntpdate
```

**2、设置服务自启动并启动服务：**



```
# chkconfig smb on
# chkconfig winbind on
# service smb start
# service winbind start
```

**3、修改 /etc/hosts 文件，添加主机对应记录：**



```
127.0.0.1 localhost localhost.localdomain localhost4 localhost4.localdomain4
::1 localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.2.150 lemon20.contoso.com lemon20
```

**4、设置 DNS 地址并与 AD 服务器同步时间：**



```
# echo "nameserver 192.168.2.122" >> /etc/resolv.conf
# ntpdate ad.contoso.com
```

**5、设置 Kerberos 票据（可选）：**


销毁已经存在的所有票据：



```
# kdestroy
```

查看当前是否还存在票据：



```
# klist                           
klist: No credentials cache found (ticket cache FILE:/tmp/krb5cc_0)  

```

生成新的票据，注意域名大写。



```
# kinit administrator@CONTOSO.COM
# klist
Ticket cache: FILE:/tmp/krb5cc_0
Default principal: administrator@CONTOSO.COM
Valid starting     Expires            Service principal
08/02/16 22:35:26  08/03/16 08:35:29  krbtgt/CONTOSO.COM@CONTOSO.COM
renew until 08/09/16 22:35:26
```

**6、以命令方式设置 samba 与 Kerberos，并加入 AD 域：**



```
#authconfig --enablewinbind  --enablewins --enablewinbindauth --smbsecurity ads --smbworkgroup=CONTOSO --smbrealm CONTOSO.COM --smbservers=ad.contoso.com --enablekrb5 --krb5realm=CONTOSO.COM --krb5kdc=ad.contoso.com --krb5adminserver=ad.contoso.com --enablekrb5kdcdns --enablekrb5realmdns --enablewinbindoffline --winbindtemplateshell=/bin/bash --winbindjoin=administrator --update --enablelocauthorize --enablemkhomedir --enablewinbindusedefaultdomain
```

注意命令中的大小写，此步骤也可以使用 authconfig-tui 完成。


**7、增加 sudo 权限（可选）：**



```
# visudo
```

加入下列设置：



```
%MYDOMAIN\\domain\ admins ALL=(ALL)  NOPASSWD: ALL
```

**8、确认是否正确加入 AD 域：**


查看 AD 的相关信息



```
# net ads info  

```

查看 MYDOMAIN\USERID 的使用者帐户



```
# wbinfo -u 
```

**补充：**


如果启用 selinux 的话，需要安装 oddjobmkhomedir 并启动其服务，这样才能确保系统对创建的家目录设置合适的 SELinux 安全上下文。
