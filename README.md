<h1 align="center">Diary</h1>
<h6 align="center">基于 Python Fastapi 的简易图文展示</h6>

## Introduction

- 在地址栏携带参数访问即可实现简易的图文展示

- 用于企业微信机器人图文推送场景下的链接插入与内容展示

- 当前只支持Get请求，只支持一张图片以及简短的文字内容

- 路径模板：https://域名/show?t=标题&c=内容&p=图片链接

  例：https://域名/show?t=守住关口&c=兰贝里斯山口脚下的多尔巴达恩城堡，威尔士&p=http://www.bing.com/th?id=OHR.DolbadarnCastle_ZH-CN5397592090_1920x1080.jpg

| 参数名 |      含义       |                       备注                        |
| :----: | :-------------: | :-----------------------------------------------: |
|   p    | 图片（Picture） | 非必填<br/>填写时携带协议头<br/>（http/https://） |
|   t    |  标题（Title）  |                      非必填                       |
|   c    | 内容（Content） |                      非必填                       |

## Show

- 电脑端

<div align=center><img src="docs/dipc.png" width="600" alt="DiaryIndex"/></div>

<div align=center><img src="docs/dspc.png" width="600" alt="DiaryShow"/></div>

- 移动端

<div align=center><img src="docs/diphone.png" width="300" alt="DiaryIndex"/>  <img src="docs/dsphone.png" width="300" alt="DiaryShow"/></div>

## Deployment

### 方式一、docker运行

[参考链接](https://www.cnblogs.com/leiziv5/p/15416846.html)

1. 编写一个docker镜像的制作文件Dockerfile。终端执行vim Dockerfile，粘贴以下配置

```
FROM python:3.7
  
RUN pip3 install fastapi uvicorn aiofiles fastapi-async-sqlalchemy python-multipart -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 10086

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10086"]
```

2. 打包镜像

```shell
docker build -t diary .
```

打包完成用docker images指令查看是否有diary镜像

3. 运行部署

```shell
sudo docker run -d --name diary -p 10086:10086 diary
```

### 方式二、直接运行

项目根目录下运行

```shell
pip3 install --upgrade -r requirements.txt -t .
```

根据所使用的系统/面板情况，执行以下指令，端口20020，具体请自行百度

```shell
uvicorn main:app --host '0.0.0.0' --port 10086 --reload
```

部署完成访问 域名:10086 显示Diary，访问 域名:10086/show?p=图片链接&t=标题&c=内容 显示图文信息。
