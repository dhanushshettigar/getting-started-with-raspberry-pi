import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

while True:
    try:
        id = reader.read()
        print(id)
    finally:
        GPIO.cleanup()