''' write linked list in python 
with menu containing all the operations 
1.append
2.prepend
3.remove
4.insert
5.display
'''
class node():
    def __init__(self,data):
        self.data = data
        self.next = None 
    
class linkedlist():
    def __init__(self):
        self.head = None
    
    def lappend(self,newdata):
        newnode = node(newdata)
        if not self.head:
            self.head = newnode
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = newnode

    def display(self):
        k = self.head
        print("\n--------------------\n")
        while k:
            print(k.data, end = " ")
            k = k.next
        print("\n--------------------\n")
    def lprepend(self, newdata):
        newnode = node(newdata)
        newnode.next = self.head
        self.head = newnode
    def lremove(self,dnode):
        k = self.head

        if self.head is None:
            print("allready empty linkedlist")
            return
        if self.head.next is None:
            if self.head.data == dnode:
                self.head = None
                print("now linkedlist empty")
            else:
                print("node not found")
        elif self.head.data == dnode:
            self.head = self.head.next
        else:
            while k.next:
                if k.next.data == dnode:
                    print("{}: deleted".format(k.next.data))
                    k.next = k.next.next
                    return
                k = k.next
            print("node not found")
    
    def inafter(self,bnode,newdata):
        newnode = node(newdata)
        k = self.head
        while k :
            if k.data == bnode:
                newnode.next = k.next
                k.next = newnode
                return

            k = k.next
        print("before node not found")



            


            

#linkedlist
mylist = linkedlist()
x = "y"
while x == "y":
    print("\n--------------------------------------------------\n")
    print("1. append\n2. prepend\n3. remove\n4. insertafter")
    print("\n--------------------------------------------------\n")
    z = int(input())
    nd = str(input())
    if z == 1:
        mylist.lappend(nd)
    elif z == 2:
        mylist.lprepend(nd)
    elif z == 3:
        mylist.lremove(nd)
    elif z == 4:
        print("after : ")
        after = str(input())
        mylist.inafter(after,nd)

    mylist.display()
    print("\nback to menu enter y")
    x = str(input())

 


