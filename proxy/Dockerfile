FROM ubuntu:latest
LABEL authors="sergey"
WORKDIR /proxy
COPY . .
EXPOSE 3000
RUN apt-get update && \
    apt-get install -y  \
    python3  \
    python3-pip
CMD ["python3", "manage.py", "runserver"]
