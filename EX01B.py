# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:03:48 2024

@author: GFLAB
"""

import ply.lex as lex
tokens = (
  'NUMBER',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*' 
t_DIVIDE = r'/' 
t_LPAREN = r'\('
t_RPAREN = r'\)'
def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value) 
   return t
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)
t_ignore = ' \t'
def t_error(t):
   print ("Illegal character '%s'" % t.value[0]) 
   t.lexer.skip(1)
lexer = lex.lex()
# Test it out 
data = '''
3 + 4 * 10
+ -20 *2 
'''
# Give the lexer some input 
lexer.input(data)
# Tokenize 
while True:
  tok = lexer.token() 
  if not tok:
     break
  print(tok)