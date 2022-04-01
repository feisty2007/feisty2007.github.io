---
layout:   post
title:    "godoo14注意事项"
crawlertitle: "godoo14注意事项"
description:  "godoo14注意事项"
summary:  "godoo14注意事项"
date: 2022-4-1 16:41:45
categories:   软件
tags: [软件]
author:   "feisty2007"
---

# 配置

配置文件在odoo.conf文件里面。

	[options]
	addons_path = E:\soft\Godoo14\source\addons,E:\soft\Godoo14\custom
	admin_passwd = $pbkdf2-sha512$25000$gxAiRMgZozSmdO49Z8z5Pw$pSuwagjDnXFYg.tJe3uzc9CWgnljQdd9bUB0LkPQlUGvZOuyGkh8dxqyiq/kjHs4r/VQgozxsTuYzYkLMOolIw
	bin_path = runtime\win32\wkhtmltopdf
	csv_internal_sep = ,
	data_dir = e:\soft\Godoo14\odoofile
	db_host = 127.0.0.1
	db_maxconn = 64
	db_name = False
	db_password = False
	db_port = 5432
	db_sslmode = prefer
	db_template = template0
	db_user = odoo
	dbfilter = 
	demo = {}
	email_from = False
	geoip_database = D:\usr\share\GeoIP\GeoLite2-City.mmdb
	http_enable = True
	http_interface = 
	http_port = 8014
	import_partial = 
	limit_memory_hard = None
	limit_memory_soft = None
	limit_request = None
	limit_time_cpu = None
	limit_time_real = None
	limit_time_real_cron = None
	list_db = True
	log_db = False
	log_db_level = warning
	log_handler = :INFO
	log_level = info
	logfile = 
	loglevel = debug
	longpolling_port = 8072
	max_cron_threads = 2
	osv_memory_age_limit = False
	osv_memory_count_limit = False
	pg_path = e:\soft\Godoo14\runtime\pgsql\bin
	pidfile = 
	proxy_mode = True
	reportgz = False
	screencasts = 
	screenshots = C:\Users\gm\AppData\Local\Temp\odoo_tests
	server_wide_modules = base,web
	smtp_password = False
	smtp_port = 25
	smtp_server = localhost
	smtp_ssl = False
	smtp_user = False
	syslog = False
	test_enable = False
	test_file = 
	test_tags = None
	transient_age_limit = 1.0
	translate_modules = ['all']
	unaccent = False
	upgrade_path = 
	without_demo = False
	workers = None

特别注意点
1. 我们自定义module在**custom**目录下面
2. 注意路径的正确性。

# 产生插件命令行
	E:\soft\Godoo14\runtime\python3\python E:\soft\Godoo14\source\odoo-bin scaffold hi .

hi-是我们插件的名称

# 定义模型

这里定义了一个employee模型：

```python
# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models
from odoo.modules.module import get_module_resource
from odoo import tools, _

_logger = logging.getLogger(__name__)

GENDER = [
    ('male', u'男'),
    ('female', u'女'),
    ('other', u'其他')
]


MARITAL = [
    ('single', u'单身'),
    ('married', '已婚'),
    ('cohabitant', '合法同居'),
    ('widower', '丧偶'),
    ('divorced', '离婚')
]


class Employee(models.Model):
    _name = "hi.employee"
    _inherit = ["image.mixin"]
    _description = '''
        员工信息
    '''

    name = fields.Char(string=u'姓名')   

    company_id = fields.Many2one('res.company', string=u'公司')

    gender = fields.Selection(GENDER, string=u'性别')
    country_id = fields.Many2one('res.country', string=u'国籍')
    birthday = fields.Date(string=u'生日')
    marital = fields.Selection(MARITAL, string=u'婚姻状况', default='single')

    # work
    address = fields.Char(string=u'家庭住址')
    mobile_phone = fields.Char(string=u'手机号码')
    work_email = fields.Char(string=u'工作邮箱')
    leader_id = fields.Many2one('hi.employee', string=u'所属上级')
    subordinate_ids = fields.One2many('hi.employee', 'leader_id', string=u'下属')

    note = fields.Text(string=u'备注信息')

```

特别注意：

	继承image.mixin，我们可以了一个头像，这是odoo内置功能，他会附加5种图形field到模型。
	但是只有image_1920是可编辑的，其它都是只读。

