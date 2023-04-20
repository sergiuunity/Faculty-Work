bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,printf                ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf  msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;B7
    ;A string of doublewords T is given. Compute string R containing only high bytes from high words from eachdoubleword from string S.
    ;If S = 12345678h, 1a2b3c4dh => D = 12h, 1ah(in mem: 12 | 1a)->print: 18 26
    ;s in mem: 78 | 56 | 34 | 12 ||| 4d | 3c | 2b | 1a |
    ;so we search throuh 12, 1a => start = 3, step = 4
    s dd 12345678h, 1a2b3c4dh
    ls  equ ($-s)/4
    r resb ls
    countingR dd 0
    msj db 'The result is: '
    copie dd 0
    format db '%d ', 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 3;s
        mov edi, 0;r
        mov ecx, ls
        repeta:
            mov al, byte[s+esi]
            mov byte[r+edi], al
            add esi, 4
            add edi, 1
            inc dword[countingR]
        loop repeta
        
        ;printare mesaj
        push dword msj
        call [printf]
        
        ; print string d
        mov ecx, [countingR]
        mov esi, 0
        repetaprint:
            mov al, byte[r+esi]
            movsx eax, al
            mov [copie], ecx
            push eax
            push dword format
            call [printf]
            mov ecx, [copie]
            add esi, 1
        loop repetaprint    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
