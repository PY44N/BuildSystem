import os
from sys import platform

# Settings
CC = "gcc"
CFLAGS = "-std=c17"

LINKFLAGS = ""

NAME = "out"
SRCDIR = "src"

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
