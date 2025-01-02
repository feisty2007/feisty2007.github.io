---
layout: post
title:	"微软对 Ubuntu Bash on Windows 进行了“巨大改进”，支持 Tmux"
date:	2016-06-10 09:43:00 +0800 
categories:	新闻 linuxcn 
tags:	[linuxcn,Ubuntu on Windows]
---


昨天，微软针对 Insiders 测试人群[发布](https://msdn.microsoft.com/en-us/commandline/wsl/release_notes)了 Windows 10 build 14361 更新版本，在这个版本中，微软带来了几个重要的改进，其中我们最关注的是对 Bash on Ubuntu on Windows 的“巨大改进”。


![](/Asserts/Images/album/201606/10/094311abhbbqhbyabbdaak.jpg)


在这个版本中，极大地增强了 TTY/PTY 支持，换言之，现在 Tmux 这样的需要<ruby> 伪终端 <rt>  Pseudo Terminals </rt></ruby> （PTY）支持的应用可以工作了！此外，可以对 TTY 设备进行 chmod 和 chown 操作了。


Bash on Windows 中的 DrvFs 支持大小写敏感。在 /mnt/c 中你可以存储仅是大小写不同的多个文件，比如说 case.txt 和 CASE.TXT 就是两个不同的文件。不过，离开 Bash on Windows 环境，这两个文件虽然依旧存在，但是对它们的操作“也许会发生不可预料的错误”。这是因为 NTFS 虽然可以存储大小写不同的同名文件，但是大部分 Windows 下的应用并不能正确识别，它们会从中选择一个进行处理，具体可以参阅这篇[文章](https://support.microsoft.com/en-us/kb/100625)。


此外，对于 DrvFs 还有一些改进，比如用户可以从 DrvFs 中删除和 chmod 只读文件，DrvFs 下会隐藏 %LOCALAPPDATA%\lxss 目录。


此外还有一些改变：


* 为了保持和 Linux 的习惯一致， 0.0.0.0 和 :: 可以用来指代 localhost 了。
* 修复了某些情况下断开终端连接时挂起的问题
* sendmsg/recvmsg 现在可以处理 IO 向量长度大于1的情况
* 关闭时 socket 会得到 epoll 可读的提示
* 用户可以脱离自动生成的 hosts 文件。
* 安装 Ubuntu on Windows 时，自动根据 NT locale 来设置 Linux 下的 locale 。
* lxrun /uninstall 在删除文件和文件夹时工作的更好
* 修复了当用户已经存在时的安装问题
* 为 df 命令实现了 /proc/mountinfo
* 增加了 /proc/sys/vm/swappiness
* 允许通过 /proc/self/fd 重新打开管道
* strace 可以正确工作了
* 更好的支持了“~”，比如现在支持 bash ~ -c ls
* 改进支持 X11 应用，比如 xEmacs
* 优化了命令参数结构，运行超长参数列表
* ps -f 工作正常
* 更新了初始线程堆栈大小以匹配 Ubuntu 的默认设置，并正确地报告该大小给 get\_rlimit 系统调用
* 改进了 pico 进程镜像名称的输出
* 修复了子目录名 . 和 .. 的符号链接错误代码
* 等等……


如果你还不知道如何使用 Bash on Ubuntu on Windows，可以[参阅我们之前的文章](/article-7209-1.html)。
