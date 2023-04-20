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
    ;string of bytes. extract in string d all bytes which are negative and even
    s db 1,-1,2,-2,3,-3,4,-4
    ls equ ($-s)
    d times ls db -1
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov esi, s
        mov edi, d
        
        mov ecx, ls
        repeta:
            lodsb
            ;current byte is in al
            cmp al, 0
            jge next 
            jl thenNegative
            thenNegative:
                mov dl, al
                cbw
                mov bl, 2
                idiv bl
                ;residue in ah
                cmp ah, 0
                je thenEven
                jne next
                thenEven:
                    mov al, dl
                    stosb
            next:
            
        loop repeta
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
