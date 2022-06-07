import os
from sys import platform
import argparse
import multiprocessing

# Settings
CC = "gcc"  # The compiler
CFLAGS = "-std=c17"  # Compiler flags

LINKFLAGS = ""  # Linker flags

NAME = "out"  # Executable name
SRCDIR = "src"  # Source directory

# Source

parser = argparse.ArgumentParser(
    description='A light-weight build system written in python')

parser.add_argument("-j", "--jobs", type=int,
                    help="The number of jobs [default: %(default)s on your machine]", default=multiprocessing.cpu_count())

parser.add_argument("-c", "--clean", action='store_true',
                    help="Clean up object files after build")

args = parser.parse_args()

jobCount = args.jobs

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

if args.clean:
    for subdir, dirs, files in os.walk(SRCDIR):
        for file in files:
            if ".o" not in file:
                continue

            file = os.path.join(subdir, file)
            print(f"Removing {file}")
            os.remove(file)
