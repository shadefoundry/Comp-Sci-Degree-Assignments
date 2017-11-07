;code does not entirely work as intended
;I could not find how to store the user input in a variable,
;so I had to resort to having a hard coded user input.
;The code to reverse the case does work though, so this is what
;is important to me.
.model small
.stack 100h
.data
input db "InsertUserInputHere$"
.code



mov AX,@data
mov DS,AX
mov SI,offset input
LOOP1:mov AL,[SI]
    CMP AL,'$'  ;searches for '$' to know when to stop inverting
    JE LOOP2
    XOR AL,32
    MOV [SI],AL
    INC SI
    JMP LOOP1
LOOP2:MOV [SI],AL
    MOV DX,offset input
    MOV AH,9
    INT 21h
    MOV AH ,4ch
    INT 21h
END
RET