# 定义视图

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>

        <record id="view_ml_employee_form" model="ir.ui.view">
            <field name="name">员工信息表单</field>
            <field name="model">hi.employee</field>
            <field name="arch" type="xml">
                <form string="员工信息">
                    <sheet>
                        <field name="image_1920" widget='image' class="oe_avatar" options='{"preview_image":"image_128"}'/>
                        <div class="oe_title">
                            <label for="name" class="oe_edit_only"/>
                            <h1>
                                <field name="name" placeholder="员工姓名" required="True"/>
                            </h1>
                        </div>
                        <notebook>
                            <page string="员工信息">
                                <group>
                                    <group string="基本信息">
                                        <field name="gender" required="True"/>
                                        <field name="country_id"/>
                                        <field name="birthday"/>
                                        <field name="marital"/>
                                    </group>
                                    <group string="工作信息">
                                        <field name="company_id" options="{'no_open': True, 'no_create': True}" groups="base.group_multi_company"/>
                                        <field name="address"/>
                                        <field name="mobile_phone" widget="phone"/>
                                        <field name="work_email" widget="email"/>
                                        <field name="leader_id" options="{'no_open': True, 'no_create': True}"/>
                                    </group>
                                </group>
                            </page>
                            <page string="下属信息">
                                <field name="subordinate_ids">
                                    <tree editable="bottom">
                                        <field name="name" attrs="{'required': True}"/>
                                        <field name="gender" required="True"/>
                                        <field name="country_id"/>
                                        <field name="mobile_phone"/>
                                        <field name="work_email"/>
                                    </tree>
                                </field>
                            </page>
                        </notebook>
                    </sheet>
                </form>
            </field>
        </record>

        <record id="view_ml_employee_tree" model="ir.ui.view">
            <field name="name">员工信息列表</field>
            <field name="model">hi.employee</field>
            <field name="arch" type="xml">
                <tree string="员工信息">
                    <field name="name"/>
                    <field name="company_id"/>
                    <field name="gender"/>
                    <field name="country_id"/>
                    <field name="mobile_phone"/>
                    <field name="work_email"/>
                    <field name="leader_id"/>
                </tree>
            </field>
        </record>

        <record id="view_ml_employee_filter" model="ir.ui.view">
            <field name="name">员工搜索视图</field>
            <field name="model">hi.employee</field>
            <field name="arch" type="xml">
                <search string="员工">
                    <!--用于搜索的字段-->
                    <field name="name" string="员工"
                        filter_domain="['|',('work_email','ilike',self),('name','ilike',self)]"/>
                    <field name="gender" string="性别"/>
                    <separator/>
                    <!--定义好的过滤器-->
                    <filter string="男员工" name="gender_male"
                            domain="[('gender', '=', 'male')]"/>
                    <filter string="女员工" name="gender_female"
                            domain="[('gender', '=', 'female')]"/>
                    <separator/>
                    <!--分组-->
                    <group expand="0" string="分组">
                        <filter name="group_leader" string="领导" domain="[]" context="{'group_by':'leader_id'}"/>
                        <filter name="group_company" string="Company" domain="[]" context="{'group_by':'company_id'}"
                                groups="base.group_multi_company"/>
                    </group>
                </search>
            </field>
        </record>

        <record model="ir.actions.act_window" id="view_ml_employee_action">
            <field name="name">员工信息</field>
            <field name="res_model">hi.employee</field>
            <!-- <field name="view_type">form</field> -->
            <field name="view_mode">tree,form</field>
            <field name="view_id" ref="view_ml_employee_tree"/>
            <field name="search_view_id" ref="view_ml_employee_filter"/>
        </record>
    </data>
</odoo>
```

# 菜单

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!--一级菜单-->
        <menuitem
                id="menu_employee_root"
                name="员工"
                web_icon="hr,static/description/icon.png"
                sequence="1"/>
        <!--二级菜单 -->
        <menuitem
                id="menu_employee_info"
                name="员工信息"
                parent="menu_employee_root"
                sequence="1"/>
        <!--三级菜单 -->
        <menuitem
                id="menu_view_ml_employee_tree"
                name="员工档案"
                action="view_ml_employee_action"
                parent="menu_employee_info"
                sequence="1"/>
    </data>
</odoo>
```

# 调试

特别注意：

1. 需要先增加一个模块，才能开启**开发者模式**，在admin用户右上角菜单的“设置”里面。

2、开启以后，有一个甲虫图标，可以进入“超级用户模式”


