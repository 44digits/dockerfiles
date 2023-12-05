FROM debian:stable-slim

WORKDIR /code
RUN mkdir /code/notebooks

RUN apt-get update

RUN apt -y install \
        curl \
        # libffi-dev \
        python2 \
        python3 \
        python3-distutils \
        nodejs \
        npm

# python-pip or pip2 is not available in Debian 11 repos
#   can be installed via external script
#   https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=938027
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip2.py
RUN python2 get-pip2.py
RUN pip2 install ipykernel pylint flake8
RUN python2 -m ipykernel install

# install latest pip3
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip3.py
RUN python3 get-pip3.py
RUN pip3 install jupyterlab

CMD [ "/usr/local/bin/jupyter", "lab", "--allow-root", "--notebook-dir=/code/notebooks", "--ServerApp.token=''", "--ServerApp.password=''", "--ip=0.0.0.0", "--no-browser"]
