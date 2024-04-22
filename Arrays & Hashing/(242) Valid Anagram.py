class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #checking if the string are equal
        if len(s) != len(t): 
            return False
        
        #creating the hashmaps for S and T strings to store the letter and number of that letter in a string.
        hashS, hashT = {}, {} 

        #it doesn't matter what string you will choose, because on this stage they has to be equal.
        #building the hashmaps
        for i in range(len(s)): 
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)



        #Comparing the hashmaps
        for c in hashS:
            if hashS[c] != hashT.get(c, 0):
                return False

        return True