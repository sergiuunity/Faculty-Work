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
    ;if a%7 este diferit de 0 atunci exp = a*7
                             ;altfel exp = b/3 + c
    ;a-word
    ;b-byte
    ;c-doubleword
    a dw 49
    b db -62
    c dd -24
    exp dd 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a/7
        mov eax, 0
        mov al, [a]
        mov bl, 7
        idiv bl
        ;al-q, ah-r

        
        cmp ah, 0
        JE egal
        JNE diferit
        
        egal:
            ;exp = b/3 + c
            ;b/3
            mov al, [b]
            movsx ax,al
            mov bl, 3
            idiv bl
            ;al-q, ah-r
            
            ;b/3 + c
            mov ebx, 0
            mov bl, al
            add ebx, [c]
            ;ebx = b/3 + c = -44
            
            mov [exp], ebx
            ;exp = b/3 + c = -44(pt. a=49)
        
        diferit:
            ;exp = a*7
            mov ax, 7
            imul word[a]
            ;dx:ax = a*7
            mov word[exp+0], ax
            mov word[exp+2], dx
            mov eax, [exp]
            ;exp = a*7 = 350(pt. a=50)
            jmp endmyif
        
        endmyif:
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
