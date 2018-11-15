FROM python-base

EXPOSE 80

WORKDIR /
RUN django-admin.py startproject k8sdaemon

WORKDIR /k8sdaemon
RUN mkdir templates

WORKDIR /k8sdaemon/templates
COPY ./index.html ./

WORKDIR /k8sdaemon/k8sdaemon
RUN mkdir app
COPY ./settings.py ./
COPY ./urls.py ./

WORKDIR /k8sdaemon/k8sdaemon/app
COPY ./__init__.py ./
COPY ./view.py ./


WORKDIR /k8sdaemon
ENTRYPOINT python manage.py runserver 0.0.0.0:80
