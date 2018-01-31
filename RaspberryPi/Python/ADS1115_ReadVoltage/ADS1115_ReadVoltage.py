import sys
sys.path.append('../')
import time
from DFRobot_ADS1115 import ADS1115
ADS1115_REG_CONFIG_PGA_6_144V		= 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V		= 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V		= 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V		= 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V		= 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V		= 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()

while True :
  #Set the IIC address
	ads1115.setAddr_ADS1115(0x49)
  #Sets the gain and input voltage range.
	ads1115.set_gain(ADS1115_REG_CONFIG_PGA_4_096V)
  #Get the channel you need to enter
	ads1115.set_channel()
  #Configuration using a single read
	ads1115.config_single_ended()
	time.sleep(0.1)
  #Read ADC value
	adc = ads1115.read_adc()
	print "Digital Value of Analog Input : %d mV"%(adc['r'])
	print " ********************************************* "
	time.sleep(0.8)