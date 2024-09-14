// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@R1
A=M
D=M
@R0
M=D
@R2
D=M

//JUMP to loop
@LOOP
D;JEQ
@R3
M=D-1

//loop
(LOOP)
@R1
M=M+1
A=M
D=M

@R0
D=D-M
@MIN
D;JLT
@R3
M=M-1
@LOOP_END
D=M
D;JEQ
@LOOP
0;JMP

(MIN)
@R1
A=M
D=M
@R0
M=D

@R3
M=M=1
@LOOP_END
D=M
D;JEQ
@LOOP
0;JMP

(LOOP_END)
@LOOP_END
0;JMP
