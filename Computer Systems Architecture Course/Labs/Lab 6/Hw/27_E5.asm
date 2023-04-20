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
    ;e5 = a - b / c + 9/d 
    ;a doubleword, b-byte, c –word, d- word
    ;print value of e5 on screen
    a dd 100
    b db 15
    c dw 2
    d dw 6
    ;=> e5 = 100 - 15/2 + 9/6 = 100 - 7 + 1 = 94
    formatmsg db 'rez: %d', 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;b/c
        ;b->dx:ax
        mov bx, word[c]
        mov al, byte[b]
        cbw
        cwd
        idiv bx
        ;ax=q,dx=r
        mov cx, ax
        
        
        ;9/d
        mov bx, word[d]
        mov al, 9
        cbw
        cwd
        idiv bx
        ;ax=q,dx=r
        
        
        ;-b/c+9/d = -cx+ax = -6
        sub ax, cx
        
        
        ;a+(-b/c+9/d)
        ;ax->eax
        cwde
        add eax, dword[a]
        ;eax = a+(-b/c+9/d) = 94
        
        
        ;printing eax
        push eax
        push dword formatmsg
        call[printf]
        add esp, 4*2
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
