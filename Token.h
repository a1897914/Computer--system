// Token.h
#ifndef TOKEN_H
#define TOKEN_H

#include "ParseTree.h"

class Token : public ParseTree {
public:
    Token(const std::string& node_type, const std::string& value);
};

#endif
