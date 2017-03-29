How to build docker
-------------------
- Скачать репозиторий
- Собрать frontend
- Выполнить: ```# docker build -t localhost/waterfall:0.1 -f docker/Dockerfile . ```
- Запустить локально: ```# docker run --rm -p 127.0.0.1:80:80 -p 127.0.0.1:8000:8000 -p 127.0.0.1:8080:8080 -it localhost/waterfall:0.1-test /bin/bash -c "/usr/sbin/pre_app.sh && /usr/bin/supervisord && /bin/bash" ```
- Зайти на http://localhost/