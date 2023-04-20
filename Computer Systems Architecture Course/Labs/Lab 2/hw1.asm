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
    ;a - 10h * b + c / 6 = 146 = 92h
    a dd 200
    b dw 4
    c db 61
    aux dd 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;10h * b
        mov eax, 0
        mov edx, 0
        mov ax, 10h
        mul word[b]
        ;10h * b -> dx:ax
        
        ;saving dx:ax in aux
        mov word[aux+0], ax
        mov word[aux+2], dx
        
        ;a - 10 * b
        mov ecx, [a]
        sub ecx, [aux]
        
        ;c / 6
        mov eax, 0
        mov al, [c]
        mov ebx, 0
        mov bl, 6
        div bl
        ;cat->al
        
        ;a - 10 * b + c/6
        mov edx, 0
        mov dl, al
        add ecx, edx
        ;exc->rezultat
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
