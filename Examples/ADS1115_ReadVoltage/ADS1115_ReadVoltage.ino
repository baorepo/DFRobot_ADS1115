/*
 * file ADS1115_ReadVoltage.ino
 *
 * @ https://github.com/DFRobot/DFRobot_ADS1115
 *
 * connect ADS1115 I2C interface with your board (please reference board compatibility)
 *
 * The voltage value read by A0 A1 A2 A3 is printed through the serial port.
 *
 * Copyright   [DFRobot](http://www.dfrobot.com), 2016
 * Copyright   GNU Lesser General Public License
 *
 * version  V1.0
 * date  2018-01-21
 */
#include <DFRobot_ADS1115.h>

DFRobot_ADS1115 ads;

void setup(void) 
{
    Serial.begin(115200);
    ads.setAddr_ADS1115(ADS1115_IIC_ADDRESS0);   // 0x48
    ads.setGain(eGAIN_TWOTHIRDS);   // 2/3x gain  6.144V
    ads.setMode(eMODE_CONTIN);       // Continuous conversion mode
    ads.setRate(eRATE_128);          // 128SPS (default)
    ads.setOSMode(eOSMODE_SINGLE);   // Set to start a single-conversion
    ads.init();
}

void loop(void) 
{
    if (ads.check_ads1115())
    {
        int16_t adc0, adc1, adc2, adc3;
        adc0 = ads.readVoltage(0);
        Serial.print("The voltage value of A0 is: ");
        Serial.print(adc0);
        Serial.println("mV");
        adc1 = ads.readVoltage(1);
        Serial.print("The voltage value of A1 is: ");
        Serial.print(adc1);
        Serial.println("mV");
        adc2 = ads.readVoltage(2);
        Serial.print("The voltage value of A2 is: ");
        Serial.print(adc2);
        Serial.println("mV");
        adc3 = ads.readVoltage(3);
        Serial.print("The voltage value of A3 is: ");
        Serial.print(adc3);
        Serial.println("mV");
    }
    else
    {
        Serial.println("ADS1115 Disconnected!");
    }

    delay(1000);
}
