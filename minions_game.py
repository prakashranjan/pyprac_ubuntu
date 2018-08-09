def minion_game(s):
    V = frozenset("AEIOU")
    n = len(s)
    ksc = sum(q for c, q in zip(s, range(n, 0, -1)) if c in V)
    ssc = n * (n + 1) // 2 - ksc
    if ksc > ssc:
        print("Kevin {:d}".format(ksc))
    elif ssc > ksc:
        print("Stuart {:d}".format(ssc))
    else:
        print("Draw")


#my 
#    answer

def minions_game(string):
    # your code goes here
    x= list(string)
    s_c = 0
    k_c = 0
    s_ar= []
    k_ar= []
    
    for i in range(len(x)):
        #print (i)
        #print(len(x))
        for j in range(len(x),i,-1):
            #print("".join(x[i:j]))
            nword =" ".join(x[i:j])
            if nword[0]=='A' or nword[0]=='E' or nword[0]=='I' or nword[0]=='O' or nword[0]=='U':
                if nword not in k_ar:
                    k_ar.append(nword)
                    tempk = 0
                    for l in range(len(string)):
                        nword = nword.replace(" ", "")
                        if string[l:l+len(nword)] == nword:
                            #print(nword)
                            tempk +=1
                    
                    #print (tempk)
                    k_c += tempk
            else:
                if nword not in s_ar:
                    s_ar.append(nword)
                    temps = 0
                    for l in range(len(string)):
                        nword = nword.replace(" ", "")
                        if string[l:l+len(nword)] == nword:
                            #print(nword)
                            temps +=1
                    
                    #print (temps)
                    s_c += temps
    
    
    
    
    if s_c > k_c :
        print("Stuart "+str(s_c))
    elif k_c > s_c:
        print("Kevin "+str(k_c))
    else:
        print("Draw")
            