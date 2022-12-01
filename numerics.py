#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:46:34 2022

@author: jonathanmaurer
"""
import numpy as np

tf = 1
dt = 0.01
n = int(tf / dt)
t = np.linspace(0, tf, n)


def fx(t):  # Set of slopes, change function for diff ODE's
    for i in range(1, n):
        dx[i] = -3 * t[i]
    return dx


dx = np.zeros([int(n)])  # Recieving arrrays for dx ans
dx = fx(t)


def FwdEuler_1d(fx, tf, dt):
    for i in range(1, n):
        x[i] = x[i - 1] + (dx[i - 1]) * dt
    return x


x = np.zeros([int(n)])  # Recieving arrrays for x ans
x0 = 10
x[0] = x0
x = FwdEuler_1d(fx(t), tf, dt)

import matplotlib.pyplot as plt

plt.plot(t, x)
plt.xlabel("Time")
plt.ylabel("X")
