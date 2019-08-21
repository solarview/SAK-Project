import spidev
import RPi.GPIO as GPIO
import time
import sak_setting


def set_gpios():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sak_setting.GPIO_BUZZER, GPIO.OUT)
    GPIO.setup(sak_setting.GPIO_BUTTON, GPIO.IN)


def get_from_adc(bus_num = 0, device_num: int = 0, channel: int = 0):
    spi = spidev.SpiDev()
    spi.open(bus_num, device_num)
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    acd_out = ((r[1] & 3) << 8) + r[2]
    return acd_out


def get_bpm():
    return get_from_adc(sak_setting.ADC_SPI_BUS_NUM, sak_setting.ADC_SPI_DEVICE_NUM, sak_setting.ADC_CHANNEL_BPM)


def out_beep_sound(sleep_duration: int):
    while True:
        GPIO.output(sak_setting.GPIO_BUZZER, GPIO.HIGH)
        time.sleep(sleep_duration)
        GPIO.output(sak_setting.GPIO_BUZZER, GPIO.LOW)
        time.sleep(sleep_duration)
