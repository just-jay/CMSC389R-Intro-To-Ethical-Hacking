<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #10</h2>
  
---
Part 1: 
For this part we had to trace 2 different programs written in x86 assembly. Below, I've provided the programs, as well as a comment on each line explaining what is happening at that stage in the program.

Program 1:
``` 
; what does this return?
section .text
do_this:        ; These 2 lines set up a new stack frame
  push ebp      ; Store the previous base pointer
  mov ebp, esp  ; Set the base pointer to the top of stack

  mov ecx, 4    ; Move 4 into the ecx register
  mov dl, 0ffh  ; put the hex value 0ff into dl (11111111 in binary)

f:
  shl eax, 8    ; bit shift left the value in eax by 8 bits
  or al, dl     ;
  loop f        ;

  mov ecx, 8    ; Move 8 into the ecx register
  mov dx, 6761h ; put the hex value 6761 in dx (110011101100001 in binary)
  shl edx, cl   ; bit shift left the value in edx by the value in cl, in this case 8 bits
  shl edx, cl   ; bit shift left the value in edx by the value in cl, in this case 8 bits
                ; now 6761 is in the 'front half' of edx
  mov dx, 6c66h ; put the hex value 6c66 into dx (110110001100110 in binary)
                ; edx now holds 67616c66 in hex
  xor eax, edx  ; 
  not eax       ;
                ; These last three lines restore the frame and reset the pointers we moved at the beginning
  mov esp, ebp  ; set the stack pointer to the base pointer (undo what we did to make the frame)
  pop ebp       ; pop off the current base pointer
  ret           ; Return the value of the function
  ```
