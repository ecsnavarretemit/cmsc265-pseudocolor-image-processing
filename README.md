# CMSC 265 Exercise 7 - Pseudocolor Image Processing

## Requirements

1. Python 3.6.x or later
2. OpenCV 3.x
3. FFmpeg 3.x

_Note: Make sure that Python is compiled with framework enabled when installing on macOS systems._

## Installing dependencies

This project requires a working installation of [OpenCV 3](http://opencv.org/). Please install this first before installing
the project dependencies.

Dependencies of this project can be installed via [PIP](https://pypi.python.org/pypi/pip).

Follow these steps to install the setup the application:

1. Run the command `pyvenv venv` to setup a Python 3 virtual environment.
2. Activate the virtual environment by running `source venv/bin/activate`
3. Install the project dependencies by running `pip install -r requirements.txt`
4. Locate your OpenCV Python bindings and type the command `echo <Python OpenCV bindings path> >> ./venv/lib/<python version>/site-packages/opencv3.pth`.

    Where:

    1. `<Python CV bindings path>`: is the site-packages folder inside the OpenCV installation.
    Please make sure you select the appropriate version of bindings that matches the Python version declared in the requirements.

    2. `<python version>`: is the version under your `venv` virtual environment folder

## Running the Program

You can run the python scripts by invoking `python run.py` or `./run.py`.

## License

MIT


