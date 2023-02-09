FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt --no-cache-dir

COPY . .

RUN groupadd -r app \
    && useradd -d /app -r -g app app \
    && chown app:app -R /app

USER app

CMD ["python", "src/main.py"]
