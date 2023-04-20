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
    ;a*4-b/c+d+x
    a dw 3
    b db 20
    c dd 3
    d dd 10
    aux dd 0
    aux2 dd 0
    x dq 1122334455667700h
    rez dd 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a*4
        mov ax, 4
        mul word[a];DX:AX = a*4=000Ch(DX=00, AX=0C)
        
        ;save dx:ax in aux
        mov word[aux+0], ax
        mov word[aux+2], dx
        
        ;b/c
        ;b->edx:eax
        mov eax, 0
        mov al, [b]
        mov edx, 0
        div dword[c]
        ;eax = cat
        ;edx rest (se ignora)
        mov [aux2], eax
        ;a*4-b/c+d
        
        ;aux-aux2+d
        ;doubleword - doubleword+doubleword
        mov ecx,[aux]
        sub ecx, [aux2]
        add ecx,  [d]
        ;ecx=12-6+10-16=...
        
        ;a*4-b/c+d+x
        ;          ecx+x
        ;          dd+quad
        ;          dword[x+0]+dword[x+4]
        mov ebx, 0
        ;ebx:ecx +dword[x+0] dword[x+4]
        add ecx, dword[x+0]
        adc ebx, dowrd [x+4]
        ;adc op1, op2
        ;=>op1 = op1+op2+transport
        ;transport este salvat intr-o unitate care stocheaza doar un bit(1 dc exista transport si 0 dc nu) si se numeste carry flag
        
        ;ebx:ecx rez expresiei
        
        mov [rez+0], ecx
        mov [rez+4], ebx
        
        
        ;mov [rez], ecx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
