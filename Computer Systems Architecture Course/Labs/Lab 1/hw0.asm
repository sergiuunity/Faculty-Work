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
    ;take 3 variables (3 data type) and 2 constants and create an expresion with +,-, then write the code to solve it
    ;a + 11 - b + 1ch - c
    a db 33
    b dd 3
    c db 13
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a + 11
        
        mov al, [a]
        add al, 11
        
        ;a + 11 - b
        
        mov ebx, 0
        mov bl, al
        sub ebx, [b]
        
        ;a + 11 - b + 2dh
        
        add ebx, 1ch
        
        ;a + 11 - b + 2dh - c
        
        sub ebx, [c]
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
