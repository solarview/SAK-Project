import os

NUMBER_OF_MEDICINE_CONTAINER = 8
RESOURCE_DIR_PATH = os.path.dirname(
    os.path.realpath(__file__)) + "\\" + "resources" + "\\"

'''
Rpi Pin setting
'''

#GPIO setting
GPIO_BUZZER = 0

#ADC setting
ADC_SPI_DEVICE_NUM = 0
ADC_CHANNEL_BPM = 0