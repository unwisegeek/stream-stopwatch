from time import sleep
from math import floor
from os.path import expanduser
import sys, re

# Constants, don't change these.
USERHOME = expanduser("~")

# Configuration values, you can change these.

# Replace or rearrange the following to suit 
# your needs. Must contain 2 M's and 2 S's
TIMEFMT = "T - M M : S S"

# Replace with the default amount of time to
# countdown from if no time is given on the
# command line.
DEFAULTTIME = "0h10m0s"

# Replace this with the path of the file
CDFILE="~/obs-countdown"

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
    # Squash all arguments
    args = ""
    for i in range(1, len(sys.argv)):
        args += sys.argv[i]
    timestr = args
except:
    timestr = DEFAULTTIME

secs = convert_timestr_to_secs(timestr)
if secs == 0:
    secs = convert_timestr_to_secs(DEFAULTTIME)

timeline = convert_timefmt(TIMEFMT)

# Open CDFILE for writing.
f = open(CDFILE.replace('~', USERHOME), 'w+')

while secs >= 0:
    min_str = str(secs // 60)
    sec_str = str(secs % 60)

    # Prepend a 0 if the str is single digit
    if len(min_str) == 1:
        min_str = "0" + min_str
    if len(sec_str) == 1:
        sec_str = "0" + sec_str
    
    # Overwrite the contents of the file
    f.seek(0)
    f.write(timeline.format(min_str[0], min_str[1], sec_str[0], sec_str[1]))
    f.truncate()

    # Close the file and bail out if 0
    if secs == 0:
        f.close()
        sys.exit()
    # Subtract and sleep if not 0.
    secs -= 1
    sleep(1)

# Close the file in case we break out of the loop somehow.
f.close()