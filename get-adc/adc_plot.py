from matplotlib import pyplot as plt
import RPi.GPIO as GPIO
import time
import r2r_adc as r2r

def plot_voltage_vs_time(rime, voltage, max_voltage):
    plt.figure(figsize = (10, 6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid(True)
    plt.show()

voltage_values = []
time_values = []
duration = 3.0

try:
    dac = r2r.R2R_ADC(3.29, 0.0001)
    start = time.time()
    while (time.time() - start) < duration:
        c = time.time() - start
        vol = dac.get_sc_voltage()
        voltage_values.append(vol)
        time_values.append(c)
    plot_voltage_vs_time(time_values, voltage_values, 3.29)
finally:
    dac.deinit()