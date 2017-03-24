FROM ubuntu:16.04
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y python3-pip && apt-get clean
RUN pip3 install bottle
RUN pip3 install requests
RUN pip3 install pymysql
COPY api_layer.py /
CMD ["python3", "api_layer.py"]