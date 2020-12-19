grammar math2;

file : (expression WS?)* EOF;

expression
   :  addition (TIMES addition)*
   ;

addition
   :  atom (PLUS addition)*
   |  paren_expression (PLUS addition)*
   ;

paren_expression
   : LPAREN expression RPAREN
   ;

atom
   : number
   ;

number
   : INTEGER
   ;

INTEGER
   : NUMBER
   ;

fragment NUMBER
   : ('0' .. '9')+
   ;

LPAREN
   : '('
   ;

RPAREN
   : ')'
   ;

PLUS
   : '+'
   ;

TIMES
   : '*'
   ;

DIV
   : '/'
   ;

WS
   : [ \r\n\t] + -> skip
   ;