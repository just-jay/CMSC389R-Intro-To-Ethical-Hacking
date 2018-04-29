<b>I pledge on my honor that I have not given or received any unauthorized assistance on this homework or assignment. -Jacob Elspas</b>

<h2>Homework #10</h2>
  
---
Part 1: 
For this part we had to trace 2 different programs written in x86 assembly. Below, I've provided the programs, as well as a comment on each line explaining what is happening at that stage in the program

``` 
; what does this return?
section .text
do_this:
  push ebp
  mov ebp, esp

  mov ecx, 4
  mov dl, 0ffh

f:
  shl eax, 8
  or al, dl
  loop f

  mov ecx, 8
  mov dx, 6761h
  shl edx, cl
  shl edx, cl
  mov dx, 6c66h

  xor eax, edx
  not eax

  mov esp, ebp
  pop ebp
  ret 
  ```
