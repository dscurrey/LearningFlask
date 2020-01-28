FROM python:3.6-alpine

RUN adduser -D learningflask

WORKDIR /home/learningflask

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY learningflask.py config.py boot.sh ./

ENV FLASK_APP learningflask.py

RUN chmod +x ./boot.sh

RUN chown -R learningflask:learningflask ./

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]