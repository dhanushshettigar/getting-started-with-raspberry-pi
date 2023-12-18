
# BME280 Temperature, Humidity and Pressure Sensor

Learn how to interface the BME280 sensor with the Raspberry Pi to get temperature, humidity, and pressure readings. You’ll learn how to connect the sensor to the Raspberry Pi board and write a Python script that gets sensor data and displays it on the terminal.

# Wiring the BME280 to the Raspberry Pi

![reference-randomnerdtutorials](https://raw.githubusercontent.com/dhanushshettigar/getting-started-with-raspberry-pi/main/images/BME280-PI.jpg)

| BME280 | Raspberry Pi     |
| :-------- | :------- |
| `Vcc` | `3.3v` |
| `Gnd` | `Gnd` |
| `SCL` | `GPIO 3` |
| `SDA` | `GPIO 2` |

# Enabling I2C

- **Open a terminal**. If you are using the Raspberry Pi Desktop you can open a terminal by pressing **CTRL+ALT+T** at the same to open a terminal. But if you are using headless mode, you can connect via SSH and go from there.
- Open the raspi-config tool:

```bash
  sudo raspi-config
```
- Go to “Interface option” > “I2C”.
- "Would you like the SPI interface to be enabled?" Yes!
- Exit raspi-config and accept to reboot the device.

That’s it. You have I2C enabled.


# Getting the Sensor I2C Address

With the sensor connected to the Raspberry Pi, let’s check if the sensor is connected properly by searching for its I2C address.

Open a Terminal window on your Raspberry Pi and run the following command:


```bash
  sudo i2cdetect -y 1
```

It should show your sensor I2C address:

![reference-randomnerdtutorials](https://raw.githubusercontent.com/dhanushshettigar/getting-started-with-raspberry-pi/main/images/DETECT.jpg)

# About Python virtual environments

In previous versions of the operating system, it was possible to install libraries directly, system-wide, using the package installer for Python, commonly known as pip. You’ll find the following sort of command in many tutorials online.

```bash
  pip install buildhat
```

In newer versions of Raspberry Pi OS, and other operating systems, this is disallowed. If you try and install a Python package system-wide you’ll receive an error similar to this:

```bash
$ pip install buildhat
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
  python3-xyz, where xyz is the package you are trying to
  install.

  If you wish to install a non-Debian-packaged Python package,
  create a virtual environment using python3 -m venv path/to/venv.
  Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
  sure you have python3-full installed.

  For more information visit http://rptl.io/venv

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

This error is generated because you’re trying to install a third-party package into the system Python. A long-standing practical problem for Python users has been conflicts between OS package managers like apt and Python-specific package management tools like pip. These conflicts include both Python-level API incompatibilities and conflicts over file ownership.

Therefore from Bookworm onwards, packages installed via pip must be installed into a Python virtual environment using venv. A virtual environment is a container where you can safely install third-party modules so they won’t interfere with, or break, your system Python.

## Using pip with virtual environments

[Follow this documentation](https://www.raspberrypi.com/documentation/computers/os.html#installing-python-packages-using-apt)

## Breaking The System (Not Recommended But Works!!!)

```bash
  # make sure you replace python version
  sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
```

# Install BME280 Library

There are several libraries compatible with the Raspberry Pi to read from the BME280 sensor. We’ll be using the RPi.BME280 library. This library is available to install through PIP (a package manager for Python packages).

First, install or upgrade pip by running the following command:

```bash
  sudo pip install --upgrade pip
```

Then, run the following command to install the library using pip:

```bash
  sudo pip install RPI.BME280
```
## Acknowledgements

 [Random Nerd Tutorials](https://randomnerdtutorials.com/)
