import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(pins, GPIO.OUT)
dynamic_range = 3.16

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range: .2f} B)")
        print("устанавливаем 0.0 B")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    GPIO.output(pins, [int(element) for element in bin(number)[2:].zfill(8)])

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы не ввели число\n")
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()