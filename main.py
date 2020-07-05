#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port, Button, Color, ImageFile, SoundFile
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks import ev3brick as brick
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
brick.sound.beep(1000, 500)
brick.sound.beep()
color_sensor = ColorSensor(Port.S1)
color = color_sensor.color()
left = Motor(Port.C)
right = Motor(Port.B)
robot = DriveBase(left, right, 56, 114)
brick.sound.beep()

while not color_sensor.color() == Color.BLACK:
    robot.drive(-10, 0)
    if color_sensor.color() == Color.BLACK:
        break
