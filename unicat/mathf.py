import math, string, random
import os, sys
import asyncio, time
import re, struct, typing
import getpass
import socket, select, selectors, pickle
import tkinter as tk
import json, csv
import threading as thr
import _thread as thread

__import__ = [
    "math",
    "string",
    "random",
    "os",
    "sys",
    "asyncio",
    "time",
    "re",
    "struct",
    "typing",
    "getpass",
    "socket",
    "select",
    "selectors",
    "pickle",
    "tkinter",
    "json",
    "csv",
    "threading",
    "_thread"
]

# Add Subtract Multiply Divide

"""Addition: Any amount of arguments are allowed: Example: 1 + 1 = 2"""
def add(*args):
    return sum(args)

"""Subtraction: Any amount of arguments are allowed: Example: 5 - 2 = 3"""
def subtract(*args):
    return args[0] - sum(args[1:])

"""Multiplication: Any amount of arguments are allowed: Example: 5 * 5 = 25"""
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

"""Division: Any amount of arguments are allowed: Example: 10 / 5 = 2"""
def divide(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return int(result)

# Radians Degrees

"""Allows Calculation of radians: Example: 45 = 0.7853981633974483"""
def calculate_radians(degrees):
    radians = math.radians(degrees)
    return radians

"""Allows Calculation of degrees: Example: 0.7853981633974483 = 45"""
def calculate_degrees(radians):
    degrees = math.degrees(radians)
    return degrees

# Sin Cos Tan & aSin aCos aTan

"""Allows calculation of sin: Example: 0.7853981633974483 = 0.7071067811865475"""
def sine(angle):
    return math.sin(angle)

"""Allows calculation of cos: Example: 0.7853981633974483 = 0.7071067811865476"""
def cosine(angle):
    return math.cos(angle)

"""Allows calculation of tan: Example: 0.7853981633974483 = 0.9999999999999999"""
def tangent(angle):
    return math.tan(angle)

"""Allows calculation of inverse sin: Example: 0.7071067811865476 = 0.7853981633974485"""
def inverse_sine(value):
    return math.asin(value)

"""Allows calculation of inverse cos: Example: 0.7071067811865476 = 0.7853981633974483"""
def inverse_cosine(value):
    return math.acos(value)

"""Allows calculation of inverse tan: Example: 0.7071067811865476 = 0.6154797086703874"""
def inverse_tangent(value):
    return math.atan(value)
