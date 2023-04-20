bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
import scanf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    ;e1 = a * b + c / (-4) – d 
    ;a-byte, b – word, c –byte, d - doubleword
    ;print value of e1 on screen
    a db 10
    b dw -8
    c db 26
    d dd -70
    ;=>e1 = -80 - 6 + 70 = -16
    copie dd 12345678h
   
    msj db 'the result is ', 0
    format db '%d', 0
    
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a*b
        ;a->ax
        movsx ax, byte[a]
        mov bx, word[b]
        imul bx
        ;a*b->dx:ax
        mov [copie+0], ax
        mov [copie+2], dx
        mov ebx, dword[copie]
        
        
        ;c/(-4)
        movsx ax, byte[c]
        mov dl, -4
        idiv dl
        ;al=q, ah=r
        
        
        ;a * b + c / (-4)
        movsx ecx, al
        add ebx, ecx
        
        
        ;a * b + c / (-4) – d 
        sub ebx, dword[d]
        ;e1 = ebx
        
        
        ;printing msj
        push msj
        call [printf]
        add esp, 4*1
        
        
        ;printing e1
        push ebx
        push format
        call [printf]
        add esp, 4*2

    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
