---
layout: post
title:	"如何在 WinSCP 中使用 sudo"
date:	2019-03-13 11:54:00 +0800 
categories:	技术 linuxcn 
tags:	[linuxcn,sudo,WinSCP]
---



> 
> 用截图了解如何在 WinSCP 中使用 sudo。
> 
> 
> 


![](/Asserts/Images//attachment/album/201903/13/115351nqxhm7qzq9zjecbv.png)


首先你需要检查你尝试使用 WinSCP 连接的 sftp 服务器的二进制文件的位置。


你可以使用以下命令检查 SFTP 服务器二进制文件位置：



```
[root@kerneltalks ~]# cat /etc/ssh/sshd_config |grep -i sftp-server
Subsystem sftp  /usr/libexec/openssh/sftp-server
```

你可以看到 sftp 服务器的二进制文件位于 `/usr/libexec/openssh/sftp-server`。


打开 WinSCP 并单击“高级”按钮打开高级设置。


![winSCP advance settings](/Asserts/Images//attachment/album/201903/13/115407mke8dkgizngtrd6h.jpg)


*WinSCP 高级设置*


它将打开如下高级设置窗口。在左侧面板上选择“Environment”下的 “SFTP”。你会在右侧看到选项。


现在，使用命令 `sudo su -c` 在这里添加 SFTP 服务器值，如下截图所示：


![SFTP server setting in winSCP](/Asserts/Images//attachment/album/201903/13/115409bw7tzrsvjl9s0spz.jpg)


*WinSCP 中的 SFTP 服务器设置*


所以我们在设置中添加了 `sudo su -c /usr/libexec/openssh/sftp-server`。单击“Ok”并像平常一样连接到服务器。


连接之后，你将可以从你以前需要 sudo 权限的目录传输文件了。


完成了！你已经使用 WinSCP 使用 sudo 登录服务器了。




---


via: <https://kerneltalks.com/tools/how-to-use-sudo-access-in-winscp/>


作者：[kerneltalks](https://kerneltalks.com) 选题：[lujun9972](https://github.com/lujun9972) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创编译，[Linux中国](https://linux.cn/) 荣誉推出
