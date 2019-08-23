import os

NUMBER_OF_MEDICINE_CONTAINER = 8
RESOURCE_DIR_PATH = os.path.dirname(
    os.path.realpath(__file__)) + "\\" + "resources" + "\\"

'''
Rpi Pin setting
'''

#GPIO setting
GPIO_BUZZER = 24
GPIO_BUTTON = 22

#ADC setting
ADC_SPI_BUS_NUM = 1
ADC_SPI_DEVICE_NUM = 0
ADC_CHANNEL_BPM = 0

'''
RPi <-> ADC pinout
pin 12 <-> CS or CE 0 , ADC_SPI_DEVICE_NUM = 0
pin 11 <-> CS or CE 1 , ADC_SPI_DEVICE_NUM = 1
pin 36 <-> CS or CE 2 , ADC_SPI_DEVICE_NUM = 2
pin 35 <-> MISO
pin 38 <-> MOSI
pin 40 <-> SCLK or CLK
'''
