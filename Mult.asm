// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@R0
M=0
@R1
D=M
@END_LOOP
D;JEQ
@R1
D=M
(LOOP_START)
@R0
M=M+D
@R2
M=M-1
D=M
@LOOP_START
D;JGT
(END_LOOP)
0;JMP