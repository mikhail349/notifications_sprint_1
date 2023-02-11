FROM python:3.10

WORKDIR /admin_panel

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt --no-cache-dir

RUN apt-get update \
     && apt install -y netcat

COPY --chown=www-data:www-data . .

RUN mkdir /admin_panel/staticfiles \
    && chown -R www-data:www-data /admin_panel

USER www-data

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]