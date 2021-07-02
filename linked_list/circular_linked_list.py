class Node:
    
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "[Node data: %s]" % self.data

class Circular_Linkedlist:
    def __init__(self):
        self.head = None


    # Checking if list is empty or not
    def is_empty(self):
        if self.head == None:
            return"Linked list is empty"



    # Displaying linked list
    def display(self):
        if self.head == None:
            return "Empty Linked-list"
        else:
            #dl = []
            current_node = self.head
            while current_node.next_node != self.head:
                print(current_node,end=' ')
                print("-->",end=' ')
                current_node = current_node.next_node
            
            print(current_node,"-->",end=" ")
        print(current_node.next_node)
        return " "

    
    

    #Adding nodes at the begining
    def add_at_beg(self,data):
        new_node = Node(data)
        if self.head == None:# checking if list is empty
            self.head = new_node 
            #print("New node: %s" % new_node)
        else:
            new_node.next_node = self.head # shifting the existing first node to next node of new node
            self.head = new_node #assigning head to new node
            #print("New node: %s" % self.head)
            
    # Adding nodes at the end of the linked list
    def add_at_end(self,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next_node != None: # traversing to the last node whose next node is none
            #if current_node.next_node != None:
            current_node = current_node.next_node # Keeping the node whose next node is none
            #else:
            #    break
        
        current_node.next_node = new_node #Assigning new node at the end
        a = current_node.next_node
        a.next_node = self.head
        #print(a.data)
        #print(a.next_node.data)
    

    # adding nodes at roandom position
    def add_at_middle(self,data):
        new_node = Node(data)
        x = int(input("enter position after which u want to add node:"))
        if self.head == None:#Checking if linkedlist is empty or not
            add_at_beg(new_node)
        else:
            current_node = self.head
            y = 0
            while y < x-1:# traversing to that node after which new node has to be inserted
                current_node = current_node.next_node
                y+=1
            #print(current_node)
        #Insertion of new node at given position
        a = current_node.next_node
        current_node.next_node = new_node
        new_node.next_node = a
        #print(current_node.next_node)


    #Deleting element from begining
    def del_at_beg(self):
        #print(self.head)
        a = self.head
        self.head = a.next_node
        #print(self.head)

    #Deleting node at the end
    def del_at_end(self):
        prev = None
        current_node = self.head

        if current_node.next_node == None:
            current_node = None

        while current_node: # traversing to the last node whose next node is none
            if current_node.next_node != None:
                prev = current_node #preserving the second last node
                current_node = current_node.next_node # Keeping the node whose next node is none
            
            else:
                break
        prev.next_node = None


    #Deleting the random elements from linkedlist
    def del_at_middle(self,pos):
        #pos = int(input("Delete at the position:"))
        current_node = self.head
        y = 0
        prev = None
        while y < pos-1:# traversing to that node which has to be deleted
            prev = current_node
            current_node = current_node.next_node
            y+=1
        prev.next_node = current_node.next_node


    def length_of_cll(self):
        cur_element = self.head
        count = 0
        #print(cur_element.next_node)
        while cur_element.next_node.data != self.head.data:
            count += 1
            cur_element = cur_element.next_node
        return count+1

    def check_circular_loop(self):
        cur_element = self.head
        #prev = None
        #print(cur_element.next_node.data)
        while cur_element.next_node.data != self.head.data:
            cur_element = cur_element.next_node
            
        a = cur_element.next_node
    
        if self.head.data == a.data :
            return "True...Its a circular linkedlist"
        else:
            return "No loop exist...."


    def reverse(self):
        cur_element = self.head
        c_node = self.head
        while c_node.next_node != self.head:
            c_node = c_node.next_node
        #print(c_node)    
        prev = c_node
        #print(cur_element.next_node)
        while cur_element.next_node.data!=self.head.data:
            next_val = cur_element.next_node
            cur_element.next_node = prev
            prev = cur_element
            cur_element = next_val
            #prev = prev.next_node
            
        cur_element.next_node = prev
        #print(cur_element.next_node)
        self.head = cur_element
        return ""



    def swap(self,k):
        
        cur_element = self.head
        current_element = self.head
        s = self.length_of_cll()
        prev = None
        pref = None
        y = 0
        z = 0

        if k == 1 or k == s:
            while cur_element.next_node != self.head:  #kth element from last
                ch = cur_element
                cur_element = cur_element.next_node
            #print(cur_element)
            #print(ch)
            ch.next_node = self.head
            ab = self.head.next_node
            cur_element.next_node = ab
            self.head = cur_element
            ch.next_node.next_node = self.head
            
        elif k < s and k != 1:
            
            while y<=s-(k+1):  # kth element from last
                y+=1
                prev = cur_element
                cur_element = cur_element.next_node
            
            
            while z < k-1:   # kth element from first
                z+=1
                pref = current_element
                current_element = current_element.next_node
           
            c = cur_element.next_node 
            b = current_element.next_node
            pref.next_node = cur_element
            cur_element.next_node = b
            prev.next_node = current_element
            current_element.next_node = c

        else:
            print("value passed is greater thane size of linked list")


    def smallest_element(self):
        
        cur_node = self.head
        small = cur_node.data
        while cur_node.next_node != self.head:
            if small > cur_node.data:
                small = cur_node.data
            cur_node = cur_node.next_node
        return small
            

    def largest_element(self):
        
        cur_node = self.head
        large = cur_node.data
        while cur_node.next_node != self.head:
            if large < cur_node.data:
                large = cur_node.data
            cur_node = cur_node.next_node
        return large

      
        
cl = Circular_Linkedlist()
cl.add_at_beg(1)
cl.add_at_beg(23)
cl.add_at_beg(4)
cl.add_at_beg(2)
cl.add_at_end(8)
#cl.add_at_middle(45)
#cl.del_at_middle(2)
#print(cl.length_of_cll())
#cl.display()
#print(cl.check_circular_loop())
#cl.reverse()
#cl.display()
#cl.swap(5)
#cl.display()
print(cl.smallest_element())
print(cl.largest_element())


