class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Declaration of left and right pointers on first and last element
        left, right = 0, len(s)-1


        #Iterate through the string until pointers meets each other
        while left<right:
            #while pointer doesnt show on Alfa-numeric symbol, increment or decrement
            while left<right and not self.checkIfAlNum(s[left]):
                left += 1
            while right>left and not self.checkIfAlNum(s[right]):
                right -= 1



            #if values aren't equal return False. Remember that we have to 
            #convert symbol to lowerCase.
            if s[left].lower() != s[right].lower():
                return False

            #Update the indexes. Increment left one, and decrement the right one.     
            left, right = left + 1, right - 1
        return True

    #function that checks the ASCII values of a-z, A-Z and 0-9 characters.
    def checkIfAlNum(self, element):
            return(ord('A') <= ord(element) <= ord('Z') or
                   ord('a') <= ord(element) <= ord('z') or
                   ord('0') <= ord(element) <= ord('9'))