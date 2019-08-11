from serial import Serial

serialport = None

def call_by_gsm():
    global serialport
    serialport = Serial("/dev/ttyAMA0", 115200, timeout=0.5)
    serialport.write("AT\r")
    response = serialport.readlines(None)
    serialport.write("ATE0\r")
    response = serialport.readlines(None)
    serialport.write("AT\r")
    response = serialport.readlines(None)
    print(response)
    serialport.write("AT\r")
    response = serialport.readlines(None)
    serialport.write("ATD 119;\r")
    response = serialport.readlines(None)
    

def call_off():
    global serialport
    serialport.write("AT\r")
    response = serialport.readlines(None)
    serialport.write("ATH\r")
    response = serialport.readlines(None)
    print(response)