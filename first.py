import re

def first(s,productions):
    first=set()
    for i in range(len(productions[s])):
        #print(productions)
        #print(productions[s])
        for j in range(len(productions[s][i])):
            #print(productions[s][i])
            c=productions[s][i][j]
            #print(c)
            if(c.isupper()): # if c is a Non-Terminal
                f=first(c,productions) 
                if('eps' not in f): # if A->BC then First(A)=First(B) if eps not in First of B
                    for k in f:
                        first.add(k)
                    break
                else: # if eps in First of B then First(A)=First(B) union First(C)
                    if (j==len(productions[s][i]-1)):
                        for k in f:
                            first.add(k)
                    else:
                        f.remove('eps')
                        for k in f:
                            first.add(k)
            
            else: #if A->a alpha First(A)={a}
                first.add(c)
                break
    return first

def main():
    productions = {}
    grammar = open("grammar.txt", "r")
    
    fst = {}
    
    for prod in grammar:
        l = re.split("( /->/\n/)*", prod)
        m = []
        for i in l:
            if (i == "" or i == None or i == '\n' or i == " " or i == "-" or i == ">"):
                pass
            else:
                m.append(i)
        
        left_prod = m.pop(0)
        right_prod = []
        t = []
        
        for j in m:
            if(j != '|'):
                t.append(j)
            else:
                right_prod.append(t)
                t = []
        
        right_prod.append(t)
        productions[left_prod] = right_prod
    
    for s in productions.keys():
        fst[s] = first(s, productions)
    
    print("*****FIRST*****")
    for lhs, rhs in fst.items():
        print(lhs, ":" , rhs)

    grammar.close()

if __name__ == "__main__":
    main()