class Node:
    
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "[Node data: %s]" % self.data

class Linkedlist:
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
            while current_node:
                print(current_node,end=' ')
                print("-->",end=' ')
                #dl.append(current_node)
                current_node = current_node.next_node
        print("None")
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
        #print(a)
        a.next_node = None
    

    # adding nodes at roandom position
    def add_at_middle(self,data,pos):
        new_node = Node(data)
        current_node = None
        #x = int(input("enter position after which u want to add node:"))
        if self.head == None:#Checking if linkedlist is empty or not
            self.add_at_beg(new_node)    
        else:
            current_node = self.head
            y = 0
            while y < pos-1:# traversing to that node after which new node has to be inserted
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



    def size_of_list(self):
        count = 0
        
        current_node = self.head
        
        while current_node:
            count+=1
            current_node = current_node.next_node
        #print(type(count))
        return count

    
    def middle_node(self):
        current_node = self.head
        count = 0
        
        current_node = self.head
        
        while current_node:
            count+=1
            current_node = current_node.next_node
        #print("size of list:",count)
        
        x = (count+1)//2
        
        if count == 0:
            print("----first insert nodes----")
        elif count%2 != 0:  # If the size of the linked-list is odd 
            y = 0
            current_node = self.head
            while y<x-1:
                current_node = current_node.next_node
                y+=1
            print(current_node)
        else:  #If the size of linked-list is even
            z = 0
            current_node = self.head
            while z<x-1:
                current_node = current_node.next_node
                z+=1
            print(current_node,end=' ')
            print("-->",current_node.next_node)



    def search_the_list(self,info):
        cur_node = self.head
        while cur_node:
            if cur_node.data == info:
                #print("data present")
                return True
            
            cur_node = cur_node.next_node
        return "No Data found"

    def search_based_update(self,element):
        if self.search_the_list(element) == True:
            print("Node already exists")
        else:
            count = int(input("position a which node has to be inserted"))
            self.add_at_middle(element,count)
            self.display()


    def search_based_deletion(self,element):
        if self.search_the_list(element) == True:
            if element == self.head.data:
                self.delete_at_beg()
                self.display()
            #else:
            #    self.delete_at_middle()
            #    self.display()
        else:
            self.add_at_middle(element)
            self.display()

        
        

