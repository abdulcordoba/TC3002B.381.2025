/* De prefererencia cambiar el nombre del lenguaje aquí y en el nombre del archivo */
grammar Mayo;

/* Sintáctico */
program: (sentencia | expresion)+;

sentencia:
    declaracion #decl
    | 'si' expresion 'entonces' sentencia 'fin' #if
    | 'mientras' expresion 'haz' sentencia 'fin' #while
    | 'def' SIMBOLO '->' parametro (',' parametro)* '<-' ':' sentencia 'fin' #funcion
    | expresion #expr
    | SIMBOLO '(' expresion (',' expresion)* ')' #call
    ;

parametro: SIMBOLO ':' tipo;

tipo: 'entero' | 'flotante' | 'cadena';


declaracion:
    'entero' SIMBOLO (',' SIMBOLO)*      #dec_entera
    | 'flotante' SIMBOLO (',' SIMBOLO)*  #dec_flotante
    ;

expresion:
    expresion 'x' expresion #mult
    | expresion '+' expresion #add
    | SIMBOLO   #var
    | NUMERO    #number
    | FLOTANTE  #float
    | CADENA    #string
    ;


/*
La sintaxis de las reglas es:

regla1:
    regla2 TOKEN1 regla2 "tokenliteral" regla2 #nombredelnodo1
    | regla2 TOKEN1 regla2 "tokenliteral" regla2 #nombredelnodo2
    | regla2 TOKEN1 regla2 "tokenliteral" regla2 #nombredelnodo3
    ;

    Se puede usar libremente la recursión.

    Por ejemplo

expresion:
    expresion "**" expresion    #dobleasterisco
    | expresion "##" expresion  #doblehash
    | TOKEN                     #casoHoja
    ;

*/


/* Léxico
En mayúsculas el nombre del token y luego una regexp. Se usan arriba en las reglas de la gramática.
*/

SIMBOLO: [A-Z] [a-z]+;
NUMERO: [0-9]+;
FLOTANTE: [0-9]+ '.' [0-9]* | [0-9]* '.' [0-9]+;
CADENA: '"' [a-zA-Z0-9]+ '"';


ESPACIOS: [ \t\n] -> skip;


/*
Ejemplos:

TOKEN1: "palabrareservada";
TOKEN2: "mas" | "de" | "una";

TOKEN3: [b-x]+;

BLANK: "todosmissblanks" -> skip;

*/