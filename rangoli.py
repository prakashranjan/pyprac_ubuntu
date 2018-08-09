def print_rangoli(size):
    # your code goes here
    ch = chr(97+size)
    t= 4*size - 3
    
    x=[]
    y=[]
    z=[]
    k=[]
    
    for c in range(96+size,96,-1):
        x.append(chr(c))
        #print (x)
        y.append(chr(c))
            
        z=y[::-1]
        #print (z[1:])
        k=x+z[1:]
        f = "-".join(x+z[1:])
        print (f.center(t,'-'))
    #print(k)

    for d in range(97,96+size,1):
        #print(k)
        k.remove(chr(d))
        k.remove(chr(d+1))
        
        f = "-".join(k)
        print (f.center(t,'-'))
if __name__ == "__main__":
    n=int(input())
    print_rangoli(n)

        
        
            
            
            
        