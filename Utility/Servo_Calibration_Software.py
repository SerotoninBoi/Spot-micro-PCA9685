import tkinter as tk
from board import SCL, SDA
from busio import I2C
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# Initialize the PCA9685
i2c = I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

# Create servo objects
servos = [servo.Servo(pca.channels[i]) for i in range(12)]

# Function to set servo angle
def set_servo_angle(servo_number, angle):
    servos[servo_number].angle = angle

# GUI creation
root = tk.Tk()
root.title("Servo Calibrator")

for i in range(12):
    row = tk.Frame(root)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    label = tk.Label(row, text=f"Servo {i}", width=10)
    label.pack(side=tk.LEFT)

    slider = tk.Scale(
        row,
        from_=0,
        to=180,
        orient=tk.HORIZONTAL,
        command=lambda angle, i=i: set_servo_angle(i, int(angle)),
    )
    slider.set(90)
    slider.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

root.mainloop()