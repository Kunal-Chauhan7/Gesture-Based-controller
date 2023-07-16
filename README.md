# Gesture-Based-controller-Glove
This is a IOT based project in which anyone even physically challenged can control their pc

## Main.ino
This code snippet demonstrates the usage of an MPU6050 accelerometer and gyroscope sensor along with buttons to control the movement of an object. Here's a breakdown of the code:

1. The necessary libraries, "Wire.h", "I2Cdev.h", and "MPU6050.h", are included. These libraries provide functions for working with the I2C communication protocol and the MPU6050 sensor.

2. Two constant variables, `buttonPin_right` and `buttonPin_left`, are defined with their corresponding pin numbers (7 and 8, respectively). These pins will be used to connect buttons for controlling the object.

3. Two integer variables, `buttonState_right` and `buttonState_left`, are declared to store the state of the buttons. They are initially set to 0.

4. The `MPU6050` object `mpu` is declared. This object will be used to interact with the MPU6050 sensor.

5. Several integer variables (`ax`, `ay`, `az`, `gx`, `gy`, `gz`) are defined to store the raw accelerometer and gyroscope data read from the MPU6050 sensor.

6. A struct called `MyData` is defined, which has two byte fields `X` and `Y`. This structure will be used to store the processed data from the accelerometer.

7. The `data` variable of type `MyData` is declared to hold the processed data.

8. The `setup()` function is called once during initialization. Inside this function:
   - Serial communication is started at a baud rate of 9600.
   - The I2C communication is initialized using `Wire.begin()`.
   - The MPU6050 sensor is initialized using `mpu.initialize()`.
   - The button pins (`buttonPin_right` and `buttonPin_left`) are set as inputs using `pinMode()`.

9. The `loop()` function is the main program loop that continuously executes. Inside this function:
   - A delay of 500 milliseconds is introduced using `delay(500)`.
   - The states of the right and left buttons are read using `digitalRead()` and stored in `buttonState_right` and `buttonState_left` variables.
   - If the left button is pressed (`buttonState_left == 1`), the string "leftClick" is printed to the Serial Monitor.
   - If the right button is pressed (`buttonState_right == 1`), the string "rightClick" is printed to the Serial Monitor.
   - The accelerometer and gyroscope data are read from the MPU6050 sensor using `mpu.getMotion6()` and stored in the respective variables (`ax`, `ay`, `az`, `gx`, `gy`, `gz`).
   - The accelerometer data is mapped from the range of -17000 to 17000 to a range of 0 to 255 and stored in the `data.X` and `data.Y` variables using `map()`.
   - Conditional statements are used to check the values of `data.X` and `data.Y` and print corresponding messages ("up", "down", "left", "right") to the Serial Monitor.

In summary, this code reads the accelerometer and gyroscope data from an MPU6050 sensor and maps the accelerometer data to a range of 0 to 255. It also monitors the state of two buttons and prints messages to the Serial Monitor based on the button states and the processed accelerometer data.

## Main.py
This code snippet utilizes a serial connection to receive data and control keyboard and mouse inputs based on the received data. Here's an explanation of the code:

1. The necessary libraries, `serial`, `pynput.mouse`, and `pynput.keyboard`, are imported. These libraries provide functions for serial communication and controlling the keyboard and mouse inputs.

2. The serial connection is established with a specific port ('COM7') and baud rate (9600) using the `serial.Serial()` function and stored in the variable `s`.

3. Instances of the `Controller` class from `pynput.keyboard` and `pynput.mouse` are created and stored in the variables `keyboard` and `mouse`, respectively.

4. The code enters an infinite loop using `while True`.

5. Inside the loop, data is read from the serial connection using `s.readline()`, and stored in the variable `data`.

6. Conditional statements are used to check the decoded and stripped value of `data` against different strings ("up", "down", "left", "right", "leftClick", "rightClick").

7. If the received data is "up", the code simulates pressing and releasing the up arrow key using the `keyboard.press()` and `keyboard.release()` functions, respectively. A delay of 0.4 seconds is introduced using `time.sleep()` between pressing and releasing the key.

8. Similar to step 7, if the received data is "down", "left", or "right", the corresponding arrow keys are simulated.

9. If the received data is "leftClick" or "rightClick", the code simulates pressing and releasing the left or right mouse button using the `mouse.press()` and `mouse.release()` functions, respectively. A delay of 1 second is introduced using `time.sleep()` between pressing and releasing the button.

10. After each action, a corresponding message is printed to the console.

In summary, this code reads data from a serial connection and controls keyboard and mouse inputs based on the received data. It simulates pressing and releasing arrow keys for movement and pressing and releasing mouse buttons for clicking.

## Circuit Diagram

![Cicuit Diagram 1](./images/diagram%201.png)

![Cicuit Diagram 2](./images/diagram%202.png)

## Picture of Working model

![Model Picture 1](./images/image%201.jpg)

![Model Picture 2](./images/image%202.jpg)


## video demonstration 

[![Watch the video](http://i3.ytimg.com/vi/3vMhn5RamHw/hqdefault.jpg)](https://youtu.be/3vMhn5RamHw)

