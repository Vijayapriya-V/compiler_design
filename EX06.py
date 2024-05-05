print("Recursive Descent Parsing for given grammar")
print("E -> TE'\nE' -> +TE' | @\nT -> FT'\nT' -> *FT' | @\nF -> (E) | i")
global s
global i
s=list(input('Enter a string:'))
i=0

def match(a):
    global s
    global i
    if i >= len(s):
        return False
    elif s[i]==a:
        i += 1
        return True
    else:
        return False

def F():
    if match('('):
        if E():
            return match(')')
        else:
            return False
    else:
        return match('i')
    
def Tx():
    if match('*'):
        if F():
            return Tx()
        else:
            return False
    else:
        return True
    
def T():
    if F():
        return Tx()
    else:
        return True
    
def Ex():
    if match('+'):
        if T():
            return Ex()
        else:
            return False
    else:
        return True
    
def E():
    if T():
        return Ex()
    else:
        return False
    
if E():
    if i==len(s):
        print("String is accepted")
    else:
        print("String is not accepted")
else:
    print("String is not accepted")