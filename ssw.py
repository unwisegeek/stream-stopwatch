from time import sleep
from math import floor
import sys, re

# Constants, change these to suit your needs.

# Replace or rearrange the following to suit 
# your needs. Must contain 2 M's and 2 S's
TIMEFMT = "T - M M : S S"

# Replace with the default amount of time to
# countdown from if no time is given on the
# command line.
DEFAULTTIME = "0h10m0s"

def convert_timefmt(time):
    new_str = ""
    for n in range(0, len(time)):
        if time[n] == "M" or time[n] == "S":
            new_str += "{}"
        else:
            new_str += time[n]
    return new_str

def convert_timestr_to_secs(timestr):
    secs = 0
    hours = re.findall("\d+h", timestr)
    minutes = re.findall("\d+m", timestr)
    seconds = re.findall("\d+s", timestr)

    if len(hours) > 0:
        secs += int(hours[0].strip("h")) * 3600
    if len(minutes) > 0:
        secs += int(minutes[0].strip("m")) * 60
    if len(seconds) > 0:
        secs += int(seconds[0].strip("s"))
    return secs


# Get time for stopwatch from command line, or default to DEFAULTTIME
try:
    timestr = sys.argv[1]
except:
    timestr = DEFAULTTIME

seconds = convert_timestr_to_secs(timestr)
if seconds == 0:
    seconds = convert_timestr_to_secs(DEFAULTTIME)
print(seconds)
