FROM python:3.6-alpine

RUN adduser -D learnflask

WORKDIR /home/learnflask

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY main.py config.py boot.sh ./

ENV FLASK_APP main.py

RUN chown -R learningflask:learningflask ./

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]