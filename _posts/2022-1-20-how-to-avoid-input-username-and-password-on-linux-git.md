---
layout:   post
title:    "Linux系统使用git，如何避免每次都需要输入用户名和秘密"
crawlertitle: "Linux系统使用git，如何避免每次都需要输入用户名和秘密"
description:  "Linux系统使用git，如何避免每次都需要输入用户名和秘密"
summary:  "Linux系统使用git，如何避免每次都需要输入用户名和秘密"
date: 2022-1-20 11:35:19
categories:   软件
tags: [软件]
author:   "feisty2007"
---

### 现状

最近在Linux上面工作，发现一个比较麻烦的情况。在推送代码给git的时候，需要输入用户名和密码。

在Windows下面，只需要一次就够了，以后就不需要继续输入了！

但是，在Linux上面，似乎不会缓存git账户信息。


### 怎么做

#### 在linux上面产生ssh密钥文件

>ssh-keygen -t ed25519 -C "your_email@example.com"

邮件地址，就是git的默认邮箱。

如果想不起来，可以查看home目录下面的.gitconfig文件。

ed25519是一种加密算法，它的特点是非常快，用在验证上面是非常好的。

执行上面的命令，一路回车就可以了。

在我的电脑上面，产生的文件在home的.ssh目录下面，有2个：

1. y
2. y.pub

pub是公钥文件，你需要拷贝其内容到github上面。


#### 上传密钥到github

找到settings，然后是SSH and GPG Keys，添加一下，就可以了。

可以使用下面的命令进行测试：

> ssh -v git@github.com

如果提示successful，就表示成功了！

#### 使用ssh方式下载git

然后在“git clone"阶段，请不要使用https这种形式，而是需要ssh方式。

### 测试一下

你会发现，现在无需密码，就可以进行推送密码了


