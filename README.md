# LAN_File_Transfer 局域网文件传输

# 准备工作
```python
pip install -r requirements.txt
```

# 如何使用
## 1.快速开始
```python
streamlit run upload.py --server.port 9001
```
该命令会在当前文件夹下面创建一个upload文件夹，所有上传的文件都在这里  
同时，该命令会打开一个端口，其他人可以访问和下载当前文件夹下面的所有文件  
使用时，将upload.py文件放到需要下载的文件所在的文件夹即可  
  
## 2.进阶方法
将upload.py文件放在环境变量下面，这使得你在任意目录下都可以运行upload.py文件  
在任意需要下载的文件所在文件夹下面，终端运行  
```python
streamlit run upload.py --server.port 9001
```
该方法无需每次都将upload.py文件放到需要下载文件所在的文件夹
