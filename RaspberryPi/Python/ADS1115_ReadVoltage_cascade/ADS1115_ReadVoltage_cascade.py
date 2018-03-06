import sys
sys.path.append('../')
import time
from DFRobot_ADS1115 import ADS1115
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()

while True :
    #Set the IIC address
    ads1115.setAddr_ADS1115(0x48)
    #Sets the gain and input voltage range.
    ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
    #Get the Digital Value of Analog of selected channel
    adc = ads1115.readVoltage(0)
    print "Digital Value of Analog of ADC1 A0 : %d mV"%(adc['r'])
    print " ********************************************* "
    time.sleep(0.8)
    adc = ads1115.readVoltage(1)
    print "Digital Value of Analog of ADC1 A1 : %d mV"%(adc['r'])
    print " ********************************************* "
    time.sleep(0.8)
    adc = ads1115.readVoltage(2)
    print "Digital Value of Analog of ADC1 A2 : %d mV"%(adc['r'])
    print " ********************************************* "
    time.sleep(0.8)
    adc = ads1115.readVoltage(3)
    print "Digital Value of Analog of ADC1 A3 : %d mV"%(adc['r'])
    print " ********************************************* "

    ads1115.setAddr_ADS1115(0x49)
    ads1115.setGain(ADS1115_REG_CONFIG_PGA_4_096V)
    adc = ads1115.readVoltage(0)
    print "Digital Value of Analog of ADC2 A0 : %d mV"%(adc['r'])
    print " ********************************************* "
    time.sleep(0.8)
    adc = ads1115.readVoltage(1)
    print "Digital Value of Analog of ADC2 A1 : %d mV"%(adc['r'])
    print " ********************************************* "
    time.sleep(0.8)
    adc = ads1115.readVoltage(2)
    print "Digital Value of Analog of ADC2 A2 : %d mV"%(adc['r'])
    print " ********************************************* "
    time.sleep(0.8)
    adc = ads1115.readVoltage(3)
    print "Digital Value of Analog of ADC2 A3 : %d mV"%(adc['r'])
    print " ********************************************* "
