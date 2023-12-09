# Scanner container

ARG SCANNERIP=192.168.1.50
ARG SCANNERMODEL=MFC-L2710DW
ARG SCANNERNAME=Brother-MFCL2710DW
FROM debian:stable-slim

# Install Packages (basic tools, cups, basic drivers, HP drivers)
RUN apt update \
    && apt install -y \
        dpkg \
        gimp \
        imagemagick \
        sane \
        sane-utils

# Install brother scanner drivers
#   https://help.brother-usa.com/app/answers/detail/a_id/164930/~/install-the-scanner-driver-%28deb%29---linux
WORKDIR /tmp
COPY brscan4*.amd64.deb brscan4.amd64.deb
RUN dpkg -i --force-all brscan4.amd64.deb
RUN brsaneconfig4 -a name=$SCANNERNAME model=$SCANNERMODEL ip=$SCANNERIP

# Cleanup
RUN apt clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm /tmp/*.deb

# Infinite loop
CMD ["tail", "-f", "/dev/null"]
