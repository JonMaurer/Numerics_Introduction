#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:46:34 2022

@author: jonathanmaurer

Basic 4th order RK methods for solving ODEs
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Equations (Change)
def fx(t, x):
    return -0.4 * x


def fy(t, x, y, z):
    rho = 28
    return x * (rho - z - y)


def fz(t, x, y, z):
    beta = 8 / 3
    return (x * y) - (beta * z)


#%% Explicit Functions
def FwdEuler_1d(fx, t0, x0, te, dt):
    t = np.arange(t0, te + dt, dt)

    x = np.zeros(len(t))
    x[0] = x0
    for i in range(1, len(t)):
        x[i] = x[i - 1] + fx(t[i - 1], x[i - 1]) * dt
    return t, x


def FwdEuler_2d(fx, fy, t0, x0, y0, te, dt):
    t = np.arange(t0, te + dt, dt)

    x = np.zeros(len(t))
    x[0] = x0
    y = np.zeros(len(t))
    y[0] = y0

    for i in range(1, len(t)):
        x[i] = x[i - 1] + fx(t[i - 1], x[i - 1], y[i - 1]) * dt
        y[i] = y[i - 1] + fy(t[i - 1], x[i - 1], y[i - 1]) * dt
    return t, x, y


def FwdEuler_3d(fx, fy, fz, t0, x0, y0, z0, te, dt):
    t = np.arange(t0, te + dt, dt)

    x = np.zeros(len(t))
    x[0] = x0
    y = np.zeros(len(t))
    y[0] = y0
    z = np.zeros(len(t))
    z[0] = z0

    for i in range(1, len(t)):
        x[i] = x[i - 1] + fx(t[i - 1], x[i - 1], y[i - 1], z[i - 1]) * dt
        y[i] = y[i - 1] + fy(t[i - 1], x[i - 1], y[i - 1], z[i - 1]) * dt
        z[i] = z[i - 1] + fz(t[i - 1], x[i - 1], y[i - 1], z[i - 1]) * dt
    return t, x, y, z


def midpoint_1d(fx, t0, x0, te, dt):
    t = np.arange(t0, te + dt, dt)

    x = np.zeros(len(t))
    x[0] = x0
    for i in range(1, len(t)):
        x[i] = x[i - 1] + dt * fx(
            t[i - 1] + dt / 2, x[i - 1] + (dt / 2) * fx(t[i - 1], x[i - 1])
        )
    return t, x


#%% Testing + Plotting
t, x = midpoint_1d(fx, 0, 10, 10, 0.01)

plt.figure()
plt.plot(t, x)
