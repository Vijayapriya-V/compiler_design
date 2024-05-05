def nfa_1(i,state):
    ns = state + 1
    return f"{state}-->{i}-->{ns}"

def occurance(state):
    ns = state + 1
    return f"{ns}-->e-->{state}"

def check(re):
    state = 0
    regex = re.split()
    if '(' in re:
        regex = re.replace('(' , ' ( ').replace(')', ' ) ').split()
        regex.remove('(')
        regex.remove(')')

    for i in regex:
        if '*' not in i and  '|' not in i:
            print(nfa_1(i,state))
            state += 1
        
        elif '*' in i:
            ch = i[:-1]
            startingnode = state
            ns = state + 1
            print(f"{state}-->e-->{ns}")
            state += 1
            print(nfa_1(ch,state))
            #state += 1
            print(occurance(state)) 
            state += 1
            ns = state + 1
            print(f"{state}-->e-->{ns}")
            print(f"{startingnode}-->e-->{ns}")
            state += 1

        elif '|' in i:
            startingnode = state
            ch = i.split('|')
            if '' in ch : ch.remove('')
            endingnode  = (len(ch) * 2 + 1) + state
            for j in ch:
                ns = state + 1
                print(f"{startingnode}-->e-->{ns}")
                state += 1
                print(nfa_1(j,state))
                state += 1
                print(f"{state}-->e-->{endingnode}")
            state += 1

re_input = input ('Enter the expression:')
check(re_input)