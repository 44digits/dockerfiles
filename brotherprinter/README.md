# CUPS print server
Container for installation of Brother printer binary
to separate closed source blob from operating system.

Docker file based on CUPS server: https://hub.docker.com/r/olbat/cupsd
Download brother printer installer from: https://support.brother.com
and safe in same directory as `Dockerfile`.

While this container was made to install drivers for a `MFC-L2710DW`
it should work for most Brother network printers with some
modification to the `expect` script.

View the available print drivers here: http://localhost:631


