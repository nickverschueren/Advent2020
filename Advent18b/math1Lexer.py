# Generated from math1.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("+\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\6\3\27\n\3\r\3\16\3\30\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t&\n\t\r")
        buf.write("\t\16\t\'\3\t\3\t\2\2\n\3\3\5\2\7\4\t\5\13\6\r\7\17\b")
        buf.write("\21\t\3\2\3\5\2\13\f\17\17\"\"\2+\2\3\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\3\23\3\2\2\2\5\26\3\2\2\2\7\32\3\2\2\2\t")
        buf.write("\34\3\2\2\2\13\36\3\2\2\2\r \3\2\2\2\17\"\3\2\2\2\21%")
        buf.write("\3\2\2\2\23\24\5\5\3\2\24\4\3\2\2\2\25\27\4\62;\2\26\25")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\6\3\2\2\2\32\33\7*\2\2\33\b\3\2\2\2\34\35\7+\2\2\35\n")
        buf.write("\3\2\2\2\36\37\7-\2\2\37\f\3\2\2\2 !\7,\2\2!\16\3\2\2")
        buf.write("\2\"#\7\61\2\2#\20\3\2\2\2$&\t\2\2\2%$\3\2\2\2&\'\3\2")
        buf.write("\2\2\'%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\b\t\2\2*\22\3\2")
        buf.write("\2\2\5\2\30\'\3\b\2\2")
        return buf.getvalue()


class math1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    LPAREN = 2
    RPAREN = 3
    PLUS = 4
    TIMES = 5
    DIV = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "LPAREN", "RPAREN", "PLUS", "TIMES", "DIV", "WS" ]

    ruleNames = [ "INTEGER", "NUMBER", "LPAREN", "RPAREN", "PLUS", "TIMES", 
                  "DIV", "WS" ]

    grammarFileName = "math1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


