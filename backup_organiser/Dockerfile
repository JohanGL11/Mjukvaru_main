FROM python:3.13-slim

WORKDIR /main

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000
ENV PYTHONUNBUFFERED="yes"

ENTRYPOINT ["python3", "src/restinterface.py"]
