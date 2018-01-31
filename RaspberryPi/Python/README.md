# ADS1115
The ADS1115 is a high precision analog-to-digital converter (ADC) with 16-bit resolution. And with A0-A3, 4 ADC ports


## DFRobot_ADS1115.py Library for Raspberry pi
---------------------------------------------------------
Provides an Raspberry pi library to read ADS1115 data over I2C. Use this library to read analog voltage values.
## Table of Contents

* [Installation](#installation)
* [Methods](#methods)
<snippet>
<content>

## Installation

Download and install smbus library on Raspberry pi. Steps to install smbus are provided at:

https://pypi.python.org/pypi/smbus-cffi/0.5.1 Download (or git pull) the code in pi.
The Raspberry pi i2c1 and the board's i2c interface connected.
Run the program:

```cpp

$> python DFRobot_MCP4725.py

```

Run the demo:

```cpp

$> python ADS1115_ReadVoltage.py

```

## Credits

Written by DFRobot_xiaowu, 2018. (Welcome to our [website](https://www.dfrobot.com/))
