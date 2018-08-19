#implementing stack
class stack:
    
    #Constructor
    def __init__(self):
        self.stack = list()

    #cheking whether the stak is empty or not
    def isempty(self):
        return self.stack == []

    #pushing into the stack
    def push(self,element):
        self.stack.append(element)
   
    #popping from the stack
    def pop(self):
        #checking whether the list is empty or not
        if stack.isempty(self)==True:
            print("stack is Empty")
        else:
            self.stack.pop()

    #returuning the size of stack
    def stacksize(self):
        return len(self.stack)

    #displaying the stack
    def display(self):
        print("Top of the Stack\n---------")
        for i in range(-1,len(self.stack)-1):
            print(self.stack[i])
        print("---------")
    
#creating an object of a class
mystack = stack()

#adding elements to the stack
mystack.push(12)
mystack.push(30)
mystack.push(16)

#displaying the stack
mystack.display()

#pop the last element from the stack
mystack.pop()

#displaying the stack
mystack.display()

#checking whether the stack is empty or not
is_empty=mystack.isempty()
print("Is the stack empty?",is_empty)
