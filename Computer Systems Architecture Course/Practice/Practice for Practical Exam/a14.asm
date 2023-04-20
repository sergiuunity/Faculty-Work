bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;A string of bytes A is given. Construct string B containing only values divisible with 7 from string A.
    ;If A = 12, 13, 14, 18, 21 => B = 14, 21
    a db 12, 13, 14, 18, 21
    la equ $-a
    b resb la
    copie dd 0
    contorD dd 0
    format db '%d ', 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 0
        mov edi, 0
        mov ecx, la
        
        repeta:
            mov al, byte[a+esi]
            cbw
            mov bl, 7
            idiv bl
            ;ah=r
            cmp ah, 0
            je divisible
            jne next
            divisible:
                mov al, byte[a+esi]
                mov [b+edi], al
                inc edi
                mov dl, 1
                add [contorD], dl
            next:
                inc esi
        loop repeta
        
        
        
        ;printing
        mov esi, 0
        mov ecx, dword[contorD]
        repetaPrint:
            mov al, byte[b+esi]
            cbw
            cwde
            inc esi
            mov [copie], ecx
            push eax
            push dword format
            call[printf]
            add esp, 4*2
            mov ecx, dword[copie]
        loop repetaPrint
        
        
        ;13.40
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
