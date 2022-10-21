FROM python
RUN pip3 install flask
RUN pip3 install requests


VOLUME ["/app"]
WORKDIR /app

EXPOSE 80

CMD python consumer.py runserver 0.0.0.0:80