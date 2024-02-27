#!/usr/bin/env python3
import os
import subprocess

# Remove any previously compiled binary
subprocess.call("rm -f ./a.out", shell=True)

# Compile the C++ source file
retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True)
if retcode:
    print("failed to compile walk.cc")  # This line should be indented
    exit  # This line should be indented

# Remove any existing output file
subprocess.call("rm -f ./output", shell=True)

# Execute the test script
retcode = subprocess.call("./test.sh", shell=True)
print("Score: " + str(retcode) + " out of 2 correct.")  # This line should be indented
print("*************Original submission*************")
with open('uploads/walk.cc','r') as fs:
    print(fs.read())  # This line should be indented
