import sys
import ply.lex as lex # for token definition
import ply.yacc as yacc # for parsing rules

sys.set_int_max_str_digits(1_000_000_000)
tokens = ('NUMBER','PLUS','MINUS','MULTIPLY','DIVIDE','POWERED','LPAREN','RPAREN')

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_POWERED = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'

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
def p_exp_plus(p):
    'exp : exp PLUS term'
    p[0] = p[1] + p[3]

def p_exp_minus(p):
    'exp : exp MINUS term'
    p[0] = p[1] - p[3]

def p_exp_term(p):
    'exp : term'
    p[0] = p[1]
    
def p_term_mul(p):
    'term : term MULTIPLY factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_powered(p):
    'factor : subfactor POWERED factor'
    p[0] = p[1] ** p[3]

def p_factor_subfactor(p):
    'factor : subfactor'
    p[0] = p[1]

def p_factor_paren(p):
    'subfactor : LPAREN exp RPAREN'
    p[0] = p[2]

def p_subfactor_number(p):
    'subfactor : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

# parser
if __name__ == '__main__':
    parser = yacc.yacc()
    def eval_exp(exp):
        return parser.parse(exp)

    # import pickle
    # with open('parser.pickle', 'wb') as f:
    #     pickle.dump(parser, f)

    while True:
        print(eval_exp(input('eval> ')))
