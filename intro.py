#one line comment
"""
multi 
line 
comment 

"""

'''
multi line comment 
embeded in  single qoutes
right...

'''


print("hello world")
print('hello world2')
print("print \n hello \n world")

print('print \n hello\n world\n  2\n')

ar = [1,2,3,4,5,6,"hell"]
print(ar)
print(ar[3])

asar = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(asar['b'])


#inline print
again = "again"
print (1,2,3,4,"hello world")
print ("hello "+"world "+ again)

print ('__dirname')
print ("__dirname")
print (r"_______dirname")

# ***underscore has a special meaning in python***

print ("-----------------------------------------------------------------")

print                             ()

print(12)


#underscore properties

x,_,y = (1,2,3)
# here 2 is assigned to underscore


print(x,_,y)

x,*_,y  = ( 1,2,3,4,5,6,7,8)
print(x,*_,y)

x,*z,y  = ( 1,2,3,4,5,6,7,8)
print(x,*z,y)

#got same output for above two prints
f = 0
#f = 1
if f == 1:
    exit(1)

print ("hell")

print(10/3)
print(10//3)
help(print)


# hacker rank is the best 


#format print
percentage = 98.765432

print('%.2f' % percentage)
print ('{:.2f}'.format(percentage))

#split and join
def split_and_join(line):
    # write your code here
    #input is "this is my life"
    ar = line.split()
    return ("-".join(ar)) 
#output is "this-is-my-life"

#Read a given string, change the character at a given index and then print the modified string.
def mutate_string(string, position, character):
    snew = list(string)
    snew[position] = character
    snew = "".join(snew)
    return snew

#formating is the king
'''
learn new formating syntax 
'''
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1,1):
        xb = str(bin(number))[2:]
        xblen= len(xb)
        
        print ("{:{x}}".format(int(i),x=xblen) ,end=" ")
        print ("{:{x}}".format(int((oct(i))[2:]), x=xblen) ,end=" ")
        print ("{:{x}X}".format(i, x=xblen) ,end=" ")
        print ("{:{x}}".format(int(str(bin(i))[2:]), x= xblen) )
        
        
        
        

