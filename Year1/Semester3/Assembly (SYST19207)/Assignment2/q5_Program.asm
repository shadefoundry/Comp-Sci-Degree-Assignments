;program must:
;-use get string to obtain string
;-store string in buffer
;-use loop to get length of string
;-print length of string with PRINT_NUM
;Code Built: Jul 27, 2016
org 100h
include 'emu8086.inc'  

PRINTN "Enter a string"
LEA DI,buffer   ;find the buffer
MOV DX,20       ;shove the buffer size in dx
CALL GET_STRING ;get the string     

PRINTN      
PRINTN "String entered is"
MOV SI,DI;put the buffer value into si
CALL PRINT_STRING;print the value from si to the screen


PRINTN
PRINTN "String length is"
LEA SI, buffer
MOV CX, -1
LOOP1:
    LODSB
    INC CX
    CMP AL, 0
    JNE LOOP1
MOV AX, CX
CALL PRINT_NUM_UNS

buffer DB 20 DUP(?)      

DEFINE_GET_STRING
DEFINE_PRINT_STRING
DEFINE_PRINT_NUM
DEFINE_PRINT_NUM_UNS
END
RET