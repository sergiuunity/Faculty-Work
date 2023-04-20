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
    ;a string of doublewords is given
    ;save in string b only higher bytes from low words from the string
    s dd 12345678h, 1a2b3c4dh
    ls equ($-s)/4
    b resb ls
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 1 ; s
        mov edi, 0; b
        mov ecx, ls
        repeta:
            mov al, byte[s+esi]
            mov byte[b+edi], al
            add esi, 4
            add edi, 1; b - sir de bytes
        loop repeta
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
