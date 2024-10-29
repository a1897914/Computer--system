// CompilerParser.h
#ifndef COMPILERPARSER_H
#define COMPILERPARSER_H

#include "Token.h"
#include <vector>
#include <stdexcept>

class CompilerParser {
public:
    CompilerParser(const std::vector<Token*>& tokens);
    ParseTree* compileClass();
    ParseTree* compileClassVarDec();
    ParseTree* compileReturn(); 
    ParseTree* compileExpression(); 

private:
    std::vector<Token*> tokens;
    size_t tokenIndex;
};

#endif
