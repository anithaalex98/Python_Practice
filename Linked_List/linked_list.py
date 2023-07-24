class Node:
    def __init__(self,data):
        self.data = data #contains the value 
        self.nextval = None #points to next node

class LinkedList:
    def __init__(self):
       self.head = None #points to the first node. Used to traverse linkedlist

    #to print all values in a linkedlist
    def printLinkedList(self):
        val = self.head
        print("Linked List -")
        while val is not None:
            print(val.data)
            val = val.nextval
        print("##################")
    
    def insertAtBegining(self,data):
        newval = Node(data)
        newval.nextval = self.head
        self.head = newval
        print("Successfully inserted data ",data," in linked list - ")
    
    def insertAtEnd(self,data):
        newval = Node(data)
        if self.head is None:
            self.head = newval
        else:
            iteratehead = self.head
            while iteratehead is not None:
                if iteratehead.nextval is None:
                    break
                else:
                    iteratehead = iteratehead.nextval
            iteratehead.nextval = newval
        print("Successfully inserted data ",data," in linked list - ")
    
    def insertInBetween(self,middledata,data):
        newval = Node(data)
        if self.head is None:
            self.head = newval
        else:
            iteratehead = self.head
            while iteratehead is not None:
                if iteratehead.data == middledata:
                    break
                else:          
                    iteratehead = iteratehead.nextval
            if iteratehead is None:
                print("No such data in linkedlist")
                return
            
            newval.nextval = iteratehead.nextval
            iteratehead.nextval = newval
        print("Successfully inserted data ",data," in linked list - ")
    
    def deleteNodeByValue(self, data):
        if self.head is None:
            print("LinkedList is empty")
        else:
            iteratehead = self.head
            prevhead = None
            while iteratehead is not None:
                if iteratehead.data == data:
                    break
                prevhead = iteratehead          
                iteratehead = iteratehead.nextval
            
            if iteratehead is None:
                print("No such data in linkedlist")
                return
            
            if prevhead is not None:
                prevhead.nextval = iteratehead.nextval
            else: #If data is the first node data
                self.head = iteratehead.nextval
            iteratehead = None
            print("Successfully Deleted data ",data," in linked list - ")

    #Reverse the liked list
    #Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed.
    def reverseLinkedList(self): 
        if self.head is not None:
            rhead = self.head
            prev = None
            curr = rhead
            
            while curr is not None:            
                nexxt = curr.nextval
                curr.nextval = prev
                prev = curr
                curr = nexxt
                rhead = prev
            
            self.head = rhead
            print("Successfully Reversed linked list - ")
            self.printLinkedList()
        
    
list1 = LinkedList()
list1.head = Node("B")
val2 = Node("C")
list1.head.nextval = val2 

list1.printLinkedList()
list1.insertAtBegining("A")
list1.printLinkedList()
list1.insertAtEnd("E")
list1.printLinkedList()
list1.insertInBetween("C","D")
list1.printLinkedList()
list1.deleteNodeByValue("A")
list1.printLinkedList()
list1.reverseLinkedList()