// ParseTree.h
#ifndef PARSETREE_H
#define PARSETREE_H

#include <string>
#include <vector>
#include <iostream>

class ParseTree {
public:
    // Constructor
    ParseTree(const std::string& node_type, const std::string& value = "");

    // Method to add a child to the parse tree
    void addChild(ParseTree* child);

    // Method to get children of the parse tree
    const std::vector<ParseTree*>& getChildren() const;

    // Method to get the type of the node
    const std::string& getType() const;

    // Method to get the value of the node
    const std::string& getValue() const;

    // Method to print the parse tree
    void print(int depth = 0) const;

private:
    std::string node_type;
    std::string value;
    std::vector<ParseTree*> children;
};

#endif
