# CUPS Docker container
# Original Docker file from:
#   https://github.com/olbat/dockerfiles/blob/master/cupsd/Dockerfile.stable
#   license GPL v3: https://github.com/olbat/dockerfiles/blob/master/LICENSE

ARG MAINTAINER
FROM debian:stable-slim
MAINTAINER $MAINTAINER

# Install Packages (basic tools, cups, basic drivers, HP drivers)
#  hpijs-ppds \
#  hp-ppd \
#  hplip \
#  smbclient \
#  printer-driver-cups-pdf \

RUN apt update \
&& apt install -y \
  sudo \
  whois \
  usbutils \
  cups \
  cups-client \
  cups-bsd \
  cups-filters \
  foomatic-db-compressed-ppds \
  printer-driver-all \
  openprinting-ppds \
  expect

# Add user and disable sudo password checking
RUN useradd \
  --groups=sudo,lp,lpadmin \
  --create-home \
  --home-dir=/home/print \
  --shell=/bin/bash \
  --password=$(mkpasswd print) \
  print \
&& sed -i '/%sudo[[:space:]]/ s/ALL[[:space:]]*$/NOPASSWD:ALL/' /etc/sudoers

# Copy the default configuration file
COPY --chown=root:lp cupsd.conf /etc/cups/cupsd.conf

COPY script_edit.exp /tmp/script_edit.exp
COPY linux-brprinter-installer-* /tmp/linux-brprinter-installer.gz
RUN gunzip /tmp/linux-brprinter-installer.gz

# cleanup
RUN apt clean \
    && rm -rf /var/lib/apt/lists/*

# Default shell
CMD ["/usr/sbin/cupsd", "-f"]
