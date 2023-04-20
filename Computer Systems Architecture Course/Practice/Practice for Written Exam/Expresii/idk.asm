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
    ;else exp=1010b+(-b)*3+e
    ;a-byte
    ;b-double
    ;c-byte
    ;d-doubleword
    ;e-quadword
    
    a db 25
    b dd 10
    c db -5
    d dd 23
    e dq -11
    
    
    exp dq -1
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a/b
        ;a->edx:eax
        mov al, byte[a]
        cbw
        cwde
        cdq
        mov ebx, dword[b]
        idiv ebx
        ;eax=a/b
        
        cmp eax, 1
        je then
        jne otherwise
        
        then:
            ;a=15
            ;a*b+c/(-3) + d
            ;a*b->edx:eax
            mov al, byte[a]
            cbw
            cwde
            mov ebx, dword[b]
            imul dword[b]
            mov [exp+0], eax
            mov [exp+4], edx
            ;c/(-3)->ax
            mov al, byte[c]
            cbw
            mov bl, -3
            idiv bl
            ;a*b+c/(-3)=ecx:ebx
            cbw
            cwde
            cdq
            mov ebx, [exp+0]
            mov ecx, [exp+4]
            add ecx, edx
            adc ebx, eax
            ;a*b+c/(-3) + d = 174
            mov eax, dword[d]
            cdq
            add ecx, edx
            adc ebx, eax
            mov [exp+0], ebx
            mov [exp+4], ecx
            jmp otherwise
            
        otherwise:
            ;a=25
            ;1010h+(-b)*3+e
            ;(-b)*3->edx:eax
            mov eax, dword[b]
            neg eax
            mov ebx, 3
            imul ebx
            ;(-b)*3+e
            mov ebx, dword[e+0]
            mov ecx, dword[e+4]
            add ebx, eax
            adc ecx, edx
            ;1010h+(-b)*3+e
            mov eax, 1010b
            cdq
            add ebx, eax
            adc ecx, edx
            mov [exp+0], ebx
            mov [exp+4], ecx
            ;exp=-31
            
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
