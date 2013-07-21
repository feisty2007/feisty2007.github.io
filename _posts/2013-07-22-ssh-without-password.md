---
layout: post
title: "ssh登陆，避免重复输入密码"
description: "利用ssh-keygen产生远程登陆秘钥"
category: blog 
tags: [ssh]
---
{% include JB/setup %}

###产生本地秘钥文件

ssh-keygen -t rsa

根据提示，输入远程密码。

在.ssh/目录下面产生2个文件

+ id_rsa
+ id_rsa.pub

现在需要做的就是把pub文件拷贝到服务器上面。

###拷贝到服务器

这里设定下，remote_user表示远程用户名，remote_host代表远处主机。

先登陆下远程主机，看一下.ssh目录是否存在：
    
    ssh remote_user@remote_host
    输入密码
    mkdir .ssh
    
不管怎样，.ssh目录存在了。

现在拷贝：

    cd .ssh
    scp id_rsa.pub remote_user@remote_host：～/.ssh/
    
###服务器最后修改

登陆远程服务器

    ssh remote_user@remote_host
    cd .ssh    
    cat id_rsa.pub >> authorirzed_keys
    
###完成

OK，现在登陆，应该不需要密码了。
尝试一下：

    ssh remote_user@remote_host
    
如果不需要输入密码，应该是成功了！
