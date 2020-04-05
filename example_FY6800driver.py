#!/usr/bin/env python
"""
Example python script to test the simplified driver "FY6800driver.py"
for the FY6800 signal generator

5. April 2020  ChrisMicro:    initial version

"""

import FY6800driver as signalGenerator
import time

# !!! be sure to addapt the port seen by your PC !!!!!!
#  To list the available serial ports on your system:
#  python -m serial.tools.list_ports
sg=signalGenerator.FY6800driver("/dev/ttyUSB0",readtimeout=2)


channel=2
sg.setOutputOFF(channel)

channel=1
sg.setFrequency(1000,channel)

sg.setOutputON(channel)

sg.setAmplitude(3.3,channel)
time.sleep(3);

sg.setAmplitude(1.2345,channel)
time.sleep(3);

sg.setFrequency(2000,channel)


