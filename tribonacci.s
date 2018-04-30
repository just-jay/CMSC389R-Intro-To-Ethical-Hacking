; code to compute the tribonacci function in x86

section .text ; text section, used for the actual code
trib:         ; This sets up the frame for this function call (a symbolic label called do_this)

push ebp      ; Store the previous base pointer
mov ebp, esp  ; set the base pointer to the top of this stack
push edi      ; save teh values of the register that this function uses

              ;base cases
mov 0, ebx    ; store 0
cmp ebx, eax  ; compare 0 to passed in value
je finish     ; if it equals 0, jump to finish

mov 2, ebx    ; store 2
cmp ebx, eax  ; comapre 2 to passed in value
jge ret_one   ; if 2 >= passed in number, return 1

              ; Otherwise we need to do calculations
              ; TIME FOR SOME RECUSINO BOIIIS            
sub eax, 1    ; subtract 1 from eax


jmp finish    ; jump to the finish 

ret_one:      ; return 1 base case
mov 1, eax    ; put 1 into eax

finish:       ; finish label
pop edi       ; pop edi
mov esp, ebp  ; set the stack pointer to the base pointer (undo what we did to make the frame)
pop ebp       ; pop off the current base pointer
ret           ; Return the value of the function
