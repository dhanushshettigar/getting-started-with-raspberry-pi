import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()
GPIO.setwarnings(False)

# Run read.py to get your key and replace here
access_rfid = "837634989748"

try:
    print('Started Reading')
    while True:
        id, text = reader.read()
        print(id)
        if str(id) == access_rfid:
            print('Access Granted')
        else:
            print('Access Denied')
        time.sleep(1)
finally:
    GPIO.cleanup()