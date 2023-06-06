import machine
import math
import utime

# LED pin numbers
led_pins = [2, 3, 4, 5]

# Frequencies for each LED (in Hz)
frequencies = [90, 110, 130, 150]

# Create PWM instances for each LED
pwms = [machine.PWM(machine.Pin(pin)) for pin in led_pins]

# Modulation parameters
num_steps = 360  # Number of steps in the sine wave
max_intensity = 65535  # Maximum intensity (duty cycle)

# Initialize phase and time references for each LED
phases = [0] * len(led_pins)
start_times = [utime.ticks_us()] * len(led_pins)

# Modulate LED intensities in sine waves
while True:
    current_time = utime.ticks_us()
    
    for i, pwm in enumerate(pwms):
        freq = frequencies[i]
        period = 1 / freq
        time_delta = utime.ticks_diff(current_time, start_times[i]) / 1_000_000
        
        # Calculate the intensity based on the current phase and time delta
        intensity = max_intensity * (math.sin(2 * math.pi * freq * time_delta + phases[i]) + 1) / 2
        pwm.duty_u16(int(intensity))
        
        # Check if it's time to update the phase and start time for the LED
        if time_delta >= period:
            phases[i] += 2 * math.pi * freq * period
            start_times[i] = current_time
    
    # Wait for a short period before the next iteration
    utime.sleep_us(10)
