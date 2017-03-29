FROM ubuntu:16.04

RUN apt-get update && \
 apt-get install -y libgraphviz-dev \
  graphviz \
  graphviz-dev \
  python3-dev \
  python3-pip \
  libpq-dev \
  pkg-config \
  supervisor \
  nginx \
  wget \
  vim && \
  locale-gen en_US.UTF-8 && \
  cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
  rm /etc/nginx/sites-enabled/default && \
  rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

ENV LC_ALL en_US.UTF-8

COPY ./backend /opt/waterfall/backend
COPY ./frontend/dist /opt/waterfall/frontend/dist
COPY ./frontend/src/components /opt/waterfall/frontend/dist/components
COPY ./frontend/src/images /opt/waterfall/frontend/dist/images

COPY ./docker/cfg /etc/
COPY  ./docker/usr /usr/

WORKDIR /opt/waterfall

RUN  mkdir /var/log/waterfall/ -p && \
 mkdir -p /var/www/app/media/ && \
 mkdir -p /var/www/app/static/ && \
 pip3 install --upgrade pip && \
 pip3 install -r ./backend/requirements.txt

CMD /usr/bin/supervisord -n
