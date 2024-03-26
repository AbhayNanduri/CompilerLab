import re
from first import first 

def follow(s, productions,first):
    follow=set() #a set to hold follow

    if len(s)!=1:
        return {}
    if(s==list(productions.keys())[0]):
        follow.add('$') # If S is start symbol add $ to follow of S

    for i in productions:
        for j in range(len(productions[i])):
            if(s in productions[i][j]):
                idx=productions[i][j].index(s)  #find the index of the target NT in RHS of production
                n=len(productions[i][j])
                if(idx==n-1):
                    if(productions[i][j][idx]==i):
                        break
                    else: 
                        f=follow(i,productions,first)
                        for x in f:
                            follow.add(x)
                else:
                    while(idx!=n-1): #if A->alpha B beta and then Follow(B) is First(beta) if beta starts with a terminal
                        idx=idx+1
                        if(not productions[i][j][idx].isupper()):
                            follow.add(productions[i][j][idx])
                            break
                        else:
                            f=first(productions[i][j][idx],productions)

                            if('eps' not in f):
                                for x in f:
                                    follow.add(x)
                                break
                            elif('eps' in f and idx!=n-1):
                                f.remove('eps')
                                for k in f:
                                    follow.add(k)
                            elif('eps' in f and idx==len(productions[i][j]-1)):
                                f.remove('eps')
                                for k in f:
                                    follow.add(k)
                                
                                f=follow(i,productions,first)
                                for x in f:
                                    follow.add(x)


    return follow

def main():
    productions = {}
    grammar = open("grammar.txt", "r")
    
    fst = {}
    flw={}
    
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

    print("")
    
    for lhs in productions:
        flw[lhs] = set()
    
    for s in productions.keys():
        flw[s] = follow(s, productions, first)
    
    print("*****FOLLOW*****")
    for lhs, rhs in flw.items():
        print(lhs, ":" , rhs)

    grammar.close()

if __name__ == "__main__":
    main()