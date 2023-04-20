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
    ;A string of words S is given. Compute string D containing only high bytes multiple of 7 from string S.
    ;If S = 1735h, 0778h, 0E20h => D = 07h, 0Eh
    ;S in mem: 35|17| 78|07| 20|0E
    ;D:07, 0E - start=1 cu step=2->d in memorie 07 | 0E
    s dw 1735h, 0778h, 0E20h
    ls equ ($-s)/2
    d resb ls
    nr db 7

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 1;s
        mov edi, 0; d
        mov ecx, ls
        repeta:
            mov al, byte[s+esi]
            mov bl, al
            cbw
            idiv byte[nr]
            cmp ah, 0
            je adaugaInD
            jne next
                adaugaInD:
                    mov byte[d+edi], bl
                    add edi, 1
                    add esi, 2
                    jmp myendif
                next:
                    add esi, 2
                myendif:
        loop repeta

        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
