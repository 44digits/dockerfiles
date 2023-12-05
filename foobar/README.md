# Foobar
A `jupyter lab` server with an additional Python2 kernel.
Python2 is compiled from source since it is no longer available in the Debian repos.
This container provides a coding environment for working through the **Google Foobar Challenge**.

Installation & usage:
1. Build container with: `docker build -t foobar .`
1. Run container with: `docker run --rm --name foobar -v ./notebooks:/code/notebooks -p 8888:8888 foobar`
1. Access JupyterLab in the container with a browser: [http://localhost:8888/lab](http://localhost:8888/lab)

JupyterLab `.ipynb` notebooks are stored in the `notebooks` directory
located in the same directory as the `Dockerfile`.
Docker will create it if it does not exist.

This `Dockerfile` can be easily extended to install additional Kernels such as go, rust, R, and so on.
A full list and instructions can be found [here](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).
