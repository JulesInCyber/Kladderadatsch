; exit.asm - small program that exits with code 42
global _start

section .text
_start:
    mov rax, 60
    mov rdi, 42
    syscall
