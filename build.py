import os
from sys import platform
import argparse
import multiprocessing
from threading import Thread

# Settings
CC = "gcc"  # The compiler
CFLAGS = "-std=c17"  # Compiler flags

LINKFLAGS = ""  # Linker flags

NAME = "out"  # Executable name
SRCDIR = "src"  # Source directory

FILEENDING = ".c"  # The file ending for the language

# Source

parser = argparse.ArgumentParser(
    description='A light-weight build system written in python')

parser.add_argument("-j", "--jobs", type=int,
                    help="The number of jobs [default: %(default)s on your machine]", default=multiprocessing.cpu_count())

parser.add_argument("-c", "--clean", action='store_true',
                    help="Clean up object files after build")

parser.add_argument("-r", "--run", action='store_true',
                    help="Run the file after compiling")


args = parser.parse_args()

jobCount = args.jobs

if platform == "win32":
    NAME += ".exe"

objects = []
toCompile = []

for subdir, dirs, files in os.walk(SRCDIR):
    for file in files:
        if FILEENDING in file:
            toCompile.append(os.path.join(subdir, file))


def compileTask():
    while len(toCompile) > 0:
        inputFile = toCompile.pop(0)
        outputFile = inputFile.replace(FILEENDING, ".o")
        cmd = f"{CC} -o {outputFile} -c {inputFile} {CFLAGS}"
        print(cmd)
        os.system(cmd)
        objects.append(outputFile)


threads = []

for i in range(jobCount):
    threads.append(Thread(target=compileTask, name=str(i)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

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

if args.run:
    os.system(f"./{NAME}")
