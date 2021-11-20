import os
import sys
import subprocess


#
bashCommand = "youtube-dl --proxy 10.104.1.9:8080 -f worstaudio -o input.webm https://www.youtube.com/watch?v=RSpb1rMEDjA&t=7613s"
#bashCommand = "youtube-dl -f worstaudio https://www.youtube.com/watch?v=V_6WlQuMplg"
#
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()

#process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()
print(output)