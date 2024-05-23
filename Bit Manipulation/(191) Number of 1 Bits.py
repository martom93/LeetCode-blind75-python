class Solution:
    def hammingWeight(self, n: int) -> int:
        #Resault variable to keep track of 1's bits
        resault = 0
        #Keep looping until n contains only 0's
        while n:    
            #checking if our last bit is 1, then
            #shift the number by one using >>
            if n % 2 == 1:
                resault += 1
                n = n >> 1
            else: 



                n = n >> 1
        return resault