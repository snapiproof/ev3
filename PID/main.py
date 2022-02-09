#!/usr/bin/env python3
from ev3dev.ev3 import *
from math import pi
import time

mR = LargeMotor("outA")
mL = LargeMotor("outD")
gyro = GyroSensor("in3")
ts = TouchSensor("in2")

def U_satur(U,lowerLimit,upperLimit):
    if U > upperLimit:
        return upperLimit
    if U < lowerLimit:
        return lowerLimit
    return U

kp = 15
ki = 0
kd = 10

I = 0
u = 0
DEG0 = gyro.rate_and_angle[0]

t = time.time()

while True :
    dt = time.time() - t
    t = time.time()
    I = dt * (gyro.rate_and_angle[0] - DEG0) + I

    u = (kp * (gyro.rate_and_angle[0] - DEG0) + ki * I + kd * gyro.rate_and_angle[1])
    UU = U_satur(u,-100,100)

    print(kp * (gyro.rate_and_angle[0] - DEG0), ki * I, kd * gyro.rate_and_angle[1])

    if ts.is_pressed:
        mR.run_direct(duty_cycle_sp = 0)
        mL.run_direct(duty_cycle_sp = 0)
        DEG0 = gyro.rate_and_angle[0]
        I = 0
    else:
    	mR.run_direct(duty_cycle_sp = UU)
    	mL.run_direct(duty_cycle_sp = UU)

mR.run_direct(duty_cycle_sp = 0)
mL.run_direct(duty_cycle_sp = 0)
