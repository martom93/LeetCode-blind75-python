class Solution:
    def reverseBits(self, n: int) -> int:
        
        #Declare the variable for our resault. resault contain 32-bit number
        resault = 0


        #We have to loop this 32 times, because our number has 32bits to check
        for i in range(32):
            #take the value of n-th bit AND it with logic 1
            currentBit = (n >> i) & 1
            #shift resault to the corect slot
            resault = resault | currentBit << (31 - i)
        





        return resault