// Calculates R1 + R2 - R3 and stores the result in R0.
// (R0, R1, R2, R3 refer to RAM[0], RAM[1], RAM[2], and RAM[3], respectively.)

// Put your code here.
// Load the value of R1 into the accumulator (ACC)
LOAD R1         // ACC = RAM[1]

// Add the value of R2 to the accumulator
ADD R2          // ACC = ACC + RAM[2]

// Subtract the value of R3 from the accumulator
SUB R3          // ACC = ACC - RAM[3]

// Store the result in R0
STORE R0        // RAM[0] = ACC

