#!/usr/bin/env python
"""
Example python script to test the FY6xxx class library
Requires a FeelElec FY6800, however, a FY6600, will probably
work with for the most part, but may require some slight changes.

Requires:  pyserial

Developed in python 2.7 and tested with python 3.6.x

For library documentation issue the following at the command line:
pydoc FY6xxx

Licensed under the GPL v3 by Nikki Cooper.

-. ----- ----  Nikki Cooper:  initial version
4. April 2020  ChrisMicro:    frequency stepping example

"""

import FY6xxx
import math
import time


"""
 To list the available serial ports on your system:
 python -m serial.tools.list_ports
 """

# Set the FY6800 to some sane default values first
def setDefaults():
    # Set Default CH1 & CH2 waveform frequencies
    fy6800.setCh1WaveFreq(ch1WaveformFreqDef)
    fy6800.setCh2WaveFreq(ch2WaveformFreqDef)

    # Set Default CH1 & CH2 waveforms
    fy6800.setCh1WaveByKey(ch1WaveformDef)
    fy6800.setCh2WaveByKey(ch2WaveformDef)

    # Set Default CH1 & CH2 waveform amplitude voltage
    fy6800.setCh1WaveAmplitude(ch1WaveformAmplitudeDef)
    fy6800.setCh2WaveAmplitude(ch2WaveformAmplitudeDef)
    return

# Read the default settings from the FY6800
def readOriginal():
    # Read the ORIGINAL freq of CH1 & CH2 waverforms before changing them
    ch1WaveformFreqOrg = fy6800.getCh1WaveFreq()
    ch2WaveformFreqOrg = fy6800.getCh2WaveFreq()

    # Read ORIGINAL CH1 & CH2 waveform type keys before changing them
    ch1WaveformOrg = fy6800.getCh1WaveDesc()
    ch2WaveformOrg = fy6800.getCh2WaveDesc()

    # Read ORIGINAL CH1 & CH2 waveform amplitude voltages before changing them
    ch1WaveformAmplitudeOrg = fy6800.getCh1WaveAmplitude()
    ch2WaveformAmplitudeOrg = fy6800.getCh2WaveAmplitude()

    # Setup the ORIGINAL CH1 & CH2 strings to be printed
    CH1org = ch1WaveformOrg + ", " + ch1WaveformFreqOrg + " Hz, " + str(ch1WaveformAmplitudeOrg) + "V"
    CH2org = ch2WaveformOrg + ", " + ch2WaveformFreqOrg + " Hz, " + str(ch2WaveformAmplitudeOrg) + "V"

    # Print out the ORIGINAL CH1 & CH2 waveform type, waveform freq and waveform amplitude voltage
    print("Original CH1: " + CH1org)
    print("Original CH2: " + CH2org)
    return

# Once the desired NEW values are written to the FY6800, read them from the FY6800 into these
def readNew():
    # Read the NEW waveform type of CH1 & CH2
    ch2WaveformNew = fy6800.getCh2WaveDesc()
    ch1WaveformNew = fy6800.getCh1WaveDesc()

    # Read the NEW freq of CH1 & CH2 waverforms
    ch1WaveformFreqNew = fy6800.getCh1WaveFreq()
    ch2WaveformFreqNew = fy6800.getCh2WaveFreq()

    # Read the NEW waveform type amplitude voltage of CH1 & CH2
    ch1WaveformAmplitudeNew = fy6800.getCh1WaveAmplitude()
    ch2WaveformAmplitudeNew = fy6800.getCh2WaveAmplitude()

    # Setup the NEW CH1 & CH2 strings to be printed
    CH1new = ch1WaveformNew + ",     " + ch1WaveformFreqNew + " Hz, " + str(ch1WaveformAmplitudeNew) + "V"
    CH2new = ch2WaveformNew + ", "     + ch2WaveformFreqNew + " Hz, " + str(ch2WaveformAmplitudeNew) + "V"

    # Print out the NEW CH1 & CH2 waveform type, waveform freq and waveform amplitude voltage
    print("New CH1: " + CH1new)
    print("New CH2: " + CH2new)
    return
   
# Set the FY6800 with the new desired values
def setNew():
    fy6800.setCh2WaveByKey(ch2Waveform)
    fy6800.setCh1WaveByKey(ch1Waveform)

# Set NEW CH1 & CH2 waveform frequencies
    resp = fy6800.setCh1WaveFreq(ch1WaveformFreq)
    if resp == '0xa':
        print("\nCH1 frequency set to: " + str(float(ch1WaveformFreq) / 1000e9) + " MHz")

    resp = fy6800.setCh2WaveFreq(ch2WaveformFreq)
    if resp == '0xa':
        print("CH2 frequency set to:  " + str(float(ch2WaveformFreq) / 1000e6) + " KHz\n")

    # Set NEW CH1 & CH2 waveform amplitude voltage
    fy6800.setCh1WaveAmplitude(ch1WaveformAmplitude)
    fy6800.setCh2WaveAmplitude(ch2WaveformAmplitude)
    return

# convert the frequency into the FY6800 string format
# example: 1234.555666Hz converts to 00001234555666
#
def freq2String(f_Hz):
    text=format(math.trunc(f_Hz*1000*1000), '014d')
    return text

