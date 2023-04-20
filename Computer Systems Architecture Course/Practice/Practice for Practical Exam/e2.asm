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
    ;e2 = a / b + c * (-4) – d ; a-byte, b – word, c –byte, d - doubleword
    ;print value of e2 on screen
    a db 10
    b dw -3
    c db 23
    d dd 17
    format db '%d', 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a/b=-3
        mov al, byte[a]
        cbw
        cwd
        mov bx, word[b]
        idiv bx
        ;ax=q, dx=r
        mov cx, ax
        ;cx = a/b
        
        
        ;c*(-4)=-92
        mov al, byte[c]
        mov bl, -4
        imul bl
        ;ax=c*(-4)
        
        
        ;a / b + c * (-4) = cx + ax = -95
        add ax, cx
        
        
        ;a / b + c * (-4) – d = -112
        cwde
        mov ebx, dword[d]
        sub eax, ebx
        ;e2 = eax = -112
        
        
        ;printing
        push eax
        push dword format
        call[printf]
        add esp, 4*2
    
    
        ;16 min
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
