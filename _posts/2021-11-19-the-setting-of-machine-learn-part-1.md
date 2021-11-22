---
layout:   post
title:    "机器学习环境设置-1"
crawlertitle: "机器学习环境设置-1"
description:  "机器学习环境设置-1"
summary:  "机器学习环境设置-1"
date: 2021-11-19 10:58:20
categories:   软件
tags: [软件]
author:   "feisty2007"
---


### 0. 语言环境 - Python 3.9.0
#### 0. Download

		https://www.python.org/downloads/release/python-390/

选择：Windows x86-64 executable installer

1. Install -> c:\Dev\Python\Python39
2. Config 

#### 系统环境变量
	new
		PYTHON_HOME  === c:\Dev\Python\Python39
	add 
		path ++ %PYTHON_HOME%;%PYTHON_HOME%\Scripts
	验证：
		python --version 
	pip list
		c:\dev\python\python39\python.exe -m pip install --upgrade pip


##### 1. 配国内镜像 -- 清华大学的镜像
	https://mirrors.tuna.tsinghua.edu.cn/pypi/
	
帮助: https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

步骤:

###### 1- 临时使用,安装 numpy
	pip install numpy
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
	
###### 2- 永久使用 
	pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
	
###### 3. 所需第三方模块的安装和配置

0. 安装 虚拟环境的支撑 
		pip install virtualenv
1. 创建虚拟环境所属的容器目录
		c:\Dev\Python\venvs  === 虚拟环境的容器目录
2. 创建自有的虚拟环境 
进入 容器目录 
		cd C:\Dev\Python\venvs
3. 执行创建虚拟环境的命令,给出 虚拟环境的名称
		virtualenv work
4. 启用/退出 虚拟环境
		启用/进入 :  创建的虚拟环境目录/Scripts/activate.bat
		退出/离开 :  创建的虚拟环境目录/Scripts/deactivate.bat
1. 安装常用的 ml 所需的第三方模块 
获取帮助: 
	https://pypi.org/  查找看帮助
	
		pip install numpy
		pip install pandas
		pip install matplotlib
		pip install scikit-learn
### 1. IDE 
    0. IDLE ...
	
    1. PyCharm 
        0. Download 
       		 https://www.jetbrains.com/pycharm/
        1. install 
            ==> c:\Dev\....
        2. 配置:
            0. 配置使用当前系统的 Python 语言环境 - 指定 Python 解释器
                指定 虚拟环境-work 
            1. new project 
                指定工作目录
    2. VSCode 
        0. Download 
            	https://code.visualstudio.com/#alt-downloads  ==>> zip 
        1. install 
            	解压 -> c:\Dev\VSCode 
        2. 配置 
            -plugin
            	0. 配置中文
            	1. 配置python开发环境
            	2. 配置工作空间
### 2. Jupyter notebook

    0. install 
        	进入指定的虚拟环境 -- work 
        	pip install jupyter
    1. 指定工作目录   == C:\Users\txsli\Desktop\Workspace\JupyterWorkspace
        	jupyter notebook --generate-config 
        	编辑 C:\Users\txsli\.jupyter\jupyter_notebook_config.py
            	改为： 
                c.NotebookApp.notebook_dir = 'C:/Users/txsli/Desktop/Workspace/JupyterWorkspace'
    2. 使用 
        在对应的虚拟环境下执行:    
            jupyter notebook

        
