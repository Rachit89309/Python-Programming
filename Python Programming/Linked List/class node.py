class Node:
    def __init__(self, data):
        self.data= data 
        self.next = None

a = Node(13)
b = Node(15)
a.next = b
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)
print(b)
print(b.next)


# input of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    while head is not None:
        print(str(head.data) + "->", end = "")
        head = head.next
    print("None")
    return    

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currData in inputList:
       if currData == -1:
           break
       
       newNode = Node(currData)
       if head is None:
           head = newNode
           
       else:
           curr = head
           while curr.next is not None:
              curr = curr.next 
           curr.next = newNode    
    return head   

head = takeInput()  
printLinkedList(head)      
            