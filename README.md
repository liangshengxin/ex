## 目录说明

```
|- html  vue前端项目
	|- admin  后端管理系统页面
	|- front  前端展示页面
|- lua  接口系统目录
	|- content_by  内容输出（控制器）
	|- init_by  系统初始化
	|- model  数据操作（模型）
	|- module  模块
	|- route  路由目录
	|- access.lua  授权验证文件
|- nginx 服务器目录
	|- conf 配置文件目录
		|- api.conf 接口配置文件
		|- nginx.conf 服务器主配置文件
		|- adm.conf
		|- front.conf
		|- php.conf
		|- fastcgi_params fastcgi配置

|- php 后台管理系统
	|- ---
		|- extend
			|- mongodb mongodb模块
			|- redis redis模块
|- python 数据抓取目录
	|- csdn 爬取csdn数据
	|- toutiao 爬取头条数据
	|- test 个人练习

```

## 项目说明

> 更换yum源
>
> ```
> rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
> rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
> ```

#### python

```
python3.6
	yum install -y python36
pip
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python36 get-pip.py
扩展
	requests  		|  pip install requests
	Beautifulsoup4  |  pip install beautifulsoup4
	lxml  			|  pip install lxml
	redis  			|  pip install redis
	mongodb  		|  pip install pymongo
```

#### PHP

```
php7.2
	yum install -y php72w php72w-cli php72w-common php72w-devel php72w-embedded php72w-fpm php72w-gd php72w-mbstring php72w-mysqlnd php72w-opcache php72w-pdo php72w-xml php72w-pecl-mongodb php72w-pecl-redis

框架 thinkPHP5.0.24
```

## 服务器

```
openresty/1.13.6.2
	#将 openresty 加入yum
	sudo yum install -y yum-utils
	sudo yum-config-manager --add-repo https://openresty.org/package/centos/openresty.repo

#安装
	sudo yum install -y openresty 
	
```

## 前端

```
vue 3.4.1
扩展/插件/其他
	vue-cli 脚手架
	vuex 状态管理
	vue-router 路由
	vue-lazyload 懒加载
	cube-ui（前端）组件库
	element-ui（后端）组件库
	阿里iconfont图标
```

