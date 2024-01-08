from sly import Lexer

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


class ZealCLexer(Lexer):
    tokens = {ID, STRING, CHAR_CONSTANT, NUMBER,SINGLE_QUOTE, PLUS, MINUS, TIMES, DIVIDE, MODULO, ASSIGN,
              EQ, NEQ, LT, LE, GT, GE, AND, OR, NOT, LPAR, RPAR, LBRACE, RBRACE, SEMICOLON, COMMA}

    ignore = ' \t'

    # Regular expressions for tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'"[^"]*"'
    CHAR_CONSTANT = r"'.'"
    SINGLE_QUOTE=r"'"
    NUMBER = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    MODULO = r'%'
    ASSIGN = r'='
    EQ = r'=='
    NEQ = r'!='
    LT = r'<'
    LE = r'<='
    GT = r'>'
    GE = r'>='
    AND = r'&&'
    OR = r'\|\|'
    NOT = r'!'
    LPAR = r'\('
    RPAR = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
    SEMICOLON = r';'
    COMMA = r','

    @_(r'//.*')
    def ignore_comment(self, t):
        pass

    @_(r'/\*(.|\n)*?\*/')
    def ignore_multiline_comment(self, t):
        self.lineno += t.value.count('\n')

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f"Illegal character '{t.value[0]}' at line {self.lineno}")
        self.index += 1

if __name__ == '__main__':
   
    file_path = "ZealCompiler/test.zc"  # Change this to the actual path of your file
    with open(file_path, "r") as file:
        code = file.read()

    lexer = ZealCLexer()
    for token in lexer.tokenize(code):
        print(token)
