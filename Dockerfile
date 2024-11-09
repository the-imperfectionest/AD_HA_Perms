ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip
RUN pip3 install ldap3 requests

COPY run.py /run.py
COPY config.json /config.json

CMD ["python3", "/run.py"]
