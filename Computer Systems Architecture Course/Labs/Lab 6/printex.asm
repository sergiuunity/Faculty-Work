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
    ; a*(-b) + c/5 - d
    ;a byte
    ;b word
    ;c byte
    ;d doubleword
    ; print the result on screen
    a db -4
    b dw 3
    c db 11
    d dd 7
    ; signed
    aux dd 0
    formatmsg db 'rez: %d in decimal and %x in hexdecimal', 0 ; asciiz
    
; our code starts here
segment code use32 class=code
    start:
        ; a*(-b)
        ;-b
        mov ax,[b]
        neg ax ; ax = -b
        ; mov ax, 0
        ;sub ax,[b]; ax = -b
        ;a-> word
        movsx bx, byte[a]
        imul bx ; dx:ax = a*(-b)
        ;save dx:ax into aux
        mov [aux+0], ax
        mov [aux+2], dx
        
        ; c/5
        ;c-> word ax
        movsx ax, byte[c]
        mov bl, 5
        idiv bl ; ax/5 = al cat, ah rest
        
        ;; a*(-b) + c/5 - d
        ;   aux    + al  -dd
        ;al->eax
        movsx eax, al
        add eax, [aux]
        sub eax,[d]; rez este in eax
        
        ; print eax
        ;printf (format, val de printat)
        ; pe stiva de la dr la st
        ;  formatmsg db 'rez: %d in decimal and %x in hexdecimal', 0 ; asciiz
        ;                      eax              eax
        push eax
        push eax
        push dword formatmsg
        call [printf]
        add esp, 4*3
        
        
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
