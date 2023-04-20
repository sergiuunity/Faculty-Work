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
    a db 00h
    b dw 1234h
    c dd 12345678h
    d dq 1122334455667788h
    e dq 1122334455667788h
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;mov al, [b+0];al = 34
        ;mov bl, [b+1];bl = 12
        
        mov eax, [d+0]
        mov edx, [d+4];edx:eax = d
        
        mov ebx, [e+0]
        mov ecx, [e+4];ecx:ebx = e
    
        add eax, ebx
        adc edx, ecx;edx:eax=edx:eax+ecx:ebx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
