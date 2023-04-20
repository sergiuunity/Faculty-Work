bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;A string of bytes A is given. 
    ;Construct string B such that each element from B represent the sum of two consecutive elements from string A.
    ;If A = 2, 3, 4 => B = 5, 7
    ;Print the resulted string on screen.
    a db 2,3,4
    la equ $-a
    b resb la-1
    format db '%d ', 0
    copie dd 0

    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, 0
        mov edi, 0
        mov ecx, la-1
        
        repeta:
            mov al, byte[a+esi]
            mov bl, byte[a+esi+1]
            add al, bl
            mov byte[b+edi], al
            inc esi
            inc edi
        loop repeta
        
        
        ;printing b
        mov edi, 0
        mov ecx, la-1
        repetaPrint:
            mov al, byte[b+edi]
            cbw
            cwde
            mov [copie], ecx
            push eax
            push dword format
            call [printf]
            add esp, 4*2
            mov ecx, dword[copie]
            inc edi
        loop repetaPrint
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
