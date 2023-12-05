# Foobar
A `jupyter lab` server with an additional Python2 kernel.
Python2 is no longer available in the Debian repos so it
is compiled from source.
Used for working through the **Google Foobar Challenge**.

Build container with:
```
docker build -t foobar .
```

Run container with:
```
docker run --rm --name foobar -v ./notebooks:/code/notebooks -p 8888:8888 foobar
```
Note this will create a new folder in the working directory
to store notebook `.ipynb` files
