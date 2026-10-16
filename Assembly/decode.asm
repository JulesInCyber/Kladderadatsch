; decode.asm - Output will be investigatet with objdump
; `objdump -d -M intel decode
global _start

section .text
_start:
    mov eax, 42
    mov eax, 255
    mov eax, 256
    ; exiting
    mov rax, 60
    mov rdi, 0
    syscall
