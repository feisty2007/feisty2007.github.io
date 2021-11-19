---
layout:   post
title:    "MRBS会议室预定系统添加新会议类型步骤"
crawlertitle: "MRBS会议室预定系统添加新会议类型步骤"
description:  "MRBS会议室预定系统添加新会议类型步骤"
summary:  "MRBS会议室预定系统添加新会议类型步骤"
date: 2021-11-19 9:26:44
categories:   软件
tags: [软件]
author:   "feisty2007"
---

### 1、添加类别代号，

**类别代号**，这个是mrbs里面特有的一个定义。这可能有点绕口，那我们来实际说一下。

默认情况，mrbs有2个类别代号，分别是
> I -  内部会议
E – 外部会议

另外mrbs还定义了很多这种单字母类别的类别，分别为A、B、C，并在这些类别代号的基础上可以定义类别的显示名称和显示颜色。

回到主题，在systemdefaults.inc.php里面可以添加，具体位置见截图：
![](/assets/images/2021-11-19-1e6263a2-f63f-4b27-ad17-0036781a1dc8.png)

在1143行处可以增加自定义类型，譬如：
$booking_types[]=”A“

在1145处可以定义默认类型。

### 2、定义显示名称

这个可以在mrbs的语言文件里面定义。我们的语言设置是zh_CN,就可以在”Lang/lang.zh_CN”文件里面添加，看看截图：
![](/assets/images/2021-11-19-e82894b1-0fce-4655-9f4d-90a8453e800b.png)
这里，我们可以给A类型，添加一行：
$vocab[“type.A”] = “一级会议”

### 3、给类型统计自定义颜色

这类，在“Themes/default/styling.inc”里面更改，看看这个文件里面已有的截图：
![](/assets/images/2021-11-19-1dafceb6-792c-44c2-89da-b83ae2a89531.png)

这里定义了一个字典，在这里可以定制颜色。譬如“A”的颜色代码是“#ffff99”，这个地方还可以更改！

### 4、至此，一个自定义类型就会出现在主界面和会议预定编辑界面。

如果想自定义的类型的最大时长或者限定时间，可以在edit_entry.php里面的form里面的onsubmit事件里面添加自定义JS代码，如果达不到指定条件，相关操作就无法进行。


另外需要注意的一点是需要有一个EnableSubmitButton的函数，因为mrbs默认提交以后那些submit button是禁用的，因此为了方便修改，我设定了一个1秒以后的启用submit button操作。


