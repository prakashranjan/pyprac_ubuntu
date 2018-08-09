# Complete the solve function below.
def solve(s):
    ar = s.split(" ")
    #print (ar[0], ar[1])
    for i in range(len(ar)):
        ar[i]= ar[i].strip(" ")
        
        ar[i] = str(ar[i]).capitalize()
        #print (ar[i])
    return " ".join(ar)