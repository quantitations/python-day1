
############## READING, WRITING, AND MANIPULATION ################

import os

os.getcwd() # what directory are we currently working in?


# Read

with open('declaration.txt') as f:
    declaration = f.read()

declaration[:100]


# or go directly to the list of lines with "readlines()"
with open('declaration.txt') as f:
    lines = f.readlines()

lines[:2]


# Write

with open("declaration-intro.txt", "w") as f:
    f.write(declaration[:500])


# or write the list of lines directly with "writelines()"
with open("declaration-evenlines.txt", "w") as f:
    f.writelines(lines[1::2])


# Rename

os.rename("declaration-evenlines.txt", "dec-even.txt")


# Move

os.rename("dec-even.txt", "utility/dec-even.txt")


# Delete

os.remove("utility/dec-even.txt")
os.remove("declaration-intro.txt")



############### ALTERNATIVE APPROACH: PATHLIB MODULE #############

from pathlib import Path

dir_path = Path("new_dir")
dir_path.mkdir()

file_path = dir_path / "new_file.txt"
file_path
str(file_path) # the path as a string
file_path.name
file_path.stem
file_path.suffix

file_path.write_text("hi")
file_path.read_text()
file_path.write_text("overwriting it")
file_path.read_text()

# to append rather than overwriting
with file_path.open("a") as f:
    f.write("\nappending this")

print(file_path.read_text())

lines = file_path.read_text().splitlines() # list of lines of text
lines

# if you're dealing with a really big file and want to process
# one line at a time without bringing the whole file into memory, e.g.
with open(file_path) as f:
    for line in f:
        print(line.upper()) # do whatever processing you want inside this for loop

# alternatively if you want to WRITE a lot of output to a file, piece by piece,
# it's better to "keep the file open", e.g.
with file_path.open("w") as f:
    for line in lines:
        f.write(line + "\n")

# get absolute path (file_path itself is a relative path)
file_path_abs = file_path.resolve()
file_path_abs


os.listdir() # list the files in dir_path
os.listdir(dir_path) # list the files in dir_path
os.chdir(dir_path) # change the current working directory
os.getcwd()
os.listdir()

file_path.read_text() # what's wrong here?
file_path_abs.read_text()

os.chdir("..") # go "up" one directory - now you're back to where you were
os.getcwd()

dir_path.glob("*.txt")
[f.name for f in dir_path.glob("*.txt")]
# intead use "rglob" to search through all files in the path and its subdirectories
[str(f) for f in Path().rglob("*.txt")] # Path() with empty arg points to cwd
# CAREFUL: In general, rglob can take a long time to run,
# depending on how many subdirectories and files you're searching through.

# delete the file we made
file_path.unlink()

# delete the (now empty) directory
dir_path.rmdir()
# OR os.rmdir(dir_path)

# Note that rmdir only works on empty directories.
# There is a function ("rmtree" in the "shutil" module) for deleting non-empty directories,
# BUT BE CAREFUL as it's very dangerous for beginners!
# You would need to make sure you know exactly what you're doing
# or you can accidentally delete a lot more than you were planning to.


