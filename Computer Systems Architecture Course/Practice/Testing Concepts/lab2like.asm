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
    ;If a/b=1 then exp = a*b+c/(-3) + d
    ;else exp=1010h+(-b)*3+e
    ;a-byte
    ;b-double
    ;c-byte
    ;d-doubleword
    ;e-quadword
    a db 10
    b dd -5;
    c db 32
    d dd 123
    e dq -74
    exp dq 1122334455667788h
    j dq 92h
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a*b
        movsx eax, byte[a]
        imul dword[b]
        ;edx:eax = a*b

        ;c/(-3)
        mov [exp+0], eax
        mov [exp+4], edx
        ;exp = a*b
        movsx ax, byte[c]
        mov cl, -3
        idiv cl
        ;al-q;ah-r
        
        ;a*b+c/(-3)
        add eax, dword[exp]
        movsx ecx, al
        add eax, dword[ecx]
        add eax, dword[d]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        ;a/b
        ;mov al, [a]
        ;cbw
        ;cwde
        ;cdq
        ;idiv dword[b]
        ;eax-q, edx-r
        
     
        
        ;then
        ;a*b+c/(-3) + d
        ;a*b
        ;movsx eax, byte[a]
        ;imul dword[b]
        ;edx:eax-a*b
        ;mov [exp+0], eax
        ;mov [exp+4], edx
        ;exp = a*b
        ;c/(-3)
        ;movsx ax, byte[c]
        ;mov cl, -3
        ;idiv cl
        ;al-q, ah-q
        ;a*b+c/(-3)
        ;cbw
        ;cwde
        ;add eax, [exp]
        ;eax = -50+(-10)
        ;a*b+c/(-3) + d = 63
        ;add eax, [d]
        ;cdq
        ;rez = edx:eax
        ;mov [exp+0], eax
        ;mov [exp+4], edx
        
        
        
        ;else
        ;1010h+(-b)*3+e
        mov eax, [b]
        neg eax
        mov cx, 3
        movsx ebx, cx
        imul ebx
        ;edx:eax=-b*3
        ;ecx:ebx
        ;-b*3+e
        mov ebx, [e+0]
        mov ecx, [e+4]
        add ecx, edx
        adc ebx, eax
        mov [exp+0], ebx
        mov [exp+4], ecx
        
        mov ax, 1010h
        cwde
        cdq
        add ecx, edx
        adc ebx, eax
        mov [exp+0], ebx
        mov [exp+4], ecx
        
        
        ;4053
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
