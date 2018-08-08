#Nested Lists


if __name__ == '__main__':
    stus = []
    dtus = []
    sec=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        stu = []
        stu.insert(0, name)
        stu.insert(1, score)
        stus.append(stu)
    #print(stus)    
    m = min(stus, key=lambda x: x[1])
    min1 = m[1]
    #print(min1)
    for j in range(_+1):
        #print (j)
        if stus[j][1] > min1:
            #print (stus[j],"\n-----------")
            dtus.append(stus[j])
            
    #print(dtus)        
    m2= min(dtus, key=lambda x: x[1])
    for i in range(len(dtus)):
        if dtus[i][1] == m2[1]:
            sec.append(dtus[i][0])
            
    #print(stus)        
    sec.sort()    
    print("\n".join(sec))
    
        
    
#Solution code
'''
N = int(raw_input())

students = []
for i in range(2*N):
    students.append(raw_input().split())
grades = {}
for j in range(0, len(students), 2):
    grades[students[j][0]] = float(students[j + 1][0])
result = []
num_to_match = sorted(set(grades.values()))[1]
for pupil in grades.keys():
    if grades[pupil] == num_to_match:
        result.append(pupil)
for k in sorted(result):
    print k        
    
    '''

'''
Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.


'''
if __name__ == '__main__':
    s = input()
     
    p = {'alnum':0,'alpha':0,'digit':0,'lower':0,'upper':0}
    for x in range(len(s)):
        if s[x].isalnum():
            p['alnum'] += 1
        if s[x].isalpha():
            p['alpha'] += 1
        if s[x].isdigit():
            p['digit'] += 1
        if s[x].islower():
            p['lower'] += 1
        if s[x].isupper():
            p['upper'] += 1   
    #print(p)
    q= ['alnum', 'alpha' , 'digit', 'lower', 'upper']
    for j in q:
        i = p[j]
        #print (i)
        if i != 0:
            print (True)
        else: 
            print (False)
   


   