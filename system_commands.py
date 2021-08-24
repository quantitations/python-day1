
### Running a terminal command from Python ###

# Let's send a command to the command line
# (a.k.a. the "Command Prompt" in Windows or the "Terminal" in Mac/Linux)
# e.g. Run the following if using Windows:
# import os
# os.system("notepad")

# Many programs can be run via the command line, so "os.system()"
# is a powerful part of automating complicated processes with Python.



### Running Python code from the terminal ###


# You can also run a Python script from the command line.
# Open "Anaconda Prompt" if in Windows, or an ordinary terminal window in Mac or Linux.
# Navigate to the folder containing this file and run it using the command:
# python system_commands.py David 3


import sys

for i in range(int(sys.argv[2])):
  sys.stdout.write(f"Hi, { sys.argv[1] }. ")

# Arguments passed to the script are accessbile in sys.argv.
# The sys.stdout.write() function passes output back to the command prompt
# in such a way that it can be "piped" into another program if desired.

