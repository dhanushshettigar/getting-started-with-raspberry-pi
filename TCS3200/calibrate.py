import RPi.GPIO as GPIO
import time

s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)

def mesure():
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    return NUM_CYCLES / duration   #in Hz

def loop():
    while(1):
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.LOW)
        red = mesure()
        print("red value - ",red)

        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.HIGH)
        blue = mesure()
        print("blue value - ",blue)

        GPIO.output(s2,GPIO.HIGH)
        GPIO.output(s3,GPIO.HIGH)
        green = mesure()
        print("green value - ",green)

try:
    loop()

except KeyboardInterrupt:
    GPIO.cleanup()
     