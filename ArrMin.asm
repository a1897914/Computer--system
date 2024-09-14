// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1
A=M
D=M
@R0
M=D
@R2
D=M
@END_LOOP
D;JEQ
@R3
M=D-1
(LOOP_START)
@R1
M=M+1
A=M
D=M
@R0
D=D-M
@UPDATE_MIN
D;JLT
@R3
M=M-1
@LOOP_END
D=M
D;JEQ
@LOOP_START
0;JMP

(UPDATE_MIN)
@R1
A=M
D=M
@R0
M=D
@R3
M=M-1
@LOOP_END
D=M
D;JEQ
@LOOP_START
0;JMP
(LOOP_END)
@END
0;JMP
