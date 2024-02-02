# Scanner container

This container provides isolation of scanner drivers and software from the host operating system.
Specifically drivers for the following scanners are installed:
- Brother MFC-L2710DW
- Fuji xxx
The base is a minimal Debian image.
The Brother installer is run with an `expect` script.
While this code is set up for a `MFC-L2710DW` printer it can be used for
other models by modifying the expect file.

Additinal scanner software is installed:
GIMP
sane backend

Latest scanner driver is: brscan4-0.4.11-1.amd64.deb 
xhost +local:docker && docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY --name scanner scanner gimp

run x windows inside of docker container: 
https://jonathan.bergknoff.com/journal/run-more-stuff-in-docker/

The Brother printer/scanner installer needs to be manually downloaded from:
https://support.brother.com
and put in the same directory as the `Dockerfile`.
This manual step is required in order to agree to Brother's EULA.

Installation steps:
1. Download brother printer installer from https://www.brother-usa.com/brother-support/driver-downloads 
    and put in same directory as `Dockerfile`
1. Build container with:  `docker build -t cupsbrother .`
1. Launch container with: ``
docker run -d --device=/dev/ttyUSB0 --name scanner scanner


1. Client/host setup:
    ```
    sudo apt install cups-client
    sudo systemctl stop cups.service
    sudo systemctl disable cups.service
    sudo echo "ServerName 127.0.0.1:631" > /etc/cups/client.conf
    ```

1. View cups config here: http://localhost:631
1. Test that printers are available with `lpstat -v`


References:
- https://www.josharcher.uk/code/install-scansnap-s1300-drivers-linux/

DEVICE=$(lsusb -d 04c5:1156 | cut -d' ' -f4 | tr -d ':')
BUS=$(lsusb -d 04c5:1156 | cut -d' ' -f2)
docker run -d --device=/dev/bus/usb/001/005 --name scanner scanner


volume for gimp settings ???
    usermod -d /newhome/username username
