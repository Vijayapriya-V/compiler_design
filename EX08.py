OPERATORS = set(['+','-','*','/','(',')'])
PRE = {'+':1,'-':1,'*':2,'/':2}

def infix_to_postfix(express):
    stack = []
    output = ''
    for ch in express:
        if ch not in OPERATORS:
            output += ch
        
        elif ch == '(':
            stack.append('(')

        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        else:
            while stack and stack[-1] != '(' and PRE[ch] <= PRE[stack[-1]]:
                output +=stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()
    print(f"POSTFIX->{output}")
    return output
    
def generate3AC(pos):
    print("### THREE ADDRESS CODE ###")
    exp_stact = []
    t=1
    for i in pos:
        if i not in OPERATORS:
            exp_stact.append(i)
        else:
            print(f't{t}:={exp_stact[-2]}{i}{exp_stact[-1]}')
            exp_stact = exp_stact[:-2]
            exp_stact.append(f't{t}')
            t += 1
ip = input('Enter the expression:')
pos = infix_to_postfix(ip)
generate3AC(pos)

