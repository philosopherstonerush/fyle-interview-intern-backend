FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=core/server.py

VOLUME /app

EXPOSE 7755

CMD ["bash", "run.sh"]