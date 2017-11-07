include 'emu8086.inc'
org 100h

printn "Enter a string"
lea di,buffer      ; Buffer address for get_string
mov dx,20          ; Buffer size for get_string
call get_string     

printn
printn "String entered is"
mov si,di           ; Make print address 'si' the same as 'di'
call print_string
                



printn
printn "The length of the string is"

lea si, buffer 
mov cx, -1
loop1:
    LODSB
    INC CX
    CMP AL, 0 
    JNE loop1
mov ax, cx 
call print_num_uns


buffer DB ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?      

define_get_string
define_print_string   
define_print_num
define_print_num_uns

end


 

ret




