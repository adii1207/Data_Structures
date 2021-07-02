class Node:
    def __init__(self,data=None,next_node=None,prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return "[Node data: %s]" % self.data

class double_linked_list:
    def __init__(self):
        self.head = None

    def add_at_beg(self,info):
        new_node = Node(info)
        
        if self.head == None :
            self.head = new_node
            self.head.prev_node = None
            
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
            self.head.prev_node = None
        return ' '     
            #print(x)
            #print(self.head)
            #print(self.head.next_node)

    def add_at_end(self,info):
        new_node = Node(info)

        current_node = self.head
        while current_node.next_node != None:
            current_node = current_node.next_node

        current_node.next_node = new_node
        new_node.next_node = None
        new_node.prev_node = current_node
        #print(current_node)
        #print(new_node.prev_node)
        #print(current_node.next_node)



    def add_at_middle(self,info):
        new_node = Node(info)
        x = int(input("Enter position after you which you want to enter the new node:"))
        if self.head == None:
            self.add_at_beg(new_node)
        else:
            current_node = self.head
            y = 0
            while y < x-1:# traversing to that node after which new node has to be inserted
                current_node = current_node.next_node
                y+=1
            #print(current_node)
        a = current_node.next_node
        #print(a.prev_node)
        current_node.next_node = new_node
        new_node.prev_node = current_node
        new_node.next_node = a
        a.prev_node = new_node
        #print(current_node)
        #print(current_node.next_node)
        #print(new_node.next_node,a)



    def delete_at_beg(self):
        self.head = self.head.next_node
        #print(self.head)



    def delete_at_end(self):
        cur_element = self.head
        while cur_element.next_node != None:
            cur_element = cur_element.next_node
        #print(cur_element)
        #cur_element = None
        a = cur_element.prev_node
        a.next_node = None
        #print(a.next_node)
            


    def delete_at_middle(self,pos):
        current_node = self.head
        y = 0
        while y < pos-1:# traversing to that node which has to be deleted
            prev = current_node
            current_node = current_node.next_node
            y+=1
        #print(current_node)
        a = current_node.prev_node
        b = current_node.next_node
        a.next_node = b
        b.prev_node = a
        
        
        
            


    def display(self):
        if self.head == None:
            return "Empty linked list"
        else:
            x = None
            current_node = self.head
            while current_node:
                if current_node == self.head:
                    print("None","<--",end='')
                    print(current_node,end=' ')
                    print("--> ",end='')
                else:
                    print("<-- ",end='')
                    print(current_node,end=' ')
                    print("--> ",end='')
                current_node = current_node.next_node
            print("None")
            return " "


    def size_of_list(self):
        
        cur_node = self.head
        count  = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next_node
            
        return count

    def reverse(self):
        cur_element = self.head
        prev = None
        while cur_element!=None:
            next_val = cur_element.next_node
            cur_element.next_node = prev
            prev = cur_element
            cur_element = next_val
            
        self.head = prev
        return ""
        
                

    def swap(self,k):
        
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
            #print(prev)
            
            while z < k-1:   # kth element from first
                z+=1
                pref = current_element
                current_element = current_element.next_node
            #print(pref)
            
            c = cur_element.next_node 
            b = current_element.next_node
            pref.next_node = cur_element
            cur_element.next_node = b
            prev.next_node = current_element
            current_element.next_node = c

            
            
            
        else:
            print("value passed is more than size of list")


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



dl = double_linked_list()
dl.add_at_beg(10)
dl.add_at_beg(60)
dl.add_at_beg(50)
dl.add_at_beg(40)
dl.add_at_beg(30)
dl.add_at_end(3)
#dl.add_at_middle(45)
#dl.delete_at_beg()
#dl.delete_at_end()
#dl.delete_at_middle(2)
dl.display()
#print(dl.size_of_list())
#dl.reverse()
dl.swap(6)
dl.display()
print(dl.smallest_element())
print(dl.largest_element())
