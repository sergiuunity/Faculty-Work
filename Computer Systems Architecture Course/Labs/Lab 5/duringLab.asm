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
    ;a string of words is given
    ;create the string D with the words in reversed order.
    ;s=1234h,5678h
    ;d=5678h,1234h
    s dw 1234h, 5678h;in mem:34|12|78|56
    ;                          0  1  2  3
    ;                               esi; adresa de inceput al ultimului elem din sir
    ls equ ($-s)/2
    d resw ls

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, ls*2-2;poz esi la adresa 2; s
        mov edi, 0 ; d
        mov ecx, ls
        repeta:
            mov ax, word[s+esi];ax=5678h
            mov word[d+edi], ax
            sub esi,2
            sub edi,2
        loop repeta
            
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
