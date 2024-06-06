import ply.lex as lex # for token definition
import ply.yacc as yacc # for parsing rules

tokens = ('NUMBER','PLUS','MINUS')

t_PLUS = r'\+'
t_MINUS = r'-'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"bad input {t.value[0]}")
    t.lexer.skip(1)

# building
lexer = lex.lex()

# yacc code
# exp -> expression
# term -> terminal
def p_exp_plus(p):
    'exp : exp PLUS term'
    p[0] = p[1] + p[3]

def p_exp_minus(p):
    'exp : exp MINUS term'
    p[0] = p[1] - p[3]

def p_exp_term(p):
    'exp : term'
    p[0] = p[1]

def p_term_number(p):
    'term : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

# parser
parser = yacc.yacc()

def eval_exp(exp):
    return parser.parse(exp)

print(eval_exp('196+204'))