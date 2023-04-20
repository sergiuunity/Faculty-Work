bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, gets, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

import printf msvcrt.dll
import gets msvcrt.dll
import scanf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
     s resb 20
    format_sir db '%s', 0
    mesaj db 'S-a citit acest sir:', 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword s
        call [gets]
        add esp, 4*1
        
        ;print pe ecran mesajul
        
        push dword mesaj
        
        call [printf]
        add esp, 4*1
        
        ; print pe ecran sirul citit
        
        
        push dword s
        push dword format_sir
        call [printf]
        add esp, 4*2

        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
