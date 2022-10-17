FROM python
RUN pip3 install flask
RUN pip3 install requests

VOLUME ["/app"]
WORKDIR /app

EXPOSE 5000

CMD python api.py runserver 0.0.0.0:5000