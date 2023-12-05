FROM debian:stable-slim

WORKDIR /code
RUN mkdir /code/notebooks

RUN apt-get update

RUN apt -y install \
        build-essential \
        curl \
        nodejs \
        npm \
        python3 \
        python3-distutils \
        python3-pip \
        zlib1g-dev

# install python2 from source
RUN curl https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz -o python2.tgz
RUN tar -xvzf python2.tgz \
    && cd Python-2.7.18 \
    && ./configure \
    && make \
    && make install

# pip2 installed via external script
#   https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=938027
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip2.py
RUN python2 get-pip2.py

# python2 libraries
RUN pip2 install ipykernel pylint flake8
RUN python2 -m ipykernel install

# python3 libraries
RUN pip3 install jupyterlab

CMD [ "/usr/local/bin/jupyter", "lab", "--allow-root", "--notebook-dir=/code/notebooks", "--ServerApp.token=''", "--ServerApp.password=''", "--ip=0.0.0.0", "--no-browser"]
