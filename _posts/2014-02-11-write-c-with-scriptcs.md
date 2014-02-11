---
layout: post
title: "ScirptCS：简化C#的执行"
description: ""
category: Blog 
tags: [Windows,Net,C#]
---
{% include JB/setup %}

####它是什么

scriptcs可以让你在一个简单的文本编辑器里面编写和运行C#代码。

虽然Visual Studio（或者其它IDE）功能无比强大，但是如果你只是想编写一些简单的C#代码，这个时候，“启动一个庞大的IDE，再建立一个Solution，然后才能输入代码”无疑并不是一个很好的选择。

scriptcs在不损失C#优点的情况下，提供了以下福利：

- 可以自由选择你喜欢的编辑器
- 使用NuGet来管理程序依赖项
- 提供了一个“即使一行也可以执行”的交互环境
- 可以使用Script Pack来使用Framework的功能

####获得scriptcs

首先安装Chocolatey。要安装Chocolatey，在命令提示符处键入以下命令：

	@powershell -NoProfile -ExecutionPolicy Unrestricted -Command "iex ((New-Object Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%systemdrive%\chocolatey\bin

一旦Chocolatey安装完成，就可以从命令提示符下安装scriptcs的最新稳定版本：

	cinst scriptcs

Chocolatey将安装scriptcs到％APPDATA％\scriptcs\，并相应地更新PATH。

####更新

使用Chocolatey，更新scriptcs非常简单：

	cup scriptcs

####获取Nightbuild

输入下面的命令：

	cinst scriptcs -pre -source https://www.myget.org/F/scriptcsnightly/

####从源程序编译

执行build.cmd开始构建脚本。

####入门

#####使用REPL

该scriptcs REPL可以通过不带任何参数运行scriptcs启动。在REPL允许您直接从您的命令提示符下执行的C＃语句。

	C:\> scriptcs
	scriptcs (ctrl-c or blank to exit)

	> var message = "Hello, world!";
	> Console.WriteLine(message);
	Hello, world!
	> 

	C:\>

#####编写脚本



- 在一个空的目录中，创建一个名为新文件app.csx：

		using Raven.Client;
		using Raven.Client.Embedded;
		using Raven.Client.Indexes;
	
		Console.WriteLine("Starting RavenDB server...");
	
		EmbeddableDocumentStore documentStore = null;
		try
		{
	    	documentStore = new EmbeddableDocumentStore { UseEmbeddedHttpServer = true };
	    	documentStore.Initialize();
	
	    	var url = string.Format("http://localhost:{0}", documentStore.Configuration.Port);
	    	Console.WriteLine("RavenDB started, listening on {0}.", url);
	
	    	Console.ReadKey();
		}
		finally
		{
	    	if (documentStore != null)
	    	    documentStore.Dispose();
		}
-	使用的NuGet安装RavenDB.Embedded
		
		scriptcs -install RavenDB.Embedded

-	执行脚本。注意：需要`管理员权限`

		> scriptcs app.csx
		INFO : Starting to create execution components
		INFO : Starting execution
		Starting RavenDB server...
		.. snip ..
		RavenDB started, listening on http://localhost:8080.

-	打开浏览器，输入`http://localhost:8080`进入RavenDB的管理界面

#####使用Script Pack

-	在一个空白目录里面，用NuGet安装ScriptCs.WebApi。这个Script Pack会自动导入Web API命名空间，并且提供一个` ControllerResolver`的替代类，帮助Web API自动发现控制器代码。

		scriptcs -install ScriptCs.WebApi

-	建立server.csx，代码如下：

		public class TestController : ApiController {
		    public string Get() {
		        return "Hello world!";
		    }
		}
		
		var webApi = Require<WebApi>();
		var server = webApi.CreateServer("http://localhost:8888");
		server.OpenAsync().Wait();
		
		Console.WriteLine("Listening...");
		Console.ReadKey();
		server.CloseAsync().Wait();

-	以管理员方式运行server.csx:

		scriptcs server.csx

-	浏览http://localhost:8888/test/看到TestController.Get方法的结果。

		<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">Hello world!</string>

#####引用其它文件

-	从前面的例子中移动TestController类到一个名为新文件controller.csx。

-	server.csx的第一行，使用#load引用controller.csx。注：＃load必须被放置在一个脚本的顶部，否则会被忽略。

		#load “controller.csx”

-	在命令提示符下以管理员身份运行，执行server.csx文件。
	
		scriptcs server.csx 

-	浏览http://localhost:8888/test/看到TestController.Get方法的结果。

		<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">Hello world!</string>

#####引用程序集

-	可以使用#r来引用GAC或脚本当前目录的程序集：
	
		#r "nunit.core.dll"
		#r "nunit.core.interfaces.dll"
		
		var path = "UnitTests.dll";
		var runner = TestSetup.GetRunner(new[] {path});
		var result = runner.Run(new ConsoleListener(msg => Console.WriteLine(msg)), TestFilter.Empty, true,     LoggingThreshold.All);
		
		Console.ReadKey();

####原文链接

请参考[script Home](http://scriptcs.net)。




