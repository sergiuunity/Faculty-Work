bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
x dw 15
y db 5
z dd 4
    ; x-7+y-2-3+z
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
    
    ;x-7
    mov bx, [x]
    sub bx, 7
    
    ;x-7+y
    mov cx, 0
    mov cl, [y]
    add bx, cx
    
    
    ;x-7+y-2
    sub bx, 2
    
    ;x-7+y-2-3
    
    sub bx, 3
    
    ;x-7+y-2-3+z
    
    mov edx, 0
    mov dx, bx
    sub edx, [z]
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program

        