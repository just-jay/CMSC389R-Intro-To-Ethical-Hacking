<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #10</h2>
  
---
Part 1: 
For this part we had to trace 2 different programs written in x86 assembly. Below, I've provided the programs, as well as a comment on each line explaining what is happening at that stage in the program.

Program 1:
``` 
; what does this return?
section .text   ; text section, used for actual code
do_this:        ; These 2 lines set up a new stack frame (a symbolic label called do_this)
  push ebp      ; Store the previous base pointer
  mov ebp, esp  ; Set the base pointer to the top of stack

  mov ecx, 4    ; Move 4 into the ecx register
  mov dl, 0ffh  ; put the hex value 0ff into dl (11111111 in binary)

f:              ; a symbolic label called f
  shl eax, 8    ; bit shift left the value in eax by 8 bits
  or al, dl     ; does a logical or of the current value in al and dl
  loop f        ; loop instruction automaticaly decrements ECX by 1 and keeps going while ECX != 0 (so 4 times)
                ; At the end of this looop eax has FFFFFFFF
  mov ecx, 8    ; Move 8 into the ecx register
  mov dx, 6761h ; put the hex value 6761 in dx (110011101100001 in binary)
  shl edx, cl   ; bit shift left the value in edx by the value in cl, in this case 8 bits
  shl edx, cl   ; bit shift left the value in edx by the value in cl, in this case 8 bits
                ; now 6761 is in the 'front half' of edx
  mov dx, 6c66h ; put the hex value 6c66 into dx (110110001100110 in binary)
                ; edx now holds 67616c66 in hex
  xor eax, edx  ; convert the xor of FFFFFFFF and 67616c66 -> 989e9399
  not eax       ; calculate the logical not of 989e9399 -> 67616c66
                ; These last three lines restore the frame and reset the pointers we moved at the beginning
  mov esp, ebp  ; set the stack pointer to the base pointer (undo what we did to make the frame)
  pop ebp       ; pop off the current base pointer
  ret           ; Return the value of the function, 67616c66
  ```
  
  Program 2:
  ```
  ; what does this return?
section .text         ; text section, used for the actual code
do_this:              ; This sets up the frame for this function call (a symbolic label called do_this)
  push ebp            ; Store the previous base pointer
  mov ebp, esp        ; set the base pointer to the top of this stack
  push edi            ; save teh values of the register that this function uses

  mov al, 33h         ; move 33 (in hex 110011) to the al part of the register
  mov cl, 4           ; move 4 to the  cl part of the register
  lea edi, [x]        ; put the memory contents at address x (which is 0) into edi

  rep stosb           ; This runs 4 times. It put 33h into x each time, giving us 33h33h33h33h in x
 
  xor BYTE [x], 0     ; 1st byte of x: -> 33h XOR 0 -> 110011
  xor BYTE [x+1], 0bh ; 2nd byte of x: -> 33h XOR 1011 -> 111000
  xor BYTE [x+2], 0ah ; 3rd byte of x: -> 33h XOR 1010 -> 111001
  xor BYTE [x+3], 61h ; 4th byte of x: -> 33h XOR 1100001 -> 1010010

  mov eax, [x]        ; move the value in [x] to eax
                      ; Now we're gonan start undoing the setup we did at the beginning of the function
  pop edi             ; pop the top element of the stack into edi
  mov esp, ebp        ; move stack pointer to the base
  pop ebp             ; pop the base pointer
  ret                 ; return the value and end the function -> 1100111110001110011010010

section .data         ; the data section of the program, used to declare initialized data
x dd 0                ; declare a 4 byte value, reffered to as location X, initialized to 0
```

---
Part 2
Compute the tribonacci sequence. In Assembly. Oh dear.

[An Attempt Was Made]()

Well, I tried.
