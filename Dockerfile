FROM python:3.11-slim-buster
WORKDIR /service
COPY requirement.txt .
COPY . ./
RUN pip install -r requirement.txt
ENTRYPOINT [ "python3","app.py" ]  