// CompilerParser.cpp
#include "CompilerParser.h"

CompilerParser::CompilerParser(const std::vector<Token*>& tokens) : tokens(tokens), tokenIndex(0) {}

ParseTree* CompilerParser::compileClass() {
    ParseTree* classTree = new ParseTree("class", "");
    if (tokenIndex < tokens.size() && tokens[tokenIndex]->getType() == "keyword" && tokens[tokenIndex]->getValue() == "class") {
        classTree->addChild(tokens[tokenIndex++]);
        if (tokenIndex < tokens.size() && tokens[tokenIndex]->getType() == "identifier") {
            classTree->addChild(tokens[tokenIndex++]);
            if (tokenIndex < tokens.size() && tokens[tokenIndex]->getValue() == "{") {
                classTree->addChild(tokens[tokenIndex++]);
                while (tokenIndex < tokens.size() && tokens[tokenIndex]->getValue() != "}") {
                    classTree->addChild(compileClassVarDec());
                }
                if (tokenIndex < tokens.size() && tokens[tokenIndex]->getValue() == "}") {
                    classTree->addChild(tokens[tokenIndex++]);
                } else {
                    throw std::runtime_error("Expected '}' at the end of class");
                }
            } else {
                throw std::runtime_error("Expected '{' after class name");
            }
        } else {
            throw std::runtime_error("Expected class name");
        }
    } else {
        throw std::runtime_error("Expected 'class' keyword");
    }
    return classTree;
}

ParseTree* CompilerParser::compileClassVarDec() {
    ParseTree* varDecTree = new ParseTree("classVarDec", "");
    if (tokenIndex < tokens.size() && (tokens[tokenIndex]->getValue() == "static" || tokens[tokenIndex]->getValue() == "field")) {
        varDecTree->addChild(tokens[tokenIndex++]);
        if (tokenIndex < tokens.size() && (tokens[tokenIndex]->getType() == "keyword" || tokens[tokenIndex]->getType() == "identifier")) {
            varDecTree->addChild(tokens[tokenIndex++]);
            if (tokenIndex < tokens.size() && tokens[tokenIndex]->getType() == "identifier") {
                varDecTree->addChild(tokens[tokenIndex++]);
                while (tokenIndex < tokens.size() && tokens[tokenIndex]->getValue() == ",") {
                    varDecTree->addChild(tokens[tokenIndex++]);
                    if (tokenIndex < tokens.size() && tokens[tokenIndex]->getType() == "identifier") {
                        varDecTree->addChild(tokens[tokenIndex++]);
                    } else {
                        throw std::runtime_error("Expected variable name after ','");
                    }
                }
                if (tokenIndex < tokens.size() && tokens[tokenIndex]->getValue() == ";") {
                    varDecTree->addChild(tokens[tokenIndex++]);
                } else {
                    throw std::runtime_error("Expected ';' after variable declaration");
                }
            } else {
                throw std::runtime_error("Expected variable name");
            }
        } else {
            throw std::runtime_error("Expected type for variable declaration");
        }
    }
    return varDecTree;
}

ParseTree* CompilerParser::compileReturn() {
    ParseTree* returnTree = new ParseTree("returnStatement", "");
    if (tokenIndex < tokens.size() && tokens[tokenIndex]->getType() == "keyword" && tokens[tokenIndex]->getValue() == "return") {
        returnTree->addChild(tokens[tokenIndex++]);
        if (tokenIndex < tokens.size() && tokens[tokenIndex]->getValue() != ";") {
            returnTree->addChild(compileExpression());
        }
        if (tokenIndex < tokens.size() && tokens[tokenIndex]->getValue() == ";") {
            returnTree->addChild(tokens[tokenIndex++]);
        } else {
            throw std::runtime_error("Expected ';' after return statement");
        }
    } else {
        throw std::runtime_error("Expected 'return' keyword");
    }
    return returnTree;
}

ParseTree* CompilerParser::compileExpression() {
    // Placeholder for actual expression compilation logic
    ParseTree* expressionTree = new ParseTree("expression", "");
    if (tokenIndex < tokens.size()) {
        expressionTree->addChild(tokens[tokenIndex++]);
    }
    return expressionTree;
}
