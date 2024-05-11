FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD ["python3","app.py"]