---
layout: post
title:	"如何在Docker容器中运行GUI程序"
date:	2015-04-20 08:10:00 +0800 
categories:	容器与云 linuxcn 
tags:	[linuxcn,Docker,GUI]
---


各位，今天我们将学习如何在[Docker](http://docker.io/)之中运行GUI程序。我们可以轻易地在Docker容器中运行大多数GUI程序且不出错。Docker是一个开源项目，提供了一个打包、分发和运行任意程序的轻量级容器的开放平台。它没有语言支持、框架或者打包系统的限制，并可以运行在任何地方、任何时候，从小型的家用电脑到高端的服务器都可以运行。这让人们可以打包不同的包用于部署和扩展网络应用，数据库和后端服务而不必依赖于特定的栈或者提供商。


![](/Asserts/Images//attachment/album/201504/18/232858p2oz2upa22bpwa22.jpg)


下面是我们该如何在Docker容器中运行GUI程序的简单步骤。本教程中，我们会用Firefox作为例子。


### 1. 安装 Docker


在开始前，我们首先得确保在Linux主机中已经安装了Docker。这里，我运行的是CentOS 7 主机，我们将运行yum管理器和下面的命令来安装Docker。



```
# yum install docker

```

![](/Asserts/Images//attachment/album/201504/18/232901gojxj1juj5ayuvft.png)



```
# systemctl restart docker.service

```

### 2. 创建 Dockerfile


现在，Docker守护进程已经在运行中了，我们现在准备创建自己的Firefox Docker容器。我们要创建一个Dockerfile，在其中我们要输入需要的配置来创建一个可以工作的Firefox容器。为了运行 Docker 镜像我们需要使用最新版本的CentOS。要创建 Docker 镜像，我们需要用文本编辑器创建一个名为Dockerfile的文件。



```
# nano Dockerfile

```

接着，在Dockerfile中添加下面的行并保存。



```
#!/bin/bash
FROM centos:7
RUN yum install -y firefox
# 用你自己的 uid /gid 替换下面的0
RUN export uid=0 gid=0
RUN mkdir -p /home/developer
RUN echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd
RUN echo "developer:x:${uid}:" >> /etc/group
RUN echo "developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN chmod 0440 /etc/sudoers
RUN chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer
CMD /usr/bin/firefox

```

![](/Asserts/Images//attachment/album/201504/18/232902cstspczpmq4lssls.png)


**注意：在第四行的配置中，用你自己的用户和组id来替换0。 我们可以用下面的命令在shell或者终端中得到uid和gid。**



```
#  id $USER

```

![](/Asserts/Images//attachment/album/201504/18/232902nggp9cwomzg97un7.png)


### 3. 构造Docker容器


下面我们就要根据上面的Dockerfile构建一个容器。它会安装firefox浏览器和它需要的包。它接着会设置用户权限并让它可以工作。这里镜像名是firefox，你可以根据你的需要命名。



```
# docker build --rm -t firefox .

```

![](/Asserts/Images//attachment/album/201504/18/232903omy6qvvfqaamh5a1.png)


### 4. 运行Docker容器


现在，如果一切顺利，我们现在可以在运行在CentOS 7镜像中的Docker容器里面运行我们的GUI程序也就是Firefox浏览器了。



```
# docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix firefox

```

### 总结


在Docker容器中运行GUI程序是一次很棒的体验，它对你的主机文件系统没有任何的伤害。它完全依赖你的Docker容器。本教程中，我尝试了CentOS 7 Docker中的Firefox。我们可以用这个技术尝试更多的GUI程序。如果你有任何问题、建议、反馈请在下面的评论栏中写下来，这样我们可以提升或更新我们的内容。谢谢！




---


via: <http://linoxide.com/linux-how-to/run-gui-apps-docker-container/>


作者：[Arun Pyasi](http://linoxide.com/author/arunp/) 译者：[geekpi](https://github.com/geekpi) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
