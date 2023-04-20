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
    ;if a este par then
     ;exp = 2*(-a)-b/c
     ;else
     ;exp=e-a/b
     
     a dd 6
     b db 8
     c db -12
     e dq 19
     exp dq 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a/2
        
        ;mov eax, [a]
        ;cdq
        ;mov bx, 2
        ;div bx
        ;al-q,ah-r
        ;sau
        mov ax, [a+0]
        mov dx, [a+2]
        mov bx, 2
        idiv bx;dx:ax/bx=ax q dx-r
        
        
        cmp ah, 0
        JE thenlabel
        JNE elselabel
        
        thenlabel:
            mov eax, [a]
            neg eax
            mov ebx, 2
            imul ebx;edx:eax = 2*(-a)
            ;edx:eax->ecx:ebx
            mov ebx,eax
            mov ecx, edx
            
            ;b/c
            movsx ax, byte[b]
            idiv byte[c]
            ;al->edx:eax
            movsx eax, al
            cdq
            ;ecx:ebx=2*(-a)     -
            ;edx:eax = b/c
            sub ebx,eax
            sbb ecx, edx
            mov [exp+0], ebx
            mov [exp+4], ecx
            
            jmp endlabel
        
        elselabel:
            ;a/b
            mov ax, [a+0]
            mov dx, [a+2]
            movsx bx, byte[b]
            idiv bx; dx:ax/bx = ax q
            movsx eax, al
            cdq
            ;e->ecx:ebx
            mov ebx, [e+0]
            mov ecx, [e+4]
            ;ecx:ebx-
            ;edx:eax
            sub ebx, eax
            sbb ecx, edx
            mov [exp+0], ebx
            mov [exp+4], ecx
            
            
            
            
        endlabel:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
