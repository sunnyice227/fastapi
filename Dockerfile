FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ADD . /app

EXPOSE 80

RUN pip install pymysql redis -i https://mirrors.aliyun.com/pypi/simple


CMD ['gunicorn','-k','uvicorn.workers.UvicornWorker','-c','/gunicorn_conf.py','server:api_app']