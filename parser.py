import ply.yacc as yacc
from lexer import tokens

from my_ast import AssignNode, VarNode, PrintNode, IfNode, WhileNode, BinOpNode, UnaryOpNode, NumNode, BoolNode, NotNode, StringNode  # Import the node classes

# Precedence rules to handle the order of operations
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NE'),
    ('left', 'LT', 'LE', 'GT', 'GE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'NOT', 'UMINUS'),
)



def p_program(p):
    '''program : statement SEMICOLON program
               | statement'''
    if len(p) == 2:  # Single statement
        p[0] = [p[1]]
    else:  # Multiple statements
        p[0] = [p[1]] + p[3]

def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN block ELSE block
                 | IF LPAREN expression RPAREN block'''
    if len(p) == 8:
        p[0] = IfNode(p[3], p[5], p[7])
    else:
        p[0] = IfNode(p[3], p[5])

def p_statement_while(p):
    'statement : WHILE LPAREN expression RPAREN block'
    p[0] = WhileNode(p[3], p[5])
    
def p_statement_print(p):
    'statement : PRINT expression'
    p[0] = PrintNode(p[2])

def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression'
    p[0] = AssignNode(p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]
    
def p_block(p):
    '''block : LBRACE statement_list RBRACE
             | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[2]

def p_statement_list(p):
    '''statement_list : statement SEMICOLON statement_list
                      | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = BinOpNode(p[1], p[2], p[3])

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = UnaryOpNode(p[1], p[2])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = NotNode(p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = NumNode(p[1])

def p_expression_boolean(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = BoolNode(p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0] = StringNode(p[1][1:-1])  # Remove the surrounding quotes

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = VarNode(p[1])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser and make it available to import
parser = yacc.yacc()