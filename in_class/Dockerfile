FROM python

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

VOLUME ["/app"]
WORKDIR /app

EXPOSE 8000