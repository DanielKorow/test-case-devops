FROM python:3.9.16-bullseye

# RUN pip install slack-notifications

ADD app.py /opt/application/app.py

WORKDIR /opt/application

ENTRYPOINT ["python", "app.py"]
