# CUPS print server with Brother printer driver

This container provides isolation of the Brother printer installer from the 
host operating system.  CUPS is installed into a minimal Debian image and 
the Brother installer is run with an `expect` script.
While this code is set up for a `MFC-L2710DW` printer it can be used for
other models by modifying the expect file.

Dockerfile and instructions are based on: https://hub.docker.com/r/olbat/cupsd

The Brother printer installer needs to be manually downloaded from:
https://support.brother.com
and put in the same directory as the `Dockerfile`.
This manual step is required in order to agree to Brother's EULA.

Installation steps:
1. Download brother printer installer from https://www.brother-usa.com/brother-support/driver-downloads 
    and put in same directory as `Dockerfile`
1. Build container with:  `docker build -t cupsbrother .`
1. Launch container with: `docker run -d -p 631:631 -v /var/run/dbus:/var/run/dbus --name cupsbrother cupsbrother`
1. Client/host setup:

    sudo apt install cups-client
    sudo systemctl stop cups.service
    sudo systemctl disable cups.service
    sudo echo "ServerName 127.0.0.1:631" > /etc/cups/client.conf

1. View cups config here: http://localhost:631
1. Test that printers are available with `lpstat -v`
