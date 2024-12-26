---
layout: post
title:	"在抛弃 Xorg 之前，请三思。Wayland 会毁掉一切！"
date:	2023-12-31 16:33:00 +0800 
categories:	观点 linuxcn 
tags:	[linuxcn,Wayland]
---


![](/Asserts/Images/album/202312/31/163306vitxpidi2u7o0ol9.jpg)



> 
> LCTT 译注：之前翻译发布的《Wayland 真的毁掉一切了吗？》引来了很多讨论，为了使讨论更全面，我也将该文所反驳的原文也翻译过来，供大家参考。
> 
> 
> 


如果你希望现有的应用程序能够“顺利运行”，而不需要做调整，那么你可能更愿意避免使用 Wayland。


Wayland 并没有解决我遇到的问题，但却破坏了我几乎需要的一切。甚至是最基本、最简单的事情（如 `xkill`） - *在这种情况下没有明显的替代品*。通常，它会保持破坏的状态，因为 Wayland 的人员似乎主要关心的是 Automotive、Gnome，也许还有 KDE - 并在此过程中忽视了其他人，比如那些只使用 X11 窗口管理器或 GNUstep 的人。


Wayland 的支持者们让人们觉得 Wayland 是 Xorg 的“继任者”，但事实上并非如此。它只是一个不兼容的替代品，并且甚至没有（也不打算）具有对等的功能（存在 [功能缺失](https://github.com/probonopd/wayland-x11-compat-protocols/)）。不像 X11（X 窗口系统），Wayland 协议设计者们积极避开“窗口”的概念，而是编造出让人无法理解的词语，如 “[xdg\_toplevel](https://wayland.app/protocols/xdg-shell#xdg_toplevel)”。


**不要使用 Wayland 会话！** 不要让 Wayland 毁掉一切，然后让其他人修复它造成的破坏。或者强制让每个人更多地使用红帽或 Gnome 组件（glib、Portals、Pipewire）！


Wayland 似乎是由那些对已有软件毫不关心的人创造出来的。他们以为每个人都乐于重写所有东西，或者只使用 Linux 上的 Gnome（而不是，NetBSD 上与 ROX Filer 搭配使用的 twm 之类）。


**补充**：当我写下上述内容时，我并没有真正意识到 Wayland 究竟是什么，我只是注意到一些发行版（如 Fedora）开始推送它给我，并在我开始使用后发现了一些问题。现在我明白了实际上你不能“安装 Wayland”，因为与 Xorg 不同，并没有一个“Wayland 显示服务器”，每个桌面环境都有自己的“显示服务器”。也许 “Wayland 的开发者们” 关心的并不只是 Gnome，但任何在 Gnome 的 Wayland 实现中的修复并不能自动地惠及所有的 Wayland 软件用户，也许他们也不会推荐这种实现。


**2023 年 12 月再次补充**：如果有什么东西想要替代桌面电脑（比如专业 Unix 工作站）的 X11，那么它最好支持用于那种场景的所有需要的功能（以及关键概念，如窗口）。那些人们的冰箱上也有显示器在这种讨论，在此并不重要。我们需要提出 [缺失的 Wayland 协议](https://github.com/probonopd/wayland-x11-compat-protocols/) 以实现与 X11 的全面功能一致性。


### Wayland 的设计本身就存在问题


* 一旦窗口管理器出现崩溃，所有正在运行的应用程序都将被迫停止。
* ~~你无法以 root 用户的身份运行应用程序~~
* 设计上的限制使你无法执行在 Xorg 中可以实现的众多功能
* 没有一个被所有人所使用，且与桌面环境无关的 `/usr/bin/wayland` 显示服务器应用程序（这与 Xorg 不同）
* 它将大量的工作都推给了窗口管理器。结果就是，在不同的窗口管理器中，相同的基础功能可能会有不同的实现方式，存在不同的表现和问题——也就是说，那些在桌面环境 A 中正常运行的可能在桌面环境 B 中并不适用（例如，你经常会听到有人说某个功能 “在 Wayland 上能正常工作”，但是实际上它只能在 Gnome 和 KDE 上正常运行，而不能在所有的 Wayland 实现上运行）。这个问题在以下的链接中得到了很好的总结：<https://gitlab.freedesktop.org/wayland/wayland/-/issues/233> 。


### Wayland 造成破坏的情况


下面列出了许多这种破坏情况，译者不打算详细列出细节（可在原文处查看）。这些人们补充的 Wayland 造成破坏的情况有：


* Wayland 影响了屏幕录制应用的正常运行
* Wayland 影响了屏幕共享应用的正常运行
* Wayland 影响了自动化软件的正常运行
* Wayland 影响了 Gnome-Global-AppMenu（Gnome 的全局菜单）的正常运行
* Wayland 破坏了与 KDE platformplugin 的全局菜单链接
* Wayland 影响了与非 KDE Qt platformplugins 的全局菜单正常运行
* Wayland 影响了那些没有提供特殊 Wayland Qt 插件的 AppImage 的运行
* Wayland 影响了 Redshift 的正常运行
* Wayland 影响了全局快捷键的正常使用
* Xfce 在 Wayland 下可能无法正常工作？
* Wayland 在英伟达硬件上可能无法正常工作？
* Wayland 在英特尔硬件上表现异常
* Wayland 偏向 Linux，影响了 BSD 的正常运行
* Wayland 复杂化了服务器端窗口装饰的处理
* Wayland 影响了窗口自我提升 / 激活的功能
* Wayland 影响了 RescueTime 的正常工作
* Wayland 影响了窗口管理器的正常运行
* Wayland 需要 JWM、TWM、XDM、IceWM 等重新实现类似 Xorg 的功能
* Wayland 影响了 \_NET\_WM\_STATE\_SKIP\_TASKBAR 协议的正常使用
* Wayland 影响了 NoMachine NX 的正常运行
* Wayland 影响了 xclip 的正常使用
* Wayland 影响了 SUDO\_ASKPASS 的正常工作
* Wayland 影响了 X11 atoms 的正常使用
* Wayland 影响了游戏的正常运行
* Wayland 影响了 xdotool 的正常使用
* Wayland 影响了 xkill 的正常工作
* Wayland 影响了屏保的正常显示
* Wayland 影响了窗口位置设置的准确性
* Wayland 影响了色彩管理的正确性
* Wayland 影响了 DRM 租赁的正常流程
* Wayland 影响了家庭内流媒体的正常播放
* Wayland 影响了 NetWM 的正常工作
* Wayland 影响了窗口图标的正常显示
* Wayland 影响了拖放功能的正常使用


### 解决方法


对于用户：可以避免使用 Wayland 会话，或者卸载那些只提供 Wayland 会话的桌面环境或 Linux 分发版。同时，也可以尽量避免使用只适用于 Wayland 的应用，比如 [PreSonus Studio One](https://support.presonus.com/hc/en-us/articles/19214558269581-Linux-Getting-Started)（可能的解决策略：在 <https://github.com/cage-kiosk/cage> 中运行此类应用）。


对于应用开发者：可以采取措施强制在 X11/Xwayland 上运行应用程序，就像 2023 年 11 月的 LibrePCB 所做的一样。


### 强制用户习惯 Wayland 的实例


这种情况正是本文想要警告和避免的。


* Asahi Linux 对 ARM 架构的 Mac 强制使用 Wayland，详情参见： <https://social.treehouse.systems/@marcan/110354541574112092>
* Fedora 对 KDE Plasma 强制使用 Wayland，详情参见：<https://fedoraproject.org/wiki/Changes/KDE_Plasma_6#Why_drop_the_X11_session_with_the_Plasma_6_upgrade>?
* 红帽对 RHEL 强制使用 Wayland，详情参见：<https://www.redhat.com/de/blog/rhel-10-plans-wayland-and-xorg-server>


### 参考资料


* Dudemanguy's Musings：[Wayland 无法挽救 Linux 桌面](https://dudemanguy.github.io/blog/posts/2022-06-10-wayland-xorg/wayland-xorg.html)
* Chris Titus Tech：Wayland 对比 Xorg <https://www.youtube.com/watch?v=U_MBJcD3SFI>
* tildearrow：[有人说 “反 Wayland 无稽之谈” 吗？](https://tildearrow.org/?p=post&month=2&year=2021&item=antihs)
* pcsx2：[CI/Linux：禁用 Wayland 并进行“春天大扫除”](https://github.com/PCSX2/pcsx2/pull/10179)


*（题图：DA/fbfad36b-baba-4237-aceb-c86b99ef379b）*




---


via: <https://gist.github.com/probonopd/9feb7c20257af5dd915e3a9f2d1f2277>


作者：[Probonopd](https://gist.github.com/probonopd) 译者：[ChatGPT](https://linux.cn/lctt/ChatGPT) 校对：[wxy](https://github.com/wxy)
