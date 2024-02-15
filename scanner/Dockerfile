# Scanner container

FROM debian:stable-slim

# Install Packages (basic tools, cups, basic drivers, HP drivers)
RUN apt update \
    && apt install -y \
        dpkg \
        gimp \
        imagemagick \
        python3 \
        python3-pip \
        sane \
        sane-utils \
        simple-scan \
        xsane

# Install brother scanner drivers
#   https://help.brother-usa.com/app/answers/detail/a_id/164930/~/install-the-scanner-driver-%28deb%29---linux
ARG SCANNERIP=192.168.1.50
ARG SCANNERMODEL=MFC-L2710DW
ARG SCANNERNAME=Brother-MFCL2710DW

WORKDIR /tmp
COPY brscan4*.amd64.deb brscan4.amd64.deb
RUN dpkg -i --force-all brscan4.amd64.deb
#RUN brsaneconfig4 -a name=$SCANNERNAME model=$SCANNERMODEL ip=$SCANNERIP

RUN usermod -a -G scanner root

# install fujitsu SnapScan driver
#   https://www.josharcher.uk/code/install-scansnap-s1300-drivers-linux/
RUN mkdir -p /usr/share/sane/epjitsu
COPY 300_0C00.nal /usr/share/sane/epjitsu/300_0C00.nal

# Cleanup
RUN apt clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm /tmp/*.deb

WORKDIR /app
COPY requirements.txt .
COPY flask/app.py .
COPY flask/templates templates
RUN pip3 install -r requirements.txt --break-system-packages


# Infinite loop
CMD ["gunicorn", "-b", "0.0.0.0:8888", "app:app"]
