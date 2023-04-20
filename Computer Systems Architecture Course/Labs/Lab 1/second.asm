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
;a+4-b-0101b+c
a dw 10; word = 16 bits
b db 2 ; byte = 8 bits
c dd 0ch ; doubleword = 32 bits

; our code starts here
segment code use32 class=code
    start:
        ; ...
    
    ;a+4
    mov bx,[a];bx=a=10
    add bx, 4;bx=14=000Eh
    
    ; a+4-b-0101b
    ;convert byte to word
    mov cl, [b]
    mov ch, 0
    ;cx = 0002h
    sub bx, cx; bx = bx-cx = 12 = 000Ch
    
    ; a+4-b-0101b
    sub bx, 0101b; b - b for binary base
    ;bx -bx-0101b-12-0101b = 7 = 0007h
    ;convert cx to  a doubleword, for instance to EAX
    
    mov eax, 0
    mov ax, bx;
    ;eax = 00000007h
    
    ;a+4-b-0101b+call
    add eax, [c]; eax = 00000007h+0000000ch= 19 = 13h
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
