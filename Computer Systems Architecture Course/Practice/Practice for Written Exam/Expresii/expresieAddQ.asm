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
    ;a + b/3 - c*4 + d
    ;a-byte, b-word, c-double, d-quadword
    a db 19
    b dw -11
    c dd 5
    d dq -5
    ;19-3-20-5=-9
    format db 'Result: %d', 0
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;b/3
        mov ax, word[b]
        mov bl, 3
        idiv bl
        ;q=al, r=ah
        mov cl, al
        
        
        ;a+b/3
        mov bl, [a]
        add al, bl
        cbw
        cwde
        cdq
        mov ecx, edx
        mov ebx, eax
        
        
        ;c*4
        mov eax, dword[c]
        mov edx, 4
        imul edx
        ;c*4->edx:eax
        
        
        ;a+b/3-c*4=ecx:ebx-edx:eax
        sub ebx, eax
        sbb edx, ecx
        
        
        ;a+b/3-c*4+d
        mov eax, dword[d+0]
        mov edx, dword[d+4]
        add eax, ebx
        adc edx, ecx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
