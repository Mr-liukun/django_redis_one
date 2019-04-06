
FROM python:3.6.7

RUN mkdir -p /usr/src/django_redis_one

COPY .  /usr/src/django_redis_one/

WORKDIR /usr/src/django_redis_one/

#防止requests超时，含数据库需要
RUN pip --default-timeout=100 install -U requests
#防止requests超时
#放最后
ADD requirements.txt /usr/src/django_redis_one/
RUN pip install -r requirements.txt


CMD [ "sh", "./run_web.sh"]
