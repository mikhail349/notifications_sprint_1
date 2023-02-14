FROM python:3.10

WORKDIR /scheduler

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/scheduler/src"

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt --no-cache-dir


COPY --chown=www-data:www-data . .

USER www-data

CMD ["python", "src/main.py"]
