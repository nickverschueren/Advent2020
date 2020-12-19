grammar math1;

file : (expression WS?)* EOF;

expression
   :  expression (TIMES | PLUS) expression
   |  LPAREN expression RPAREN
   |  atom
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