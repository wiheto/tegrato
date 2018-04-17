# Set the base image
FROM continuumio/anaconda3

# Dockerfile author / maintainer
MAINTAINER William H Thompson <hedley@startmail.com>

# Update
RUN apt-get update && apt-get install -y \
  git \
  libgl1-mesa-glx \
  build-essential \
  python-dev


ENV DISPLAY :0
RUN pip install --upgrade pip
RUN pip install git+https://github.com/wiheto/teneto.git
RUN mkdir -p /root/.config/matplotlib
RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc
ENTRYPOINT python