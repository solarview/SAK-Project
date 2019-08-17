import spidev
import RPi.GPIO as GPIO
import time
import sak_setting


def set_gpios():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sak_setting.GPIO_BUZZER, GPIO.OUT)


def get_from_adc(device_num: int = 0, channel: int = 0):
    spi = spidev.SpiDev()
    spi.open(0,device_num)
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    acd_out = ((r[1]&3) << 8) + r[2]
    return acd_out


def get_bpm():
    return get_from_adc(sak_setting.ADC_SPI_DEVICE_NUM, sak_setting.ADC_CHANNEL_BPM)

def out_beep_sound(sleep_duration: int):
    p = GPIO.PWN(sak_setting.GPIO_BUZZER, 100)
    p.start(100)
    p.ChangeDutyCycle(90)
    p.ChangeFrequency(349)
    time.sleep(sleep_duration / 2)
    p.ChangeFrequency(329)
    time.sleep(sleep_duration / 2)
    p.stop()