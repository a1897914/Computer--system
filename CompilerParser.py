from ParseTree import *

class CompilerParser :

    
    

    def __init__(self,tokens):
        """
        Constructor for the CompilerParser
        @param self.tokens A list of self.tokens to be parsed
        """
        
        self.tokens = tokens
        self.tokenCount = -1
        self.tokenNow = ""


        pass
    

    def compileProgram(self):
        """
        Generates a parse tree for a single program
        @return a ParseTree that represents the program
        """

        programTree = None

        self.readToken()
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "class":
            programTree = self.compileClass()
        else:
            raise ParseException("The program doesn't begin with a class")

        return programTree
    
    
    def compileClass(self):
        """
        Generates a parse tree for a single class
        @return a ParseTree that represents a class
        """
        classTree = ParseTree("class", "")
        #classTree.addChild(self.tokenNow)

        if self.tokenCount < 0:
            self.readToken()

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "class":
            classTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("The program doesn't begin with a class")

       
        if self.tokenNow.getType() == "identifier":
            classTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No identifier found")



        if self.tokenNow.getValue() == "{" and self.tokenNow.getType() == "symbol": 
            classTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No opening bracket")
        

        while self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "static" or self.tokenNow.getValue() == "field":
            classTree.addChild(self.compileClassVarDec())


        while self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "function" or self.tokenNow.getValue() == "method" or self.tokenNow.getValue() == "constructor":
            classTree.addChild(self.compileSubroutine())


        if self.tokenCount < len(self.tokens)-1:
            self.readToken()

        while self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "function" or self.tokenNow.getValue() == "method" or self.tokenNow.getValue() == "constructor":
            classTree.addChild(self.compileSubroutine())


        if self.tokenNow.getValue() == "}" and self.tokenNow.getType() == "symbol":
            classTree.addChild(self.tokenNow)
        else:
            raise ParseException("No closing bracket")

        
        return classTree 
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """

        classVarDecTree = ParseTree("classVarDec","")
        #classVarDecTree.addChild(self.tokenNow)

        if self.tokenCount < 0:
            self.readToken()
        

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "static" or self.tokenNow.getValue() == "field":
            classVarDecTree.addChild(self.tokenNow)
            self.readToken()
        
 
            if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['int', 'char', 'boolean']:
                classVarDecTree.addChild(self.tokenNow)
                self.readToken()
            elif self.tokenNow.getType() == "identifier": 
                classVarDecTree = ParseTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("No type")

        
            if self.tokenNow.getType() == "identifier":
                classVarDecTree.addChild(self.tokenNow)
                self.readToken()
            else: 
                raise ParseException("No variable")

        
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ",":
                classVarDecTree.addChild(self.tokenNow)
                self.readToken()

                if self.tokenNow.getType() == "identifier":
                    classVarDecTree.addChild(self.tokenNow)
                    self.readToken()
                else:
                    raise ParseException("???")


            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ";":
                classVarDecTree.addChild(self.tokenNow)
                if self.tokenCount < len(self.tokens) - 1:
                    self.readToken()
            else: 
                raise ParseException("????")


        
        return classVarDecTree 
    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        subroutineTree = ParseTree("subroutine","")
        #subroutineTree.addChild(self.tokenNow)

        if self.tokenCount < 0:
            self.readToken()

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['function', 'method', 'constructor']:
            subroutineTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No function method or constructor")

        
        if self.tokenNow.getType() == "identifier" or (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['void', 'int', 'char', 'boolean']):
            subroutineTree.addChild(self.tokenNow)
            self.readToken()
        
        
        if self.tokenNow.getType() == "identifier":
            subroutineTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No identifier")
        
        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "(":
            subroutineTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No opening parathesis")

  
        if self.tokenNow.getType() == "identifier" or (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['int', 'char', 'boolean']):
            subroutineTree.addChild(self.compileParameterList())
        

        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ")":
            subroutineTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No closing parathesis")


        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "{":
            subroutineTree.addChild(self.compileSubroutineBody())
        else:
            raise ParseException("No opening bracket for function body")

        
        return subroutineTree 
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        parameterListTree = ParseTree("parameterList","")
        #parameterListTree.addChild(self.tokenNow)

        if self.tokenCount < 0:
            self.readToken()
        

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['int', 'char', 'boolean']:
            parameterListTree.addChild(self.tokenNow)
            self.readToken()
        elif self.tokenNow.getType() == "identifier": 
            parameterListTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No type")

        #print(self.tokenNow)
        if self.tokenNow.getType() == "identifier":
            parameterListTree.addChild(self.tokenNow)
        else: 
            raise ParseException("No variable")

        # HOW TO CHECK IF THEIR IS A COMMA OR JUST 1 VARIABLE
        if self.tokenCount < len(self.tokens) - 1:
                self.readToken()
        else:
            return parameterListTree

        
        while self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ",":
            parameterListTree.addChild(self.tokenNow)
            self.readToken()
            
            if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['int', 'char', 'boolean']:
                parameterListTree.addChild(self.tokenNow)
                self.readToken()
            elif self.tokenNow.getType() == "identifier": 
                parameterListTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("No type")

            if self.tokenNow.getType() == "identifier":
                parameterListTree.addChild(self.tokenNow)
                if self.tokenCount < len(self.tokens) - 1:
                    self.readToken()
            else:
                raise ParseException("No variable after comma")


        return parameterListTree
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        subroutineBodyTree = ParseTree("subroutineBody","")
        #subroutineBodyTree.addChild(self.tokenNow)

        if self.tokenCount < 0:
            self.readToken()
        
        if self.tokenNow.getValue() == "{" and self.tokenNow.getType() == "symbol": 
            subroutineBodyTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No opening bracket")

     
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "var":
            subroutineBodyTree.addChild(self.compileVarDec())

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "let" or self.tokenNow.getValue() == "do" or self.tokenNow.getValue() == "if" or self.tokenNow.getValue() == "while" or self.tokenNow.getValue() == "return":
            subroutineBodyTree.addChild(self.compileStatements())

        
        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "}":
            subroutineBodyTree.addChild(self.tokenNow)
        else:
            raise ParseException("No closing bracket")


        return subroutineBodyTree
    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """
        varDecTree = ParseTree("varDec","")
        #varDecTree.addChild(self.tokenNow)
        
        if self.tokenCount < 0:
            self.readToken()
        #print(self.tokenNow)
        while self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "var":
            varDecTree.addChild(self.tokenNow)
            self.readToken()

            #print(self.tokenNow)
            if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['int', 'char', 'boolean']:
                varDecTree.addChild(self.tokenNow)
                self.readToken()
            elif self.tokenNow.getType() == "identifier": 
                varDecTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("No type")

            #print(self.tokenNow)
            if self.tokenNow.getType() == "identifier":
                varDecTree.addChild(self.tokenNow)
                self.readToken()
            else: 
                raise ParseException("No variable")

            
            while self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ",":
                varDecTree.addChild(self.tokenNow)
                self.readToken()

                if self.tokenNow.getType() == "identifier":
                    varDecTree.addChild(self.tokenNow)
                    self.readToken()
            
            
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ";":
                varDecTree.addChild(self.tokenNow)
                if self.tokenCount < len(self.tokens) - 1:
                    self.readToken()
            else:
                raise ParseException("No ;")

        

        return varDecTree 
    

    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """
        statementsTree = ParseTree("statements","")
        
        if self.tokenCount < 0:
            self.readToken()


        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "let":
            statementsTree.addChild(self.compileLet()) 
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "if":
            statementsTree.addChild(self.compileIf())
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "while":
            statementsTree.addChild(self.compileWhile())
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "do":
            statementsTree.addChild(self.compileDo())
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "return":
            statementsTree.addChild(self.compileReturn())

        return statementsTree 
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        letStatementTree = ParseTree("letStatement","")

        if self.tokenCount < 0:
            self.readToken()

        while self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "let":
            letStatementTree.addChild(self.tokenNow)
            self.readToken()
        
       
            if self.tokenNow.getType() == "identifier":
                letStatementTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("Variable has no name")

        
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "[":
                letStatementTree.addChild(self.tokenNow)
                self.readToken()

            
            if (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "skip") or self.tokenNow.getType() == "integerConstant" or self.tokenNow.getType() == "stringConstant":
                letStatementTree.addChild(self.compileExpression())

           
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "]":
                letStatementTree.addChild(self.tokenNow)
                self.readToken()
            
           
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "=":
                letStatementTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("Nothing following variable name")

        
            if (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "skip") or self.tokenNow.getType() == "integerConstant" or self.tokenNow.getType() == "stringConstant":
                letStatementTree.addChild(self.compileExpression())
            else:
                raise ParseException("Variable doesn't equal anything")

            
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ";":
                letStatementTree.addChild(self.tokenNow)
                if self.tokenCount < len(self.tokens) - 1:
                    self.readToken()
            else:
                raise ParseException("No ;")


        return letStatementTree 
    

    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        ifStatementTree = ParseTree("ifStatement", "")

        if self.tokenCount < 0:
            self.readToken()

        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "if":
            ifStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("Statement doesn't begin with if")

        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "(":
            ifStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("missing opening paranthesis")

        
        if (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "skip") or self.tokenNow.getType() == "integerConstant" or self.tokenNow.getType() == "stringConstant":
            ifStatementTree.addChild(self.compileExpression())
        else:
            raise ParseException("if statement has no expression")
        

        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ")":
            ifStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("missing closing paranthesis")


        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "{":
            ifStatementTree.addChild(self.tokenNow)
            self.readToken()
        else: 
            raise ParseException("missing opening bracket for if statement body")

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "let":
            ifStatementTree.addChild(self.compileStatements())
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "if":
            ifStatementTree.addChild(self.compileStatements())
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "while":
            ifStatementTree.addChild(self.compileStatements())
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "do":
            ifStatementTree.addChild(self.compileStatements())
        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "return":
            ifStatementTree.addChild(self.compileStatements())
        
        
        
        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "}":
            ifStatementTree.addChild(self.compileStatements())
            ifStatementTree.addChild(self.tokenNow)
            if self.tokenCount < len(self.tokens) - 1:
                self.readToken()
        else:
            raise ParseException("missing closing bracket for if statement body")



        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "else":
            ifStatementTree.addChild(self.tokenNow)
            self.readToken()

            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "{":
                ifStatementTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("missing opening bracket for else statement body")

            
            if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "let":
                ParseTree.statementsTree.addChild(self.compileStatements())
            elif self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "if":
                ParseTree.statementsTree.addChild(self.compileStatements())
            elif self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "while":
                ParseTree.statementsTree.addChild(self.compileStatements())
            elif self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "do":
                ParseTree.statementsTree.addChild(self.compileStatements())
            elif self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "return":
                ParseTree.statementsTree.addChild(self.compileStatements())
           
        
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "}":
                ifStatementTree.addChild(self.tokenNow)
            else:
                raise ParseException("missing closing bracket for if statement body")


        return ifStatementTree 
    
    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        whileStatementTree = ParseTree("whileStatement", "")

        if self.tokenCount < 0:
            self.readToken()

        
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "while":
            whileStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("Statement doesn't begin with while")

        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "(":
            whileStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("missing opening paranthesis")

        if (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "skip") or self.tokenNow.getType() == "integerConstant" or self.tokenNow.getType() == "stringConstant":
            whileStatementTree.addChild(self.compileExpression())
        else:
            raise ParseException("while statement has no expression")
        

        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ")":
            whileStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("missing closing paranthesis")

        
        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "{":
            whileStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("No opening bracket for while statement body")

    
        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "let":
            whileStatementTree.addChild(self.compileStatements())

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "if":
            whileStatementTree.addChild(self.compileStatements())

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "while":
            whileStatementTree.addChild(self.compileStatements())

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "do":
                whileStatementTree.addChild(self.compileStatements())

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "return":
            whileStatementTree.addChild(self.compileStatements())
        

        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "}":
            whileStatementTree.addChild(self.compileStatements())
            whileStatementTree.addChild(self.tokenNow)
        else:
            raise ParseException("missing closing bracket for while statement body")

        return whileStatementTree 
    

    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        doStatementTree = ParseTree("doStatement", "")

        if self.tokenCount < 0:
            self.readToken()

        
        while self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "do":
            doStatementTree.addChild(self.tokenNow)
            self.readToken()

        
            if (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "skip") or self.tokenNow.getType() == "integerConstant" or self.tokenNow.getType() == "stringConstant":
                doStatementTree.addChild(self.compileExpression())
            else:
                raise ParseException("do statement has no expression")
            
            #print(self.tokenNow) dont put read token here
            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ";":
                doStatementTree.addChild(self.tokenNow)
            else:
                raise ParseException("missing ;")


        return doStatementTree 
    

    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        returnStatementTree = ParseTree("returnStatement", "")

        if self.tokenCount < 0:
            self.readToken()


        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "return":
            returnStatementTree.addChild(self.tokenNow)
            self.readToken()
        else:
            raise ParseException("Statement doesn't begin with return")

        if (self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "skip") or self.tokenNow.getType() == "integerConstant" or self.tokenNow.getType() == "stringConstant":
            returnStatementTree.addChild(self.compileExpression())

        if self.tokenCount < len(self.tokens) - 1:
            self.readToken()


        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ";":
            returnStatementTree.addChild(self.tokenNow)
        else:
            raise ParseException("missing ;")

        return returnStatementTree 
    

    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        expressionTree = ParseTree("expression","")

        if self.tokenCount < 0:
            self.readToken()

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() == "skip":
            expressionTree.addChild(self.tokenNow)
            if self.tokenCount < len(self.tokens) - 1:
                self.readToken()
        
        if self.tokenNow.getType() == "integerConstant":
            expressionTree.addChild(self.compileTerm)
        
        if self.tokenNow.getType() == "stringConstant":
            expressionTree.addChild(self.compileTerm)
        
        if self.tokenNow.getType() == "identifier":
            expressionTree.addChild(self.compileTerm)

        return expressionTree 
    

    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        termTree = ParseTree("term","")

        if self.tokenCount < 0:
            self.readToken()

        if self.tokenNow.getType() == "integerConstant":
            termTree.addChild(self.tokenNow)

        if self.tokenNow.getType() == "stringConstant":
            termTree.addChild(self.tokenNow)

        if self.tokenNow.getType() == "keyword" and self.tokenNow.getValue() in ['true', 'false', 'null', 'this']:
            termTree.addChild(self.tokenNow)


        if self.tokenNow.getType() == "identifier":
            termTree.addChild(self.tokenNow)
            if self.tokenCount < len(self.tokens) - 1:
                self.readToken()

            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "[":
                termTree.addChild(self.tokenNow)
                self.readToken()
            
                if self.tokenNow.getType == "keyword" and self.tokenNow.getValue() == "skip":
                    termTree.addChild(self.compileExpression)
                elif self.tokenNow.getType == "integerConstant" or self.tokenNow.getType() == "stringConstant":
                    termTree.addChild(self.tokenNow)
                else:
                    raise ParseException("no expression in brackets")

                if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "]":
                    termTree.addChild(self.tokenNow)
                else:
                    raise ParseException("no closing bracket")

        
        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == "(":
            termTree.addChild(self.tokenNow)
            self.readToken()

            if self.tokenNow.getType == "keyword" and self.tokenNow.getValue() == "skip":
                termTree.addChild(self.compileExpression())
            elif self.tokenNow.getType == "integerConstant" or self.tokenNow.getType() == "stringConstant":
                termTree.addChild(self.tokenNow)
                self.readToken()
            elif self.tokenNow.getType() == "identifier":
                termTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("no expression in paranthesis")

            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() in ['+', '-', '*', '/']:
                termTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("not doing anything with variable in paranthesis")

            if self.tokenNow.getType() == "identifier" or self.tokenNow.getType() == "integerConstant":
                termTree.addChild(self.tokenNow)
                self.readToken()
            else:
                raise ParseException("invalid syntax")

            if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() == ")":
                termTree.addChild(self.tokenNow)
            else:
                raise ParseException("no closing paranthesis")

        if self.tokenNow.getType() == "symbol" and self.tokenNow.getValue() in ['-', '~']:
            termTree.addChild(self.tokenNow)
            self.readToken()

            if self.tokenNow.getType == "integerConstant" or self.tokenNow.getType() == "stringConstant":
                    termTree.addChild(self.tokenNow)
            else: 
                raise ParseException("unary Op term has no term")   

        # if self.tokenNow.getType() == "identifier"   


                
        return termTree 
    

    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        return None 

    def readToken(self): 
        self.tokenCount+=1
        self.tokenNow = self.tokens[self.tokenCount]
    


if __name__ == "__main__":


    """ 
    self.tokens for:
        class MyClass {
        
        }
    """
    tokens = []


    parser = CompilerParser(tokens)

    result = parser.compileProgram()    
 

    print(result)
