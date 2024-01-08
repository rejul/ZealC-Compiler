import ply.lex as lex


# Define ZealC tokens





#for signed 0-8 byte 
#Builtin_type_Signed=('I0','I8','I16','I32','I64')

#for Unsigned 0-8 byte 
#Builtin_type_Unsigned=('U0','U8','U16','U32','U64')

#float type
#type_float=("F64")


""" U0          void, but ZERO size!
    I8          char
    U8          unsigned char
    I16         short
    U16         unsigned short
    I32         int
    U32         unsigned int
    I64         long (64-bit)
    U64         unsigned long (64-bit)
    F64         double
 """


"""   
void DemoC(char drv, char *format, char *name, int age)
  {
    printf("Hello World!\n");
    printf("%s age %d\n", name, age);
    printf(format, name, age);
    putchar(drv);
    putchar('*');
  }
  
  U0 DemoZealC(U8 drive, U8 *format, U8 *name, I64 age)
  {
    "Hello World!\n";
    "%s age %d\n", name, age;
    "" format, name, age;
    '' drive;
    '*';
  } 
  
"""





tokens = (
    'ID', 'NUMBER', 'STRING', 'CHAR_CONSTANT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA', 'DOT', 'ARROW',
    'EQ', 'NEQ', 'LT', 'LE', 'GT', 'GE',
    'ASSIGN', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'TIMES_ASSIGN', 'DIVIDE_ASSIGN', 'MOD_ASSIGN',
    'AND', 'OR', 'NOT', 'BIT_AND', 'BIT_OR', 'BIT_XOR', 'BIT_NOT', 'LSHIFT', 'RSHIFT',
    'QUESTION', 'COLON',
    'INCREMENT', 'DECREMENT',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_ARROW = r'->'
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_ASSIGN = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_BIT_AND = r'&'
t_BIT_OR = r'\|'
t_BIT_XOR = r'\^'
t_BIT_NOT = r'~'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_QUESTION = r'\?'
t_COLON = r':'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'




    
# Regular expression rules with actions
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_STRING(t):
    r'\"([^"\\]|\\.)*?\"'
    t.value = t.value[1:-1]  # remove quotes
    return t

def t_CHAR_CONSTANT(t):
    r'\'.\''
    t.value = t.value[1]  # remove quotes
    return t


# Ignored characters (whitespace and comments)
t_ignore_COMMENT = r'\/\/[^\n]*'
t_ignore_MULTILINE_COMMENT = r'\/\*(.|\n)*?\*\/'
t_ignore = ' \t\r\f\v'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with the provided C-like code
file_path = "ZealCompiler/test.zc"  # Change this to the actual path of your file
with open(file_path, "r") as file:
    source_code = file.read()
lexer.input(source_code)

# Tokenize and print tokens
for token in lexer:
    print(token)  # The tokens are printed within the tokenization rules