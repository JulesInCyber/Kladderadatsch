; Prints a message and exits
global _start

section .data
    msg:    db "Hello World!", 10   ; text + newline
    msg_len: equ $ - msg            ; length = current address - start of msg

section .text
_start:
    mov rax, 1          ; syscall number 1 = write
    mov rdi, 1          ; fd 1 = stdout
    mov rsi, msg        ; address of the text
    mov rdx, msg_len    ; number of bytes
    syscall
    
    ; exit(0)
    mov rax, 60
    mov rdx, 0
    syscall
