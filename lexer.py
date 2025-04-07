import ply.lex as lex

# List of token names
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LT',
    'LE',
    'GT',
    'GE',
    'EQ',
    'NE',
    'AND',
    'OR',
    'NOT',
    'TRUE',
    'FALSE',
    'STRING',
    'IDENTIFIER',
    'ASSIGN',
    'PRINT',
    'IF',
    'ELSE',
    'WHILE',
    'SEMICOLON',
    'LBRACE',
    'RBRACE'
)

# Regular expressions for tokens
t_PLUS    = r'\b[a-zA-Z]{1}\b'  # +
t_MINUS   = r'\b[a-zA-Z]{2}\b'  # -
t_TIMES   = r'\b[a-zA-Z]{3}\b'  # *
t_DIVIDE  = r'\b[a-zA-Z]{4}\b'  # /
t_LPAREN  = r'\b[a-zA-Z]{5}\b'  # (
t_RPAREN  = r'\b[a-zA-Z]{6}\b'  # )
t_LBRACE  = r'\b[a-zA-Z]{7}\b'  # {
t_RBRACE  = r'\b[a-zA-Z]{8}\b'  # }

# Comparison operators
t_LT      = r'\b[a-zA-Z]{9}\b'  # <
t_LE      = r'\b[a-zA-Z]{10}\b'  # <=
t_GT      = r'\b[a-zA-Z]{11}\b'  # >
t_GE      = r'\b[a-zA-Z]{12}\b'  # >=
t_EQ      = r'\b[a-zA-Z]{13}\b'  # ==
t_NE      = r'\b[a-zA-Z]{14}\b'  # !=

# Logical operators
t_AND     = r'\b[a-zA-Z]{15}\b'  # and
t_OR      = r'\b[a-zA-Z]{16}\b'  # or
t_NOT     = r'\b[a-zA-Z]{17}\b'  # !

# Boolean literals
def t_TRUE(t):
    r'\b[a-zA-Z]{18}\b'  # true
    t.value = True
    return t

def t_FALSE(t):
    r'\b[a-zA-Z]{19}\b'  # false
    t.value = False
    return t

# String literal
t_STRING  = r'\"([^\\\n]|(\\.))*?\"'

# Assignment operator
t_ASSIGN  = r'\b[a-zA-Z]{20}\b'  # =

def t_IF(t):
    r'\b[a-zA-Z]{21}\b'  # if
    return t

def t_ELSE(t):
    r'\b[a-zA-Z]{22}\b'  # else
    return t

def t_WHILE(t):
    r'\b[a-zA-Z]{23}\b'  # while
    return t

t_SEMICOLON = r'\b[a-zA-Z]{24}\b'  # ;

# Print keyword
def t_PRINT(t):
    r'\b[a-zA-Z]{25}\b'  # print
    return t

# Identifiers (variable names)
def t_IDENTIFIER(t):
    r'\b[a-zA-Z]{26}\b'
    return t

# A regular expression rule with some action code for numbers and negative numbers
def t_NUMBER(t):
    r'([a-zA-Z]{2})?\d+(\.\d+)?'
    if t.value.startswith('aa'):
        t.value = -float(t.value[2:])
    else:
        t.value = float(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer and make it available to import
lexer = lex.lex()
