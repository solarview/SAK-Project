import spidev
import RPi.GPIO as GPIO
import time
import sak_core
import json

BUZZER = 0
BPM_CHN = 0
BPM_ADC = 0

def set_gpios():
    global BUZZER, BPM_CHN, BPM_ADC
    f = open(sak_core.RESOURCE_DIR_PATH + "gpio_setting_pin", "r+")
    js = json.loads(f.read())

    BPM_CHN = js["bpm_channel"]
    BPM_ADC = js["bpm_adc"]

    BUZZER = js["buzzer_gpio"]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.setup(BUZZER, False)


def get_from_adc(device_num: int, channel: int):
    spi = spidev.SpiDev()
    spi.open(0,device_num)
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    acd_out = ((r[1]&3) << 8) + r[2]
    return acd_out


def get_bpm():
    return get_from_adc(BPM_ADC, BPM_CHN)

def out_beep_sound(sleep_duration: int):
    GPIO.output(BUZZER, True)
    time.sleep(sleep_duration)
    GPIO.output(BUZZER, False)