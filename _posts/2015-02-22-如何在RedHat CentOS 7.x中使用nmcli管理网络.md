---
layout: post
title:	"如何在RedHat/CentOS 7.x中使用nmcli管理网络"
date:	2015-02-23 09:51:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,nmcli,NetworkManager]
---


[**Red Hat Enterprise Linux 7**](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/7.0_Release_Notes/)和**CentOS 7**的一个新特性是默认的网络服务由**NetworkManager**提供，这是一个动态的网络控制和配置守护进程，它在网络设备和连接可用时保持链接正常，同时也提供了典型的ifcfg类型的配置文件。NetworkManager可以用于下面这些连接：Ethernet、 VLANs、桥接、Bonds、Teams、 Wi-Fi、 移动宽带 (比如 3G)和IP-over-InfiniBand(IPoIB)。


NetworkManager可以由命令行工具**nmcli**控制。


![](/Asserts/Images/album/201502/22/220239kpgjgdipg2np3p32.png)


### nmcli的通常用法


nmcli的通常语法是：



```
# nmcli [ OPTIONS ] OBJECT { COMMAND | help }

```

一件很酷的事情是你可以使用tab键来补全操作，这样你在何时忘记了语法你都可以按下tab来看到可用的选项了。


![nmcli tab](/Asserts/Images/album/201502/22/220243z4qzyhe22gfr4elf.jpg)


nmcli通常用法的一些例子：



```
# nmcli general status

```

会显示NetworkManager的整体状态。



```
# nmcli connection show

```

会显示所有的连接



```
# nmcli connection show -a

```

仅显示活跃的连接



```
# nmcli device status

```

显示NetworkManager识别的设备列表和它们当前的状态。


![nmcli general](/Asserts/Images/album/201502/22/220245tysrpteu7ypu0c3t.jpg)


### 启动/停止网络设备


你可以使用nmcli从命令行启动或者停止网络设备，这等同于ifconfig中的up和down。


停止网络设备使用下面的语法：



```
# nmcli device disconnect eno16777736

```

要启动它使用下面的语法：



```
# nmcli device connect eno16777736

```

### 添加一个使用静态IP的以太网连接


要用静态IP添加一个以太网连接可以使用下面的命令：



```
# nmcli connection add type ethernet con-name NAME_OF_CONNECTION ifname INTERFACE-NAME ip4 IP_ADDRESS gw4 GW_ADDRESS

```

将NAME*OF*CONNECTION替换成新的连接名（LCTT 译注：这个名字以后可以用来对其操作，可以使用任何简单明了的名称），INTERFACE-NAME 替换成你的接口名，IP*ADDRESS替换成你要的IP地址，GW*ADDRESS替换成你使用的网关地址（如果你并不使用网关，你可以忽略这部分）。



```
# nmcli connection add type ethernet con-name NEW_STATIC ifname eno16777736 ip4 192.168.1.141 gw4 192.168.1.1

```

要设置这个连接所使用的DNS服务器使用下面的命令：



```
# nmcli connection modify NEW_STATIC ipv4.dns "8.8.8.8 8.8.4.4"

```

要启用新的以太网连接，使用下面的命令：



```
# nmcli connection up NEW_STATIC ifname eno16777736

```

要查看新配置连接的详细信息，使用下面的命令：



```
# nmcli -p connection show NEW_STATIC

```

![nmcli add static](/Asserts/Images/album/201502/22/220246b3wcgjuqmgtkqxcu.jpg)


### 添加一个使用DHCP的连接


如果你想要添加一个使用DHCP来配置接口IP地址、网关地址和dns服务器地址的新的连接，你要做的就是忽略上述命令中的ip/gw部分，NetworkManager会自动使用DHCP来获取配置细节。


比如，要创建一个新的叫NEW\_DHCP的DHCP连接，在设备eno16777736上你可以使用下面的命令：



```
# nmcli connection add type ethernet con-name NEW_DHCP ifname eno16777736

```



---


via: <http://linoxide.com/linux-command/nmcli-tool-red-hat-centos-7/>


作者：[Adrian Dinu](http://linoxide.com/author/adriand/) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
