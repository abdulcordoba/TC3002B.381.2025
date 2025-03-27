grammar Expr;

prog:   (expr NEWLINE)* ;

expr:   expr op=MULT expr #mult
    |   expr op=DIV expr #div
    |   expr op=ADD expr #add
    |   expr op=SUB expr #sub
    |   INT #int
    |   '(' expr ')' #group
    ;

MULT: 'x';
DIV: '/';
ADD: '+';
SUB: '-';
ASSIGN: '<--';
NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;

FUNC: 'funcion';
VARIABLES: [a-z]+;

