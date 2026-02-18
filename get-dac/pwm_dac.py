import RPi.GPIO as GPIO
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    
    def set_number(self, number):
        GPIO.output(self.gpio_pin, [int(element) for element in bin(number)[2:].zfill(8)])
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range: .2f} B)")
            print("устанавливаем 0.0 B")
            return 0
        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)
        return number