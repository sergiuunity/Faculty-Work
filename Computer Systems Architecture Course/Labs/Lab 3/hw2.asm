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
    ;17/a + b*7 - c =
    a dw 6
    b db -5
    c dd 43
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;17/a
        ;17->dx:ax
        mov eax, 0 
        mov al, 17
        cbw
        cwd
        ;dx:ax=a
        div word[a]
        ;ax=17/a
        mov bx, ax
        ;bx=17/a
        
        ;b*7
        mov al, 7
        imul byte[b]
        ;ax = b*7
        
        ;17/a + b*7
        add ax, bx
        
        ;17/a+b*7-c
        cwde
        add eax, [c]
        ;eax = 17/a+b*7-c
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
