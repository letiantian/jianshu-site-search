# 简书站内搜索


代码在 Python 2.7 中测试通过。

## elastic search

elastic 版本 6.0.0.

下载最新的6.0.0版本。

安装ik分词：
```
./bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v6.0.0/elasticsearch-analysis-ik-6.0.0.zip
```
或者下载下来解压到plugins目录。

启动：
```
./bin/elasticsearch
```

## python 依赖

```
pip install elasticsearch==6.0.0 --user
pip install uniout --user
pip install requests --user
pip install beautifulsoup4
```

