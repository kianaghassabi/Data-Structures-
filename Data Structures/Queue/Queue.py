#Queue class 
class Queue:
    
    #constructor
    def __init__(self):
        self.queue = list()
    
    #push function
    def push(self,element):
        self.queue.insert(0,element)
    
    #pop function
    def pop(self):
        self.queue.pop()
    
    #function for showing the elements in queue
    def display(self):
        for i in range(0,len(self.queue)):
            print(self.queue[i],"\t")

#creating a queue
myqueue = Queue()

#calling the display function for showing the elements in queue
myqueue.display()

#adding elements to the queue
myqueue.push(3)
myqueue.push(14)
myqueue.push(5)
myqueue.push(1)

print("Queue:")

#calling the display function for showing the elements in queue
myqueue.display()

print("After popping  from the queue")
#pop the element from the queue
myqueue.pop()

#calling the display function for showing the elements in queue
myqueue.display()