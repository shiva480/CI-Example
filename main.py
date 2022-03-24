import math
import os
import datetime


def func1(a, b) -> int:
    return math.floor(a/b)


def func2() -> str:
    return os.getcwd()


def func3(date):
    return datetime.datetime.strptime(func3, "%H:%M:%S")
