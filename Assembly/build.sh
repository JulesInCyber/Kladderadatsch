# Script that builds and moves assembly files

# Used variables
assemblyScript=$1
assemblyObject=${assemblyScript%.asm}.o
compiledFile=${assemblyScript%.asm}

# Assembling
nasm -f elf64 $assemblyScript -o $assemblyObject
# Linking
ld $assemblyObject -o $compiledFile

# Moving files
mv $assemblyObject objects/
mv $compiledFile compiled/
