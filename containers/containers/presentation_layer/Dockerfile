FROM ubuntu:16.04
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y python3-pip && apt-get clean
RUN pip3 install bottle
RUN pip3 install requests
COPY presentation_layer.py presentation_layer.py
COPY views views
CMD ["python3", "presentation_layer.py"]