# Set the FY6800 with the new desired frequency
def setFrequency(f_Hz,channelNumber):
    if channelNumber==1:
      ch1WaveformFreq=freq2String(f_Hz)
      fy6800.setCh1WaveByKey(ch1Waveform)
       # Set NEW CH1 & CH2 waveform frequencies
      resp = fy6800.setCh1WaveFreq(ch1WaveformFreq)
      if resp == '0xa':
        print("\nCH1 frequency set to: " + str(float(ch1WaveformFreq) / 1000e9) + " MHz")
        # Set NEW CH1 & CH2 waveform amplitude voltage
        fy6800.setCh1WaveAmplitude(ch1WaveformAmplitude)

    else :
      ch2WaveformFreq=freq2String(f_Hz)

      fy6800.setCh2WaveByKey(ch2Waveform)    
      resp = fy6800.setCh2WaveFreq(ch2WaveformFreq)
      if resp == '0xa':
        print("CH2 frequency set to:  " + str(float(ch2WaveformFreq) / 1000e6) + " KHz\n")
        fy6800.setCh2WaveAmplitude(ch2WaveformAmplitude)

    return


# Tottles the on / off status of CH1 and CH2
def toggleOutputs(status):
    if status == ON:
        fy6800.setCh2Status(ON)
        fy6800.setCh1Status(ON)
    else:
        fy6800.setCh1Status(OFF)
        fy6800.setCh2Status(OFF)       
       

ON = 1
OFF = 0

# These are NEW the values written to the FY6800
ch1Waveform = 'Sine'
#ch2Waveform = 'Triangle'
ch2Waveform = 'Sine'

ch1WaveformFreq = "10115000000000"
ch2WaveformFreq = "00001000000000"
ch1WaveformAmplitude = "3.1459"
ch2WaveformAmplitude = "6.2918"

# The NEW values above, written to the FY6800, are then read into these
CH1new = ''
CH2new = ''
ch1WaveformNew = ''
ch2WaveformNew = ''
ch1WaveformFreqNew = ''
ch2WaveformFreqNew = ''
ch1WaveformAmplitudeNew = ''
ch2WaveformAmplitudeNew = ''

# DEFAULT settings to set CH1 & CH2 to.  Write to FY6800 to set some sane defaults.
ch1WaveformDef = 'Sine'
ch1WaveformFreqDef = "00010000000000"
ch1WaveformAmplitudeDef = "5.0"
ch2WaveformDef = ch1WaveformDef
ch2WaveformFreqDef = ch1WaveformFreqDef
ch2WaveformAmplitudeDef = ch1WaveformAmplitudeDef

# Read the DEFAULT settings from the FY6800 into these variables
CH1org = ''
CH2org = ''
ch1WaveformOrg = ''
ch2WaveformOrg = ''
ch1WaveformFreqOrg = ''
ch2WaveformFreqOrg = ''
ch1WaveformAmplitudeOrg = ''
ch2WaveformAmplitudeOrg = ''

"""
 
 FY6xx.FY6800 accepts the following parameters as defaults:
 
 device=None            The serial device such as '/dev/ttyUSB1'
 printsettings=None     Prints the serial device parameters and exits
 muteexeceptions=False  Mutes all serial port exception error messages
 readtimeout=1          Sets the serial device read timeout in seconds
 writetimeout=0.25      Sets the serial device write timeout in seconds
 
 ** At bare minimum you need to specify a valid serial device! **
 
 Note:  readtimeout and writetimeout deserve special consideration. 
        DO NOT set either of them to zero.  You have been warned! 
        Try the defaults first, and only change if there are timing issues.
        Probably shouldn't ever need changing, however, different systems may
        neeed special consideration.  YMMV. Just because this example code may
        use readtimeout=5, doesn't necessarily mean you should use it. 
 """



"""         
This test script accomplishes the following:
1 - Disable buzzer
2 - Disable CH1 & CH2
3 - Set various frequencies

NOTE:    It kind of sort of matters the order in which these functions are called.
WHY:     For some reason the display follows the command sent to the FY6800.
EXAMPLE: Toggling CH1 or CH2 is the same as pressing the CH1 or CH2 button on the unit.
         The screen changes to reflect this.  At first glance: Cool.
         In practice: Annoying.  Screen updates are slow.  The FY6800 can become confused
         if attempting to write data to it while these updates are occuring. I would have
         preferred the display to remain static and be given some remote commands to change
         to the desired display, but unfortunately the source code to the FY6800 is closed.
         Much room for improvement there.
"""

# !!! be sure to addapt the port seen by your PC !!!!!!
fy6800 = FY6xxx.FY6800("/dev/ttyUSB0", readtimeout=5)

print("FY6xxx test program\n")

# buzzer off
fy6800.setBuzzerStatus(OFF)
# CH1 & CH2 outputs disabled
toggleOutputs(OFF)
# Set the FY6800 CH1 & CH2 to some sane values
#setDefaults()
# Next, read them back and print em out
#readOriginal()
# Write the NEW values to the FY6800
#setNew()
# Last, read them back and print em out
# readNew()
# buzzer on
# fy6800.setBuzzerStatus(ON)
# CH1 & CH2 outputs enabled

#setFrequency(f_Hz,channelNumber):
setFrequency(1000,1)
setFrequency(1000,2)

toggleOutputs(ON)


for n in range(1,6):
  setFrequency(1000*n,1)
  setFrequency(1000*n,2)

  time.sleep(3);



print("\nThat's all folks!")

"""
Expected output:

FY6xxx test program


CH1 frequency set to: 0.001 MHz
CH2 frequency set to:  1.0 KHz


CH1 frequency set to: 0.001 MHz
CH2 frequency set to:  1.0 KHz


CH1 frequency set to: 0.002 MHz
CH2 frequency set to:  2.0 KHz


CH1 frequency set to: 0.003 MHz
CH2 frequency set to:  3.0 KHz


CH1 frequency set to: 0.004 MHz
CH2 frequency set to:  4.0 KHz


CH1 frequency set to: 0.005 MHz
CH2 frequency set to:  5.0 KHz


"""
