// Main.cpp
#include "CompilerParser.h"
#include "Token.h"
#include <iostream>
#include <vector> // Changed back to vector

int main() {
    // Example usage of CompilerParser
    std::vector<Token*> tokens = { // Changed back to vector
        new Token("keyword", "class"),
        new Token("identifier", "MyClass"),
        new Token("symbol", "{"),
        new Token("keyword", "static"),
        new Token("keyword", "int"),
        new Token("identifier", "x"),
        new Token("symbol", ";"),
        new Token("symbol", "}"),
    };

    CompilerParser parser(tokens);
    try {
        ParseTree* classTree = parser.compileClass();
        classTree->print();
        delete classTree;
    } catch (const std::runtime_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    // Clean up memory
    for (auto token : tokens) {
        delete token;
    }

    return 0;
}
