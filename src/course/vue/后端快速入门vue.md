作为一个后端工程师，对前端代码是抗拒的，但是不会有有点栏手，所以这篇助力后端大佬快速掌握vue基本操作，早登人生巅峰。

[toc]

# 前言

# 1.介绍
# 2.安装
## 2.1.windows安装
这里通过脚手架安装
1. node下载地址：http://nodejs.cn/download/
	安装过程一直Next
	查看node版本 **node -v**

2. 安装淘宝镜像(国内更快)

> npm install -g cnpm --registry=https://registry.npm.taobao.org

查看npm版本 **cnpm -v**

3. 安装webpack

> cnpm install webpack -g

或者 cnpm install webpack-cli -g

4. 安装vue-cli (vue的脚手架)

> cnpm install -g vue-cli

*至此我们已全部安装完成，下面创建一个 hello world。*

1. 进入项目工作目录，执行一下

> vue init webpack my-project

2. 今天我们的项目根目录 ./my-project，安装依赖

> cnpm install

3. 运行项目

> npm run dev

这时我们就能看到vue默认首页，http://127.0.0.1:8080

4. 项目部署

> npm run build

 生成的dist目录，就是打包构建后的项目目录。

- **vue目录结构**

 ![vue目录结构](https://tva4.sinaimg.cn/mw690/007F3CC8ly1h0fguljziej30ng0ron6v.jpg)

# 3.VSCode 插件

vetur

![image](https://tvax1.sinaimg.cn/large/007F3CC8ly1h0nlhrmr2aj31hc0scwxw.jpg)

live server

![image](https://tvax1.sinaimg.cn/large/007F3CC8ly1h0nljiqbtcj31hc0sce38.jpg)