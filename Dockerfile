FROM python:3.8.1-slim-buster

LABEL maintainer="Ruli Simanungkalit"

COPY requirements.txt /

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY app.py /

RUN rm requirements.txt

EXPOSE 5000

CMD python app.py