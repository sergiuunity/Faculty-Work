bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf  msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;A string of bytes A is given.
    ;Construct string B such that each element from B represent the division of two consecutive elements from string A
    ;If A = 17, 4, 2 => B = 4, 2
    ;Print the resulted string on screen.
    a db 17, 4, 2
    ls equ $-a
    b resb ls-1
    format db '%d ', 0
    msj db 'the resulted string is: ', 0
    copie dd 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 0
        mov edi, 0
        mov ecx, ls-1
        
        repeta:
            mov al, byte[a+esi]
            cbw
            mov bl, byte[a+esi+1]
            idiv bl
            ;al = q, ah =r
            mov byte[b+edi], al
            add esi, 1
            add edi, 1
        loop repeta
        
        
        ;printing msj
        push dword msj
        call [printf]
        add esp, 4*1
        
        
        ;printing b
        mov ecx, ls-1
        mov esi, 0
        repetaPrint:
            mov al, byte[b+esi]
            ;al->eax
            movsx eax, al
            mov [copie], ecx
            push eax
            push dword format
            call [printf]
            mov ecx, [copie]
            add esp, 4*2
            add esi, 1
        loop repetaPrint
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
