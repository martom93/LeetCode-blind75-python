class Solution:
    def isValid(self, s: str) -> bool:

        #Creating the stack to store parentheses
        stack = []

        #Creating hashmap containing matching parentheses
        openToClose = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        #Loop  for each element in a S String
        for element in s:
            #If element exist in a HashMap as a key:
            if element in openToClose:
                #check if stack is not empty, then check if the last element
                #of the stack is matching parentheses (valid key-value in a hashmap)
                #if it is - then pop this element, otherwise add this to the stack
                if stack and stack[-1] == openToClose[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
             
        #Return True if the stack is empty, or False when it is not
        return True if not stack else False