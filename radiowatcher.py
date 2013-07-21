import subprocess
import os

# Clear the screen.
os.system('clear')

##############################
### SET YOUR VARIABLES
# Our Frequency List
stations = ["88.7", "102.1", "95.5"]
squelchlist = ["20", "10", "80"]
sampletime = "3"
#webpage = /var/www/index.html
###############################

# Create empty report and sample list
report = []
sample = []

# Create a function that takes the frequency you entered and inserts it into the command. 
# Then it samples the frequency and puts it into a list called "samples" and returns the list.
def freqsample(frq, sqel, st):
    # Create a fressh sample list.
    samples = []
    # Run the sampeling
    command = "/usr/local/bin/rtl_fm -f %sM -W -s 200000 -r 48000 -l %s - | /usr/bin/aplay -r 48k -f S16_LE -v -v -v -d %s" % (frq, sqel, st)
    rawsample = subprocess.Popen([command],stdout=subprocess.PIPE, shell=True)
    for line in rawsample.stdout:
        samples.append(line)
    # Loop through the sample list and only return the last two digits minus the % at the end.
    samps = len(samples)
    total = 0
    for i in samples:
        total += int(i[-4:-2]) # Add up all the samples

    # Math to get average sample signal.
    sigavg = total / samps
    #os.system('clear') #Clear the screen.
    # Add the results to the report..
    if loopcount == 0:
        report.append("===========================================")
    report.append("Station: %s" % frq)
    report.append("Squelch Level: %s" % sqel)
    report.append("Sample Time: %s" % st)
    report.append("--------")
    report.append("Signal total is: %s " % total)
    report.append("Number of samples is %s " % samps)
    report.append("Signal average is: %f " % sigavg)
    report.append("===========================================")

# Call the function with passing the freqency you gave it as a variable to "n" in the function. 
loopcount = 0

# Main Loop
for i in stations:
    if loopcount < len(stations):
        freqsample(i, squelchlist[loopcount], sampletime)
        loopcount += 1

# Print our report.
os.system('clear')
for i in report:
   print str(i)
