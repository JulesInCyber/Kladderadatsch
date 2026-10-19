#!/bin/bash

####
# Script that builds and moves assembly files
####
set -e
# Used variables
assemblyScript=$1
assemblyObject=${assemblyScript%.asm}.o
compiledFile=${assemblyScript%.asm}

# Assembling
nasm -f elf64 "$assemblyScript" -o "$assemblyObject"
# Linking
ld "$assemblyObject" -o "$compiledFile"

# Creating needed Folders
mkdir -p objects compiled 

# Moving files
mv "$assemblyObject" objects/
mv "$compiledFile" compiled/
