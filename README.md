# ADS1115
The ADS1115 is a high precision analog-to-digital converter (ADC) with 16-bit resolution. And with A0-A3, 4 ADC ports


## DFRobot_ADS1115 Library for Arduino
---------------------------------------------------------
Provides an Arduino library to read ADS1115 data over I2C. Use this library to read analog voltage values.
## Table of Contents

* [Installation](#installation)
* [Methods](#methods)

* [History](#history)
* [Credits](#credits)
* [Compatibility](#compatibility)
<snippet>
<content>

## Installation

To use this library download the zip file, uncompress it to a folder named DFRobot_ADS1115. 
Download the zip file first to use this library and uncompress it to a folder named DFRobot_ADS1115. 

## Methods

```C++

#include <DFRobot_ADS1115.h>
#define ADS1115_IIC_ADDRESS0         (0x48)
#define ADS1115_IIC_ADDRESS1         (0x49)
/*
 * @brief Sets the IIC address
 */
void setAddr_ADS1115(IIC_ADDRESS);

 typedef enum
{
    eGAIN_TWOTHIRDS      = ADS1115_REG_CONFIG_PGA_6_144V, /*ADC Range: 0~6.144V (1 bit = 0.1875mV)*/
    eGAIN_ONE            = ADS1115_REG_CONFIG_PGA_4_096V, /*ADC Range: 0~4.096V (1 bit = 0.125mV)*/
    eGAIN_TWO            = ADS1115_REG_CONFIG_PGA_2_048V, /*ADC Range: 0~2.048V (1 bit = 0.0625mV)*/
    eGAIN_FOUR           = ADS1115_REG_CONFIG_PGA_1_024V, /*ADC Range: 0~1.024V (1 bit = 0.03125mV)*/
    eGAIN_EIGHT          = ADS1115_REG_CONFIG_PGA_0_512V, /*ADC Range: 0~0.512V (1 bit = 0.015625mV)*/
    eGAIN_SIXTEEN        = ADS1115_REG_CONFIG_PGA_0_256V  /*ADC Range: 0~0.256V (1 bit = 0.0078125mV)*/
} eADSGain_t;
/*
 * @brief Sets the gain and input voltage range.
          This configures the programmable gain amplifier
 */
void setGain(eADSGain_t gain);

typedef enum
{
    eMODE_CONTIN         = ADS1115_REG_CONFIG_MODE_CONTIN,
    eMODE_SINGLE         = ADS1115_REG_CONFIG_MODE_SINGLE
} eADSMode_t;
/*
 * @brief Sets the Device operating mode.
 *        This controls the current operational mode of the ADS1115
 */
void setMode(eADSMode_t mode);

typedef enum
{
    eRATE_8              = ADS1115_REG_CONFIG_DR_8SPS,
    eRATE_16             = ADS1115_REG_CONFIG_DR_16SPS,
    eRATE_32             = ADS1115_REG_CONFIG_DR_32SPS,
    eRATE_64             = ADS1115_REG_CONFIG_DR_64SPS,
    eRATE_128            = ADS1115_REG_CONFIG_DR_128SPS,
    eRATE_250            = ADS1115_REG_CONFIG_DR_250SPS,
    eRATE_475            = ADS1115_REG_CONFIG_DR_475SPS,
    eRATE_860            = ADS1115_REG_CONFIG_DR_860SPS
} eADSRate_t;
/*
 * @brief Sets the Date Rate
          This controls the data rate setting
 */
void setRate(eADSRate_t rate);

typedef enum
{
    eOSMODE_SINGLE       = ADS1115_REG_CONFIG_OS_SINGLE,
    eOSMODE_BUSY         = ADS1115_REG_CONFIG_OS_BUSY,
    eOSMODE_NOTBUSY      = ADS1115_REG_CONFIG_OS_NOTBUSY
} eADSOSMode_t;
/*
 * @brief Sets the Operational status/single-shot conversion to start
          This determines the operational status of the device
 */
void setOSMode(eADSOSMode_t osmode);

/*
 * @brief Gets the Operational status/single-shot conversion start
 * @return result:
 *     eADSOSMode_t
 */
eADSOSMode_t getOSMode();

typedef enum
{
    eCOMPMODE_TRAD       = ADS1115_REG_CONFIG_CMODE_TRAD,
    eCOMPMODE_WINDOW     = ADS1115_REG_CONFIG_CMODE_WINDOW
} eADSCompMode_t;
/*
 * @brief Sets the Comparator mode
 *        This controls the comparator mode of operation
 */
 
void setCompMode(eADSCompMode_t compmode);

typedef enum
{
    eCOMPPOL_LOW         = ADS1115_REG_CONFIG_CPOL_ACTVLOW,
    eCOMPPOL_HIGH        = ADS1115_REG_CONFIG_CPOL_ACTVHI
} eADSCompPol_t;
/*
 * @brief Sets the Comparator polarity
 *        This controls the polarity of the ALERT/RDY pin
 */
void setCompPol(eADSCompPol_t comppol);

/*
 * @brief Gets the Comparator polarity
 *
 * @return result:
 *     eADSCompPol_t
 */
eADSCompPol_t getCompPol();

typedef enum
{
    eCOMPLAT_NONLAT      = ADS1115_REG_CONFIG_CLAT_NONLAT,
    eCOMPLAT_LATCH       = ADS1115_REG_CONFIG_CLAT_LATCH
} eADSCompLat_t;
/*
 * @brief Sets the Latching comparator
 *        This controls whether the ALERT/RDY pin latches once asserted 
 *        or clears when conversions are within the margin of the upper 
 *        and lower threshold values
 */
void setCompLat(eADSCompLat_t complat);

/*
 * @brief Gets the Latching comparator
 *
 * @return result:
 *     eADSCompLat_t
 */
eADSCompLat_t getCompLat();

typedef enum
{
    eCOMPQUE_ONE         = ADS1115_REG_CONFIG_CQUE_1CONV,
    eCOMPQUE_TWO         = ADS1115_REG_CONFIG_CQUE_2CONV,
    eCOMPQUE_FOUR        = ADS1115_REG_CONFIG_CQUE_4CONV,
    eCOMPQUE_NONE        = ADS1115_REG_CONFIG_CQUE_NONE
} eADSCompQue_t;
/*
 * @brief Sets the Comparator queue and disable
          This perform two functions. 
          It can disable the comparator function and put the ALERT/RDY pin into a high state.
          It also can control the number of successive conversions exceeding the upper 
          or lower thresholds required before asserting the ALERT/RDY pin.
 */
void setCompQue(eADSCompQue_t compque);

/*
 * @brief Gets the Comparator queue and disable
 *
 * @return result:
 *     eADSCompQue_t
 */
eADSCompQue_t getCompQue();

/*
 * @brief Sets the low threshold value
 */
void setLowThreshold(int16_t threshold);

/*
 * @brief Gets the low threshold value
 *
 * @return result:
 *      Low threshold
 */
int16_t getLowThreshold();

/*
 * @brief Sets the high threshold value
 */
void setHighThreshold(int16_t threshold);

/*
 * @brief Gets the high threshold value
 *
 * @return result:
 *      High threshold
 */
int16_t getHighThreshold();

/*
 * @brief init ADS1115 device
 */
void init(void);

/*
 * @brief Checks the connection status of ads1115
 *
 *@return result:
 *     true or false
 */
bool checkADS1115(void);

/*
 * @brief Reads the voltage of the specified channel
 *
 * @return result:
 *      Voltage
 */
uint16_t readVoltage(uint8_t channel);

/*
 * @brief Sets up the comparator causing the ALERT/RDY pin to assert 
 *      (go from high to low) when the ADC value exceeds the specified upper or lower threshold
 *      ADC is Differential input channel
 *
 * @return result:
 *      Voltage
 */
int16_t ComparatorVoltage(uint8_t channel)
```

## Compatibility

MCU                | Work Well | Work Wrong | Untested  | Remarks
------------------ | :----------: | :----------: | :---------: | -----
FireBeetle-ESP32  |      √       |             |            | 
FireBeetle-ESP8266  |      √       |             |            | 
Arduino uno |       √      |             |            | 


## Credits

Written by DFRobot_xiaowu, 2018. (Welcome to our [website](https://www.dfrobot.com/))
