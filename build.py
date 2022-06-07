import os
from sys import platform

# Settings
CC = "gcc"  # The compiler
CFLAGS = "-std=c17"  # Compiler flags

LINKFLAGS = ""  # Linker flags

NAME = "out"  # Executable name
SRCDIR = "src"  # Source directory

# Source

if platform == "win32":
    NAME += ".exe"

objects = []

for subdir, dirs, files in os.walk(SRCDIR):
    for file in files:
        if ".c" not in file:
            continue

        inputFile = os.path.join(subdir, file)
        outputFile = inputFile.replace(".c", ".o")
        cmd = f"{CC} -o {outputFile} -c {inputFile} {CFLAGS}"
        print(cmd)
        os.system(cmd)
        objects.append(outputFile)

objectString = " ".join(objects)
cmd = f"{CC} -o {NAME} {objectString} {LINKFLAGS}"
print(cmd)
os.system(cmd)
