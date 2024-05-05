print("Recursive Descent Parsing for given grammar")
print("L -> SL'\nL' -> ,SL' | @\nS -> (L) | a")
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

def S():
    if match('('):
        if L():
            return match(')')
        else:
            return False
    else:
        return match('a')
    
def Lx():
    if match(','):
        if S():
            return Lx()
        else:
            return False
    else:
        return True
    
def L():
    if S():
        return Lx()
    else:
        return True
    

    
if L():
    if i==len(s):
        print("String is accepted")
    else:
        print("String is not accepted")
else:
    print("String is not accepted")