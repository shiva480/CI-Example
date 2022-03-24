import math
import os
from datetime import datetime


def func1(a, b) -> int:
    return math.floor(a/b)


def func2() -> str:
    return os.getcwd()


def func3(date):
    return datetime.strptime(func3, "%H:%M:%S")
