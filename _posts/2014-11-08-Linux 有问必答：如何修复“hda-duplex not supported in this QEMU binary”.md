---
layout: post
title:	"Linux 有问必答：如何修复“hda-duplex not supported in this QEMU binary”"
date:	2014-11-25 22:30:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,virt-manager,virsh,声卡]
---



> 
> **提问**： 当我尝试在虚拟机中安装一个新的Linux时，虚拟机不能启动且报了下面这个错误："unsupported configuration: hda-duplex not supported in this QEMU binary."（“不支持的配置：hda-duplex在此QEMU文件中不支持。”） 我该如何修复？
> 
> 
> 


![](/Asserts/Images/album/201411/25/223052khxxx0f96lolxumr.png)


这个错误可能来自一个当默认声卡型号不能被识别时的一个qemu bug。


![](/Asserts/Images/album/201411/25/223055ot43juu06j4u6ho8.png)



```
无法完成安装：‘不支持的配置：hda-duplex在此QEMU文件中不支持’

```

要解决这个问题，按照下面的做。


### 方案一: virt-manager


在**virt-manager**中，打开虚拟机的虚拟硬件详细菜单，进入声卡选项，改变默认的设备型号为ac97。


![](/Asserts/Images/album/201411/25/223057s8p1xllz8zsh16x7.jpg)


点击“应用”按钮并保存设置。看一下虚拟机现在是否可以启动了。


### 方案二: Virsh


如果你使用的是**virsh** 而不是**virt-manager**， 你可以编辑VM相应的配置文件。在节点中查找**sound**节点，并按照下面的默认声卡型号改成**ac97**。



```
<devices>
  . . .
  <sound model='ac97'>
    <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
  </sound>
  . . .
</device>

```



---


via: <http://ask.xmodulo.com/hda-duplex-not-supported-in-this-qemu-binary.html>


译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