#############################################################

    """#def partition(self,low,high):

    def quick_sort_list(self):
        low = 0
        high = size_of_list() - 1
        pivot_node = self.head
        pre_node = None
        while pivot_node:
            pre_node = pivot_node
            pivot_node = pivot_node.next_node
        pivot_node = pre_node
        
        if size_of_list() == 1:
            return self.head
        
        #if low < high:
        #    p = partition(low,high)
        #    quick_sort_list(low,p-1)
        #    quick_sort_list(p+1,high)
        #return diplay()"""


    def remove_duplicates(self):
        cur_node = self.head
        elist = []
        count = 0
        while cur_node:
            
            if cur_node.data in elist:
                if cur_node.next_node == None:
                    print(self.del_at_end())
                else:
                    print(self.del_at_middle(count+1))
            else:
                elist.append(cur_node.data)
            cur_node = cur_node.next_node    
            count+=1    
        return self.display()


    """def palindrome_list(self):
        #size = self.size_of_list()
        pivot_node = self.head
        pre_node = None
        while pivot_node:
            pre_node = pivot_node
            pivot_node = pivot_node.next_node
        pivot_node = pre_node
        #print(type(pivot_node))
        #if size%2 != 0:"""

    def check_circular_loop(self):
        cur_element = self.head
        #prev = None
        print(cur_element.next_node.data)
        while cur_element.next_node != None:
            #prev = current_node
            cur_element = cur_element.next_node
        a = cur_element.next_node
        if a != None and self.head.data == a :
            return "True...Its a circular linkedlist"
        else:
            return "No loop exist...."



    def reverse_list(self):
        cur_element = self.head
        prev = None
        while cur_element!=None:
            next_val = cur_element.next_node
            cur_element.next_node = prev
            prev = cur_element
            cur_element = next_val
            
        self.head = prev
        return ""


    def third_from_end(self):
        cur_element = self.head
        s = self.size_of_list()
        
        y = 0
        while y<=s-4:
            y+=1
            cur_element = cur_element.next_node

        return cur_element.data
            


    def swap(self,k):
        # This function swaps node from kth position from last to kth position from front or vice versa 
        cur_element = self.head
        current_element = self.head
        s = self.size_of_list()
        prev = None
        pref = None
        y = 0
        z = 0

        if k == 1 or k == s:
            while cur_element.next_node != None:  #kth element from last
                ch = cur_element
                cur_element = cur_element.next_node
            
            ch.next_node = self.head
            ab = self.head.next_node
            cur_element.next_node = ab
            self.head = cur_element
            ch.next_node.next_node = None
            
            
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
            print("value passed is more than size of list")


    """def palindrome(self):
        cur_node = self.head
        q = []
        while cur_node.next_node != None:
            q.append(cur_node.data)
            cur_node = cur_node.next_node
        print(q)"""
    def smallest_element(self):
        cur_node = self.head
        small = cur_node.data
        while cur_node.next_node != None:
            if small > cur_node.data:
                small = cur_node.data
            cur_node = cur_node.next_node
        return small
            

    def largest_element(self):
        cur_node = self.head
        large = cur_node.data
        while cur_node.next_node != None:
            if large < cur_node.data:
                large = cur_node.data
            cur_node = cur_node.next_node
        return large

    def insert_sorted_order(self,node):
        if self.size_of_list() == 0:
            self.add_at_beg(node)
            return self.display()
        
        else:      
            if node < self.head.data: # checking if node is greater than first node
                self.add_at_beg(node)
                return self.display()

            elif self.head.next_node == None: # if linked list contain only one node 
                self.add_at_end(node)
                return self.display()

            else: # if linked list has more than one node
                prev = self.head
                cur_node = self.head.next_node
                while cur_node:
                    if node > cur_node.data:
                        if cur_node.next_node == None:
                            self.add_at_end(node)
                            return self.display()
                        else:
                            prev = cur_node
                            cur_node = cur_node.next_node
                            #count += 1
                    else:
                        new_node = Node(node)
                        prev.next_node = new_node
                        new_node.next_node = cur_node
                        return self.display()

# This function is incomplete 
# involves concept of backtracking 
def max_sum_list():

    list1 = Linkedlist()
    list2 = Linkedlist()
    # Taking node as an input from user for first linked list
    #ab = int(input("Enter the size of first sorted linked list:"))
    #for i in range(ab):
        #x = int(input("Enter the node data: "))
    list1.insert_sorted_order(23)
    list1.insert_sorted_order(1)
    list1.insert_sorted_order(78)
    list1.insert_sorted_order(45)
    # taking node as an input from user for second linked list    
    #cd = int(input("Enter the size of sorted second linked list:"))
    #for i in range(cd):
    #    y = int(input("Enter the node data: "))
    list2.insert_sorted_order(34)
    list2.insert_sorted_order(89)
    list2.insert_sorted_order(15)
    list2.insert_sorted_order(0)
    list2.insert_sorted_order(3)
    
    a = list1.head
    b = list2.head


        

#max_sum_list()
l = Linkedlist()
#print(l.display())
l.add_at_beg(1)
l.add_at_beg(14)
#print(l.display())
#l.add_at_beg(13)
#l.add_at_beg(12)
#l.add_at_beg(23)
#l.add_at_beg(4)
#l.add_at_beg(2)
l.add_at_end(8)
l.add_at_middle(45,2)
#l.display()
#l.del_at_middle(2)
#l.display()
#l.middle_node()
#print(l.search_the_list(40))
#l.search_based_update(12)
#l.quick_sort_list()
#print(l.remove_duplicates())
#l.palindrome_list()
#print(l.check_circular_loop())
l.reverse_list()
l.display()
#print(l.third_from_end())
#print(l.size_of_list())
#l.display()
#l.swap(6)
#l.display()
#print("Smallest element is:",l.smallest_element())
#print("Largest element is:",l.largest_element())
#l.insert_sorted_order(240)
#l.insert_sorted_order(511)
#l.insert_sorted_order(1)
#l.insert_sorted_order(3)
#l.insert_sorted_order(90)
#l.insert_sorted_order(30)
#l.insert_sorted_order(120)


