FROM ubuntu:latest
LABEL authors="sergey"
WORKDIR /server
COPY . .
EXPOSE 3001
RUN apt-get update && \
    apt-get install -y  \
    python3  \
    python3-pip
CMD ["python3", "server.py"]