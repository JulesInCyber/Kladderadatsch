; prints two separate lines of text
global _start

section .data
    msg_1       db "This is line 1", 10     ; text + Newline
    msg_1_len   equ $ - msg_1               ; length of msg_1
    msg_2       db "This is line 2", 10
    msg_2_len   equ $ - msg_2

section .text
_start:
    ; printing the first line
    mov rax, 1
    mov rdi, 1
    mov rsi, msg_1
    mov rdx, msg_1_len
    syscall

    ; printing the second line
    mov rax, 1
    mov rdi, 1
    mov rsi, msg_2
    mov rdx, msg_2_len
    syscall

    ; exit on 0
    mov rax, 60
    mov rdi, 0
    syscall
