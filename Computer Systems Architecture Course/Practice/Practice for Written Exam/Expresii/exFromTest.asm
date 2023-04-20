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
    ;a + 7/b - c*5, a-doubleword, b-word, c-byte, signed
    a dd 15
    b dw -3
    c db 11
    format db '%d', 0
    ;=15-2-55=-2-40=-42
    
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ;7/b
        ;7->dx:ax
        mov ax, 7
        cwd
        mov bx, word[b]
        idiv bx
        ;7/b->ax,r=dx
        mov cx, ax
        
        
        ;c*5
        mov al, byte[c]
        mov bl, 5
        imul bl
        ;c*5->ax
        
        
        ;7/b - c*5
        sub cx, ax
        
        
        ;a + 7/b - c*5
        movsx eax, cx
        mov ebx, dword[a]
        add eax, ebx
        ;rez = eax
        
        push eax
        push dword format
        call[printf]
        add esp, 4*2
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
