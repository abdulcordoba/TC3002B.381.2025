grammar Expr;		

prog:	(expr)* ;

expr:	expr ('*'|'/') expr
    |	expr ('+'|'-') expr
    |	INT
    |	LPAR expr RPAR
    ;



NEWLINE : [\r\n]+ -> skip;
BLANK   : [ ]+ -> skip;
INT     : [0-9]+ ;
LPAR    : '(';
RPAR    : ')';

