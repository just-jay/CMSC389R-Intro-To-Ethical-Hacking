; code to compute the tribonacci function in x86

section .text ; text section, used for the actual code
trib:         ; This sets up the frame for this function call (a symbolic label called trib)

push ebp      ; Store the previous base pointer
mov ebp, esp  ; set the base pointer to the top of this stack

              ;base cases
mov 0, ebx    ; store 0
cmp ebx, eax  ; compare 0 to passed in value
je finish     ; if it equals 0, jump to finish

mov 2, ebx    ; store 2
cmp ebx, eax  ; comapre 2 to passed in value
jge ret_one   ; if 2 >= passed in number, return 1

              ; Otherwise we need to do calculations
mov ecx, eax  ; move eax to ecx
sub ecx, 3    ; subtract 3 from ecx so we loop the right number of times
mov eax, 0    ; move 0 to eax
mov ebx, 1    ; move 1 to ebx
mov edx, 1    ; move 1 to edx

trib:         ; tribonacci label
             
add eax, ebx  ; add ebx to eax (ex. 0 + 1 = 1)
add eax, edx  ; add edx to eax (ex. 1 + 1 = 2)

mov edi, eax  ; save the current calculated sum (temp == current tribnacci value)
mov eax, ebx  ; update eax to be ebx
mov ebx, edx  ; update ebx to be edx
mov edx, edi  ; update edx to be edi (set edx equal to the current tribonacci number)
loop trib     ; keep looping until ecx reaches 0

jmp finish    ; jump to the finish 

ret_one:      ; return 1 base case
mov 1, eax    ; put 1 into eax

finish:       ; finish label
mov esp, ebp  ; set the stack pointer to the base pointer (undo what we did to make the frame)
pop ebp       ; pop off the current base pointer
ret           ; Return the value of the function
