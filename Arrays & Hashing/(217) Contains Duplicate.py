class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #Creating the set of unique element of array
        hashSet = set()

        #Iterate through each element of the array.
        #If element already exists, return false, if not
        #add this element to our set
        for element in nums:
            if element in hashSet:
                return True
            hashSet.add(element)




        return False