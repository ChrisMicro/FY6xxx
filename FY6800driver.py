"""

simpified driver class for signal generator FY6800 

based on the testFy.py python script licensed under the GPL v3 
by Nikki Cooper.


List of authors:

-. ----- ----  Nikki Cooper:  testFy.py
5. April 2020  ChrisMicro:    initial version of FY6800driver.py

"""

import FY6xxx
import math

# convert the frequency into the FY6800 string format
# example: 1234.555666Hz converts to 00001234555666
#
def freq2String(f_Hz):
    text=format(math.trunc(f_Hz*1000*1000), '014d')
    return text

# convert the amplitude into the FY6800 string format
#
def amplitude2String(amp_Volt):
    text=f"{amp_Volt:.4f}"
    return text

class FY6800driver:
  """ A simple driver for the FY6800 Signal Generator"""

  ON = 1
  OFF = 0

  # These are NEW the values written to the FY6800
  ch1Waveform = 'Sine'
  #ch2Waveform = 'Triangle'
  ch2Waveform = 'Sine'

  ch1WaveformFreq = "00001000000000"
  ch2WaveformFreq = "00001000000000"
  ch1WaveformAmplitude = "1.0"
  ch2WaveformAmplitude = "1.0"

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

  fy6800=[]

  def __init__(self,serialPort,readtimeout=5):
    print("init FY68000 signal generator")
    self.fy6800 = FY6xxx.FY6800("/dev/ttyUSB0", readtimeout=5)
    # Set the FY6800 with the new desired frequency

  # turn generator output voltage ON
  def setOutputON(self,channelNumber):
    if channelNumber == 1:
        self.fy6800.setCh1Status(self.ON) 
    else:
        self.fy6800.setCh2Status(self.ON)
       
  # turn generator output voltage ON
  def setOutputOFF(self,channelNumber):
    if channelNumber == 1:
        self.fy6800.setCh1Status(self.OFF) 
    else:
        self.fy6800.setCh2Status(self.OFF)

  # Set the FY6800 with the new desired frequency
  def setFrequency(self,f_Hz,channelNumber):
      if channelNumber==1:
        self.ch1WaveformFreq=freq2String(f_Hz)
        self.fy6800.setCh1WaveByKey(self.ch1Waveform)
         # Set NEW CH1 & CH2 waveform frequencies
        resp = self.fy6800.setCh1WaveFreq(self.ch1WaveformFreq)
        if resp == '0xa':
          print("\nCH1 frequency set to: " + str(float(self.ch1WaveformFreq) / 1000e6) + " KHz")
          # Set NEW CH1 & CH2 waveform amplitude voltage
          self.fy6800.setCh1WaveAmplitude(self.ch1WaveformAmplitude)
        else:
          print("FY6xxx communikation error")

      else :
        self.ch2WaveformFreq=freq2String(f_Hz)

        self.fy6800.setCh2WaveByKey(self.ch2Waveform)    
        resp = self.fy6800.setCh2WaveFreq(self.ch2WaveformFreq)
        if resp == '0xa':
          print("CH2 frequency set to:  " + str(float(self.ch2WaveformFreq) / 1000e6) + " KHz\n")
          self.fy6800.setCh2WaveAmplitude(self.ch2WaveformAmplitude)
        else:
          print("FY6xxx communikation error")

      return

  # Set the FY6800 with the new desired Amplitude
  def setAmplitude(self,amp_Volt,channelNumber):
      if channelNumber==1:
        self.ch1WaveformAmplitude=amplitude2String(amp_Volt)
        #self.fy6800.setCh1WaveByKey(self.ch1Waveform)
         # Set NEW CH1 & CH2 waveform amplitudes

        resp = self.fy6800.setCh1WaveAmplitude(self.ch1WaveformAmplitude)
        if resp == '0xa':
          print("\nCH1 amplitude set to: " + str(float(self.ch1WaveformAmplitude) ) + " Volt")
          # Set NEW CH1 & CH2 waveform amplitude voltage
          #self.fy6800.setCh1WaveAmplitude(self.ch1WaveformAmplitude)
        else:
          print("FY6xxx communikation error")

      else :
        self.ch1WaveformAmplitude=amplitude2String(amp_Volt)

        #self.fy6800.setCh2WaveByKey(self.ch2Waveform)    
        resp = self.fy6800.setCh2WaveAmplitude(self.ch2WaveformAmplitude)
        if resp == '0xa':
          print("CH2 amplitude set to:  " + str(float(self.ch2WaveformAmplitude) ) + " Volt\n")
          #self.fy6800.setCh2WaveAmplitude(self.ch2WaveformAmplitude)
        else:
          print("FY6xxx communikation error")

      return





