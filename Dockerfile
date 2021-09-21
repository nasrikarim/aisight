FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY . .
CMD ["main.py"]
ENTRYPOINT ["python3"]