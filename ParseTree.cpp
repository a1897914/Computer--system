// ParseTree.cpp
#include "ParseTree.h"

ParseTree::ParseTree(const std::string& node_type, const std::string& value)
    : node_type(node_type), value(value) {}

void ParseTree::addChild(ParseTree* child) {
    children.push_back(child);
}

const std::vector<ParseTree*>& ParseTree::getChildren() const {
    return children;
}

const std::string& ParseTree::getType() const {
    return node_type;
}

const std::string& ParseTree::getValue() const {
    return value;
}

void ParseTree::print(int depth) const {
    // Set indentation
    std::string indent;
    for (int i = 0; i < depth; ++i) {
        indent += "  | ";
    }

    // Generate output
    if (!children.empty()) {
        // Output if the node has children
        std::cout << node_type << "\n";
        for (const auto& child : children) {
            std::cout << indent << "  └ ";
            child->print(depth + 1);
        }
        std::cout << indent << "\n";
    } else {
        // Output if the node is a leaf/terminal
        std::cout << node_type << " " << value << "\n";
    }
}