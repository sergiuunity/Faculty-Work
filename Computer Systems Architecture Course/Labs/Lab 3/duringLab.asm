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
              ;else exp=1010h-(-b)*3+e
    
     a db 13
     b dw 3
     c db 16
     d dd 12345600h
     e dq 1122334455660000h
     aux dd 0
     exp dq 0
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ;a/b
        ;a byte-> dx:ax
        mov al, [a]
        movsx ax, al; sau cbw
        cwd;ax->dx:ax
        idiv word[b]
        ;ax-q dx-r
        cmp ax, 1
        JE thenlabel
        JNE elselabel
        
        thenlabel:
            ;exp = a*b+c/(-3) + d
            ;a*b
            mov al,[a]
            cbw; ax=a*b
            imul word[b];dx:ax=a*b
            ;dx:ax->aux
            mov word[aux+0],ax
            mov word[aux+2],dx
            
            ;c/(-3)
            mov al, [c]
            movsx ax,al
            mov bl, -3
            idiv bl;ax/bl=al-q, ah-r
            ;convert al la eax
            movsx eax, al
            add eax, [aux]
            add eax, [d]
            cdq
            mov [exp+0], eax
            mov[exp+4],edx
            
            jmp myendif
            
            elselabel:
            ;exp=1010h-(-b)*3+e
            ;-b*3
            mov ax, [b]
            neg ax;ax=-b
            mov bx, 3
            imul bx;dx:ax = -b *3
            ;dx:ax->aux
            mov word[aux+0], ax
            mov word[aux+2], dx
            ;1010h - (-b)*3
            sub ebx, [aux];ebx=1010h-(-b)*3
            ;ebx->edx:eax
            mov eax, ebx
            cdq;edx:eax = 1010h-(-b)*3
            ;edx:eax+
            ;phe:ple
            add eax, dword[e+0]
            adc edx, dword[e+4] 
            mov [exp+0], eax
            mov[exp+4],edx
            
        myendif:        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
