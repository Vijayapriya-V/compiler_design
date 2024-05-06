import re
def lex(ip):
    token_specification = {
          'KEYWORD': r'if|else|while|for|int|float|char|return',
          'OPERATOR': r'\+|-|\*|/|=|==|!=|(|)',
          'IDENTIFIER': r' [a-zA-Z][a-zA-Z0-9_]', 
          'NUMBER': r'\d+(\.\d+)?',
          'STRING':r'"([^"]*)"',
          'COMMENT':r' //.*|/\*(.|\n)*?\*/', 
          'WHITESPACE':r'\s+'
}
    words=ip.split()
    for word in words:
        for key, value in token_specification.items():
            if re.match(value, word):


                word=word.replace(";","")
                print (f"{word}: {key}")
                break

ip = """float x=(9.9);
int x = 0;"""
lex(ip)