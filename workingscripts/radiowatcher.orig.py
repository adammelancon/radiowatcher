import subprocess
import os

os.system('clear')
rawsample = subprocess.Popen(["/usr/local/bin/rtl_fm -f 94.5M -W -s 200000 -r 48000 -l 9 - | /usr/bin/aplay -r 48k -f S16_LE -v -v -v -d 3"],stdout=subprocess.PIPE, shell=True)

samples = []
for line in rawsample.stdout:
    samples.append(line)

total = 0
samps = 0
for i in samples:
    total += int(i[-4:-2])
    samps += 1

sigavg = total / samps
os.system('clear')
print "Signal total is: %s " % total
print "Number of samples is %s " % samps
print "Signal average is: %f " % sigavg
