# Read and Write RFID Tags With Raspberry Pi

Reading and writing data to and from RFID tags requires an RFID Reader and RFID Tags. With the help of the RFID Reader, the Raspberry Pi can read data from these RFID tags and at the same time write data into it.

# Wiring the RC522 to the Raspberry Pi

![reference-raspberrytips](https://raw.githubusercontent.com/dhanushshettigar/getting-started-with-raspberry-pi/main/images/RFID-PI.jpg)

| RC522 | Raspberry Pi     |
| :-------- | :------- |
| `SDA` | `GPIO 8` |
| `SCK` | `GPIO 11` |
| `MOSI` | `GPIO 10` |
| `MISO` | `GPIO 9` |
| `GND` | `GND` |
| `RST` | `GPIO 25` |
| `3.3V` | `3.3V` |

# Enabling SPI

- **Open a terminal**. If you are using the Raspberry Pi Desktop you can open a terminal by pressing **CTRL+ALT+T** at the same to open a terminal. But if you are using headless mode, you can connect via SSH and go from there.
- Open the raspi-config tool:

```bash
  sudo raspi-config
```
- Go to “Interface option” > “SPI”.
- "Would you like the SPI interface to be enabled?" Yes!
- Exit raspi-config and accept to reboot the device.

That’s it. You have SPI enabled.

# Setting up virtual environments

Since the release of Raspberry Pi OS Bookworm, it is now mandatory to run virtual environments when working with Python packages. The reason for this is to prevent any changes to the system-level Python packages and to have a separate area to work on.

**Execute this command to create a virtual environment:**

```bash
python3 -m venv foobar
```

- **-m** – Command tells Python that you’ll be running a module.
- **venv** – This module is what we’ll be running to create a virtual environment.
- **foobar** – This is the name we will give to our virtual environment. You can also specify the path here where you want to store this virtual environment.

**To run the virtual environment, execute the following command:**

```bash
source foobar/bin/activate
```

- **source** – Tells Python that we will be running a virtual environment.
- **foobar/bin/activate** – This tells where our virtual environment is and where to find the ‘activate’ script to run the environment.

Once you run this, you should see (foobar) before in your terminal. This indicates that you are in your “foobar” virtual environment.

# Install Python libraries

In order to use the SPI in our Python scripts, we need to install the spi-dev library.

**Execute this command in the terminal to install the spi-dev library:**

```bash
sudo apt-get install python3-spidev
```

Another library that we also need to install is the MFRC522. This will be used to interact with the RC522 Module.

**To install this, run the following command:**

```bash
sudo pip3 install mfrc522-python
```

## Acknowledgements

[Raspberry Tips](https://raspberrytips.com/)