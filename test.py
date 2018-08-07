if __name__ == '__main__':
    N = int(input())
    
  
    myli = []
    
    while N>=1:
        
        x = input()
        if x == "print":
            print(myli)
        elif x == "reverse":
            myli.reverse()
        elif x == "pop":
            myli.pop()
        elif x == "sort":
            myli.sort()    
        else:
            ar = []
            ar = x.split()
            if ar[0] == "insert":
                myli.insert(int(ar[1]), int(ar[2]))
            elif ar[0] == "append":
                myli.append(int(ar[1]))
            elif ar[0] == "remove":
                myli.remove(int(ar[1]))
        N = N -1
                    
        
            


