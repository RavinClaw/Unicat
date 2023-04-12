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


def Object():
    ...

"""A game console"""

class Console:
    def __init__(self):
        self.unicatid = "".join(random.choice(string.ascii_letters + str(string.digits)) for _ in range(20))
    
    def Log(self, *args):
        print("[Unicat]", *args)

