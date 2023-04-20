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
    ;se da un sir de bytes.
    ;sa se determine bytes care au ultima cifra egala cu o const k.
    ;sa se salveze in sirul d acesti bytes.
    ;s=123, 113, 23, 24, 114, k=3 => d=23, 113, 23
    s db 123, 113, 23, 24, 114
    ls equ $-s
    d resb ls ;se aloca ls bytes in mem pt d
    k equ 3
    zece db 10
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 0;s
        mov edi, 0;d
        mov ecx, ls
        repeta:
            mov al, byte[s+esi];a=123
            mov bl, al
            cbw;ax=123
            idiv byte[zece];ah-rest
            cmp ah, k
            JE adaugainD
            JNE next
                adaugainD:
                    mov byte[d+edi], bl
                    inc edi
                    inc esi
                    
                    jmp myendif
                next:
                    inc esi
                    
                myendif:
                
        loop repeta
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
