---
layout:   post
title:    "近期注意事项"
crawlertitle: "近期注意事项"
description:  "近期注意事项"
summary:  "近期注意事项"
date: 2021-12-30 16:27:29
categories:   软件
tags: [软件]
author:   "feisty2007"
---

### Elment UI

组件使用的使用，不要使用</>的样式，譬如<el-table-column />,这样容易导致组件无法渲染

### Asp.net Core 3.1

下面这些配置：

	app.useAuthorization()
	app.useCORS()

应该在app.UseEndPoints函数前面，否则不起作业！

