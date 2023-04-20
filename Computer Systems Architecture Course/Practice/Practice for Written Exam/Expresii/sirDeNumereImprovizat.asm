bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;citeste sir de n doubleword-uri si afiseaza-le
    n dd 0
    x dd 0
    formatN db 'give n: ', 0
    formatNumber db '%d', 0
    formatX db 'give current x: ', 0
    formatXPrint db '%d ', 0
    newline db 10, 0

    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;reading n
        push formatN
        call [printf]
        add esp, 4*1
        push n
        push formatNumber
        call [scanf]
        add esp, 4*2
        
        ;reading numbers
        mov ecx, dword[n]
        repeta:
            mov ebx, ecx
            ;reading current number
            push formatX
            call [printf]
            add esp, 4*1
            push x
            push formatNumber
            call [scanf]
            add esp, 4*2
            
            
            ;printing current number
            push dword[x]
            push formatXPrint
            call [printf]
            add esp, 4*2
            
            push dword newline
            call [printf]
            add esp, 4*1

            
            
            
            mov ecx, ebx
        loop repeta
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
