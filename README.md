# Calculator-Parser
A Simple Calculator Parser written using Python Lex Yacc

## Need
It is made to use as an alsternate to using the eval function and th terminal prompt to evaluate expressions 
## Precedence
`()` > `^` > `* /` > `+ -`

## Grammar
```sh
S' -> exp
exp -> exp PLUS term
exp -> exp MINUS term
exp -> term
term -> term MULTIPLY factor
term -> term DIVIDE factor
term -> factor
factor -> subfactor POWERED factor
factor -> subfactor
subfactor -> LPAREN exp RPAREN
subfactor -> NUMBER
```

Spaces and tabs are ignored

## Expressions cross-checked 

### short
```sh
eval> (3 + 5) * (4 - 2^3) + 7
-25
eval> 2^3 * (2 + 5) - 8 / 4 + 3
57.0
eval> 6 + 3^2 * (2 + 2) - 4 / 2
40.0
```
### Longer
```sh
eval> (3 + 5^2 * (6 - 2) / 4) * (2 + 3^3) - (7 * (8 / 2 + 5)) + 4^3 * (3 - 1) + 6 / (2 + 1) - 50
829.0
eval> ((4 + 2^3 * (5 - 3) + 7) / (3 * (8 - 5) - 2) + (6 + 4^2) - 5 * (3 + 2) + (7^2 / 2 - 1)) * 2
48.714285714285715
eval> (6 + 3^2 * (4 - 1) - 5 / (2 + 1)) + (8^2 / 4) * (3 + 5) - (7 * (6 - 4) + 9^2) + (10 / 2 + 3 * 5)
84.33333333333334
```

### No parenthesis
```sh
eval> 3 + 5^2 * 4 - 2 / 3 * 2 + 2^3 - 6 * 9 / 3 + 5 + 4^3 * 2 - 1 + 8 / 2 + 2 - 40 / 2 + 3
212.66666666666669
eval> 7 + 8 * 3^2 - 4 / 2 - 5 + 4^2 * 6 - 2 + 3 + 2^3 * 5 - 3 / 2 - 7 * 2 + 5^2 * 2 - 3
240.5
eval> 2^3 + 5 * 7 - 3^2 + 8 / 6 * 2 + 1 + 4^3 - 9 + 2^3 * 2 / 5 + 6 - 4 + 3 * 2 + 2 - 8 / 2
101.86666666666666
```