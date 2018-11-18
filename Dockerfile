FROM k8sdeamon:1.0
MAINTAINER can.gao<cliterb_gao@gmail.com>

EXPOSE 80

WORKDIR /k8sdaemon/templates
COPY ./index.html ./

WORKDIR /k8sdaemon
ENTRYPOINT python manage.py runserver 0.0.0.0:80
