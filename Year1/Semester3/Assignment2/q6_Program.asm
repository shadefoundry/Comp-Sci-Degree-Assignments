.model small
.stack 100h
.data
input db "DeepRaj$"
.code


swapCase proc
mov ax,@data
mov ds,ax
mov si,offset input
L1:mov al,[si]
;mov bl,al
cmp al,'$'
je L3
xor al,32
mov [si],al
inc si
jmp L1
L3:mov [si],al
mov dx,offset input
mov ah,9
int 21h
mov ah,4ch
int 21h
swapCase endp
end swapCase