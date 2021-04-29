from time import sleep
from math import floor
import sys, re

# Constants, change these to suit your needs.

# Replace or rearrange the following to suit 
# your needs. Must contain 2 M's and 2 S's
TIMEFMT = "T - M M : S S"

def convert_timefmt(time):
    new_str = ""
    for n in range(0, len(time)):
        if time[n] == "M" or time[n] == "S":
            new_str += "{}"
        else:
            new_str += time[n]
    return new_str
