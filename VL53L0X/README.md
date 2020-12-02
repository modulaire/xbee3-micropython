The example here is for PWM control, after reception of a lidar sensor.
To control a brushless motor with this pwm pulse it is required to use additional hardware. Starting with a classic arduino we can create 50Hz pulse using the servo library.
To minimalize the electonic footprint we can use an attiny. However the servo library does not work on an attiny. We thus need to manually change the pwm cycle. The codes for this stuff are found in the arduino-brushless-control folder.
