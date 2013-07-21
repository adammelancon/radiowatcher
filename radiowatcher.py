import subprocess
import os

# Clear the screen.
os.system('clear')

# Our Frequency List
stations = ["94.5", "99.9", "107.1"]

# Create an empty list.
samples = []
report = []

# Create a function that takes the frequency you entered and inserts it into the command. 
# Then it samples the frequency and puts it into a list called "samples" and returns the list.
def freqsample(n):
    command = "/usr/local/bin/rtl_fm -f %sM -W -s 200000 -r 48000 -l 9 - | /usr/bin/aplay -r 48k -f S16_LE -v -v -v -d 3" % n
    rawsample = subprocess.Popen([command],stdout=subprocess.PIPE, shell=True)
    for line in rawsample.stdout:
        samples.append(line)
    # Set baselines for my counters.
    total = 0
    samps = 0
    # Loop through the sample list and only return the last two digits minus the % at the end.
    for i in samples:
        total += int(i[-4:-2]) # Add up all the samples
        samps += 1 # Make a counter to find out how many samples we took.

    # Math to get average sample signal.
    sigavg = total / samps
    os.system('clear') #Clear the screen.
    # Print the results.
    if loopcount == 0:
        report.append("===========================================")
    report.append("Station: %s" % n)
    report.append("Signal total is: %s " % total)
    report.append("Number of samples is %s " % samps)
    report.append("Signal average is: %f " % sigavg)
    report.append("===========================================")

# Call the function with passing the freqency you gave it as a variable to "n" in the function. 
loopcount = 0
print loopcount
for i in stations:
    if loopcount < len(stations):
        freqsample(i)
        loopcount += 1
# Print our report.
os.system('clear')
for i in report:
   print str(i)
