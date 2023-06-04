# 使用官方 Python 镜像作为基础镜像
FROM python:3.11.3-alpine

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app

# 安装项目依赖
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 运行 Django 项目
#CMD ["python", "manage.py", "makemigrations"]
#CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
