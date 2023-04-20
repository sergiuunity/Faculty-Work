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

    a db 7
    b db 8
    c db 5
    x db 3
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
mov eax, 0
mov ebx, 0
mov ecx, 0
mov edx, 0
;a+b
;transform a byte into a word
mov al, [a]
mov ah, 0
;ax = a = 0007
add ax, [b]; a=7+8

;a+b-call;convert ax into EAX
sub EAX, [c];7+8-5
;beacuse we added value 0 in EAX on the beginning

mov bl, [x]
sub eax, ebx

mov cx, [y]
add eax, ecx;
    
  
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
