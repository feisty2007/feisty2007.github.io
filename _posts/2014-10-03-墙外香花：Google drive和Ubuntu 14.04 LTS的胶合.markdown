---
layout: post
title:	"墙外香花：Google drive和Ubuntu 14.04 LTS的胶合"
date:	2014-10-07 21:38:00 +0800 
categories:	分享 linuxcn 
tags:	[linuxcn,Google Drive,grive]
---


Google尚未发布用于从Ubuntu访问其drive的**官方Linux客户端**。然开源社区却业已开发完毕非官方之软件包‘**grive-tools**’。


grive乃是Google Drive（**在线存储服务**）的GNU/Linux系统客户端，允许你**同步**所选目录到云端，以及上传新文件到Google Drive。


### grive-tools安装步骤


步骤：1 使用下列命令添加grive-tools PPA：



```
# sudo add-apt-repository ppa:thefanclub/grive-tools

```

步骤：2 更新列表



```
#sudo apt-get update

```

步骤：3 安装grive-tools



```
# sudo apt-get install grive-tools 

```

### 访问Google Drive的步骤


**步骤：1** 安装完了，通过输入**Grive**在**Unity Dash**搜索应用，并打开之。


![](/Asserts/Images//attachment/album/201410/07/213807pvg3rizifqf7xklv.jpg)


**步骤：2** 登入google drive，你将被问及访问google drive的权限。


![](/Asserts/Images//attachment/album/201410/07/213808tsxpi9fi0epq10o6.png)


点击**下一步**时，新的浏览器中讲打开**Google登录页**


登入你的Google帐号，并点击**接受**，如下所示：


![](/Asserts/Images//attachment/album/201410/07/213809m8j79zbzwsqbhbbf.png)


**步骤：3** 下面将提供给你一个 **google代码**，复制并粘贴到**Grive设置框**内。


![](/Asserts/Images//attachment/album/201410/07/213858pct6qp5463u3xtjp.jpg)


![](/Asserts/Images//attachment/album/201410/07/213908ntt6tbz5bt5gtigt.jpg)


点击下一步后，将会开始同步google drive到你**家目录**下的‘**Google Drive**’文件夹。完成后，将出现如下窗口。


![](/Asserts/Images//attachment/album/201410/07/213813l220zn2y9koosklx.png)


Google Drive 文件夹会创建在**用户的主目录**下。


![](/Asserts/Images//attachment/album/201410/07/213814msq8sqfjul1s9618.jpg)




---


via: <http://www.linuxtechi.com/mount-google-drive-in-ubuntu/>


作者：[Pradeep Kumar](http://www.linuxtechi.com/author/pradeep/)  译者：[GOLinux](https://github.com/GOLinux) 校对：[wxy](https://github.com/wxy)


本文由 [LCTT](https://github.com/LCTT/TranslateProject) 原创翻译，[Linux中国](http://linux.cn/) 荣誉推出
