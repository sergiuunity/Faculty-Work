bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
                          import printf  msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; A string of words is given.
    ; extract all words from odd position.
    ; print the resulted string on screen
    s dw 1,2,3,4,5,6
    ls equ ($-s)/2
    d resw ls/2
    format db '%d ', 0
    contorelemD dd 0
    copie dd 0
    msj db ' the resulted string is: ', 0

; our code starts here
segment code use32 class=code
    start:
    
    mov esi, 2 ; prima poz impara
    mov edi, 0; d
    mov ecx, ls/2
    repeta:
        mov ax, word[s+esi]
        mov word[d+edi], ax
        inc dword[contorelemD] ; nr de elem din D
        add esi, 4
        add edi, 2 ; d string words
    loop repeta
        
        ; printare mesaj
        push dword msj
        call [printf]
        add esp, 4*1
        
        ; print string d
        mov ecx, [contorelemD]
        mov esi, 0
        repetaprint:
        
            mov ax, word[d+esi]
            ; ax -> eax
            ; stiva - 32 biti
            ; doar dd pe stiva
            movsx eax, ax
            mov [copie], ecx
            push eax
            push dword format
            call [printf]
            add esp, 4*2
            mov ecx, [copie]
            add esi, 2
            
        loop repetaprint
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
