FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3

COPY main.py ./

EXPOSE 8000
CMD ["python3", "./main.py"]
