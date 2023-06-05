#! python3

# gather input / ask if they want to pop or push / if they ask to pop check whether list is empty / if so then say nothing to pop
stack = []
def stackMaker(): 
    
    print('Please type if you would like to pop(delete) or push(insert) an item\nex. type "pop" or "push"')
    
    # take input and push into list 
    porpu = input()
    if porpu.capitalize() == 'Push':
        print('Please type something to add to the stack.')
        pushItem = input()
        stack.append(pushItem)
        print(stack)
        stackMaker()
    
    if porpu.capitalize() == 'Pop':
        if stack == []:
            print('Nothing was removed from the stack')
        else:
            print('The item '+stack[-1]+' was popped.') #notifies what item was popped
            stack.pop()
            print(stack)
        stackMaker()
stackMaker() # keep looping and keep popping and pushing             



    




